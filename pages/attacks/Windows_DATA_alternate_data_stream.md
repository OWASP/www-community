---

title: 'Windows ::DATA Alternate Data Stream'
layout: col-sidebar
author:
contributors: 
permalink: /attacks/Windows_alternate_data_stream
tags: attack
auto-migrated: 1

---

{% include writers.html %}

## Description

The NTFS file system includes support for alternate data streams. This
is not a well known feature and was included, primarily, to provide
compatibility with files in the Macintosh file system. Alternate data
streams allow files to contain more than one stream of data. Every file
has at least one data stream. In Windows, this default data stream is
called `:$DATA`.

Windows Explorer doesn't provide a way of seing what alternate data
streams are in a file (or a way to remove them without deleting the
file) but they can be created and accessed easily. Because they are
difficult to find they are often used by hackers to hide files on
machines that they've compromised (perhaps files for a rootkit).
Executables in alternate data streams can be executed from the command
line but they will not show up in Windows Explorer (or the Console).
Reference Example 1 for information on creating and accessing alternate
data streams.

Since the `:$DATA` alternate stream exists for every file it can be an
alternate way to access any file. Reference Example 2 for information on
accessing the `:$DATA` alternate data stream in a text file. Any
application that creates files or looks at or depends on the end of the
file name (or the extension) should be aware of the possibility of these
alternate data streams. If unsanitized user input is used to create or
reference a file name an attacker could use the `:$DATA` stream to change
the behavior of the software. A well-known vulnerability of this nature
existed in older versions of IIS. When IIS saw a request for a file with
an ASP extension it sent the ASP file to the application associated with
the extension. This application would run the server-side code in the
ASP file and generate the HTML response for the request. Due to a flaw
in the extension parsing of these versions of IIS, `filename.asp::$DATA`
did not match the extension and since there was no application
registered for the `asp::$DATA` extension, the asp source code was
returned to the attacker.

Proper user input sanitation is the best defense against this type of
attack.

## Examples

### Example 1 - Creating Alternate Data Streams

- `C:\> type C:\windows\system32\notepad.exe > c:\windows\system32\calc.exe:notepad.exe`
- `C:\> start c:\windows\system32\calc.exe:notepad.exe`

### Example 2 - Accessing the :$DATA Alternate Data Stream

`C:\> start c:\textfile.txt::$DATA`

### Example 3 - Exploiting the ASP Alternate Data Stream Show Code Vulnerability

Normal access:
- `http://www.alternate-data-streams.com/default.asp`

Show code bypass accessing the :$DATA alternate data stream:
- `http://www.alternate-data-streams.com/default.asp::$DATA`

In the vulnerable versions, IIS parsed the extension of this file as
`asp::$DATA`, not ASP. As such the application associated with the ASP
extension was not invoked and the ASP source code was viewable by the
attacker.
