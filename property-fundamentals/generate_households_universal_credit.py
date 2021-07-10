import simplekml
from development_district import wards
from development_district import coordinates
from development_district import district
#from statxplore_api.api import API as STATXPLORE_API
import requests
import json

#Define variables / lists
kml = simplekml.Kml()
colour = ['191400FF', '1E1400FF', '231400FF', '281400FF', '2D1400FF', '321400FF', '371400FF', '3C1400FF', '411400FF', '461400FF', '4B1400FF', '501400FF', '551400FF' ,'5A1400FF', '5F1400FF', '641400FF', '691400FF', '6E1400FF', '731400FF', '781400FF', '7D1400FF', '821400FF', '871400FF', '8C1400FF', '911400FF', '961400FF', '9B1400FF', 'A01400FF', 'A51400FF', 'AA1400FF']
#colour = ['1914E7FF', '1E14E7FF', '2314E7FF', '2814E7FF', '2D14E7FF', '3214E7FF', '3714E7FF', '3C14E7FF', '4114E7FF', '4614E7FF', '4B14E7FF', '5014E7FF', '5514E7FF' ,'5A14E7FF', '5F14E7FF', '6414E7FF', '6914E7FF', '6E14E7FF', '7314E7FF', '7814E7FF', '7D14E7FF', '8214E7FF', '8714E7FF', '8C14E7FF', '9114E7FF', '9614E7FF', '9B14E7FF', 'A014E7FF', 'A514E7FF', 'AA14E7FF']
universal_credit = [2388, 776, 2800, 1990, 1063, 1281, 1879, 1450, 1670, 1265, 1072, 1937, 1199, 1019, 1322, 1852]
ward_codes = ['E05002455', 'E05002456', 'E05002457', 'E05002458', 'E05002459', 'E05002460', 'E05002461', 'E05002462', 'E05002463', 'E05002464', 'E05002465', 'E05002466', 'E05002467', 'E05002468', 'E05002469', 'E05002470']


# url = 'https://stat-xplore.dwp.gov.uk/webapi/rest/v1/table'
# headers = {'Content-type': 'application/json','apikey':'65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a7063334d694f694a7a644849756333526c6247786863694973496e4e3159694936496e646b5a323979625746755147647459576c734c6d4e7662534973496d6c68644349364d5459794e5451354e5449334d5377695958566b496a6f69633352794c6d396b59534a392e664e67356b71762d506763346a376a3274496a67394d535f5f384748547833315251456c6330342d58586f'}
# r = requests.post(url, data=json.dumps(data), headers=headers)
# json_object = json.loads(r.content)
# json_formatted_str = json.dumps(json_object, indent=2)

# print(json_object["measures"][0]["label"])
# print(json_object["fields"][0]["items"][0]["labels"][0])
# print(json_object["fields"][1]["items"][0]["labels"][0])
# print(json_object["cubes"]["str:count:UC_Households:V_F_UC_HOUSEHOLDS"]['values'][0][0])

print(ward_codes)

universal_credit = []
pol = []
colour_scale = []
universal_credit_scale = []
#statxplore_api = STATXPLORE_API(key_path="../property-fundamentals/stat-xplore_api/key.txt")

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    
    # data = {
    # "database" : "str:database:UC_Households",
    # "measures" : ["str:count:UC_Households:V_F_UC_HOUSEHOLDS"],
    # "recodes": {
      # "str:field:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE": {
        # "map": [
          # [
            # "str:value:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE:V_C_MASTERGEOG11_WARD_TO_LA:" + ward_codes[h]
          # ],
        # ],
        # "total": True
      # },
      # "str:field:UC_Households:F_UC_DATE:DATE_NAME": {
        # "map": [
          # [
            # "str:value:UC_Households:F_UC_DATE:DATE_NAME:C_UC_DATE:202102"
          # ]
        # ],
        # "total": False
      # }
    # },
    # "dimensions": [
      # [
        # "str:field:UC_Households:F_UC_DATE:DATE_NAME"
      # ],
      # [
        # "str:field:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE"
      # ]
    # ]
    # }   

    # url = 'https://stat-xplore.dwp.gov.uk/webapi/rest/v1/table'
    # headers = {'Content-type': 'application/json','apikey':'65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a7063334d694f694a7a644849756333526c6247786863694973496e4e3159694936496e646b5a323979625746755147647459576c734c6d4e7662534973496d6c68644349364d5459794e5451354e5449334d5377695958566b496a6f69633352794c6d396b59534a392e664e67356b71762d506763346a376a3274496a67394d535f5f384748547833315251456c6330342d58586f'}
    # r[h] = requests.post(url, data=json.dumps(data), headers=headers)
    # json_object[h] = json.loads(r[h].content)
    # json_formatted_str[h] = json.dumps(json_object[h], indent=2)
    
    # universal_credit.append(json_object[h]["cubes"]["str:count:UC_Households:V_F_UC_HOUSEHOLDS"]['values'][0][0])

print(universal_credit)


#Generate price scaling information
max_universal_credit = max(universal_credit)
min_universal_credit = min(universal_credit)
delta = max_universal_credit - min_universal_credit
step = delta / (len(colour)-1)

#Normalise the colours in the price range
for i in range(0,len(colour)):
    colour_scale.insert(i,int(min_universal_credit + (i*step)))

#Assign a colour to the normalised house prices
for j in range(0,len(coordinates)):
    universal_credit_scale.append([])
    for k in range(0,len(colour_scale)):
        if (colour_scale[k] >= universal_credit[j]):
            universal_credit_scale.insert(j,colour[k])
            break
    #Add price and colour to the polygons
    #pol[j].description = json_object["measures"][0]["label"] + json_object["fields"][0]["items"][0]["labels"][0]
    pol[j].style.polystyle.color = universal_credit_scale[j]
    
#Save the polygons to a KML file
kml.save(district + "_universal credit" + ".kml")


