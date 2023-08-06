Cloud Insight API
=======================

This is an example project which shows how to access the Cloud Insight API using Python.
Overview

The Cloud Insight API is a REST API which provides many services related to the Cloud Insight system. The data transmission protocol is JSON objects. The API receives and sends answers as JSON objects and HTTP errors or confirmation as HTTP status code. The CloudInsightAPI class provides an interface and some example methods to access the Cloud Insight API. All the objects accessed by the CloudInsightAPI class will have the JSON response converted to generic Python objects (Bunch) which can have their properties accessed by obj.property syntax instead of dictionary syntax. The print of the objects will return a JSON formatted string to facilitate the visualization of the object data. The requests are made using the Requests library and will raise requests.exceptions.RequestException when some request fail according to the status code error.

The program.py provide an example of a command line script implementation of the CloudInsightAPI class


