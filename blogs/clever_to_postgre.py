import psycopg2
import csv
import time
import clevercsv
conn = psycopg2.connect(
    "host=localhost dbname=copy_clever_to_plsql user=tenant_user password=cyBer@123")
cur = conn.cursor()
print(cur)
# with open("/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv", "r", newline="", encoding="utf-8") as fp:
#     detect_data_format = clevercsv.detect_dialect('/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv')
#     print(detect_data_format)
#     reader = clevercsv.reader(fp, delimiter=',', quotechar='"', escapechar='')
#     rows = next(reader)
#     for row in reader:
#         cur.execute(
#         "INSERT INTO cl_to_psql VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#         row)
#         time.sleep(2)
#         print(row)


# ----------------------------------------------------------------------------------------------------------
# with open("/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv", "r", newline="") as fp:
#   # you can use verbose=True to see what CleverCSV does
#   dialect = clevercsv.Sniffer().sniff(fp.read(), verbose=False)
#   fp.seek(0)
#   print(dialect)
#   reader = clevercsv.reader(fp, dialect)
#   print(reader)
#   rows = list(reader)
#   print(rows)

# ----------------------------------------------------------------------------------------------
# with open('/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader) # Skip the header row.
#     for row in reader:
#         cur.execute(
#         "INSERT INTO clevercsv VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#         row
#     )

# -------------------------------------------------------------------------------------------------

# with open("/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv", "r", newline="", encoding="utf-8") as fp:
#     detect_data_format = clevercsv.read_dicts(
#         '/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv')
#     # print(detect_data_format)
#     for row in detect_data_format:
#         all_values = (row['DealerID'], row['VehicleID'], row['SiteID'])
#         cur.execute(
#             "INSERT INTO new_table(VehicleID,DealerID,SiteID) VALUES (%s,%s,%s)", all_values)
#     print("done")

data = []
column = "DealerID"
f1= open("/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv", "r", newline="", encoding="utf-8")
f2 = open("/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds1.csv","r", newline="", encoding="utf-8")
detect_data_format = clevercsv.read_dicts(
    '/home/paradise/Documents/kuljit/api_using_dj_rest_framework/feeds.csv')
# print(detect_data_format)
reader1= clevercsv.reader(f1, delimiter=',', quotechar='"', escapechar='')
reader2 = clevercsv.reader(f2, delimiter=',', quotechar='"', escapechar='')

row1 = next(reader1)
row2 = next(reader2)
idx1 = row1.index("DealerID")
idx2 = row2.index("Stock")
for r1 in reader1:
    
    # if r1[idx1] and  r2[idx2] in r1 and  r2 :
        # print(idx1,idx2)
    data.append(r1[idx1])
for r2 in reader2:
    data.append(r2[idx2])
print(data)



conn.commit()
