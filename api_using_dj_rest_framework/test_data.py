import csv
import io
import json

from decimal import Decimal
import requests
from django.contrib.gis.geos.point import Point
from django.core.files import File
CSV_URL = 'https://www.drivencarscanada.ca/feeds/drivencars-financeThat.csv'

with requests.Session() as s:
    download = s.get(CSV_URL)
    print(download) #get response 
    decoded_content = download.content.decode('utf-8') # get decoded content
    # print(decoded_content) 
    cr = csv.reader(decoded_content.splitlines(), delimiter=',') 
    # print(cr)
    my_list = list(cr) # get list of data
    # print(my_list)
    titles = my_list.pop(0) # pop index and get titles
    # print(titles)
    Total = len(my_list) # count total length 
    print(Total)
    Discarded = 0
    Added = 0
    updated = 0
    deleted = 0

    errorDataList = []
    isError = 0
    rowIndex = 0
    
    for i, item in enumerate(titles):
        if (item == "vehicle_id"):
            titles[i] = "dealer_vehicle_id"
        if (item == "vehicle_type"):
            titles[i] = "category"
        if (item == "VIN"):
            titles[i] = "vin"
        if (item == "Make"):
            titles[i] = "make"
        if (item == "Model"):
            titles[i] = "model"
        if (item == "Year"):
            titles[i] = "year"
        if (item == "Description"):
            titles[i] = "description"
        if (item == "Condition"):
            titles[i] = "v_condition"
        if (item == "Mileage"):
            titles[i] = "kilometer"
        if (item == "Hours"):
            titles[i] = "hours"
        if (item == "images"):
            titles[i] = "images"

        if (item == "Trim"):
            titles[i] = "trim"
        if (item == "Body_type"):
            titles[i] = "body_type"
        if (item == "Seating"):
            titles[i] = "seating"
        if (item == "transmission"):
            titles[i] = "transmission"
        if (item == "fuel_type"):
            titles[i] = "fuel_type"
        if (item == "Drivetrain"):
            titles[i] = "drive_train"
        if (item == "Cylinder"):
            titles[i] = "cylinder"
        if (item == "Engine_size_cc"):
            titles[i] = "engine"
        if (item == "int_color"):
            titles[i] = "color"
        if (item == "Price"):
            titles[i] = "price"
        if (item == "Location"):
            titles[i] = "location"
        if (item == "City"):
            titles[i] = "city"
        if (item == "Province"):
            titles[i] = "province"
        if (item == "Previous_owners"):
            titles[i] = "previous_owners"
        if (item == "Previous_accident"):
            titles[i] = "previous_accidents"
        if (item == "features"):
            titles[i] = "features"
    print(len(my_list))
    vehicle_list = []
    for row in my_list:
        vehicle_list.append(int(row[0])) 
    # print(vehicle_list) # get all vehicle_list
    items = {}
    # print('Row number', row) # get first row according to first vehicle
    rowIndex = rowIndex + 1
    # print(rowIndex)
    isError = 0
    VehicleMake = []
    VehicleModel = []
    VehicleBodyType = []
    VehicleFuelType = []
    VehicleDriveTrain = []
    for i, col in enumerate(row):
        print(i,col)
        item = None
        if col == "ATV":
            col = 3
            print("sdak",col) 
            type = col
        if col == "Automobile":
            col = 7
            type = col
        if i == 3:
            # item = VMake.objects.filter(PossibleTitles__icontains=col).first()
            if item:
                col = item.id
                make_id = item
                items["make_id"] = item.id
                print(item.id, 'Make found')
            else:
                isError = 1
                print(col, 'no Make found')
                VehicleMake.append(
                    'Row # ' + str(rowIndex) + ' : ' + col + ' - Make not found')
                break
                # make = VMake.objects.create(type_id=7, sub_type_id=None, make_name=col, is_active=1)
                # col = make.id
                # make_id = make
        if i == 4:
            # item = VModel.objects.filter(PossibleTitles__icontains=col).first()
            if item:
                col = item.id
                items["model_id"] = item.id
                print(item.id, 'Model found')
            else:
                isError = 1
                VehicleModel.append(
                    'Row # ' + str(rowIndex) + ' : ' + col + ' - Model not found')
                print(col, 'no Model found')
                break
                # model = VModel.objects.create(make_id=make_id, model_make=col, is_active=1)
                # col = model.id

        if i == 10:
            try:
                col = col.remove(" ", "")
            except:
                col = col
            col = col.split(",")
        if i == 12:
            # item = BodyType.objects.filter(PossibleTitles__icontains=col).first()
            if item:
                col = item.id
                items["body_type_id"] = item.id
                print(item.id, 'Body Type found')
            else:
                isError = 1
                print(col, 'no body type found')
                VehicleBodyType.append(
                    'Row # ' + str(rowIndex) + ' : ' + col + ' - Body Type not found')
                break
                # body = BodyType.objects.create(type_id=7, body_type=col)
                # col = body.id
        if i == 18:
            # item = FuelType.objects.filter(PossibleTitles__icontains=col).first()
            if item:
                col = item.id
                items["fuel_type_id"] = item.id
                print(item.id, 'Fuel Type found')
            else:
                isError = 1
                print(col, 'no Fuel Type found')
                VehicleFuelType.append(
                    'Row # ' + str(rowIndex) + ' : ' + col + ' - Fuel Type not found')
                break
                # fuel = FuelType.objects.create(fuel_type=col)
                # col = fuel.id
        if i == 19:
            if col == '4WD':
                col = '4x4'
            if col == 'Unk':
                col = 'Other'
            if col == '':
                col = 'Other'
            # item = DriveTrain.objects.filter(PossibleTitles__icontains=col).first()
            if item:
                col = item.id
                items["drive_train"] = item.id
                print(item.id, 'Drive Train if found')

        