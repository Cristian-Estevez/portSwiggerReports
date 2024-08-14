# Lab: Basic SSRF against another back-end system

## Description

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, use the stock check functionality to scan the internal `192.168.0.X` range for an admin interface on port 8080, then use it to delete the user carlos.

[ACCESS LAB](https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/ssrf-apprentice/ssrf/lab-basic-ssrf-against-backend-system#)

## Solution

1. **Ready your environment:**

   1. Launch your http proxy instance.
   1. Make sure its viewing the trafic as you navigate the page.

1. **Find the request to capture:**

   1. Click on any product.
   1. Scroll down and click the button with the text "Check stock".

1. **Find the http request:**

   1. Look for the request hitting the enpoint "/product/stock".
   1. Send that request to the section of your tool that lets you modify and resend requests.
   1. The original payload is:
      > stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D2%26storeId%3D1
   1. Send the request to the request automation section of your tool.

1. **Scan for the IP where the service runs:**

   1. Craft the payload to look like this:
      > stockApi=<http://192.168.0.X:8080/admin>.
   1. Mark "X" to be replaced each request by what the file ./ip_octet_wordlist.txt contains.
   1. Start the attack.

1. **Look for the successful request:**

   1. Find the request that responded with status code **200**.
   1. Send this request to the section of your tool that allows modifying the requests and resend.

1. **Analize the response:**

   1. Viewing the html response you will find an anchor tag that looks like this:
      `<a href="/admin/delete?username=carlos">Delete</a>`.
      This reveals the actual api call to delete a user.
   1. Change the payload to:
      > stockApi=http:[THE_IP_YOU_COPIED]/admin/delete?username=carlos
   1. Hit send and refresh the page to solve the lab.
