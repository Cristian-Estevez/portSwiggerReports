# Username enumeration

- url: <https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/authentication-apprentice/authentication/password-based/lab-username-enumeration-via-different-responses>

## Description

This lab is vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

- [Candidate usernames](<https://portswigger.net/web-security/authentication/auth-lab-usernames>)
- [Candidate passwords](<https://portswigger.net/web-security/authentication/auth-lab-passwords>)

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

[ACCESS LAB](<https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/authentication-apprentice/authentication/password-based/lab-username-enumeration-via-different-responses#>)

## Solution

1. __Ready your environment:__

    1. Launch your http proxy instance.
    1. Make sure its viewing the trafic as you navigate th page.
    1. Save the wordlists into separate files in your filesystem.

1. __Find the apropriate request:__

    1. Navigate the page into "my account".
    1. Enter any username and password and submit.
    1. In your proxy capture tool loog for the request that hits the endpoint "/login" with the payload "username=[THE_USENAME_YOU_ENTERED]&password=[THE_PASSWORD_YOU_ENTERED]" and send it to your automate tool.

1. __Make the bruteforce for username:__

    1. Mark for automated replacemanet [THE_USENAME_YOU_ENTERED] in the request.
    1. Select from your filesystem the [Candidate usernames] wordlist you saved previously.
    1. Start the attack.

1. __Analize responses for username:__
    1. Search in responses for the text "Invalid username"
    1. When you find a request that does not have a match, check for the payload sent and that woul be the valid username.

1. __Make brute force for password:__

    1. In the request, unmark [THE_USERNAME_YOU_ENTERED], and paste the correct username you found in the previous step in its place.
    1. Now mark [THE_PASSWORD_YOU_ENTERED]
    1. Select from your filesystem the [Candidate passwords] wordlist you saved previously.
    1. Start the attack.

1. __Analize responses for password:__

    1. Go through the responses searching for the words "Incorrect password".
    1. When there's no match it means you got the correct one.

1. __Resolution:__

    1. Enter the correct usernam and passwords you found into the fields.
    1. You will get the lab as solved.

### Extras

Im attaching a brute force base python script you can tweak if you want to do this through command line. You will have to perform some changes in order to point to the right lab domain, the right files and the right payload fields you want to replace.
