---

layout: col-sidebar
title: "Race Conditions"
author: "Cindy Ramirez"
permalink: pages/vulnerabilities/race_conditions
tags: ["vulnerability", "race_conditions"]

---

{% include writers.html %}

## Overview
A race condition is a server-side vulnerability that occurs when two or more threads or requests access shared state concurrently without proper coordination.
This can lead to unexpected behavior since the outcome depends on the timing of the processes.
Race conditions can be difficult to detect. This page will equip application security engineers and developers to identify race conditions
through tooling and manual code reviews, and remediate them through code changes.


## Introduction
A race condition, also known as [CWE-362](https://cwe.mitre.org/data/definitions/362.html), happens
when program behavior depends on the uncontrolled relative timing of concurrent events.
A common subtype is **Time-of-Check to Time-of-Use (TOCTOU)**: two concurrent actors both pass a check before either completes its action,
causing multiple threads to interact with the same data simultaneously and produce a "collision" that leaves the system in an inconsistent state.
The period during which a collision is possible is called the **race window**.

Race conditions appear across multiple OWASP Top 10 2025 categories depending on context:
- [A08:2025 – Software and Data Integrity Failures](https://owasp.org/Top10/2025/A08_2025-Software_and_Data_Integrity_Failures/) — most common; covers TOCTOU and concurrent state corruption
- [A01:2025 – Broken Access Control](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/) — when a race condition bypasses a permission or authentication check
- [A06:2025 – Insecure Design](https://owasp.org/Top10/2025/A06_2025-Insecure_Design/) — when the architecture fundamentally lacks any synchronization strategy

**Example:**
Two users see one item in stock. Both read `stock = 1`, both pass the `if stock > 0` check, both decrement to `0`, and both commit — final stock is `-1`. Neither request saw the other's write. That's a race condition.

For a detailed walkthrough, see the OWASP Bangkok chapter presentation: [The Race is On](https://owasp.org/www-chapter-bangkok/slides/2024/2024-07-05_The-Race-is-On.pdf).

**Real-world CVE examples:**
- **CVE-2021-21315** — Node.js `systeminformation` package: TOCTOU in a file path check allowed local privilege escalation by swapping a path between check and use.
- **CVE-2020-24815** — Ghostscript: a file permission race condition allowed an attacker to bypass access controls by replacing a file between the permission check and the open.
- **Git 2022 (`git apply`)**: a race condition in temporary file handling allowed symlink attacks during patch application on shared systems.


## How to Discover Race Conditions in Existing Code
Use a combination of automated scanning and manual code review. The Semgrep rules below automate detection of the patterns described in the checklist; use the checklist for code contexts where scanning isn't available or produces false positives.

### Scanning Tools

1. **Semgrep** – use targeted rules for specific race condition patterns. The rule below detects filesystem TOCTOU with high confidence — `exists`/`isfile`/`access` checks followed by a mutating operation on the same path almost never have a safe use; the fix is always to drop the check entirely. Similar `check-then-act` patterns exist in JavaScript, Go, and C# — apply the same logic when reviewing those codebases manually.

```yaml
rules:
  - id: toctou-filesystem-check-then-act
    languages: [python]
    severity: WARNING
    message: >
      TOCTOU: '$PATH' is checked then used in a separate operation.
      The filesystem state may change between them — an attacker can swap
      '$PATH' for a symlink (e.g., to /etc/passwd) in the window.
      Fix: open the file directly and handle the exception, or use os.open()
      with O_CREAT | O_EXCL for atomic create, or flock() for exclusive access.
    metadata:
      cwe: "CWE-367"
      confidence: HIGH
      references:
        - https://cwe.mitre.org/data/definitions/367.html
    pattern-either:
      - patterns:
          - pattern: |
              if os.path.exists($PATH):
                  ...
                  os.remove($PATH)
      - patterns:
          - pattern: |
              if os.path.exists($PATH):
                  ...
                  open($PATH, ...)
      - patterns:
          - pattern: |
              if os.path.isfile($PATH):
                  ...
                  open($PATH, ...)
      - patterns:
          - pattern: |
              if os.access($PATH, ...):
                  ...
                  open($PATH, ...)
```

What it catches:

```python
# FLAGGED — symlink swap attack window
if os.path.exists("/tmp/workfile"):
    os.remove("/tmp/workfile")

# FLAGGED — classic setuid TOCTOU
if os.access(path, os.R_OK):
    f = open(path, "r")

# SAFE — not flagged; no check means no TOCTOU window.
# os.remove() is atomic at the syscall level — the exception
# handles the missing-file case without a race.
try:
    os.remove("/tmp/workfile")
except FileNotFoundError:
    pass
```

2. **Burp Suite** – use the native **Parallel Requests** feature (Repeater → Send group in parallel) introduced in 2023, or Turbo Intruder for higher-volume testing. The example below fires 100 requests simultaneously through a single gate, maximizing the chance of hitting the race window:

```python
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=50)
    for i in range(100):
        engine.queue(target.req, gate='race1')
    engine.openGate('race1')  # releases all requests at once
```

3. **race-the-web** – a purpose-built CLI tool for sending large numbers of concurrent HTTP requests to a target endpoint. Useful for confirming race conditions found manually: [https://github.com/nicowillis/race-the-web](https://github.com/nicowillis/race-the-web)

4. **Nuclei** – community race condition templates are available in the nuclei-templates repository under `vulnerabilities/generic/race-condition*`. Run with: `nuclei -t vulnerabilities/generic/ -tags race-condition -u https://target`

5. **Go race detector** – for Go services, compile and run with `-race` to catch data races at runtime:

```bash
go test -race ./...
go run -race main.go
```


## Manual Code Review Checklist
Look for these patterns:

**Check-then-act without atomicity:**
```python
# Python
if user.balance >= amount:
    user.balance -= amount   # separate UPDATE — not atomic
```

```javascript
// JavaScript/Node.js — Promise-based TOCTOU
const balance = await getBalance(userId);      // check
if (balance >= amount) {
    await deductBalance(userId, amount);        // act — another request may have run between these two awaits
}
```

```go
// Go — goroutine race on shared map (caught by go -race)
if inventory[item] > 0 {
    inventory[item]--   // another goroutine may have decremented between check and write
}
```

```csharp
// C# — non-atomic read-modify-write
if (counter > 0) {
    counter--;   // not thread-safe without lock or Interlocked
}
```

**Two-step file operations (filesystem TOCTOU — CWE-367):**
```python
if os.path.exists(path):
    os.remove(path)          # race window between check and remove
```

The race window is the gap between `exists()` returning `True` and `os.remove()` executing. An attacker running this loop in parallel can win that window:

```bash
while true; do
    rm -f /tmp/workfile
    ln -s /etc/passwd /tmp/workfile
done
```

If the attacker wins, your process — which may be running as root or a privileged service — removes the attacker-controlled file or symlink now present at that path, not the symlink target itself. The same race becomes more serious with `open()` for writing: the attacker swaps the path for a symlink to any sensitive file, and your process may then open and write to that target with its full privileges. The fix is to drop the check entirely and handle the exception atomically:
```python
# Safe — no race window. No check means no TOCTOU window;
# the remove() syscall is atomic. The exception handles absence.
try:
    os.remove(path)
except FileNotFoundError:
    pass
```

For filesystem TOCTOU in privileged processes, also apply the principle of least privilege: run with minimal Linux capabilities (avoid `CAP_DAC_OVERRIDE`), use OpenBSD `pledge()` to restrict syscalls, or drop privileges before accessing user-controlled paths.

**Missing version checks in SQL updates:**
```sql
-- Race-prone: T1 and T2 both read qty=1, then both decrement
SELECT qty FROM inventory WHERE id = 1;
UPDATE inventory SET qty = qty - 1 WHERE id = 1;

-- Safe: atomic conditional decrement
UPDATE inventory SET qty = qty - 1 WHERE id = 1 AND qty > 0;
```


## Impact
Race conditions can be the first step in a multi-stage attack chain.

### Technical Impact

| Scenario | OWASP Category | Illustrative Example |
|---|---|---|
| **Authentication Bypass** | A01 Broken Access Control | Multiple threads replaying a one-time code may each receive a valid session |
| **Double-spend / Limit Bypass** | A08 Software and Data Integrity | Two gift card redemptions within milliseconds both succeed against the same balance |
| **Privilege Escalation** | A01 Broken Access Control | A user role is read as "viewer" but written as "admin" before the check completes |
| **Data Corruption** | A08 Software and Data Integrity | Counter incremented by 5 threads without locking ends up lower than expected |
| **Token Reuse** | A08 Software and Data Integrity | Two password reset flows complete successfully with a single token |
| **Filesystem Attack** | A08 Software and Data Integrity | Symlink swapped between permission check and file open; privileged process writes to /etc/passwd |

### Organizational Impact
- Financial loss from double-spend attacks on payment and loyalty systems
- Regulatory exposure under PCI-DSS, SOX, and HIPAA when transactional integrity is violated
- Reputational damage if authentication bypass enables mass account takeover


## Remediation

Race conditions require fixes at multiple layers. Choose the approach that matches your architecture.

### 1. Database-Level (Preferred for persistence layer)

**Isolation levels** — the default `READ COMMITTED` isolation level permits non-repeatable reads, which is the root cause of most web application race conditions. For financial or inventory operations, use `REPEATABLE READ` or `SERIALIZABLE`:

```sql
-- PostgreSQL: set isolation level for a transaction
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;   -- now locks the row until COMMIT
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

**SELECT FOR UPDATE (pessimistic locking)** — locks the row at read time, blocking any concurrent transaction from reading or modifying it until the lock is released:

```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
-- Row is now locked — concurrent transactions block here
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

**Atomic conditional UPDATE (no lock needed for simple decrements):**

```sql
-- Safe: zero rows affected = constraint violation; handle in application
UPDATE inventory SET qty = qty - 1 WHERE id = 1 AND qty > 0;
```

**Optimistic locking with a version column** — no lock held; conflict detected at write time. If `0` rows affected, another transaction won — retry or return a conflict error to the client:

```sql
UPDATE inventory
SET qty = qty - 1, version = version + 1
WHERE id = 1 AND qty > 0 AND version = :expected_version;
-- 0 rows affected = conflict; application must retry
```

**PostgreSQL advisory locks** — lightweight application-level locks managed by the database, useful when row-level locking is too coarse:

```sql
SELECT pg_advisory_xact_lock(hashtext('inventory:item:1'));
-- Lock held until transaction ends; no other session can acquire it
```

**Idempotency keys** — deduplicate concurrent or retried requests at the database level:

```python
def redeem_coupon(coupon_id, idempotency_key):
    result = db.execute(
        "INSERT INTO redemptions (coupon_id, key) VALUES (?, ?) ON CONFLICT DO NOTHING",
        (coupon_id, idempotency_key)
    )
    return result.rowcount == 1  # True only for the first request; False = duplicate
```

### 2. Application-Level Thread Synchronization (Python)

Use for shared in-process resources such as counters, caches, or file handles.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Final counter value: {counter}")  # Always 500000
```

### 3. Application-Level Synchronization (JavaScript/Node.js)

Node.js is single-threaded but async operations create TOCTOU windows between `await` calls. Serialize access with a mutex or move the check-and-act into an atomic database operation:

```javascript
const { Mutex } = require('async-mutex');
const mutex = new Mutex();

async function deductBalance(userId, amount) {
    const release = await mutex.acquire();
    try {
        const balance = await getBalance(userId);
        if (balance < amount) throw new Error('Insufficient funds');
        await setBalance(userId, balance - amount);
    } finally {
        release();
    }
}
```

Prefer moving the atomicity to the database (e.g., `UPDATE ... WHERE balance >= amount`) over application-level mutexes for multi-instance deployments.

### 4. Application-Level Synchronization (Go)

Use `sync.Mutex` for shared state, or Go's built-in `sync/atomic` for simple counters. Always run tests with `-race`:

```go
import "sync"

var mu sync.Mutex
var inventory = map[string]int{"item1": 10}

func decrement(item string) bool {
    mu.Lock()
    defer mu.Unlock()
    if inventory[item] > 0 {
        inventory[item]--
        return true
    }
    return false
}
```

### 5. Application-Level Synchronization (C#/.NET)

Use `lock` for shared in-process state, or `Interlocked` for atomic counter operations:

```csharp
private readonly object _lock = new object();
private int _counter = 0;

// Option A: lock statement
public void Decrement() {
    lock (_lock) {
        if (_counter > 0) _counter--;
    }
}

// Option B: Interlocked for simple atomic decrement (no lock needed)
public void DecrementAtomic() {
    Interlocked.Decrement(ref _counter);
}
```

### 6. Process-Level Isolation (Python)

Use for CPU-bound parallel work such as running ML models across cores.

```python
import multiprocessing

def increment(counter, lock):
    for _ in range(100000):
        with lock:
            counter.value += 1

counter = multiprocessing.Value('i', 0)
lock = multiprocessing.Lock()
processes = [multiprocessing.Process(target=increment, args=(counter, lock)) for _ in range(5)]
for p in processes: p.start()
for p in processes: p.join()
print(f"Final counter value: {counter.value}")  # Always 500000
```

### 7. Distributed Locking (Java + Redis)

For multi-instance deployments where application-level locks don't span nodes. **Important caveats:** Redis distributed locks are vulnerable to split-brain during failover (see the [Redlock controversy](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)) and network partitions. For most web applications, `SELECT FOR UPDATE` at the database level is safer and simpler. Use Redis locks only when the database cannot be the synchronization point.

```java
RLock lock = redissonClient.getLock("inventory:item:1");
lock.lock();
try {
    int qty = inventoryRepo.getQty(1);
    if (qty > 0) {
        inventoryRepo.decrement(1);
    }
} finally {
    lock.unlock();
}
```

### 8. Mutex / Synchronized Block (Java)

For shared in-process state in multithreaded Java services:

```java
private final Object lock = new Object();
private int counter = 0;

public void increment() {
    synchronized (lock) {
        counter++;
    }
}
```

### 9. Architectural Pattern — Queue-Based Processing

For high-throughput scenarios (payments, inventory), serialize updates through a message queue so a single consumer processes each logical item. This eliminates the race window **for that specific operation** when idempotency is also enforced. Note: multiple consumers can still race on the same item if partitioning is misconfigured, and at-least-once delivery can replay messages — idempotency keys at the consumer are required.

```
Client → API → Message Queue (Kafka / SQS) → Single Consumer per partition → Database
```

Always pair queue-based processing with idempotency keys to handle message replay safely.


## Reporting
AppSec engineers should identify race conditions, report them in a way developers can act on, and work through the correction together.

### Bug Report Template

**Title:** Race Condition — Non-atomic rate limit check in `auth/session.py:87`

**Severity:** High (CVSS score varies by impact — this example assumes network-accessible, no privileges required, high impact on integrity; calculate your specific score using the [CVSS calculator](https://www.first.org/cvss/calculator/3.1))

**Location:** `auth/session.py`, function `check_rate_limit()`, lines 84–91

**Race Window:** Line 87 (read: `count = self.attempts[ip]`) to line 91 (write: `self.attempts[ip] = count + 1`) — unprotected by any lock

**Reproduction:**
```bash
python exploit_poc.py --target http://app:5000/login --threads 20 --expected-limit 5
```

**Evidence:** 20 threads fired; 17 received HTTP 200 (limit should cap at 5)

**Fix:** Wrap lines 87–91 in a `threading.Lock()`, or replace the in-memory counter with an atomic database upsert

**References:** [CWE-362](https://cwe.mitre.org/data/definitions/362.html)


## References

- [CWE-362: Concurrent Execution Using Shared Resource with Improper Synchronization](https://cwe.mitre.org/data/definitions/362.html)
- [CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition](https://cwe.mitre.org/data/definitions/367.html)
- [OWASP Top 10 2025 — A08 Software and Data Integrity Failures](https://owasp.org/Top10/2025/A08_2025-Software_and_Data_Integrity_Failures/)
- [OWASP Top 10 2025 — A01 Broken Access Control](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/)
- [OWASP Top 10 2025 — A06 Insecure Design](https://owasp.org/Top10/2025/A06_2025-Insecure_Design/)
- [OWASP Bangkok Chapter — The Race is On (2024)](https://owasp.org/www-chapter-bangkok/slides/2024/2024-07-05_The-Race-is-On.pdf)
- [PortSwigger Research — Smashing the State Machine: The True Potential of Web Race Conditions (James Kettle, 2023)](https://portswigger.net/research/smashing-the-state-machine)
- [How to Do Distributed Locking — Martin Kleppmann (Redlock critique)](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)
- [race-the-web — concurrent HTTP request tool](https://github.com/nicowillis/race-the-web)
- [Understanding Race Conditions in Python](https://medium.com/yavar/understanding-race-conditions-in-python-and-how-to-handle-them-98f998708b2c)
- [What are race conditions](https://portswigger.net/web-security/race-conditions)
- [Race Conditions](https://learn.snyk.io/lesson/race-condition/?ecosystem=python)