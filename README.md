# Mapquest-API-Project
This programs uses the url, json, and mapquest api libraries to display route and geolocation information

First to use an API you must have access to it with something called an API Key

In the context of python using a mapquest API you make a http request in the form of url containing the key 
and details about what you would like the API to do for you

IN this program it involves finding a route to and from destinations given by the user.
This will involve making an http request unique to that scenario
If you want to find elevation data you would have to form another query with the same API key
and create another request in the form of a url

A url can be created from a string using urllib.parse.urlencode(string)

Once that url is created it must be encoded into bytes and then used by the urllib.request.urlopen(request_url)
This will return data from the mapquest application in the form of a nested dictionary known as a JSON object

A JSON is like a struct in cpp, or a dict in python, or like an object or class in javascript
It is a collection of fields and the data that corresponds to that field
The data that corresponds to a field can be a list, array, number, string, or another dictionary or HASH in and of itself

In Python JSON dictionaries can be converted into readable strings with JSON_INSTANCE.read().decode(enconding= some_encoding) 
#Usually utf-8

The string can be converted to a dictionary that python can use, using json.loads(dictstring)

A dictionary is like a Hash Table that has fields called keys you use to access its data, rather than indexes
d = {"John": 123, "JANE": [12,43] , "JAMES" : "PULL", "Don": 9000}
In Python there is no explicit type restriction on what the keys and data can be
to get 123 say --- > d["John"]
to get "ULL" say --> d["JAMES"][1:]
to get 12 say --> d["JANE"][0]
to get 9123 say --> d["John] + d["Don"]

e = {"John": {"A": 12 , "B": 13 , "C": 14} , 12 : [1,2,3,4] , "C" : 455}
This is possible and legal in python and the nesting of dictionaries has no limit as you'll see when you load JSON objects
x = e["John"]["B"] + e["John"]["C"] + e[12][3] + e["C"]
x =  13            +        14      +    4     + 455
x = 486

Also in these cases where the application makes use of GPS and the internet 
have exception handlers ready for network and HTTP errors

