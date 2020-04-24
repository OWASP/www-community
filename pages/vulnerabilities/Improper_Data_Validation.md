---

layout: col-sidebar
title: Improper Data Validation
author: 
contributors: 
permalink: /vulnerabilities/Improper_Data_Validation
tags: vulnerability, Improper Data Validation

---

{% include writers.html %}

## Description

### Struts: Duplicate Validation Forms

Multiple validation forms with the same name indicate that validation logic is not up-to-date.

If two validation forms have the same name, the Struts Validator arbitrarily chooses one of the forms to use for input validation and discards the other. This decision might not correspond to the programmer's expectations. Moreover, it indicates that the validation logic is not being maintained, and can indicate that other, more subtle, validation errors are present.

**Example**

Two validation forms with the same name.

```
    <form-validation>
        <formset>
            <form name="ProjectForm">
            ...
            </form>
            <form name="ProjectForm">
            ...
            </form>
        </formset>
    </form-validation>
```

It is critically important that validation logic be maintained and kept in sync with the rest of the application. Unchecked input is the root cause of some of today's worst and most common software security problems. Cross-site scripting, SQL injection, and process control vulnerabilities all stem from incomplete or absent input validation. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

### Struts: Erroneous validate() Method

The validator form defines a `validate()` method but fails to call `super.validate()`.

The Struts Validator uses a form's `validate()` method to check the contents of the form properties against the constraints specified in the associated validation form. That means the following classes have a `validate()` method that is part of the validation framework:

```
    ValidatorForm
    ValidatorActionForm
    DynaValidatorForm
    DynaValidatorActionForm
```

If you create a class that extends one of these classes and if your class implements custom validation logic by overriding the `validate()` method, you must call `super.validate()` in your `validate()` implementation. If you do not, the Validation Framework cannot check the contents of the form against a validation form. In other words, the validation framework will be disabled for the given form.

Disabling the validation framework for a form exposes the application to numerous types of attacks. Unchecked input is the root cause of vulnerabilities like cross-site scripting, process control, and SQL injection. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

### Struts: Form Does Not Extend Validation Class

All Struts forms should extend a Validator class.

In order to use the Struts Validator, a form must extend one of the
following:

```
    ValidatorForm
    ValidatorActionForm
    DynaValidatorActionForm
    DynaValidatorForm.
```

You must extend one of these classes because the Struts Validator ties in to your application by implementing the `validate()` method in these classes.

Forms derived from the following classes cannot use the Struts Validator:

```
    ActionForm
    DynaActionForm
```

Bypassing the validation framework for a form exposes the application to numerous types of attacks. Unchecked input is the root cause of vulnerabilities like cross-site scripting, process control, and SQL injection. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

### Struts: Form Field Without Validator

Every field in a form should be validated in the corresponding validation form.

Omitting validation for even a single input field may allow attackers the leeway they need.

Unchecked input is the root cause of some of today's worst and most common software security problems. Cross-site scripting, SQL injection, and process control vulnerabilities all stem from incomplete or absent input validation. Although J2EE applications are not generally
susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

Some applications use the same ActionForm for more than one purpose. In situations like this, some fields may go unused under some action mappings. **It is critical that unused fields be validated too.** Preferably, unused fields should be constrained so that they can only be empty or undefined. If unused fields are not validated, shared business logic in an action may allow attackers to bypass the validation checks that are performed for other uses of the form.

### Struts: Plug-in Framework Not In Use

Use the Struts Validator to prevent vulnerabilities that result from unchecked input.

Unchecked input is the leading cause of vulnerabilities in J2EE applications. Unchecked input leads to cross-site scripting, process control, and SQL injection vulnerabilities, among others. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

To prevent such attacks, use the Struts Validator to check all program input before it is processed by the application.

Example uses of the validator include checking to ensure that:

- Phone number fields contain only valid characters in phone numbers
- Boolean values are only "T" or "F"
- Free-form strings are of a reasonable length and composition

### Struts: Unused Validation Form

An unused validation form indicates that validation logic is not up-to-date.

It is easy for developers to forget to update validation logic when they remove or rename action form mappings. One indication that validation logic is not being properly maintained is the presence of an unused validation form.

### Struts: Unvalidated Action Form

Every Action Form must have a corresponding validation form.

If a Struts Action Form Mapping specifies a form, it must have a validation form defined under the Struts Validator. If an action form mapping does not have a validation form defined, it may be vulnerable to a number of attacks that rely on unchecked input.

Unchecked input is the root cause of some of today's worst and most common software security problems. Cross-site scripting, SQL injection, and process control vulnerabilities all stem from incomplete or absent input validation. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

An action or a form may perform validation in other ways, but the Struts Validator provides an excellent way to verify that all input receives at least a basic level of checking. Without this approach, it is difficult, and often impossible, to establish with a high level of confidence that all input is validated.

### Struts: Validator Turned Off

This action form mapping disables the form's `validate()` method.

An action form mapping should never disable validation. Disabling validation disables the Struts Validator as well as any custom validation logic performed by the form.

#### Example

An action form mapping that disables validation.

```
    <action path="/download"
        type="com.website.d2.action.DownloadAction"
        name="downloadForm"
        scope="request"
        input=".download"
        validate="false">
    </action>
```

Disabling validation exposes this action to numerous types of attacks. Unchecked input is the root cause of vulnerabilities like cross-site scripting, process control, and SQL injection. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

### Struts: Validator Without Form Field

Validation fields that do not appear in forms they are associated with indicate that the validation logic is out of date.

It is easy for developers to forget to update validation logic when they make changes to an ActionForm class. One indication that validation logic is not being properly maintained is inconsistencies between the action form and the validation form.

#### Examples

#### Example 1

An action form with two fields.

```
    public class DateRangeForm extends ValidatorForm {
        String startDate, endDate;
        public void setStartDate(String startDate) {
            this.startDate = startDate;
        }
        public void setEndDate(String endDate) {
            this.endDate = endDate;
        }
    }
```

Example 1 shows an action form that has two fields, startDate and endDate.

##### Example 2

A validation form with a third field.

```
    <form name="DateRangeForm">
        <field property="startDate" depends="date">
            <arg0 key="start.date"/>
        </field>
        <field property="endDate" depends="date">
             <arg0 key="end.date"/>
        </field>
        <field property="scale" depends="integer">
             <arg0 key="range.scale"/>
        </field>
    </form>
```

Example 2 lists a validation form for the action form. The validation form lists a third field: scale. The presence of the third field suggests that `DateRangeForm` was modified without taking validation into account.

It is critically important that validation logic be maintained and kept in sync with the rest of the application. Unchecked input is the root cause of some of today's worst and most common software security problems. Cross-site scripting, SQL injection, and process control vulnerabilities all stem from incomplete or absent input validation. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Risk Factors

TBD

## Examples

## Related [Attacks](../attacks/)

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

## References

TBD

__NOTOC__
