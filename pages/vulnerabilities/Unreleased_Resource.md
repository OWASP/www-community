---

layout: col-sidebar
title: Unreleased Resource
author: 
contributors: 
permalink: /vulnerabilities/Unreleased_Resource
tags: vulnerability, Unreleased Resource
auto-migrated: 1

---

{% include writers.html %}

# Description

The program can potentially fail to release a system resource.

Most unreleased resource issues result in general software reliability
problems, but if an attacker can intentionally trigger a resource leak,
the attacker might be able to launch a denial of service attack by
depleting the resource pool.

Resource leaks have at least two common causes:

  - Error conditions and other exceptional circumstances.
  - Confusion over which part of the program is responsible for
    releasing the resource.

# Risk Factors

  - Talk about the [factors](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
    that make this vulnerability likely or unlikely to actually happen
  - Discuss the technical impact of a successful exploit of this
    vulnerability
  - Consider the likely \[business impacts\] of a successful attack

# Examples

## Example 1

The following Java method never closes the file handle it opens. The
finalize() method for FileInputStream eventually calls close(), but
there is no guarantee as to how long it will take before the finalize()
method will be invoked. In a busy environment, this can result in the
JVM using up all of its file handles.

```
    private void processFile(String fName) throws FileNotFoundException, IOException
    {
      FileInputStream fis = new FileInputStream(fName);
      int sz;
      byte[] byteArray = new byte[BLOCK_SIZE];
      while ((sz = fis.read(byteArray)) != -1) {
        processBytes(byteArray, sz);
      }
    }
```

## Example 2

Under normal conditions the following C\# code executes a database
query, processes the results returned by the database, and closes the
allocated SqlConnection object. But if an exception occurs while
executing the SQL or processing the results, the SqlConnection object is
not closed. If this happens often enough, the database will run out of
available cursors and not be able to execute any more SQL queries.

```
    ...
    SqlConnection conn = new SqlConnection(connString);
    SqlCommand cmd = new SqlCommand(queryString);
    cmd.Connection = conn;
    conn.Open();
    SqlDataReader rdr = cmd.ExecuteReader();
    HarvestResults(rdr);
    conn.Connection.Close();
    ...
```

## Example 3

The following C function does not close the file handle it opens if an
error occurs. If the process is long-lived, the process can run out of
file handles.

```
    int decodeFile(char* fName)
    {
        char buf[BUF_SZ];
        FILE* f = fopen(fName, "r");

        if (!f) {
            printf("cannot open %s\n", fName);
            return DECODE_FAIL;
        } else {
            while (fgets(buf, BUF_SZ, f)) {
                if (!checkChecksum(buf)) {
                  return DECODE_FAIL;
                } else {
                  decodeBlock(buf);
                }
            }
        }
        fclose(f);
        return DECODE_SUCCESS;
    }
```

[Category:Code Quality
Vulnerability](Category:Code_Quality_Vulnerability "wikilink")
[Category:Java](Category:Java "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Code Snippet](Category:Code_Snippet "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")