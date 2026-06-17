
---

layout: col-sidebar
title: Insufficient Numeric Precision
author: Abdullah Al-Khalaf
contributors: 
permalink: /vulnerabilities/Insufficient_Numeric_Precision
tags: vulnerability, Insufficient Numeric Precision
auto-migrated: 1

---

{% include writers.html %}

## NVD Categorization
> [CWE-1339: Insufficient Precision or Accuracy of a Real Number](https://cwe.mitre.org/data/definitions/1339.html): The product processes a real number with an implementation in which the number's representation does not preserve required accuracy and precision in its fractional part, causing an incorrect result.

## Description
The use of real numbers with insufficient precision, such as `double` or `float` in most languages, can lead to unpredictable results and introduce bugs that attackers can exploit. 

## Risk Factors

TBD

## Examples

###  Example 1.0

In this scenario, a vulnerable bank uses the insufficient precision number data type, `double`:
```
public class VulnBank {  
    private double balance = 0.0;  
  
    public void deposit(double amount) {  
        balance += amount;  
    } 
    public void showBalance() {  
        System.out.println("Balance: " + balance);  
    }
    
    ...
      
}
```
An Attacker could deposit 0.1 dollar multiple times like so:
```
VulnBank attackerAcc = new VulnBank();
attackerAcc.deposit(0.1);
attackerAcc.deposit(0.1);
attackerAcc.deposit(0.1);
attackerAcc.showBalance();
```
One might believe the output would be `Balance: 0.3`, as it should. However, it outputs
```Balance: 0.30000000000000004```
At first glance, this is a negligible amount, but an attacker could do it multiple times, gaining significant profits.

## Solution
In many programming languages, they have a reliable decimal data type, for example, [BigDecimal](https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html) in Java, [decimal.Decimal](https://docs.python.org/3/library/decimal.html) in Python, etc. 

For example, the fixed code in [Example 1.0](#example-1.0) would be
```
import java.math.BigDecimal;

public class FixedVulnBank {  
    BigDecimal balance = BigDecimal.ZERO;  
  
    public void deposit(BigDecimal amount) {  
        balance = balance.add(amount);  
    }  
  
    public void showBalance() {  
        System.out.println("Balance: " + balance);  
    }
    
    ...
    
}
```
And the program would look like
```
FixedVulnBank acc = new FixedVulnBank();  
acc.deposit(new BigDecimal("0.1"));  
acc.deposit(new BigDecimal("0.1"));  
acc.deposit(new BigDecimal("0.1"));  
acc.showBalance(); // output: Balance: 0.3
```




## Related [Attacks](https://owasp.org/www-community/attacks/)

- [Denial of Service](https://owasp.org/www-community/attacks/Denial_of_Service)
- [Business logic vulnerability](https://owasp.org/www-community/vulnerabilities/Business_logic_vulnerability)

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

## Related [Controls](https://owasp.org/www-community/controls/)

## Related [Technical Impacts](Technical_Impacts "wikilink")

## References

- [CWE-1339](https://cwe.mitre.org/data/definitions/1339.html)
