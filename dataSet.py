#MAria I Suarez 
# 01/25/2022   
# LEarning how to read 'csv' files
#insurance_cost=250*age - 128*sex
#   + 370*bmi + 425*num+ 24000*smoker - 12500

import csv, os
os.system('cls')
#open file
file = open('insurance_data.csv')
print(type(file))  #Check what type of file

insuranceFile=csv.reader(file)
header= next(insuranceFile)
print(header)
insuranceData=[]
for row in insuranceFile:
    insuranceData.append(row)
    print(row)
# change female to 0
#change male to 1
for row in insuranceData:
    if 'female' in row:
        row[1]=0
    else:
        row[1]=1
    print(row)
    if 'y' in row:
        row[4]=1
    else:
        row[4]=0
    insurance_cost=250*int(row[0]) - 128*int(row[1]) + 370*float(row[2]) + 425*int(row[3]1+ 24000*smoker - 12500
#calculate the insurace cost and append value to the list

#Calculate the average insurance cost for the NorthWest region