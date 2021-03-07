import csv
import pandas as pd
import geopy
from geopy.geocoders import Nominatim
import time
import sys

'''
Take a csv file containing GPS coordinates with latitude and longitude
Run reverse geocoding on the file and generate complete addresses in a new csv file
Print progress to console
'''
# coordinates_file  = path_to_coordinates_csv_file
# output_file = path_to_output_file_with_addresses

user_agent = 'google'

df = pd.read_csv(coordinates_file)
count = 1
with open(output_file, "w") as output_csv:
    geolocator = Nominatim(user_agent=user_agent)
    for index, row in df.iterrows():
        (lat, lon) = row['GPS Latitude'], row['GPS Longitude']
        if  lat != 'None' and lon != 'None':
            coordinates = lat+','+lon
            locations = geolocator.reverse(coordinates, timeout=10000)
            output_csv.write(locations.address)
            output_csv.write('\n')
            print("[RECORD %s: ] %s" % (count, locations.address))
            time.sleep(50/1000)
        else:
            output_csv.write('None')
            output_csv.write('\n')
            print("[RECORD %s: ] None" % count)
        count = count + 1

