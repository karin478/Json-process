import json
import time
import base64
from array import array

# get time
TimeForNow = int(time.time())

# read json file and store the information into data value
with open('res/data.json', 'r') as f:
    data = json.load(f)
print("original json：")
print(data)


# find which devices have time problem and delete it,
# each time of delete would use counter and avoid out of index
DeletCounter = 0
length = len(data["Devices"])
for i in range(length):
    if int(data["Devices"][i-DeletCounter]["timestamp"])<TimeForNow:
        del data["Devices"][i-DeletCounter]
        DeletCounter += 1


# encode and decode value from str to integer base on base64
TotalValue = 0
for i in range(len(data["Devices"])):
    decode_dict = base64.decodebytes(data["Devices"][i]["value"].encode('utf8'))
    TotalValue += int(decode_dict.decode())
print("total value = ", TotalValue)


# slice string to get uuid from info and add to an array/list
UUIDlist = []

for i in range(len(data["Devices"])):
    UUIDRes = ""
    Str = data["Devices"][i]["Info"]
    UUIDstart = Str.find(":")
    UUIDend = Str.find(",")
    UUIDRes = Str[UUIDstart+1:UUIDend]
    UUIDlist.append(UUIDRes)

print(UUIDlist)

data2 = {
    'ValueTotal': TotalValue,
    'UUIDS': UUIDlist
}

# write result data to the json
data2 = json.dumps(data2, indent=1)
with open("data2.json", 'w', newline='\n') as f:
 	f.write(data2)



print("Result data： ")
print(data2)
