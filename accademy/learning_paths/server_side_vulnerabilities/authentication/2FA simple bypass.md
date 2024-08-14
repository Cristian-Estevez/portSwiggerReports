# 2FA simple bypass

## Description

This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, access Carlos's account page.

- Your credentials: wiener:peter
- Victim's credentials carlos:montoya

[ACCESS LAB](https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/authentication-apprentice/authentication/multi-factor/lab-2fa-simple-bypass#)

## Solution

1. Navigate to "My account"
1. Enter victims credentials.
1. When prompted for the 2FA code go to the url bar in the browser and delete from the path the word `login2`
1. At this point you are already logged in as the victim.
1. Click "My account" to solve the lab
