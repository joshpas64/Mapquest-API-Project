import ICS32Project3OutputClasses
import Ics32Proj3API



### Joshua Pascascio
### ID: 52192782
def take_inputs():
    '''Reads inputs of locations from users and fields that they might want displayed'''
    inputs = []
    outputs = []
    approved_outputs = ['STEPS','LATLONG','TOTALTIME','TOTALDISTANCE','ELEVATION']
    while True:
        try:
            number_of_locations = int(input())
            if(number_of_locations > 1):
                break
        except ValueError:
            print("Invalid int")


    for i in range(number_of_locations):
        locale = input()
        inputs.append(locale)

    while True:
        try:
            number_of_outputs = int(input())
            if (number_of_outputs  > 0):
                break
        except ValueError:
            print("Invalid integer")

    for i in range(number_of_outputs):
        output = input()
        while (output.upper() not in approved_outputs):
            print("Not valid")
            output = input()
        outputs.append(output)
    return inputs,outputs

def make_Output(outputs):
    '''Uses an user created output array to create the coinciding output classes'''
    if outputs.upper() == "STEPS":
        objects = ICS32Project3OutputClasses.Steps()
    elif outputs.upper() == "LATLONG":
        objects = ICS32Project3OutputClasses.LatLng()
    elif outputs.upper() == "TOTALTIME":
        objects = ICS32Project3OutputClasses.TotalTime()
    elif outputs.upper() == "TOTALDISTANCE":
        objects = ICS32Project3OutputClasses.TotalDistance()
    elif outputs.upper() == "ELEVATION":
        objects = ICS32Project3OutputClasses.Elevation()
    return objects
                                
def retrieve_outputs(outs,route_info):
    '''Duck type interface that outputs the fields of different object classes with the same method'''
    try:
        for i in outs:
            i.outputing(route_info)
            print()
    except KeyError:
        raise KeyError
    except:
        raise Ics32Proj3API.MapQuest_Error
        
def main_function():
    """User interface of the program that will use all modules"""
    try:
        print("A")
        user_Objects = take_inputs()
        user_Query = Ics32Proj3API.form_query(user_Objects[0])
        route_Data = Ics32Proj3API.make_API_dicts(user_Query)
        out_list = []
        for i in user_Objects[1]:
            out_list.append(make_Output(i))
        retrieve_outputs(out_list, route_Data)
    except KeyError:
        print("No Route Found")
    except Ics32Proj3API.MapQuest_Error:
        print("MAPQUEST ERROR")
if __name__=='__main__':        
    main_function()
    print()
    print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")




                                

        
