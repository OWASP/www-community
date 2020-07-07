---

layout: col-sidebar
title: Deserialization of untrusted data
author: 
contributors: 
permalink: /vulnerabilities/Deserialization_of_untrusted_data
tags: vulnerability, Deserialization of untrusted data

---

{% include writers.html %}

## Description

Data which is untrusted cannot be trusted to be well formed. Malformed data or unexpected data could be used to abuse application logic, deny service, or execute arbitrary code, when deserialized.

### Consequences

- Availability: The logic of deserialization could be abused to create recursive object graphs or never provide data expected to terminate reading.
- Authorization: Potentially code could make assumptions that information in the deserialized object about the data is valid. Functions which make this dangerous assumption could be exploited.
- Access control (instruction processing): malicious objects can abuse the logic of custom deserializers in order to affect code execution.

### Exposure period

- Requirements specification: A deserialization library could be used which provides a cryptographic framework to seal serialized data.
- Implementation: Not using the safe deserialization/serializing data features of a language can create data integrity problems.
- Implementation: Not using the protection accessor functions of an object can cause data integrity problems
- Implementation: Not protecting your objects from default overloaded functions - which may provide for raw output streams of objects - may cause data confidentiality problems.
- Implementation: Not making fields transient can often cause data confidentiality problems.

### Platform

- Languages: C, C++, Java, Python, Ruby (and probably others)
- Operating platforms: Any

### Required resources

Any

### Severity

High

### Likelihood of exploit

Medium

It is often convenient to serialize objects for convenient communication or to save them for later use. However, deserialized data or code can often be modified without using the provided accessor functions if it does not use cryptography to protect itself. Furthermore, any cryptography would still be client-side security - which is of course a dangerous security assumption.

An attempt to serialize and then deserialize a class containing transient fields will result in NULLs where the non-transient data should be. This is an excellent way to prevent time, environment-based, or sensitive variables from being carried over and used improperly.

## Risk Factors

