# Lab: Web shell upload via Content-Type restriction bypass

## Description

This lab contains a vulnerable image upload function. It attempts to prevent users from uploading unexpected file types, but relies on checking user-controllable input to verify this.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: `wiener:peter`

[ACCESS LAB](https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/file-upload-apprentice/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass#)

## Solution

1. **Ready your environment:**

   1. Launch your http proxy instance.
   1. Make sure its viewing the trafic as you navigate the page.

1. **Prepare the exploit:**

   1. Since validation is only performed clientside in the browser. We need to intercept the request with the file and change it in transit.
   1. Select the file `./scripts/exploit.php.jpeg` for uploading
   1. Set your http proxy to capture requests.
   1. Click upload.
   1. See the captured request and edit the field where you see the filename you uploaded.
   1. Leave the name of the file as exploit.php.
   1. Forward the request.

1. **When the request succeded:**

   1. Go back to "my account".
   1. Inspect the avatar image, you will see an html image tag.
   1. Right click on it and select "Open in new tab".
   1. A new tab will open in the browser containing the secret.
   1. Submit the secret to solve the lab.
