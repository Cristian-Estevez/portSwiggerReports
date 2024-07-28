# Lab: OS command injection, simple case

## Description

This lab contains an OS command injection vulnerability in the product stock checker.

The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

To solve the lab, execute the ```whoami``` command to determine the name of the current user.

[ACCESS LAB](<https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/os-command-injection-apprentice/os-command-injection/lab-simple#>)

## Solution

1. __Without intercepting the request :__

    1. Click in any product and scroll down until you see the button with the text "Check stock".
    1. Inspect the selection element with the developer tools. It Looks like this:

        ```html
        <select name="storeId">
          <option value="1">London</option>
          <option value="2">Paris</option>
          <option value="3">Milan</option>
        </select>
        ```

    1. The name attribute of that element is what the backend expects to be the parameter passed to the stock query function.
    1. Modify it to be like this:

        ```html
        <input name="storeId" value="&amp; whoami &amp;">
        ```

    1. We are setting the value to be ```& whoami &```
    1. Click the "Check stock" button to solve the lab.

1. __Intercepting the request :__

    1. This will be done with your http proxy tool. You must intercept and  change the request payload accordingly.
