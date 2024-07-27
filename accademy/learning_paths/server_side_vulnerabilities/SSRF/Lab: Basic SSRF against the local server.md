# Lab: Basic SSRF against the local server

## Description

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at <http://localhost/admin> and delete the user carlos.

[ACCESS LAB](<https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/ssrf-apprentice/ssrf/lab-basic-ssrf-against-localhost#>)

## Solution

1. __Ready your environment:__

    1. Launch your http proxy instance.
    1. Make sure its viewing the trafic as you navigate the page.

1. __Find the request to capture:__

    1. Click on any product.
    1. Scroll down and click the button with the text "Check stock".

1. __Find the http request:__

    1. Look for the request hitting the enpoint "/product/stock".
    1. Send that request to the section of your tool that lets you modify and resend requests.
    1. it original payload is:
        > stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D2%26storeId%3D1
    1. Change the payload to stockApi=<http://localhost/admin>.
    1. Send it.

1. __Analize the response:__

    1. Viewing the html response you will find an anchor tag that looks like this:
    ```<a href="/admin/delete?username=carlos">Delete</a>```.
    This reveals the actual api call to delete a user.
    1. Change the payload to:
        > stockApi=http:localhost/admin/delete?username=carlos
    1. Hit send and refresh the page to solve the lab.