- Does the deserialization take place before authentication?
- Does the deserialization limit which types can be deserialized?
- Does the deserialization host have types available which can be repurposed towards malicious ends? Sometimes, these types are called "gadgets", considering their similarity to abusable bits of code that already exist in machine code in [Return-Oriented-Programming](https://en.wikipedia.org/wiki/Return-oriented_programming) attacks.

## Examples

The following is an example from Adobe's BlazeDS AMF deserialization vulnerability ([CVE-2011-2092](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-2092)). You can specify arbitrary classes and properties for a BlazeDS application to deserialize. This particular payload creates an instance of a JFrame object on the target server. The created JFrame object will have a "defaultCloseOperation" of value 3 -- which indicates that the JVM should exit when this JFrame window is closed.

```
[RemoteClass(alias="javax.swing.JFrame")]
public class JFrame {
   public var title:String = "Gotcha!";
   public var defaultCloseOperation:int = 3;
   public var visible:Boolean = true;
}
```

The next example is one that is much more likely to be seen in custom code. This code reads an object from an untrusted source, and then casts it to an AcmeObject:

```
InputStream is = request.getInputStream();
ObjectInputStream ois = new ObjectInputStream(is);
AcmeObject acme = (AcmeObject)ois.readObject();
```

Unfortunately, the casting operation to AcmeObject occurs after the deserialization process ends. Therefore, it's not useful in preventing any attacks that happen during deserialization from occurring. It's possible that behavior in custom deserialization protocols (for instance, by overriding `Serializable#readObject()` in Java) can be re-purposed towards malicious ends. Researchers have found [complex object graphs which, when deserialized, can lead to remote code execution](http://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/) in most Java software.

The next example is a denial-of-service attack against any Java application that allows deserialization. The `HashSet` called "root" in the following code sample has members that are recursively linked to each other. When deserializing this "root" object, the JVM will begin creating a recursive object graph. It will never complete, and consume CPU indefinitely.

```
Set root = new HashSet();
Set s1 = root;
Set s2 = new HashSet();
for (int i = 0; i < 100; i++) {
  Set t1 = new HashSet();
  Set t2 = new HashSet();
  t1.add("foo"); // make it not equal to t2
  s1.add(t1);
  s1.add(t2);
  s2.add(t1);
  s2.add(t2);
  s1 = t1;
  s2 = t2;
}
```

Another example of a denial-of-service attack against any Java application that allows deserialization:

By crafting a stream, such that it contains an ArrayList with a size of `Integer.MAX_VALUE`, even if all elements are null or the same object, an internal array of length MAX_VALUE will be created, on some JVM's this will cause an `OutOfMemoryError` prior to deserialization of the elements, this doesn't require much data in the inputStream. Many collection classes and object arrays can be manipulated in similar wasy, as they create their capacity prior to reading in elements, few sanity checks are performed.

It's not like the JVM folks aren't aware, they're just hamstrung by backward compatibility with deployed code.

A quote from `ArrayList` source (GPL2 license with classpath exception):

```
/**
 * The maximum size of array to allocate.
 * Some VMs reserve some header words in an array.
 * Attempts to allocate larger arrays may result in
 * OutOfMemoryError: Requested array size exceeds VM limit
 */
private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8;
```

Even if `ObjectInputStream` is overridden to perform look ahead deserialization with an allow list, `ObjectInputStream` itself, will allow an attacker to create a multidimensional array, with a size of `Integer.MAX_VALUE` and every array element it contains, to do the same, even if these arrays all contain the same object element reference (passing reference to cached, previously serialized objects, minimizes the stream bytes transferred), it will very quickly consume all available memory in the JVM.

Fortunately `ObjectInputStream` can be completely re-implemented and overridden by subclassing, in this case the entire functionality of ObjectInputStream has to also be re-implemented to read [the Java serialization protocol](https://docs.oracle.com/javase/7/docs/platform/serialization).

Since Java's Serialization uses implicit construction, whereby the first non serializable no argument super class constructor is invoked to create a child class instance (along with some unsafe magic), it prevents classes from checking their invariant's until after construction has completed. For this reason, the standard implicit Java Serialization API is flawed from a security perspective.

It is possible to create an `ObjectInputStream` that is backward compatible with current `Serializable` object's serial form, for security, it requires a new deserialization API, the exclusion of circular references, limits placed on array lengths and the object cache, all while allowing classes to check their invariants prior to objects being created, such that no object can be created in an illegal state. In addition, administrators will need to be able to reduce the classes available for deserialization to only those required to limit the attack surface, similar to allow listing or using Permissions.

## Related [Controls](../controls/)

- Requirements specification: A deserialization library could be used which provides a cryptographic framework to seal serialized data.
- Implementation: Use the signing features of a language to assure that deserialized data has not been tainted.
- Implementation: Authenticate prior to deserializing.
- Implementation: When deserializing data, populate a new object rather than just deserializing. The result is that the data flows through safe input validation and that the functions are safe. 
- Implementation: Explicitly define final [readObject()](http://docs.oracle.com/javase/7/docs/api/java/io/Serializable.html) to prevent deserialization.

An example of this is:

```
private final void readObject(ObjectInputStream in) throws java.io.IOException {
  throw new java.io.IOException("Cannot be deserialized");
}
```

- Implementation: Make fields transient to protect them from deserialization.
- Implementation: In your code, override the [ObjectInputStream#resolveClass()](http://docs.oracle.com/javase/7/docs/api/java/io/ObjectInputStream.html) method to prevent arbitrary classes from being deserialized. This safe behavior can be wrapped in a library like [SerialKiller](https://github.com/ikkisoft/SerialKiller). Note that while this can prevent gadget attacks, it cannot prevent DOS, as there are vulnerabilities within ObjectInputStream that allow an attacker to use up all available memory.
- Implementation: Use a safe replacement for the generic `readObject()` method as seen [here](http://www.contrastsecurity.com/security-influencers/java-serialization-vulnerability-threatens-millions-of-applications). Note that this addresses "billion laughs" type attacks by checking input length and number of objects deserialized. Again this will not prevent DOS attacks on ObjectInputStream.
- Implementation: Use a Java agent to override the internals of ObjectInputStream to prevent exploitation of known dangerous types as seen in [rO0](https://github.com/Contrast-Security-OSS/contrast-rO0) and [NotSoSerial](https://github.com/kantega/notsoserial). Keep in mind that allow listing is safer than deny listing.
- Implementation: Participate in the reimplementation of ObjectInputStream; Atomic Serialization is designed with security in mind from the outset, while maintaining Object Serial Form compatibility; note this is not a drop in replacement like those above, but likely to be the most secure option.

## References

- [FoxGlove vulnerability announcement](http://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/#websphere) 
- [JFrame DoS example by Wouter Coekaerts](http://wouter.coekaerts.be/2011/amf-arbitrary-code-execution)
- [HashSet Billion-Laughs Style DoS example by Wouter Coekaerts](https://gist.github.com/coekie/a27cc406fc9f3dc7a70d)
- [Safe ObjectInputStream implementation that allows policy-based deserialization](https://github.com/ikkisoft/SerialKiller)
- [rO0, a Java agent that protects applications from deserialization attacks](https://github.com/Contrast-Security-OSS/contrast-rO0)
- [NotSoSerial, a Java agent that protects applications from deserialization attacks](https://github.com/kantega/notsoserial)
- [Atomic Serialization using constructor with input validation, no circular references, Permission limited scope limited object cache and array length limits, with stream resets](https://github.com/pfirmstone/JGDMS/wiki)
- [Java Deserialization Vulnerabilities - The Forgotten Bug Class (RuhrSec Edition)](http://www.slideshare.net/codewhitesec/java-deserialization-vulnerabilitesruhrseceditionv10) ([video](https://youtu.be/9Bw1urhk8zw))
- [What Do WebLogic, WebSphere, JBoss, Jenkins, OpenNMS, and Your Application Have in Common? This Vulnerability.](https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/)
