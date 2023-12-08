## Project 5 : Roll Your Own CDN

## Contributors:

- Nitin Mutukula
- Rohan Devasthale

## Introduction

The building blocks of CDN include a DNS server, HTTP server with cache management and a system which maps the user with nearest replica.
In this project we built these building blocks from scratch without using any inbuilt python libraries.

## High Level Approach:

- Implementing a DNS server from scratch that will respond with the IP of nearest replica
- Implementing an HTTP server that will return the web pages as per requested by user
- Using Geolocation API to determine which replica is closest to the user by calculating the distance between user and replicas
- Implementing cache management system with LFU (Least Frequently Used) approach to improve the performance of the HTTP server

## Implementation Details:

The DNS server responds to domain name cs5700cdn.example.com. It uses UDP in order to communicate with the clients. After receiving the query the DNS server parses it and extracts the transaction ID, headers and other required information. It then prepares a response packet and returns the IP of best replica to the client that made the request. We used Geolocation API in order to determine the best replica possible for the user.  A query to https://freegeoip.app/  gives us the latitude and longitude of the user making the request. We then calculate the distance between user and the replica servers and determine the best possible replica based on the shortest distance. 

We also designed an HTTP server that will respond to the requests made by the client and serve them with the web pages. Our replica servers implement a cache management using the Least Frequenly Used (LFU) approach. We found out that this approach is faster when a resource is requested multiple times. We also wrote scripts that will automatically deploy, run and stop the CDN.

## Testing

We tested the DNS server from various locations around the globe to test the efficiency of the Geolocation approach. To test the cache management and HTTP server, we used tools like Postman and wget. We also used a script to perform stress testing. This script queried the replica servers for all the possible web pages. We tested the cache management and performance via this script.

## Challenges Faced:

- Understanding DNS packet and how DNS queries work using UDP
- Implementing DNS server from scratch
- Understanding cache management in HTTP server
- Calculating the distance between user and replica servers using geolocation api
- Implementation of LFU algorithm for cache management

## Design Decisions for improving efficiency

- Using the Geolocation API to determine the best possible replica by calculating the geographical distance between user and replica servers instead of calculating RTT which consumes significant mount of bandwidth and time.
- Using cache management system based on LFU algorithm.
- Caching the incoming IP addresses of the users in DNS server to increase the efficiency and response time.

## Future Possible Enhancements

- Improve cache management by compressing the files using some compression algorithm which will improve response time of HTTP replica servers.
- Storing the cache information of replica servers in DNS server and using this information to make a better decision of replica server.
- Using better algorithms than LFU for cache management of HTTP servers

## Citations:
- https://github.com/howCodeORG/howDNS/blob/master/dns.py
- All the videos on Youtube by HowCode about the same
- https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
- https://www.geeksforgeeks.org/json-loads-in-python/
- https://gist.github.com/rochacbruno/2883505
