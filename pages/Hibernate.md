---

title: Hibernate
layout: col-sidebar
author:
contributors:
tags: java
permalink: /Hibernate

---

{% include writers.html %}

## Status

**In progress**

## Before you begin

Since ORM architecture isn't obvious, this document will explain some important things you need to know in order to analyze a Hibernate
application in a security context. This document assumes some SQL and database knowledge.

### A note about SQL injection

Since it is the hot topic, I will address it now but discuss in detail later.

- Hibernate does not grant immunity to SQL Injection, one can misuse the api as they please.
- There is nothing special about HQL (Hibernates subset of SQL) that makes it any more or less susceptible.
- Functions such as createQuery(String query) and createSQLQuery(String query) create a Query object that will be executed when the call to commit() is made. If the query string is
tainted you have sql injection. The details of these functions are covered later.

## Overview

### The problem Hibernate addresses

In object oriented systems, we represent entities as objects, and use a database to persist those objects. Generally these objects are
considered non-scalar values (non-primitive types). But many databases can only store and manipulate scalar values organized in tables. The
crux of the problem is translating those objects to forms which can be stored in the database, and which can later be retrieved easily, while
preserving the properties of the objects and their relationships; these objects are then said to be persistent. Hibernate attempts to address
this problem with Object/Relational Mapping (O/R M) by mapping attributes of objects we wish to persist to columns of a database.

