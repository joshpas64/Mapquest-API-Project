####Joshua Pascascio
### ID: 52192782
import urllib.parse
import urllib.error
import json
import ICS32Project3OutputClasses

api_key = "IsRrd10PeKhW1LF1KIa4OHrgjZmRCvwE"
base_url = "http://open.mapquestapi.com/directions/v2/route?"
class MapQuest_Error(Exception):
    pass
def form_query(inputs: [str])->list:
    '''Takes input strings of locations and makes a list of field thatwill be added to a url'''
    query = [('key',api_key)]
    for i in inputs:
        if inputs.index(i) == 0:
            query.append(('from',i))
        else:
            query.append(('to',i))
    return query


def make_API_dicts(query : [tuple]):
    """Takes a query list which represent the key and the locations and adds it to the base url
    to make a route request, if approved, will return a json object"""
    try:
        new_url = base_url + urllib.parse.urlencode(query)
        encoded_dict = urllib.request.urlopen(new_url)
        dict_string = encoded_dict.read().decode(encoding='utf-8')
        routeJson = json.loads(dict_string)
        return routeJson
    except urllib.error.HTTPError:
        raise MapQuest_Error

def get_elevation_Points(lat: float,lng: float):
    '''Latitude and Longitude Coordinates and returns the elevation at that spot'''
    try:
        url = "http://open.mapquestapi.com/elevation/v1/profile?"
        key = "IsRrd10PeKhW1LF1KIa4OHrgjZmRCvwE"
        e_Query = [('key', key)]
        latLngCollection = str(lat) + "," + str(lng)
        e_Query.append(('latLngCollection', latLngCollection))
        e_Query.append(('unit','f'))
        e_url = url + urllib.parse.urlencode(e_Query)
        elevationDict = urllib.request.urlopen(e_url)
        elevationString = elevationDict.read().decode(encoding='utf-8')
        jSon = json.loads(elevationString)
        for i in jSon['elevationProfile']:
            print(round(i['height']))
    except:
        raise MapQuest_Error

def retrieve_coord(route_info)->list:
    '''Creates a pair of latitude and longitude coordinates from a route's
    set locations and returns a list of all their latitude and longitudes'''
    coordList = []
    for i in route_info['route']['locations']:
        coordList.append(i['latLng']['lat'])
        coordList.append(i['latLng']['lng'])
    return coordList
