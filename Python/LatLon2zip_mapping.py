import csv
from uszipcode import SearchEngine
from uszipcode import Zipcode
import fileinput

search = SearchEngine(simple_zipcode=True)

csv_file = open('farmersmarkets_OpenRefine.csv', mode='r')
csv_reader = csv.DictReader(csv_file)
line_count = 0
w_csv_file = open('xyz_r3.csv', mode='w')
for row in csv_reader:
    #print(line_count, row)
    if line_count == 0:
        #print(row)
        header = list(row)
        header.append("zip_from_xy")
        writer = csv.DictWriter(w_csv_file, fieldnames=header)
        writer.writeheader()
            
    
    zipc = row['zip']
    if len(zipc) > 5:
        row['zip'] = zipc[:5]
    lat, lon = row['x'], row['y']
    latf, lonf = True, True
    try:
        row['x'] = float(lat)
    except ValueError:
        latf = False
    try:
        row['y'] = float(lon)
    except ValueError:
        lonf = False
    if latf and lonf:
        try:
            result = search.by_coordinates(float(lon), float(lat), radius=30)
        except:
            print(lat, lon)
        if len(result) < 1:
            print("*", lon, lat)
            row["zip_from_xy"] = "lookup_zip_manually"
        else:
            row["zip_from_xy"] = result[0].zipcode
    else:
        row["zip_from_xy"] = ""

            #print(row)
    writer.writerow(row)
    line_count += 1
            #if line_count == 6:
            #    break
            #break
csv_file.close()
w_csv_file.close()
