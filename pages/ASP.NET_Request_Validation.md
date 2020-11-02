---

title: ASP.NET Request Validation
layout: col-sidebar
author:
contributors:
tags: ASP.NET
permalink: /ASP-NET_Request_Validation

---

{% include writers.html %}

# Description

*Request validation* is a feature in ASP.NET that examines HTTP requests and determines whether they contain potentially dangerous content. This check adds protection from mark-up or code in the URL query string, cookies, or posted form values that might have been added for malicious purposes. This exploit is typically referred to as a *cross-site scripting* (XSS) attack. Request validation helps to prevent this kind of attack by throwing a "potentially dangerous value was detected" error and halting page processing if it detects input that may be malicious, such as mark-up or code in the request.

# Do Not Rely on Request Validation for XSS Protection

Request validation is generally desirable and should be left enabled for defense in depth. It should **NOT** be
used as your sole method of XSS protection, and does not guarantee to catch every type of invalid input. There are known, documented bypasses (such as JSON requests) that will not be addressed in future releases, and the request validation feature is no longer provided in ASP.NET vNext.

Fully protecting your application from malicious input requires validating each field of user supplied data. This should start with
[ASP.NET Validation Controls](http://msdn.microsoft.com/en-us/library/debza5t0(v=vs.100).aspx) or
[DataAnnotations attributes](http://msdn.microsoft.com/en-us/library/ee256141(VS.100).aspx) to check for:

- Required fields
- Correct data type and length
- Data falls within an acceptable range
- Allow list of permitted characters

Any string input that is returned to the client should be encoded using an appropriate method, such as those provided via
[AntiXssEncoder](http://msdn.microsoft.com/en-us/library/system.web.security.antixss.antixssencoder(v=vs.110).aspx).

`var encodedInput = Server.HtmlEncode(userInput);`

# Enabling Request Validation

Request validation is enabled by default in ASP.NET. You can check to make sure it is enabled by reviewing the following areas:

<table>
<tbody>
<tr class="odd">
<td><p>style="width: 20%;"</p></td>
<td><p>ASP.NET Web Forms (Global)</p></td>
<td><p>Ensure that request validation is set to true (or not set at all) in web.config:</p>
<pre><code>&lt;pages validateRequest=&quot;true&quot; /&gt;</code></pre></td>
</tr>
<tr class="even">
<td><p>ASP.NET Web Forms (Page Level)</p></td>
<td><p>Check to make sure request validation is set to true (or not set at all) at the page level:</p>
<pre><code>&lt;@ Page ValidateRequest=&quot;false&quot; %&gt;</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td><p>ASP.NET 4.0+</p></td>
<td><p>Starting with ASP.NET 4.0 request validation is performed for all requests, not just for .aspx page requests. To ensure this is configured correctly requestValidationMode should be set to "4.0" (or not set at all) in web.config:</p>
<pre><code>&lt;httpRuntime requestValidationMode=&quot;4.0&quot; /&gt;</code></pre></td>
<td></td>
</tr>
<tr class="even">
<td><p>ASP.NET 4.5+</p></td>
<td><p>There are enhancements added to request validation starting with ASP.NET 4.5 that include deferred ("lazy") validation, the ability to opt-out at the server control level, and the ability to access unvalidated data. In order to leverage these enhancements you will need to ensure that requestValidationMode has been set to "4.5" in web.config:</p>
<pre><code>&lt;httpRuntime requestValidationMode=&quot;4.5&quot; targetFramework=&quot;4.5&quot; /&gt;</code></pre></td>
<td></td>
</tr>
<tr class="odd">
<td><p>ASP.NET Web API</p></td>
<td><p>ASP.NET Web API does not utilize the request validation feature to sanitize user input. You will need to add this protection manually if any input will be used in HTML output. For example if user input is returned to the browser as the result from an AJAX request to a Web API method.</p></td>
<td></td>
</tr>
</tbody>
</table>

# Selectively Disabling Request Validation

In some cases you may need to accept input that will fail ASP.NET Request Validation, such as when receiving HTML mark-up from the end
user. In these scenarios you should disable request validation for the smallest surface possible.

## ASP.NET Web Forms

For ASP.NET Web Forms applications prior to v4.5, you will need to disable request validation at the page level. Be aware that when doing
this all input values (cookies, query string, form elements) handled by this page will not be validated by ASP.NET.

`<@ Page ValidateRequest="false" %>`

Starting with ASP.NET 4.5 you can disable request validation at the individual server control level by setting `ValidateRequestMode` to `Disabled`.

`<asp:TextBox ID="txtASPNet" ValidateRequestMode="Disabled" runat="server" />`

## ASP.NET MVC

To disable request validation for a specific MVC controller action, you can use the `[ValidateInput(false)]` attribute as shown below.

```
[ValidateInput(false)]
public ActionResult Update(int userId, string description)
```

Starting with ASP.NET MVC 3 you should use the `[AllowHtml]` attribute to decorate specific fields on your view model classes where request validation should not be applied:

```
public class User
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    [AllowHtml]
    public string Description { get; set; }
    [AllowHtml]
    public string Bio { get; set; }
}
```

# Extending Request Validation

If you are using ASP.NET 4.0 or higher, you have the option of extending or replacing the Request Validation logic by providing your own class that descends from `System.Web.Util.RequestValidator`. By implementing this class, you can determine when validation occurs and what type of request data to perform validation on.

```
public class CustomRequestValidation : RequestValidator
{
    protected override bool IsValidRequestString(
        HttpContext context,
        string value,
        RequestValidationSource requestValidationSource,
        string collectionKey,
        out int validationFailureIndex)
    {
        validationFailureIndex = -1;

        // This is just an example and should not
        // be used for production code.
        if (value.Contains("<%"))
        {
            return false;
        }
        else // Leave any further checks to ASP.NET.
        {
            return base.IsValidRequestString(
                context,
                value,
                requestValidationSource,
                collectionKey,
                out validationFailureIndex);
        }
    }
}
```

This class is then registered in web.config using
`requestValidationType`:

```xml
<system.web>
    <httpRuntime requestValidationType="CustomRequestValidation"/>
</system.web>
```

# References

- [Request Validation in ASP.NET](http://msdn.microsoft.com/en-us/library/hh882339(v=vs.110).aspx)
- [Validation ASP.NET Controls](http://msdn.microsoft.com/en-us/library/debza5t0(v=vs.100).aspx)
- [How to: Validate Model Data Using DataAnnotations Attributes](http://msdn.microsoft.com/en-us/library/ee256141(VS.100).aspx)
- [AntiXssEncoder Class](http://msdn.microsoft.com/en-us/library/system.web.security.antixss.antixssencoder(v=vs.110).aspx)
- [New ASP.NET Request Validation Features](http://www.asp.net/aspnet/overview/aspnet-and-visual-studio-2012/whats-new#_Toc318097379)
- [Control.ValidateRequestMode Property](http://msdn.microsoft.com/en-us/library/system.web.ui.control.validaterequestmode(v=vs.110).aspx)
- [ValidateInputAttribute Class](http://msdn.microsoft.com/en-us/library/system.web.mvc.validateinputattribute(v=vs.118).aspx)
- [AllowHtmlAttribute Class](http://msdn.microsoft.com/en-us/library/system.web.mvc.allowhtmlattribute(v=vs.118).aspx)
- [RequestValidator Class](http://msdn.microsoft.com/en-us/library/system.web.util.requestvalidator(v=vs.110).aspx)