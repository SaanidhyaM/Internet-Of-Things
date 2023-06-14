import os
import csv
def adddevice():
    print("Add A New Device")
    print("=================================================")
    f1=open('devices.csv','r',newline='\r\n')
    f=open('devices.csv','a',newline='\r\n')
    s1=csv.reader(f1)
    s=csv.writer(f)
    dno=input('Enter Device No. = ')+"."
    for row in s1:
        if row[0]==dno:
            dno=input('Enter A Device No. That Has Not Been Added Before = ')+"."
        else:
            continue
    name=input('Enter Name = ')
    condition=input('Enter Condition Of Device[On/Off] = ')
    rec=[dno,name,condition]
    s.writerow(rec)
    f.close()
    print("Record Saved")
    print("=================================================")
    input("Press Enter To Continue...")

def switchdevice():
    print("Switch A Device On Or Off")
    print("=================================================")
    try:
        f=open('devices.csv','r',newline='\r\n') 
        f1=open('temp.csv','w',newline='\r\n')
        f1=open('temp.csv','a',newline='\r\n')
        r=input('Enter Device No. You Want To Switch: ')
        s=csv.reader(f)
        s1=csv.writer(f1)
        for rec in s:
            if rec[0]==r+".":
                print("Device No. = ",r)
                print("Name = ",rec[1])
                print("Condition = ",rec[2])
                choice=input("Do You Want To Switch This Device(y/n): ")
                if choice=='y' or choice=='Y':
                    dno=rec[0]
                    name=rec[1]
                    if rec[2]=="Off":
                        condition="On"
                    elif rec[2]=="On":
                        condition="Off"
                    rec=[dno,name,condition]
                    s1.writerow(rec)
                    print("Device Switched",condition)
                else:
                    s1.writerow(rec)
            else:
                s1.writerow(rec)
        f.close()   
        f1.close()
        os.remove("devices.csv")
        os.rename("temp.csv","devices.csv")
    except FileNotFoundError:
        print("File Not Found")
    print("=================================================")
    input("Press Enter To Continue...")

def editdevice():
    print("Edit An Existing Device")
    print("=================================================")
    try:
        f=open('devices.csv','r',newline='\r\n') 
        f1=open('temp.csv','w',newline='\r\n')
        f1=open('temp.csv','a',newline='\r\n')
        r=input('Enter Device No. You Want To Edit: ')
        s=csv.reader(f)
        s1=csv.writer(f1)
        for rec in s:
            if rec[0]==r+".":
                print("Device No. = ",r)
                print("Name = ",rec[1])
                print("Condition = ",rec[2])
                choice=input("Do You Want To Edit This Device(y/n): ")
                if choice=='y' or choice=='Y':
                    dno=rec[0]
                    name=input('Enter Name Of New Device = ')
                    condition=input('Enter Condition Of New Device[On/Off] = ')
                    rec=[dno,name,condition]
                    s1.writerow(rec)
                    print("Device Edited")
                else:
                    s1.writerow(rec)
            else:
                s1.writerow(rec)
        f.close()   
        f1.close()
        os.remove("devices.csv")
        os.rename("temp.csv","devices.csv")
    except FileNotFoundError:
        print("File Not Found")
    print("=================================================")
    input("Press Enter To Continue...")

def removedevice():
    print("Remove An Existing Device")
    print("=================================================")
    try:
        f=open('devices.csv','r',newline='\r\n') 
        f1=open('temp.csv','w',newline='\r\n')
        f1=open('temp.csv','a',newline='\r\n')
        r=input('Enter Device No. You Want To Remove: ')
        s=csv.reader(f)
        s1=csv.writer(f1)
        for rec in s:
            if rec[0]==r+".":
                print("Device No. = ",r)
                print("Name = ",rec[1])
                print("Condition = ",rec[2])
                choice=input("Do You Want To Remove This Device(y/n): ")
                if choice=='y' or choice=='Y':
                    pass
                    print("Device Removed")
                else:
                    s1.writerow(rec)
            else:
                s1.writerow(rec)
        f.close()
        f1.close()
        os.remove("devices.csv")
        os.rename("temp.csv","devices.csv")
    except FileNotFoundError:
        print("File Not Found")
    print("=================================================")
    input("Press Enter To Continue...")

def search():
    print("Search A Device")
    print("=================================================")
    try:
        f=open('devices.csv','r',newline='\r\n')
        r=input('Enter Device No. You Want To Search: ')
        s=csv.reader(f)
        i=0
        for rec in s:
            if rec[0]==r+".":
                print("Device Found")
                print("Device No. = ",r)
                print("Name = ",rec[1])
                print("Condition = ",rec[2])
                i+=1
        if i==0:
            print("Device Not Found")
        f.close()
    except FileNotFoundError:
        print("File Not Found")
    print("=================================================")
    input("Press Enter To Continue...")
    
def viewall():
    print("List All Devices")
    print("=================================================")
    try:
        f=open('devices.csv','r',newline='\r\n')
        s=csv.reader(f)
        gap=' '*3  #inter-field gap of 3 spaces 
        heading=f"{'Device No.':3s}{gap}{'Device Name':20s}{gap}{'Condition':5s}"
        print(heading)
        print("-------------------------------------------------")
        for rec in s:
            data=f"{rec[0]:10s}{gap}{rec[1]:20s}{gap}{rec[2]:^3s}"
            print(data)
        f.close()
    except FileNotFoundError:
        print("File Not Found")
    print("=================================================")
    input("Press Enter To Continue...")

def mainmenu():
    choice=0
    while choice!=7:
        print("\n")
        print("Main Menu")
        print("=================================================")
        print("1. Add A New Device")
        print("2. Switch A Device On Or Off")
        print("3. Edit An Existing Device")
        print("4. Remove An Existing Device")
        print("5. Search A Device")
        print("6. List All Devices")
        print("7. Exit")
        print("=================================================")
        choice=int(input('Enter Your Choice(The Corresponding Number): '))
        print("\n")
        if choice==1:
            adddevice()
        elif choice==2:
            switchdevice()
        elif choice==3:
            editdevice()
        elif choice==4:
            removedevice()
        elif choice==5:
            search()
        elif choice==6:
            viewall()
        elif choice==7:
            print("Exit Software")
            print("=================================================")
            print("Software Terminated")
            print("=================================================")
            break
mainmenu()
