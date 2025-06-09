import os
import os.path
from datetime import date,datetime
def markAttendance(name):
    print("Entering")
    path = f'{date.today()}.csv'
    if not (os.path.isfile(path)):
        f = open(path,'w')
        print("File doesn't exist")
        f.close()
    else:
        print("File exist")
    nameList = []
    timeInList = []
    timeOutList = []
    presenceList = []
    with open(path,'r') as filer:
        myDataList = filer.readlines()
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            timeInList.append(entry[1])
            timeOutList.append(entry[2])
            presenceList.append(entry[3])
    if name not in nameList:
        with open(path,'a') as filea:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            filea.writelines(f'{name},{dtString},0,NA,0\n')
    else:
        index = nameList.index(name)
        timeIn = timeInList[index]
        timeIn = timeIn.strip()
        timeIn = datetime.strptime(timeIn,'%H:%M:%S')
        now = datetime.now()
        timeOut = now.strftime('%H:%M:%S')
        now = datetime.strptime(timeOut,'%H:%M:%S')
        inTimeDifference = str(now - timeIn)
        inTimeDifference = inTimeDifference.split(':')
        minutes = int(inTimeDifference[1])
        hours = int(inTimeDifference[0])
        print(minutes,hours)
        if minutes >= 1:
             with open(path,'w') as filew:
                for line in myDataList:
                    entry = line.split(',')
                    if entry[0] == name:
                        if minutes >= 3:
                            print("Reached")
                            filew.writelines(f'{name},{timeInList[index]},{timeOut},FULL,{hours}\n')
                        elif minutes >= 2:
                            filew.writelines(f'{name},{timeInList[index]},{timeOut},HALF,{hours}\n')
                        else:
                            filew.writelines(f'{name},{timeInList[index]},{timeOut},NA,{hours}\n')
                    else:
                            filew.writelines(line)
                            print("Writting", line)
        else:
            print(minutes)
                
markAttendance("ANU")

