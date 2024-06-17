---

layout: col-sidebar
title: Insecure Deserialization
author: Vaibhav Malik
contributors: kingthorin
tags: [vulnerability, application, web]
permalink: /vulnerabilities/Insecure_Deserialization

---

{% include writers.html %}

## Description

Insecure Deserialization is a type of vulnerability that arises 
when untrusted data is used to abuse the logic of an application's 
deserialization process, allowing an attacker to execute code, manipulate objects, or perform injection attacks.

Serialization is converting an object into a format 
that can be stored (for example, in a file or memory buffer) or 
transmitted (for example, across a network) and reconstructed later. 
Deserialization is the reverse process -- taking the serialized data and recreating the original object.

Many programming languages offer a native capability for serializing 
objects. These native formats usually provide more features than JSON or XML, including customizability of the serialization process. Unfortunately, the features of these native deserialization mechanisms can be repurposed for malicious effect when operating on untrusted data. Attacks against deserializers have been found to allow denial-of-service, access control, and remote code execution (RCE) attacks.

## Example Scenario

Suppose a Java application uses the native Java serialization to save a 
Cookie object to the user's hard drive. The Cookie object contains the user's session ID. 
The Java code might look something like this:

```java
import java.io.*;

public class SerializeCookie {
  public static void main(String[] args) {
    Cookie cookieObj = new Cookie();
    cookieObj.setValue("alice");
    
    try {
      FileOutputStream fos = new FileOutputStream("cookies.ser");
      ObjectOutputStream oos = new ObjectOutputStream(fos);
      oos.writeObject(cookieObj);
      oos.close(); 
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The `writeObject()` function serializes the `cookieObj` to a file called `cookies.ser`.

Now suppose the application later reads this serialized object from the file:

```java
import java.io.*;

public class DeserializeCookie {
  public static void main(String[] args) {
    try {
      FileInputStream fis = new FileInputStream("cookies.ser");
      ObjectInputStream ois = new ObjectInputStream(fis);
      Cookie cookieObj = (Cookie) ois.readObject();
      System.out.println(cookieObj.getValue());
    } catch (IOException | ClassNotFoundException e) {
      e.printStackTrace();
    }
  }
}
```

If an attacker is able to replace the `cookies.ser` file or its content with a 
malicious serialized object, they could potentially execute arbitrary 
code when the object is deserialized. For example, the attacker could create a serialized object that executes OS commands when deserialized.

## Impact

Insecure deserialization vulnerabilities can lead to the following:

1. Remote Code Execution: If an attacker can control the serialized object, they can execute arbitrary code on the server when deserialized.
2. Denial-of-Service (DoS) Attacks: Deserialization is computationally expensive. Attackers can submit large, complex, serialized objects to exhaust server resources.
3. Privilege Escalation: Depending on which object is being deserialized and how it's used, an attacker could escalate their privileges if the deserialized object has more rights than the attacker.

## Mitigation

The safest approach is never to accept serialized objects from untrusted sources. If that's not possible, consider the following mitigations:
1. Integrity Checks: If you must deserialize objects from untrusted sources, ensure the integrity of the serialized data using digital signatures or similar mechanisms.
2. Strict Type Constraints: Enforce strict type constraints during deserialization and allow the deserialization of only a few expected classes.
3. Isolate Code: Run the deserialization code in an isolated environment, such as a separate process or a sandbox, to limit the impact of any malicious code execution.
4. Log Deserialization Exceptions: Log any exceptions that occur during deserialization. Many deserialization exploits throw exceptions as part of the attack.
5. Monitor Deserialization: Monitor the deserialization process for abnormal memory, CPU, file system, or network usage.
6. Use Alternative Data Formats: Use less complex data formats such as JSON for serialization if possible.
7. Keep Up-to-Date: Update your software with the latest security patches, which may address known deserialization vulnerabilities.

## References
- [OWASP Top 10-2017 A8-Insecure Deserialization](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization)  
- [CWE-502: Deserialization of Untrusted Data](https://cwe.mitre.org/data/definitions/502.html)
- [Java Unmarshaller Security](https://github.com/mbechler/marshalsec)
- [.NET Deserialization Cheat Sheet](https://www.owasp.org/index.php/.NET_Deserialization_Cheat_Sheet)

[[:Category:Attack]](https://owasp.org/www-community/attacks/)
