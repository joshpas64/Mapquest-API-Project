####Joshua Pascascio
### ID: 52192782
##In this program for python to make a request it has to send it in the form of url that can open, parse, and throw error on url
## objects
import urllib.parse
import urllib.error
import json ## The end goal of what we want to have the API return data that we need, that data is in the form of a JSON object
##Usually json objects are long and have dictionaries nested in their dictionary responses i.e
#json1 = { 'latitude' : 0.341n , 'longitude': -91.2, 'moreinfo': [ { 'elevation' : 234, 'geography': rough, 'continent':north america},
#                                                                 { 'state': CA, 'city': LB, 'routeoptions' : ['walk', 'bus' , 'train', 'car']},
 #                                                                {'distance' : 1243 }], 'safety': 'very high'}
## To access this you would have to use a mix of dictionary and index notation
## For example to access 'bus' in json1 you write
## json1['moreinfo'][1]['routeoptions'][1]
## A way to get the fields or keys would be
## dict_name.keys() or something like that

##When you import a personal .py file into your python it must be referenced by filename
## Example: file1.py imports file2.py
## file2.py has functions doadd(x,y,z) and niceOutput() and constants CHANCE = 0.25 and DIMENSIONS = 12
## To access this in file1 youd have to do in your code file1.doadd(3,4,5) + file1.DIMENSIONS
## To skip assign early, including the function
## At top of file1

## do
## DIM = file1.DIMENSIONS
## Doadd = file1.doadd
## Now you could write instead Doadd(3,4,5) + DIM 
## Similar to typedef in cpp


import ICS32Project3OutputClasses

api_key = "IsRrd10PeKhW1LF1KIa4OHrgjZmRCvwE" ##You will need this for every api you use, it is unique to you, and might have some conditions
## or query limits
base_url = "http://open.mapquestapi.com/directions/v2/route?" ##Indicates you want the mapquest api to do a function for you
class MapQuest_Error(Exception):
    pass
def form_query(inputs: [str])->list:
    '''Takes input strings of locations and makes a list of field thatwill be added to a url'''
    query = [('key',api_key)] ##In Python make your query argument a list of tuples 
    for i in inputs:
        if inputs.index(i) == 0:
            query.append(('from',i)) ##Each tuple being in format ('field', value_you_wish_to_pass_in_as_that_field_
        else:
            query.append(('to',i))
    return query


def make_API_dicts(query : [tuple]):
    """Takes a query list which represent the key and the locations and adds it to the base url
    to make a route request, if approved, will return a json object"""
    try:
        new_url = base_url + urllib.parse.urlencode(query) ##url encode only takes list of tuple
        ## Remember many times, if not all, TCP,HTTP,and UDP send their info in BYTES
        ##Form the full request url
        encoded_dict = urllib.request.urlopen(new_url) ##Send it over http to mapquest and get its JSON result
        dict_string = encoded_dict.read().decode(encoding='utf-8') ##Turn result into a string make sure to decode first
        routeJson = json.loads(dict_string) ##Make string into a PYTHON dictionary
        return routeJson
    except urllib.error.HTTPError:
        raise MapQuest_Error

def get_elevation_Points(lat: float,lng: float):
    '''Latitude and Longitude Coordinates and returns the elevation at that spot'''
    try:
        url = "http://open.mapquestapi.com/elevation/v1/profile?" ##This query is for getting elevations rather than a route
        key = "IsRrd10PeKhW1LF1KIa4OHrgjZmRCvwE"
        e_Query = [('key', key)]
        latLngCollection = str(lat) + "," + str(lng)
        e_Query.append(('latLngCollection', latLngCollection))
        e_Query.append(('unit','f'))
        e_url = url + urllib.parse.urlencode(e_Query)
        elevationDict = urllib.request.urlopen(e_url)
        elevationString = elevationDict.read().decode(encoding='utf-8')  ##Same steps as before
        jSon = json.loads(elevationString)
        for i in jSon['elevationProfile']: ## In the json's elevationProfile field, there will be a list of dictionaries
            print(round(i['height'])) ## Each dictionary will have a height field, so let's print that value
    except:
        raise MapQuest_Error

def retrieve_coord(route_info)->list:
    '''Creates a pair of latitude and longitude coordinates from a route's
    set locations and returns a list of all their latitude and longitudes'''
    coordList = []
    for i in route_info['route']['locations']: ##in route_info json go to route field and in that field find locations field,
        #this will be a list of location dictionaries
        coordList.append(i['latLng']['lat']) ##Each will have a latLng Field, whose value is a dictionary, and the fields in that
        coordList.append(i['latLng']['lng']) ##dictionary will lng and lat, which will be our latitude and longitude coordinates
    return coordList
