# Lab: File path traversal, traversal sequences blocked with absolute path bypass

## Description

This lab contains a path traversal vulnerability in the display of product images.

The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

To solve the lab, retrieve the contents of the ```/etc/passwd``` file.

[ACCESS LAB](<https://portswigger.net/web-security/learning-paths/path-traversal/common-obstacles-to-exploiting-path-traversal-vulnerabilities/file-path-traversal/lab-absolute-path-bypass#>)

## Solution

1. __Ready your environment:__

    1. Launch your http proxy instance.
    1. Make sure its viewing the trafic as you navigate the page.

1. __Fin the request to tamper:__

    1. Look for a request with a payload like ```filename=12.png``` that points to path ```/images```
    1. Send the request to the section of your proxy tool that allows modifying and resending.
    1. Alter the payload to be ```filename=/etc/passwd```.
    1. The response will have the content fo the passwd file from a linux server filesystem.
