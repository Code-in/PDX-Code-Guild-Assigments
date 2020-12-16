

conversion_dict = {
    'ft' : {'ft' : 1, 'mi' : 0.000189394, 'm' : 0.3048, 'km' : 0.0003048  },
    'mi' : {'ft' : 5280, 'mi' : 1, 'm' : 1609.34, 'km' : 1.60934  }, 
    'm' : {'ft' : 3.28084, 'mi' : 0.000621371, 'm' : 1, 'km' : 0.001  },
    'km' : {'ft' : 3280.84, 'mi' : 0.621371, 'm' : 1000, 'km' : 1  }
}

# solution 1 allow user to enter distance in feet and return distance in meters
def prompt_user_for_a_distance():
     while True:
         dst = input("Enter a distance: ")
         if dst.isdigit():
             return dst


# convert the users unit type from various options into the key we need to access the ratio in the dictionary
def transform_to_unit_key(unit):
    unit = unit.lower()
    if unit in ['ft', 'f', 'feet']:
        return 'ft'
    elif unit in ['mi', 'mile']:
        return 'mi'
    elif unit in ['me', 'm', 'meter']:
        return 'm'
    elif unit in ['km', 'kilometer']:
        return 'km'
    else: 
        return 'ft'
    
# ask the user for the incoming unit type
def prompt_user_for_incoming_unit():
     while True:
        unit = input("Enter the distance unit type [ft - Feet, mi - Mile, m - Meters, km - Kilometers]: ")
        if unit in ['ft', 'f', 'feet', 'mi', 'mile', 'me', 'm', 'meter', 'km', 'kilometer']:
            return transform_to_unit_key(unit)

# ask the user for the outgoing unit type
def prompt_user_for_outgoing_unit():
     while True:
        unit = input("Enter the unit type to convert to [ft - Feet, mi - Mile, m - Meters, km - Kilometers]: ")
        if unit in ['ft', 'f', 'feet', 'mi', 'mile', 'me', 'm', 'meter', 'km', 'kilometer']:
            return transform_to_unit_key(unit)
          

# Version 1 allow user to enter distance in feet and return distance in meters
def version1():
     while True:
         ft = input("what is the distance in feet do you want converted to meters? ")
         if ft.isdigit():
             meters = int(ft) * conversion_dict['ft']['m']
             print(f"{ft} ft is {round(meters, 4)} m")

# Version 2 wants the user to set the incoming measurement type as well as specify the distance in that type then specify output type
def version2():  
    dst = prompt_user_for_a_distance() 
    iunit = prompt_user_for_incoming_unit()
    odst = int(dst) * conversion_dict[iunit]['m']
    print(f"{dst} {iunit} is {round(odst, 4)} meters")


# Version 3 wants the user to set the incoming measurement type as well as specify the distance in that type then specify output type
def version3():  
    dst = prompt_user_for_a_distance() 
    iunit = prompt_user_for_incoming_unit()
    ounit = prompt_user_for_outgoing_unit()
    odst = int(dst) * conversion_dict[iunit][ounit]
    print(f"{dst} {iunit} is {round(odst, 4)} {ounit}")


# Version 1
#version1()

# Version 2
#version2()

# Version 3
version3()