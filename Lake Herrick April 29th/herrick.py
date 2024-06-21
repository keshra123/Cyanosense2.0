import pandas as pd 
import matplotlib.pyplot as plt
import os
import math


path, dirs, files = next(os.walk("/Users/keshra123/Results/Lake Herrick April 29th/Lake Herrick/"))
file_count = len(files)
print(file_count)
# create empty list
counted_list = []

UpSensorWavelengths = []
DwnSensorWavelengths = []
upTimeStamp = [] 
dwnTimeStamp = []
upReadings = []
dwnReadings = [] 

# append datasets to the list 
for i in range(file_count):
    temp_df = pd.read_csv("/Users/keshra123/Results/Lake Herrick April 29th/Lake Herrick/"+files[i], sep='delimiter', header=None, engine='python')
    res = []
    res1 = [] 
    for j in range(len(temp_df)):  
        if str(temp_df.iloc[j].values[0]) == "Wavelength Up (Sky)": 
        #Up Wavelengths
            UpWavelength = str(temp_df.iloc[j].values[0])
            #print(UpWavelength)
            Upwavelengths = str(temp_df.iloc[j+1].values[0])
            df1 = list(Upwavelengths.replace(',',' ').split(" "))[:-1]
            res = [eval(i) for i in df1] 
            #print(res)

        #Down Wavelengths 
            DwnWavelength = str(temp_df.iloc[j+2].values[0])
            Dwnwavelengths = str(temp_df.iloc[j+3].values[0])
            df2 = list(Upwavelengths.replace(',',' ').split(" "))[:-1]
            res1 = [eval(i) for i in df2]
            #print(res1)

        #Up Sensor (Downwelling) 
            UpSensor = str(temp_df.iloc[j+6].values[0])
            UpSensor = UpSensor.replace("Up", "Sky Reading")
            print(UpSensor)
            upTimeStamp.append(UpSensor)
            UpIntensities = str(temp_df.iloc[j+7].values[0])
            df3 = list(UpIntensities.replace(',',' ').split(" "))[:-1]
            res2 = [eval(i) for i in df3]
            upReadings.append(res2)
            #print(res2)

        #Down Sensor (Downwelling) 
            DwnSensor = str(temp_df.iloc[j+8].values[0])
            DwnSensor = DwnSensor.replace("Dwn", "Water Reading")
            print(DwnSensor)
            dwnTimeStamp.append(DwnSensor)
            DwnIntensities = str(temp_df.iloc[j+9].values[0])
            df4 = list(DwnIntensities.replace(',',' ').split(" "))[:-1]
            res3 = [eval(i) for i in df4]
            dwnReadings.append(res3)
            #print(res3)
            counted_list.append(i+1)
            UpSensorWavelengths = res 
            DwnSensorWavelengths = res1


#For Plotting
for i in range(len(counted_list)):
    if (i ==4):
        plt.plot(UpSensorWavelengths, upReadings[i],color='y',label=upTimeStamp[i])
        plt.plot(DwnSensorWavelengths, dwnReadings[i],color='m',label=dwnTimeStamp[i])
    else: 
        plt.plot(UpSensorWavelengths, upReadings[i],color='r',label=upTimeStamp[i])
        plt.plot(DwnSensorWavelengths, dwnReadings[i],color='g',label=dwnTimeStamp[i])

"""
#For Plotting Individual Graphs
plt.plot(UpSensorWavelengths, upReadings[8],color='r',label=upTimeStamp[8])
plt.plot(DwnSensorWavelengths, dwnReadings[8],color='g',label=dwnTimeStamp[8])
"""

#Labeling and Showing Graph
plt.xlabel("Wavelength") 
plt.ylabel("Intensities") 
plt.xlim(450,750)
plt.title("Lake Chapman Location 2") 
plt.legend() 
plt.show()




#Rrs Graph 

Epanel = dwnReadings[4]
Eup = dwnReadings[6]
Eup1 = dwnReadings[7]
Edwn = upReadings[6]
Edwn1 = upReadings[7]

Rrs = []
Rrs1 = []
Rrs2 = [] 
Rrs3 = []
Rrs4 = []
Rrs5 = [] 
Rrs6 = []
Rrs7 = []
Rrs8 = [] 
Rrs9 = []
Rrs10 = []
Rrs11 = []
Rrs12 = [] 
Rrs13 = []
Rrs14 = []
Rrs15 = []


for i in range(len(Epanel)):    
    value = (Eup[i] * (0.02 * Edwn[i])) / (1.01 * math.pi * Epanel[i])
    Rrs.append(value)
    value1 = (Eup1[i] * (0.02 * Edwn1[i])) / (1.01 * math.pi * Epanel[i])
    Rrs1.append(value1)
    #value2 = (Eup[i] * (0.02 * Edwn[i])) / (1.01 * math.pi * Epanel[i])
    #Rrs2.append(value2)
    #value3 = (Eup1[i] * (0.02 * Edwn1[i])) / (1.01 * math.pi * Epanel[i])
    #Rrs3.append(value3)


#print(Rrs1)
plt.plot(DwnSensorWavelengths, Rrs,color='r',label='Rrs')
plt.plot(DwnSensorWavelengths, Rrs1,color='g',label='Rrs1')
#plt.plot(DwnSensorWavelengths, Rrs2,color='b',label='Rrs2') 
#plt.plot(DwnSensorWavelengths, Rrs3,color='c',label='Rrs3')
#plt.plot(DwnSensorWavelengths, Rrs4,color='m',label='Rrs4')
#plt.plot(DwnSensorWavelengths, Rrs5,color='y',label='Rrs5')
#plt.plot(DwnSensorWavelengths, Rrs6,color='k',label='Rrs6')
#plt.plot(DwnSensorWavelengths, Rrs7,color='r',label='Rrs7')
plt.xlim(450,750)
plt.xlabel("Wavelength") 
plt.ylabel("Remote Sensing Reflectance (Rrs)") 
plt.title("Lake Chapman Location 2") 
plt.legend() 
plt.show()


#Files Used and Number
print("Files  Used: " +str(counted_list))
print("Number of Files Used: "+str(len(counted_list)))