[See original article.](http://en.wikipedia.org/wiki/Object-relational_mapping)

### How it works

- Usually Hibernate applications use [JavaBeans](http://en.wikipedia.org/wiki/JavaBean) style [POJOs](http://en.wikipedia.org/wiki/Plain_Old_Java_Object) to
represent objects we want to persist in a database.
- These objects should have an identifier property (i.e private class variable) used to represent it's primary key value in the database.
- This identifier will be mapped in a hibernate mapping file, usually with the default extension `.hbm.xml`, you will see this mapping in
the `<id>` element. This file will also map all other object properties we wish to preserve to columns in a database table, along with their data types and other stuff.
- Once objects are mapped, Hibernate provides the mechanism for you to store and access them via org.hibernate.Session and org.hibernate.Transaction objects.
- The Session object has methods to `save()` objects to a session, `load()` objects from a database and `createQuery()`s to be executed against the database.
- The Transaction object often wraps a database transaction, allowing one to `begin()` transactions, `commit()` changes, and `rollback()` to a previous state.
- Other classes worth mentioning: SessionFactory, TransactionFactory, and Query.
- Hibernate's main configuration file, extension .cfg.xml, provides basic setup for things like datasource, dialect, mapping files, etc.

[See this configuration example](http://www.owasp.org/index.php/Hibernate/config-example)

### Jargon

- **Transient** - The instance is not associated with a Session, has no persistent representation in the database and no identifier assigned. An object that has just been instantiated with the new
operator is said to be transient.
- **Persistent** - Is associated with a Session, has a representation in the database and has been assigned an identifier. Hibernate
synchronizes changes on a persistent object with its representation in the database when it completes a unit of work.
- **Detatched** - was once in a persistent state, but its session has been closed. The reference is still valid and the object may be modified and even reattached to a new session later.

### Hitting the database

The Session object represents the main interface or *conversation* between Java and Hibernate. A Session is used for a single request, or
unit of work. To make an object persistent, it must first be associated with a Session. But where does the session come from? Hibernate's
Configuration object instantiates a `SessionFactory (Configuration.buildSessionFactory())` which is an expensive, immutable,
thread safe object intended to be shared by all application threads. Threads that service client requests must obtain a Session from the
factory by calling `SessionFactory.getCurrentSession()` or `SessionFactory.openSession()`.

Anyways, a Session is NOT thread safe and there are associated concurrency issues discussed in 
[this section](https://www.owasp.org/index.php/Hibernate-Guidelines#Session_and_Concurrency_issues) of the Hibernate Guidelines page. 
Once an object is associated with a Session we can begin a transaction. All database communication must occur within the scope of a 
transaction. A transaction starts with a call to `Transaction.begin()` or `Session.beginTransaction()` and ends with a call to `Transaction.commit()`.

To actually build queries, store and retrieve data we mostly use methods in the Session class. For example, `load()` will instantiate a class
object, and load the state from the database into the instance. `Session.createQuery()` will return a Query object which has many methods
with which to operate on this query string. `Query.setParameter()`, `setFloat()`, and others act similar to prepared statements. You can also
simply call `Query.executeUpdate()` to execute the query.

*Ok, why don't we just see what it looks like.* Example1

```
Session sess = factory.openSession();
Transaction tx;
try {
     tx = sess.beginTransaction();
     Query q = sess.createQuery("from DomesticCat cat where cat.name = ?");
     q.setString(0, "Izi");
     tx.commit();
}
catch (Exception e) {
    if (tx!=null) tx.rollback();
    throw e;
}
finally {
    sess.close();
}
```

*Another simple example using HQL and named parameters...this time we have a helper class to obtain a Session*

```
Session session = HibernateUtil.getSessionFactory().getCurrentSession();
session.beginTransaction(); //All database communication occurs within the scope of a transaction

Person aPerson = (Person) session
        .createQuery("select p from Person p left join fetch p.events where p.id = :pid")
        .setParameter("pid", personId);

session.getTransaction().commit();
```

## Security Implications

These issues are discussed in context on this page and are also listed in [this section](https://www.owasp.org/index.php/Hibernate-Guidelines#Important)
of Hibernate Guidelines.

- No communication with the database should occur outside of a database transaction. Doing so will probably result in synchronization issues. Transactions should also not encompass user
think time. Details are of how it's done is discussed in the [Defining Transaction Bounds section](http://www.owasp.org/index.php/Hibernate#Defining_Transaction_Bounds) of this page.
- `createQuery()` can easily be passed a tainted SQL or HQL string, dialect is irrelevant. The proper way to construct a sql string
hibernate style is to use Query and SQLQuery's `setParameter()`, `setString()`, `setXXX()` methods for named parameter and placeholder
binding. Just like prepared statements. Details are discussed in the [Creating Queries section](http://www.owasp.org/index.php/Hibernate#Creating_Queries)
of this page.
- An application should rollback and discard Session instance on error. So if the Session throws an exception, the catch block should
have `rollback()` and finally should call `Session.close()`. This applies to any SQLException. Pretty cut and dry, see Example1 above.
- You may not mix and match JDBC-style parameters ("?") and named parameters (:namedparam) in the same query.

```
 Person aPerson = (Person) session
            .createQuery("select :somenamedparameter from ? where x = :someothernamedparameter");
```

- `Transaction.setTimeout(int)` should be called to ensure that misbehaving transactions do not tie up resources in definitely.

```
 Session sess = factory.openSession();
 try {
      //set transaction timeout to 3 seconds
      sess.getTransaction().setTimeout(3);
      sess.getTransaction().begin();
      // do some work
     ...
```

## Defining Transaction Bounds

Usually, ending a Session involves four distinct phases:

- flush the session
- commit the transaction
- close the session
- handle exceptions

Note:

- If `commit()` is present, no need to call `flush()` as it does this already.
- Most database communication methods only propagate exceptions if they're outside the scope of the session. (this is an assumption
based on the many functions whose source I've examined, I won't be perusing the entire api source to back this assumption)

Consider this example:

```
// Non-managed environment idiom
Session sess = factory.openSession();
Transaction tx = null;
try {
       tx = sess.beginTransaction();
       // do some work
       ...
       tx.commit();
}
catch (RuntimeException e) {
       if (tx != null) tx.rollback();
       throw e; // or display error message
}
finally {
       sess.close();
}
```

Most Common Functions:

- `Session.beginTransaction()` - begin transaction (doh)
- `Session.getTransaction()` - begin transaction
- `Session.flush()` - end transaction
- `Session.close()` - end session
- `Transaction.begin()` - begin transaction
- `Transaction.commit()` - end transaction
- `Transaction.rollback()` -

## Creating, manipulating and executing queries

- The Session interface defines methods that create Query and SQLQuery objects - these are the methods we care about because they allow the
developer to construct query strings (as opposed to letting Hibernate perform the sql operations).
- The Query/SQLQuery objects are mutable and executable, but are not actually SUNK until `Transaction.commit()`, or `Query.executeUpdate()`
is called. However, I think it is best that we flag functions that create and construct Query objects as they would be in direct
contact with tainted data.
- Once a Query or SQLQuery object is obtained from the Session, the parameters of its sql string should be set using the setter
functions like `setParameter()`, the setters are listed here. These setters check for type mismatch, or guess the type, then check for
positional mismatch and named parameter mismatch so they're pretty safe me thinks. Concatenating tainted parameters using the '+'
operator, on the other hand, would be equivalent to mis-using a prepared-statement.

Consider this example:

```
 String table = (String) req.getParameter("table");//obviously prone to tainted input
 String parameter1 = request.getParameter("param1");

 Session session = sessionFactory.getCurrentSession();
 try{
      session.beginTransaction();
            SQLQuery query = session.createSQLQuery("SELECT * FROM " + table + "WHERE stuff= ?"); /*B00*/
            query.setParameter(0, parameter1); /*YAY*/
      session.getTransaction().commit();
 } catch (Exception e) {}
 session.close();//omfg no rollback?
```

Most Common Functions:

- `Session.createSQLQuery(String queryString)` - creates a Query with given SQL string - technically executed on commit() or flush() but
this function is more directly related to the taint source.
- `Session.createQuery(String queryString)` - creates Query with given HQL string.
- `Session.createFilter(Object collection, String queryString)` - creates a Query with filter string.
- `Query.setParameter()` - variations on this binds parameters to "?" and ":namedparams"
- `Query.executeUpdate()` -
- `Query.getQueryString()` -

#### More Examples

Using queries from other Queries:

```
 String sql;

 session.beginTransaction();
      Query q1 = session.createQuery(taintSQL); //pretend taintSQL came from unchecked input
      sql = q1.getQueryString(); //get taintSQL
 session.getTransaction.commit();

 session.beginTransaction();
      Query q2 = new QueryImpl(sql, session, parameterMetadata); //reuse taintSQL w/o validation
      session.getTransaction.commit(); //evil prevails
 session.close();
```

Using executeUpdate()

```
 public void executeUpdateHQL(Session session, String evil)//a few calls deep from where evil became tainted
{
  Query query = session.createQuery(evil);  /*B00*/
  query.setString("name","Evil");
  query.setString("newName","EEvil"); //these don't matter if the sql is already evil
  int rowCount = query.executeUpdate();  /*B00*/
  System.out.println("Rows affected: " + rowCount);

  //See the results of the update and some other random stuff
  query = session.createQuery("from Supplier");
  List results = query.list();

  displaySupplierList(results);
}
```

named parameter (preferred)

```
Query q = sess.createQuery("from DomesticCat cat where cat.name = :name");
q.setString("name", "Fritz");
Iterator cats = q.iterate();
```

positional parameter

```
Query q = sess.createQuery("from DomesticCat cat where cat.name = ?");
q.setString(0, "Izi");
Iterator cats = q.iterate();
```

named parameter list

```
List names = new ArrayList();
names.add("Izi");
names.add("Fritz");
Query q = sess.createQuery("from DomesticCat cat where cat.name in (:namesList)");
q.setParameterList("namesList", names);
List cats = q.list();
```

Executing a bunch of actions (relevant fns listed in the excel sheet)

```
private List executions;
    ....
executions = new LinkedList();
    ....
private void executeActions(List list) throws HibernateException {
    for ( Iterator execItr = list.iterator(); execItr.hasNext(); ) {
        execute( (Executable) execItr.next() );
    }
    list.clear();
    session.getBatcher().executeBatch();
}
public void execute(Executable executable) {
    final boolean lockQueryCache = session.getFactory().getSettings().isQueryCacheEnabled();
    if ( executable.hasAfterTransactionCompletion() || lockQueryCache ) {
        executions.add( executable );
    }
    if (lockQueryCache) {
        session.getFactory()
            .getUpdateTimestampsCache()
            .preinvalidate( executable.getPropertySpaces() );
    }
    executable.execute();
}
```

## Persisting tainted data

- Assume persistent objects have JavaBeans style setter methods as this is most common practice. When these setters are called with tainted parameters consider this object to be tainted.
- We should flag all functions where tainted objects are made persistent. Although most documents will define `Session.save()` or `Session.persist()` as making an object persistent, it is actually
PENDING until a call to `Transaction.commit()` is made. Whether or not we want to flag the saves, or the commits is up to scan dev - keep
in mind that if we're flagging `commit()` we must first decide that the code between `Transaction.begin()` or `Session.beginTransaction()` and `Transaction.commit()` contains evil.
- The only associated cwe I can think of right now is stored xss.

Consider this example:

```
 Session session  = sessionFactory.getCurrentSession();
 String firstname = request.getParameter("firstname");
 String lastname  = request.getParameter("lastname");

 try{
      Transaction tx = session.beginTransaction();

      Person thePerson = session.load(Person.class, new Long(69));//loading an already persistent object
      thePerson.setFirstname(firstname);// then adding tainted data to it
      thePerson.setLastname(lastname);
      session.save(thePerson);  //persisting our changes

      session.getTransaction().commit();
 } catch (Exception e) {
      if (tx!=null) tx.rollback();
      throw e;
 }
     session.close();
```

Most Common Functions:

- `Session.save(Object object)` - save object to the session, object should not contain tainted data.
- `Session.persist(Object object)` -
- `Session.void replicate(Object object, ReplicationMode?? replicationMode)` -
- `Session.void saveOrUpdate(Object object)` -
- `Session.update(Object object)` -
- `Session.evict(Object object)` - remove instance from session cache
- `Session.clear()` - evict all loaded instances
- `Session.load(Class theClass, Serializable id)` - gets an object from the db for you to manipulate.
