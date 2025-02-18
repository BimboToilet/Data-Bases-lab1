import os
import math
import random
from distutils.dir_util import copy_tree
class DataBase:
    def __init__(self, name):
        self.name = name
        self.studentid=1
        self.variantid=1
        f = open(str(self.name)+"/students.txt",'w')
        t = open(str(self.name)+"/variants.txt",'w')
        table = open(str(self.name)+"/testingtable.txt",'w')
        f.close()
        t.close()
        table.close()
    def AddStudent(self, array):
        f = open(str(self.name)+"/students.txt",'r+')
        array = array.split()[1]+" "+array.split()[0]+" "+array.split()[2]+"\n"
        for i in f.readlines():
            if array.split()==i.split()[1:]:
                f.close()
                return 0
        f.seek(0,2)
        f.write(str(self.studentid)+" "+array)
        self.studentid+=1
        f.close()
    def AddVariant(self, array):
        t = open(str(self.name)+"/variants.txt",'r+')
        array+="\n"
        for i in t.readlines():
            if array.split()==i.split()[1:]:
                t.close()
                return 0
        t.seek(0,2)
        t.write(str(self.variantid)+" "+array)
        self.variantid+=1
        t.close()
    def DeleteStudent(self, ID):
        f = open(str(self.name)+"/students.txt",'r+')
        lines = f.readlines()
        for i in lines:
            if (i.split()[0]==ID):
                lines.remove(i)
        f.seek(0,0)
        for i in lines:
            f.write(i)
        f.truncate()
        f.close()
    def DeleteVariant(self, ID):
        t = open(str(self.name)+"/variants.txt",'r+')
        lines = t.readlines()
        for i in lines:
            if (i.split()[0]==ID):
                lines.remove(i)
        t.seek(0,0)
        for i in lines:
            t.write(i)
        t.truncate()
        t.close()
    def ChangeStudent(self, ID, array):
        f = open(str(self.name)+"/students.txt",'r+')
        array = array.split()[1]+" "+array.split()[0]+" "+array.split()[2]+"\n"
        lines = f.readlines()
        for i in lines:
            if (i.split()[1:]==array.split()):
                print("Impossible")
                f.close()
                return 0
        f.seek(0,0)
        for i in lines:
            if (i.split()[0]==ID):
                f.write(ID+" "+array)
            else:
                f.write(i)
        f.truncate()
        f.close()
    def ChangeVariant(self, ID, array):
        t = open(str(self.name)+"/variants.txt",'r+')
        lines = t.readlines()
        for i in lines:
            if (i.split()[1:]==array.split()):
                print("Impossible")
                t.close()
                return 0
        t.seek(0,0)
        for i in lines:
            if (i.split()[0]==ID):
                t.write(ID+" "+array)
            else:
                t.write(i)
        t.truncate()
        t.close()
    def PrintStudent(self, ID):
        f = open(str(self.name)+"/students.txt",'r+')
        line = f.readline()
        while line!="":
            if [str(s) for s in line.split()][0]==ID:
                print(*([str(s) for s in line.split()][1:]))
            line = f.readline()
        f.close()
    def PrintVariant(self, ID):
        t = open(str(self.name)+"/variants.txt",'r+')
        line = t.readline()
        while line!="":
            if [str(s) for s in line.split()][0]==ID:
                print(*([str(s) for s in line.split()][1:]))
            line = t.readline()
        t.close()
    def CreateTestingTable(self):
        f = open(str(self.name)+"/students.txt",'r+')
        t = open(str(self.name)+"/variants.txt",'r+')
        table = open(str(self.name)+"/testingtable.txt",'r+')
        stid=[]
        vaid=[]
        for i in f.readlines():
            stid.append(int([s for s in i.split()][0]))
        for i in t.readlines():
            vaid.append(int([s for s in i.split()][0]))
        for a in stid:
            table.write(str(a)+" "+str(random.choice(vaid))+"\n")
        table.truncate()
        table.close()
        f.close()
        t.close()
    def PrintTestingTable(self):
        f = open(str(self.name)+"/students.txt",'r+')
        t = open(str(self.name)+"/variants.txt",'r+')
        table = open(str(self.name)+"/testingtable.txt",'r+')
        students=[]
        variants=[]
        for i in f.readlines():
            students.append([str(s) for s in i.split()])
        for i in t.readlines():
            variants.append([str(s) for s in i.split()])
        for i in table.readlines():
            line=[str(s) for s in i.split()]
            for b in students:
                if line[0]==b[0]:
                    for a in variants:
                        if line[1]==a[0]:
                            print(b[1],b[2],b[3],a[1])
                            break
                    break
        table.close()
        f.close()
        t.close()
DataBasesList=[]
j=0
Input = input()
while True:
    if Input=="EXIT":
        break
    elif Input.split()[0]=="CREATE":
        if Input.split()[1]=="DATABASE":
            try:
                os.mkdir(str(Input.split()[2]))
            except OSError:
                pass
            DataBasesList.append(DataBase(str(Input.split()[2])))
            if j==0:
                j+=1
        if Input.split()[1]=="TABLE":
            DataBasesList[j-1].CreateTestingTable()
        if Input.split()[1]=="BACKUP":
            copy_tree(str(DataBasesList[j-1].name),"Backups/"+str(DataBasesList[j-1].name)+"/"+str(Input.split()[2]))      
    elif Input.split()[0]=="ADD":
        if Input.split()[1]=="STUDENT":
            str1=input()
            DataBasesList[j-1].AddStudent(str1)
        if Input.split()[1]=="VARIANT":
            str1=input()
            DataBasesList[j-1].AddVariant(str1)
    elif Input.split()[0]=="LOAD":
        if Input.split()[1]=="BACKUP":
            copy_tree("Backups/"+str(DataBasesList[j-1].name)+"/"+str(Input.split()[2]),str(DataBasesList[j-1].name))
    elif Input.split()[0]=="CHANGE":
        if Input.split()[1]=="DATABASE":
            for i in range(len(DataBasesList)):
                if (DataBasesList[i].name==Input.split()[2]):
                    j=i+1
        if Input.split()[1]=="STUDENT":
            str1=input()
            DataBasesList[j-1].ChangeStudent(str(Input.split()[2]), str1)
        if Input.split()[1]=="VARIANT":
            str1=input()
            DataBasesList[j-1].ChangeVariant(str(Input.split()[2]), str1)
    elif Input.split()[0]=="DELETE":
        if Input.split()[1]=="STUDENT":
            DataBasesList[j-1].DeleteStudent(str(Input.split()[2]))
        if Input.split()[1]=="VARIANT":
            DataBasesList[j-1].DeleteVariant(str(Input.split()[2]))
    elif Input.split()[0]=="PRINT":
        if Input.split()[1]=="STUDENT":
            DataBasesList[j-1].PrintStudent(str(Input.split()[2]))
        if Input.split()[1]=="VARIANT":
            DataBasesList[j-1].PrintVariant(str(Input.split()[2]))
        if Input.split()[1]=="TABLE":
            DataBasesList[j-1].PrintTestingTable()
    elif Input.split()[0]=="AUTO":
        if Input.split()[1]=="STUDENT":
            file = open(str(Input.split()[2]),'r')
            for i in file.readlines():
                DataBasesList[j-1].AddStudent(i)
            file.close()
        if Input.split()[1]=="VARIANT":
            file = open(str(Input.split()[2]),'r')
            for i in file.readlines():
                DataBasesList[j-1].AddVariant(i)
            file.close()
    else:
        print("Unknown command")
    Input=input()
