"""
Title: Unique Email Addresses
URL: https://leetcode.com/problems/unique-email-addresses/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75, Meta, etc
Topics: String, Stack, etc

Approach:
- very simple, but wordy
- just need to realize that you can split by @ sign
- then only need to process the local part by the rules
- then just add full simplified email to a set and return its length


Time Complexity: O(m * n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        all_emails = set()
        for email in emails:
            temp = email.split('@')
            local = temp[0]
            domain = temp[1]
            simplified_email = ""
            for c in local:
                if c == ".":
                    continue
                elif c == "+":
                    break
                else:
                    simplified_email += c
            simplified_email += "@"
            simplified_email += domain
            all_emails.add(simplified_email)
        
        return len(all_emails)



"""
Question:

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
 

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.
Domain names must contain at least one character before ".com" suffix.
"""