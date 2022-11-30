import csv
import io
import json
import os
from decimal import Decimal

import django
import requests
from django.contrib.gis.geos.point import Point

# os.environ.setdefault("DJANGO_SETTINGS_MODULE",
#                       "blogs.settings")
# django.setup()
from django.core.files import File
from django.core.mail import send_mail
# from generic.models import AdDetails, AdImage, ImportLog
# from generic.serializers import AdDetailsSerializer, AdImageSerializer
# from users.models import NewUser
# from vehicle.models import (BodyType, DriveTrain, FuelType, TypeOfVehicle,
#                             VMake, VModel)
# from sentry_sdk import init, capture_message


        
CSV_URL = 'https://www.drivencarscanada.ca/feeds/drivencars-financeThat.csv'


with requests.Session() as s:
    download = s.get(CSV_URL)


    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    titles = my_list.pop(0)
    Total = len(my_list)
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
    user_id = 692
    vehicle_list = []
    # prev_ads = AdDetails.objects.filter(user_id = user_id)

    for row in my_list:
        vehicle_list.append(int(row[0]))
        items = {}

        rowIndex = rowIndex + 1
        print('Row number', row)
        isError = 0
        VehicleMake = []
        VehicleModel = []
        VehicleBodyType = []
        VehicleFuelType = []
        VehicleDriveTrain = []

        for i, col in enumerate(row):
            item = None
            if col == "ATV":
                col = 3
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
                    VehicleMake.append('Row # ' + str(rowIndex) + ' : ' + col + ' - Make not found')
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
                    VehicleModel.append('Row # ' + str(rowIndex) + ' : ' + col + ' - Model not found')
                    print(col, 'no Model found')
                    break
                    # model = VModel.objects.create(make_id=make_id, model_make=col, is_active=1)
                    # col = model.id
                

            if i == 10:
                try:
                    col = col.remove(" ","")
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
                    VehicleBodyType.append('Row # ' + str(rowIndex) + ' : ' + col + ' - Body Type not found')
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
                    VehicleFuelType.append('Row # ' + str(rowIndex) + ' : ' + col + ' - Fuel Type not found')
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
                else:
                    try:
                        # drive = DriveTrain.objects.filter(PossibleTitles__icontains='Other').first()
                        items["drive_train"] = drive.id
                        print(item.id, 'Drive Train try found')
                    except Exception as ex:
                        isError = 1
                        print(col, 'no drive train found')
                        items["drive_train"] = None
                        VehicleDriveTrain.append('Row # ' + str(rowIndex) + ' : ' + col + ' - Drive Train not found')
                        # capture_message(ex)  # Will create an event.
                        break
                # if item:
                #     col = item.id
                # else:
                #     # drive = DriveTrain.objects.create(drive_train=col)
                #     drive = DriveTrain.objects.filter(PossibleTitles__icontains='Other').first()
                #     col = drive.id
            if i == 31:
                features = col.split(',')
                feature_list = []
                for a, b in enumerate(features):
                    feature_dict = {}
                    feature_dict['id'] = a+1
                    feature_dict['v_features'] = str(b).strip()
                    feature_list.append(feature_dict)
                col = json.dumps(feature_list, separators=(',', ':'))
            items[titles[i]] = col
        # user = NewUser.objects.get(id=3)
        
        if isError == 1:
            if VehicleMake:
                errorDataList.append(VehicleMake);
            if VehicleModel:
                errorDataList.append(VehicleModel);
            if VehicleBodyType:
                errorDataList.append(VehicleBodyType);
            if VehicleFuelType:
                errorDataList.append(VehicleFuelType);
            if VehicleDriveTrain:
                errorDataList.append(VehicleDriveTrain);
            # Working capture_message
            # capture_message('Dealer Import error list : ' + str(errorDataList))  # Will create an event.
        elif isError == 0:
            items["user_id"] = user_id
            items["dealer_or_private_seller"] = 2
            items["user_type"] = 2
            items["has_bumpup"] = 1
            items["bumpup_active"] = 1
            items["price"]= round(float(items["price"]), 2)
            if items["engine"] == '':
                items["engine"] = 0
            if items["seating"] == '':
                items["seating"] = None
            if items["cylinder"] == '':
                items["cylinder"] = None
            if items["previous_owners"] == '':
                items["previous_owners"] = None
            if items["previous_accidents"] == '':
                items["previous_accidents"] = None
            items["listing_type"] = 3
            items["is_sold"] = 0
            items["is_active"] = 1
            items["hours"] = 0
            items["length"] = 0
            items["weight"] = 0
            items["longitude"] = "-89.2492720"
            items["latitude"] = "48.4108436"
            items["location_coords"] = Point((Decimal(items["longitude"]), Decimal(items["latitude"])),srid=4326)
            # try:
            #     # ad = AdDetails.objects.filter(dealer_vehicle_id=items["dealer_vehicle_id"])
            # except:
            #     ad = None
            if ad.count() >= 1:
                updated += 1
                serializer = AdDetailsSerializer(instance=ad[0], data=items, partial=True)
                if serializer.is_valid():
                    response = serializer.save()
                else:
                    print(serializer.errors,'errors')
            else:
                if (float(items["price"])> 0.00 and len(items["images"]) > 1 and items["vin"] !=''):
                    serializer = AdDetailsSerializer(data=items)
                    if serializer.is_valid():
                        response = serializer.save()
                        Added += 1
                        for i, url in enumerate(items["images"]):
                            name = url.split("/")[-1]
                            name = "generic/"+name
                            try:
                                db_image = AdImage.objects.get(image_path__icontains=name)
                            except:
                                if url != '':
                                    image = requests.get(url)
                                    image = io.BytesIO(image.content)                                
                                    image = AdImageSerializer(data={'ad_id': response.id, 'image_path': File(image, name=name.split("/")[-1]), 'photo': File(image, name=name.split("/")[-1]), 'thumbnail': File(image, name=name.split("/")[-1])})
                                    if image.is_valid():
                                        image.save()
                                    else: 
                                        print(image.errors)
                    else:
                        print(serializer.errors,'errors')
                else:
                    Discarded += 1
            
    for ad in prev_ads:
        if int(ad.dealer_vehicle_id) not in vehicle_list:
            ad.is_deleted=True
            ad.save()
            deleted += 1
            # send_mail(
            #     'A listing has been removed',
            #     f"""Hello,\n The listing below has been removed from Finance That.
            #     Listing ID: {ad.id}
            #     Vehicle: {ad.make}, {ad.model}, {ad.year}
            #     Dealer: "Driven Cars Canada"\n
            #     Regards
            #     Finance That
            #     https://www.financethat.ca
            #     1-844-354-5454""",
            #     'Finance That<listings@financethat.ca>',
            #     ['info@financethat.ca'],
            #     fail_silently=False,
            #     )

    
#     send_mail(
#     'Dealer Import Stats',
#     f"""Following Dealers were imported:\n
#     Total:{Total},
#     Added:{Added},
#     Discarded:{Discarded},
#     Deleted:{deleted},
#     Updated:{updated},
#     """,
#     'Finance That<info@financethat.ca>',
#     ['zeeshan.butt93@gmail.com','abidzain402@gmail.com'],
#     fail_silently=False,
# )
        
log = ImportLog.objects.create(dealer_id=user_id, total=Total, added=Added, discarded=Discarded, deleted=deleted, updated=updated)
