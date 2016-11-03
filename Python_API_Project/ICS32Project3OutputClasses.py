###Joshua Pascascio
## ID: 52192782

import urllib.parse
import urllib.request
import urllib.error
import json
import Ics32Proj3API
## ERRORS: KeyErrors, HTTP ERRORS 403


class Elevation:
    def outputing(self,route_info):
        print("Elevation")
        localeCoords = Ics32Proj3API.retrieve_coord(route_info)
        for i in range(0, len(localeCoords),2):
            Ics32Proj3API.get_elevation_Points(localeCoords[i],localeCoords[i+1])

class TotalTime:
    def outputing(self,route_info):
        response = "Total Time: " + str(round(route_info['route']['legs'][0]['time'] / 60)) + " minutes"
        print(response)
class TotalDistance:
    def outputing(self,route_info):
        st = "Total Distance: " + str(round(route_info['route']['legs'][0]['distance'])) + " miles"
        print(st)


class Steps:
    def outputing(self, route_info):
        print("DIRECTIONS")
        for i in route_info['route']['legs'][0]['maneuvers']:
            print(i['narrative'])
class LatLng:
    def outputing(self, route_info):
        print("LATLONGS")
        for i in route_info['route']['locations']:
            lng_suffix = ""
            lat_suffix = ""
            latit = i['displayLatLng']['lat']
            longit = i['displayLatLng']['lng']
            if (latit < 0):
                latit = latit * -1
                lat_suffix = "S"
            else:
                lat_suffix = "N"
            if(longit < 0):
                longit = longit * -1
                lng_suffix = "W"
            else:
                lng_suffix
            return_String = "{:.2f}{}, {:.2f}{}".format(latit,lat_suffix, longit,lng_suffix)
            print(return_String)

