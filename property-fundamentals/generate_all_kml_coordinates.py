from govuk_api.ofns.api import API as OFNS_API
from doogal_api.api import API as DOOGAL_API
ofns_api = OFNS_API()
doogal_api = DOOGAL_API()
import geopy.distance
import numpy as np
from govuk_api.ofns.api import NoDistrictError
from govuk_api.ofns.api import MissingDistrictError
from govuk_api.ofns.api import NoWardError
from govuk_api.ofns.api import MissingWardError
from govuk_api.ofns.api import NoOFNSDataError

coordinates = []
wards = []

district = ofns_api.get_districts()
print(district)

#Ask the user for a district
#k_string = input("Please type an district number:")
#k = int(k_string)

#wards.append(ofns_api.get_wards_from_district(district[k]))

for k in range (0,len(district)):
    print(k)
    wards.append(ofns_api.get_wards_from_district(district[k])) 
    for j in range (0,len(wards[0])):
        try:
            coordinates.append(ofns_api.get_ward_polygon(district[k], wards[0][j]))
        except NoDistrictError as e:
                print("Error: Need to specify a district.")
        except MissingDistrictError as e:
                print("Error: Could not find district '" + district[k] + "' in the csv.")
        except NoWardError as e:
                print("Error: Need to specify a ward.")
        except MissingWardError as e:
                print("Error: Could not find ward '" + wards[0][j] + "' from district '" + district[k] + "'.")
        except NoOFNSDataError as e:
                print("Using Doogal API")
                coordinates.append(doogal_api.get_ward_polygon(district[k], wards[0][j]))

    with open("C:/Users/Anchal Goel/Desktop/Coordinates/" + district[k] + ".txt", "w") as f:
        for item in coordinates:
            f.write("%s\n" % coordinates)
    coordinates.clear()
    wards.clear()


