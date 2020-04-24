---

layout: col-sidebar
title: Directory Restriction Error
author: 
contributors: 
permalink: /vulnerabilities/Directory_Restriction_Error
tags: vulnerability, Directory Restriction Error

---

{% include writers.html %}

## Description

Improper use of the `chroot()` system call may allow attackers to escape a chroot jail.

The application fails to enforce the intended restricted directory access policy. By using relative paths or other path traversal attack mechanisms, an attacker can access unauthorized files outside the restricted directory.

## Examples

Improper use of the `chroot()` system call may allow attackers to access files that are outside the new root directory, and therefore breaks the intended access control policy.

The `chroot()` system call allows a process to change its perception of the root directory of the file system. After properly invoking `chroot()`, a process cannot access any files outside the directory tree defined by the new root directory. Such an environment is called a chroot jail, and is commonly used to prevent the possibility that a processes could be subverted and used to access unauthorized files. For instance, many FTP servers run in chroot jails to prevent an attacker who discovers a new vulnerability in the server from being able to download the password file or other sensitive files on the system.

Improper use of `chroot()` may allow attackers to escape from the chroot jail. The `chroot()` function call does not change the process's current working directory, so relative paths may still refer to file system resources outside of the chroot jail after chroot() has been called.

Consider the following source code from a (hypothetical) FTP server:

```
chroot("/var/ftproot");
...
fgets(filename, sizeof(filename), network);
localfile = fopen(filename, "r");
while ((len = fread(buf, 1, sizeof(buf), localfile)) != EOF) {
  fwrite(buf, 1, sizeof(buf), network);
}
fclose(localfile);
```

This code is responsible for reading a filename from the network, opening the corresponding file on the local machine, and sending the contents over the network. This code could be used to implement the FTP GET command. The FTP server calls `chroot()` in its initialization routines in an attempt to prevent access to files outside of `/var/ftproot`. But because the server fails to change the current working directory by calling `chdir("/")`, an attacker could request the file `../../../../../etc/passwd` and obtain a copy of the system password file.

## Risk Factors

TBD

## Examples

TBD

## Related [Attacks](../attacks/)

- [Path Traversal Attacks](../attacks/Path_Traversal_Attacks)
- Attackers try to access unauthorized files, such as password files or configuration files.

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

## Related [Technical Impacts](Technical_Impacts "wikilink")

## References

TBD