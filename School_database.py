# Things to be added
# 1. Rank in class and subjectwise and overall grade to be added in records
# 2. To display class toppers rank wise
# 3. 

bla='python'            #THIS variable is for passwd
print('''If you are using this first time , then create database and tables for menu options and view functions:-
=> Each section I-X contain 3 sections A-C
=> XI and XII contain 4 section each of Science(Computer Science), Science(BIOLOGY), Commerce and Arts
Note:- Admission  no. should be unique for each student in school.''')

import mysql.connector
import pickle
from prettytable import PrettyTable


def create_database():
    # To create database for classes I-XII
    dbs=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
    for i in dbs:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla)
        mycursor=mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(i))
    print(f'DATABASE FOR CLASSES I TO XII CREATED!')

def create_table_I_X():
    # To create Tables(Class and section) for Classes I-X
    with open('Under Usage.dat','ab+') as f:
        pickle.dump([],f)
    dbs=['I','II','III','IV','V']
    tbs=['A','B','C','D']
    for i in dbs: 
        for j in tbs:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=i)
            mycursor=mydb.cursor()
            mycursor.execute('''CREATE TABLE IF NOT EXISTS {}_{}(
Adm_no      INT(5),
Name        VARCHAR(15),
Roll_no     int(4)          PRIMARY KEY, 
Father_name VARCHAR(15), 
Club        VARCHAR(8),
English1    int,
Hindi1      int,
Maths1      int,
Science1    int,
EVS1        int,
Total_mid   int,
English2    int,
Hindi2      int,
Maths2      int,
Science2    int,
EVS2        int,
Total_final int,
Overall     int,
Remarks     VARCHAR(4)
)'''.format(i,j))
    dbs=['VI','VII','VIII','IX','X']
    for i in dbs: 
        for j in tbs:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=i)
            mycursor=mydb.cursor()
            mycursor.execute('''CREATE TABLE IF NOT EXISTS {}_{}(
Adm_no       INT(5),
Name         VARCHAR(15),
Roll_no      int(4)          PRIMARY KEY, 
Father_name  VARCHAR(15), 
Club         VARCHAR(8),
English1     int,
Prac_Eng1    int,
Hindi1       int,
Prac_Hindi1  int,
Maths1       int,
Prac_Maths1  int,
Science1     int,
Prac_Scien1  int,
Social_Sc1   int,
Prac_Soc1    int,
Total_mid    int,
English2     int,
Prac_Eng2    int,
Hindi2       int,
Prac_Hindi2  int,
Maths2       int,
Prac_Math2   int,
Science2     int,
Prac_Scien2  int,
Social_Sc2   int,
Prac_Soc2    int,
Total_final  int,
Overall      int,
Remarks      VARCHAR(4)
)'''.format(i,j))

def create_table_X_XII():
    # To create Tables(Class and section) for Classes XI-XII
    dbs=['XI','XII']
    for i in dbs:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=i)
        mycursor=mydb.cursor() #Arts
        mycursor.execute('''CREATE TABLE IF NOT EXISTS {}_A(
Adm_no       INT(5),
Name         VARCHAR(15),
Roll_no      int(4)          PRIMARY KEY, 
Father_name  VARCHAR(15), 
Club         VARCHAR(8),
English1     int,
Prac_Eng1    int,
Sociology1   int,
Prac_Soc1    int,
Psychology1  int,
Prac_Psy1    int,
Geography1   int,
Prac_Geo1    int,
Economics1   int,
Prac_Eco1    int,
Total_mid    int,
English2     int,
Prac_Eng2    int,
Sociology2   int,
Prac_Soc2    int,
Psychology2  int,
Prac_Psy2    int,
Geography2   int,
Prac_Geo2    int,
Economics2   int,
Prac_Eco2    int,
Total_final  int,
Overall      int,
Remarks      VARCHAR(4)
)'''.format(i))
    for i in dbs:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=i)
        mycursor=mydb.cursor()#PCMB
        mycursor.execute('''CREATE TABLE IF NOT EXISTS {}_B(
Adm_no       INT(5),
Name         VARCHAR(15),
Roll_no      int(4)          PRIMARY KEY, 
Father_name  VARCHAR(15), 
Club         VARCHAR(8),
English1     int,
Prac_Eng1    int,
Maths1       int,
Prac_Math1   int,
Physics1     int,
Prac_Phy1    int,
Chemistry1   int,
Prac_Chem1   int,
Biology1     int,
Prac_Bio1    int,
Total_mid    int,
English2     int,
Prac_Eng2    int,
Maths2       int,
Prac_Math2   int,
Physics2     int,
Prac_Phy2    int,
Chemistry2   int,
Prac_Chem2   int,
Biology2     int,
Prac_Bio2    int,
Total_final  int,
Overall      int,
Remarks      VARCHAR(4)
)'''.format(i))
    for i in dbs:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=i)
        mycursor=mydb.cursor()#PCMC
        mycursor.execute('''CREATE TABLE IF NOT EXISTS {}_C(
Adm_no       INT(5),
Name         VARCHAR(15),
Roll_no      int(4)          PRIMARY KEY, 
Father_name  VARCHAR(15), 
Club         VARCHAR(8),
English1     int,
Prac_Eng1    int,
Maths1       int,
Prac_Math1   int,
Physics1     int,
Prac_Phy1    int,
Chemistry1   int,
Prac_Chem1   int,
Comp_Sc1     int,
Prac_Comp1   int,
Total_mid    int,
English2     int,
Prac_Eng2    int,
Maths2       int,
Prac_Math2   int,
Physics2     int,
Prac_Phy2    int,
Chemistry2   int,
Prac_Chem2   int,
Comp_Sc2     int,
Prac_Comp2   int,
Total_final  int,
Overall      int,
Remarks      VARCHAR(4)
)'''.format(i))
    for i in dbs:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=i)
        mycursor=mydb.cursor()#Commerce
        mycursor.execute('''CREATE TABLE IF NOT EXISTS {}_D(
Adm_no       INT(5),
Name         VARCHAR(15),
Roll_no      int(4)          PRIMARY KEY, 
Father_name  VARCHAR(15), 
Club         VARCHAR(8),
English1     int,
Prac_Eng1    int,
Maths1       int,
Prac_Maths1  int,
Bus_Studies1 int,
Prac_Bus1    int,
Accounts1    int,
Prac_Acc1    int,
Economics1   int,
Prac_Eco1    int,
Total_mid    int,
English2     int,
Prac_Eng2    int,
Maths2       int,
Prac_Maths2  int,
Bus_Studies2 int,
Prac_Bus2    int,
Accounts2    int,
Prac_Acc2    int,
Economics2   int,
Prac_Eco2    int,
Total_final  int,
Overall      int,
Remarks      VARCHAR(4)
)'''.format(i))
    print('CLASSES CREATED SUCCESSFULLY!')

def add_records(db):
    r='Y'
    while r.upper()=='Y': # for class I to V
        adm=int(input('Enter Admission no.: '))
        with open('Under Usage.dat','rb+') as f:
            all_adm=pickle.load(f)
        if adm not in all_adm :
            print("=> Sections are : A, B, C, D  ")
            all_adm+=[adm]
            with open ('Under Usage.dat','wb+') as p:
                pickle.dump(all_adm,p)
            if db.upper()=='I' or db.upper()=='II' or db.upper()=='III'or db.upper()=='IV'or db.upper()=='V':
                try:
                    sec=input('Enter Section: ')
                    name=input("Enter Student Name: ")
                    roll=int(input('Enter Roll No: '))
                    father=input("Enter Father's Name: ")
                    club=input('Enter Club: ')
                    print()
                    print(" ====Enter mid term marks of student====   ")
                    print()
                    eng1=int(input('Enter marks in English out of 100: '))
                    hin1=int(input('Enter marks in Hindi out of 100 : '))
                    mat1=int(input('Enter marks in Maths out of 100 : '))
                    sci1=int(input('Enter marks in Science out of 100  : '))
                    evs1=int(input('Enter marks in EVS out of 100 : '))
                    print()
                    print(" ====Enter final term marks of student====   ")
                    print()
                    eng2=int(input('Enter marks in English out of 100 : '))
                    hin2=int(input('Enter marks in Hindi out of 100 : '))
                    mat2=int(input('Enter marks in Maths out of 100 : '))
                    sci2=int(input('Enter marks in Science out of 100 : '))
                    evs2=int(input('Enter marks in EVS out of 100 : '))
                    to_mid=(eng1+hin1+mat1+sci1+evs1)//5
                    to_final=(eng2+hin2+mat2+sci2+evs2)//5
                    overall=(to_mid*(0.3))+(to_final*(0.7))
                    if overall>=33:
                        remark='PASS'
                    elif overall<33:
                        remark='FAIL'
                    mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
                    mycursor=mydb.cursor()
                    mycursor.execute("INSERT INTO {}_{} VALUES({},'{}',{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},'{}')".format(db,sec,adm,name,roll,father,club,eng1,hin1,mat1,sci1,evs1,to_mid,eng2,hin2,mat2,sci2,evs2,to_final,overall,remark))
                    mydb.commit()
                    print('Data inserted!')
                except Exception as e:
                    print(e)
            # For classes VI to X
            elif db.upper()=='VI' or db.upper()=='VII' or db.upper()=='VIII'or db.upper()=='IX'or db.upper()=='X':
                try :
                    sec=input("Enter section : ")
                    name=input("Enter Student's name : ")
                    roll=int(input("Enter Roll no. : "))
                    father=input("Enter father's name : ")
                    club=input("Enter Club : ")
                    print()
                    print(" ====Enter mid term marks of student====   ")
                    print()
                    eng1=int(input("Enter english marks out of 80 : "))
                    prac_eng1=int(input("Enter english practical marks out of 20 : "))
                    hindi1=int(input("Enter hindi marks out of 80  : "))
                    prac_hindi1=int(input("Enter hindi practical marks out of 20 : "))
                    maths1=int(input("Enter maths marks out of 80 : "))
                    prac_maths1=int(input("Enter maths practical marks out of 20 : "))
                    science1=int(input("Enter science marks out of 80 : "))
                    prac_science1=int(input("Enter science practical marks out of 20 : "))
                    social_sc1=int(input("Enter social science marks out of 80 : "))
                    prac_soc1=int(input("Enter social science practical marks out of 20 : "))
                    print()
                    print(" ====Enter final term marks of student==== ")
                    print()
                    eng2=int(input("Enter english marks out of 80 : "))
                    prac_eng2=int(input("Enter english practical marks out of 20 : "))
                    hindi2=int(input("Enter hindi marks out of 80 : "))
                    prac_hindi2=int(input("Enter hindi practical marks out of 20 : "))
                    maths2=int(input("Enter maths marks out of 80 : "))
                    prac_math2=int(input("Enter maths practical marks out of 20 : "))
                    science2=int(input("Enter science marks out of 80 : "))
                    prac_science2=int(input("Enter science practical marks out of 20 : "))
                    social_sc2=int(input("Enter social marks out of 80 : "))
                    prac_soc2=int(input("Enter social science practical marks out of 20 : "))
                    to_mid=(eng1+prac_eng1+hindi1+prac_hindi1+maths1+prac_maths1+science1+prac_science1+social_sc1+prac_soc1)//5
                    to_final=(eng2+prac_eng2+hindi2+prac_hindi2+maths2+prac_math2+science2+prac_science2+social_sc2+prac_soc2)//5
                    overall=(to_mid*(0.3))+(to_final*(0.7))
                    if overall>=33:
                        remark="PASS"
                    elif overall<33:
                        remark="FAIL"
                    mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
                    mycursor=mydb.cursor()
                    mycursor.execute("INSERT INTO {}_{} VALUES({},'{}',{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}')".format(db,sec,adm,name,roll,father,club,eng1,prac_eng1,hindi1,prac_hindi1,maths1,prac_maths1,science1,prac_science1,social_sc1,prac_soc1,to_mid,eng2,prac_eng2,hindi2,prac_hindi2,maths2,prac_math2,science2,prac_science2,social_sc2,prac_soc2,to_final,overall,remark))
                    mydb.commit()
                    print('Data inserted!')
                except Exception as e:
                    print(e)
            elif db.upper()=='XI' or db.upper()=='XII':# For XI and XII
                sec=input('Enter section: ')
                if sec.upper()=='A':# For Humanities input
                    try:
                        roll=int(input("Enter roll no. : "))
                        name=input("Enter name of student : ")
                        father=input("Enter father's name : ")
                        club=input("Enter Club : ")
                        print()
                        print(" ====Enter mid term marks of student====   ")
                        print()
                        eng1=int(input("Enter english marks out of 80 : " ))
                        prac_eng1=int(input("Enter english practical marks out of 20 : "))
                        socialogy1=int(input("Enter socialogy marks out of 80 : " ))
                        prac_soc1=int(input("Enter socialogy practical marks out of 20 : "))
                        psy1=int(input("Enter psycology marks out of 80 : " ))
                        prac_psy1=int(input("Enter psycology practical marks out of 20 : "))
                        geo1=int(input("Enter geography marks out of 80 : " ))
                        prac_geo1=int(input("Enter geography practical marks out of 20 : "))
                        eco1=int(input("Enter economics marks out of 80 : " ))
                        prac_eco1=int(input("Enter economics practical marks out of 20 : "))
                        print()
                        print(" ====Enter final term marks of student====   ")
                        print()
                        eng2=int(input("Enter englsh marks out of 80 : " ))
                        prac_eng2=int(input("Enter english practical marks out of 20 : "))
                        socialogy2=int(input("Enter socialogy marks out of 80 : " ))
                        prac_soc2=int(input("Enter socialogy practical marks out of 20 : "))
                        psy2=int(input("Enter psycology marks out of 80 : " ))
                        prac_psy2=int(input("Enter psycology practical marks out of 20 : "))
                        geo2=int(input("Enter geography marks out of 80 : " ))
                        prac_geo2=int(input("Enter geography practical marks out of 20 : "))
                        eco2=int(input("Enter economics marks out of 80 : " ))
                        prac_eco2=int(input("Enter economics practical marks out of 20 : "))
                        to_mid=(eng1+prac_eng1+socialogy1+prac_soc1+psy1+prac_psy1+geo1+prac_geo1+eco1+prac_eco1)//5
                        to_final=(eng2+prac_eng2+socialogy2+prac_soc2+psy2+prac_psy2+geo2+prac_geo2+eco2+prac_eco2)//5
                        overall=(to_mid*(0.3))+(to_final*(0.7))
                        if overall>=33:
                            remark="PASS"
                        elif overall<33:
                            remark="FAIL"
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
                        mycursor=mydb.cursor()
                        mycursor.execute("INSERT INTO {}_{} VALUES({},'{}',{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}')".format(db,sec,adm,name,roll,father,club,eng1,prac_eng1,socialogy1,prac_soc1,psy1,prac_psy1,geo1,prac_geo1,eco1,prac_eco1,eng2,prac_eng2,to_mid,socialogy2,prac_soc2,psy2,prac_psy2,geo2,prac_geo2,eco2,prac_eco2,to_final,overall,remark))
                        mydb.commit()
                        print('Data inserted!')
                    except Exception as e:
                        print(e)
                elif sec.upper()=='B':# For PCMB
                    try:
                        roll=int(input("Enter roll no. : "))
                        name=input("Enter name of student : ")
                        father=input("Enter father's name : ")
                        club=input("Enter Club : ")
                        print()
                        print(" ====Enter mid term marks of student====   ")
                        print()
                        eng1=int(input("Enter english marks out of 80 : " ))
                        prac_eng1=int(input("Enter english practical marks out of 20 : "))
                        maths1=int(input("Enter maths marks out of 80 : " ))
                        prac_maths1=int(input("Enter maths practical marks out of 20 : "))
                        physics1=int(input("Enter physics marks out of 80 : " ))
                        prac_physics1=int(input("Enter physics practical marks out of 20 : "))
                        chemistry1=int(input("Enter chemistry marks out of 80 : " ))
                        prac_chemistry1=int(input("Enter chemistry practical marks out of 20 : "))
                        biology1=int(input("Enter biology marks out of 80 : " ))
                        prac_biology1=int(input("Enter biology practical marks out of 20 : "))
                        print()
                        print(" ====Enter final term marks of student====   ")
                        print()
                        eng2=int(input("Enter english marks out of 80 : " ))
                        prac_eng2=int(input("Enter english practical marks out of 20 : "))
                        maths2=int(input("Enter maths marks out of 80 : " ))
                        prac_maths2=int(input("Enter maths practical marks out of 20 : "))
                        physics2=int(input("Enter physics marks out of 80 : " ))
                        prac_physics2=int(input("Enter physics practical marks out of 20 : "))
                        chemistry2=int(input("Enter chemistry marks out of 80 : " ))
                        prac_chemistry2=int(input("Enter chemistry practical marks out of 20 : "))
                        biology2=int(input("Enter biology marks out of 80 : " ))
                        prac_biology2=int(input("Enter biology practical marks out of 20 : "))
                        to_mid=(eng1+prac_eng1+maths1+prac_maths1+physics1+prac_physics1+chemistry1+prac_chemistry1+biology1+prac_biology1)//5
                        to_final=(eng2+prac_eng2+maths2+prac_maths2+physics2+prac_physics2+chemistry2+prac_chemistry2+biology2+prac_biology2)//5
                        overall=(to_mid*(0.3))+(to_final*(0.7))
                        if overall>=33:
                            remark="PASS"
                        elif overall<33:
                            remark="FAIL"
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
                        mycursor=mydb.cursor()
                        mycursor.execute("INSERT INTO {}_{} VALUES({},'{}',{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}')".format(db,sec,adm,name,roll,father,club,eng1,prac_eng1,maths1,prac_maths1,physics1,prac_physics1,chemistry1,prac_chemistry1,biology1,prac_biology1,to_mid,eng2,prac_eng2,maths2,prac_maths2,physics2,prac_physics2,chemistry2,prac_chemistry2,biology2,prac_biology2,to_final,overall,remark))
                        mydb.commit()
                        print('Data inserted!')
                    except Exception as e:
                        print(e)
                elif sec.upper()=='C':# For PCMC
                    try:
                        roll=int(input("Enter roll no. : "))
                        name=input("Enter name of student : ")
                        father=input("Enter father's name : ")
                        club=input("Enter Club : ")
                        print()
                        print(" ====Enter mid term marks of student====   ")
                        print()
                        eng1=int(input("Enter english marks out of 80 : " ))
                        prac_eng1=int(input("Enter english practical marks out of 20 : "))
                        maths1=int(input("Enter maths marks out of 80 : " ))
                        prac_maths1=int(input("Enter maths practical marks out of 20 : "))
                        physics1=int(input("Enter physics marks out of 80 : " ))
                        prac_physics1=int(input("Enter physics practical marks out of 20 : "))
                        chemistry1=int(input("Enter chemistry marks out of 80 : " ))
                        prac_chemistry1=int(input("Enter chemistry practical marks out of 20 : "))
                        comp_sc1=int(input("Enter computer science marks out of 80 : " ))
                        prac_comp_sc1=int(input("Enter computer science practical marks out of 20 : "))
                        print()
                        print(" ====Enter final term marks of student====   ")
                        print()
                        eng2=int(input("Enter english marks out of 80 : " ))
                        prac_eng2=int(input("Enter english practical marks out of 20 : "))
                        maths2=int(input("Enter maths marks out of 80 : " ))
                        prac_maths2=int(input("Enter maths practical marks out of 20 : "))
                        physics2=int(input("Enter physics marks out of 80 : " ))
                        prac_physics2=int(input("Enter physics practical marks out of 20 : "))
                        chemistry2=int(input("Enter chemistry marks out of 80 : " ))
                        prac_chemistry2=int(input("Enter chemistry practical marks out of 20 : "))
                        comp_sc2=int(input("Enter computer science marks out of 80 : " ))
                        prac_comp_sc2=int(input("Enter computer science practical marks out of 20 : "))
                        to_mid=(eng1+prac_eng1+maths1+prac_maths1+physics1+prac_physics1+chemistry1+prac_chemistry1+comp_sc1+prac_comp_sc1)//5
                        to_final=(eng2+prac_eng2+maths2+prac_maths2+physics2+prac_physics2+chemistry2+prac_chemistry2+comp_sc2+prac_comp_sc2)//5
                        overall=(to_mid*(0.3))+(to_final*(0.7))
                        if overall>=33:
                            remark="PASS"
                        elif overall<33:
                            remark="FAIL"
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
                        mycursor=mydb.cursor()
                        mycursor.execute("INSERT INTO {}_{} VALUES({},'{}',{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}')".format(db,sec,adm,name,roll,father,club,eng1,prac_eng1,maths1,prac_maths1,physics1,prac_physics1,chemistry1,prac_chemistry1,comp_sc1,prac_comp_sc1,to_mid,eng2,prac_eng2,maths2,prac_maths2,physics2,prac_physics2,chemistry2,prac_chemistry2,comp_sc2,prac_comp_sc2,to_final,overall,remark))
                        mydb.commit()
                        print('Data inserted!')
                    except Exception as e:
                        print(e)
                elif sec.upper()=='D': # For Commerce input
                    try:
                        roll=int(input("Enter roll no. : "))
                        name=input("Enter name of student : ")
                        father=input("Enter father's name : ")
                        club=input("Enter Club : " )
                        print()
                        print(" ====Enter mid term marks of student====   ")
                        print()
                        eng1=int(input("Enter english marks out of 80 : " ))
                        prac_eng1=int(input("Enter english practical marks out of 20 : "))
                        maths1=int(input("Enter maths marks out of 80 : " ))
                        prac_maths1=int(input("Enter maths practical marks out of 20 : "))
                        buisness1=int(input("Enter buisness studies marks out of 80 : " ))
                        prac_bus1=int(input("Enter buisness studies practical marks out of 20 : "))
                        accounts1=int(input("Enter accounts marks out of 80 : " ))
                        prac_acct1=int(input("Enter accounts practical marks out of 20 : "))
                        eco1=int(input("Enter economics marks out of 80 : " ))
                        prac_eco1=int(input("Enter economics practical marks out of 20 : "))
                        print()
                        print(" ====Enter final term marks of student====   ")
                        print()
                        eng2=int(input("Enter english marks out of 80 : " ))
                        prac_eng2=int(input("Enter english practical marks out of 20 : "))
                        maths2=int(input("Enter maths marks out of 80 : " ))
                        prac_maths2=int(input("Enter maths practical marks out of 20 : "))
                        buisness2=int(input("Enter buisness studies marks out of 80 : " ))
                        prac_bus2=int(input("Enter buisness studies practical marks out of 20 : "))
                        accounts2=int(input("Enter accounts marks out of 80 : " ))
                        prac_acct2=int(input("Enter accounts practical marks out of 20 : "))
                        eco2=int(input("Enter economics marks out of 80 : " ))
                        prac_eco2=int(input("Enter economics practical marks out of 20 : "))
                        to_mid=(eng1+prac_eng1+maths1+prac_maths1+buisness1+prac_bus1+accounts1+prac_acct1+eco1+prac_eco1)//5
                        to_final=(eng2+prac_eng2+maths2+prac_maths2+buisness2+prac_bus2+accounts2+prac_acct2+eco2+prac_eco2)//5
                        overall=(to_mid*(0.3))+(to_final*(0.7))
                        if overall>=33:
                            remark="PASS"
                        elif overall<33:
                            remark="FAIL"
                        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
                        mycursor=mydb.cursor()
                        mycursor.execute("INSERT INTO {}_{} VALUES({},'{}',{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}')".format(db,sec,adm,name,roll,father,club,eng1,prac_eng1,maths1,prac_maths1,buisness1,prac_bus1,accounts1,prac_acct1,eco1,prac_eco1,to_mid,eng2,prac_eng2,maths2,prac_maths2,buisness2,prac_bus2,accounts2,prac_acct2,eco2,prac_eco2,to_final,overall,remark))
                        mydb.commit()
                        print('Data inserted!')
                    except Exception as e :
                        print(e)
        else:
            print('Error: Duplicate entity: Admission no. already exists in this school!')
        r=input("Do you want to enter more data : ")
    
def delete_record(db) :
    sec=input('Enter section whose records are to be deleted: ')
    sec=sec.upper()
    ch=input('''
 +---------------------+
 | 1) Adm no           |
 | 2) Name             |
 | 3) Roll no          |
 | 4) club             |
 | 5) Remarks          |
 +---------------------+
Enter choice to be used to delete (1/2/3/4/5): ''')
    with open ('Under Usage.dat','rb+') as f:
        all_adm=pickle.load(f)
    if ch=='1':
        adm=int(input('Enter Adm no to delete: '))
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("select Adm_no from {}_{} where Adm_no={}".format(db,sec,adm))
            ar=mycursor.fetchall()
            no=mycursor.rowcount
            for i in ar:
                for j in i:
                    all_adm.remove(j)
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("DELETE FROM {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mydb.commit()
            print(f'{no} Records with Adm_no: {adm} deleted!')
            with open ('Under Usage.dat','wb+') as f:
                all_adm=pickle.dump(all_adm,f)
        except Exception as e:
            print(e)
    elif ch=='2':
        name=input('Enter Name to delete: ')
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("select Adm_no from {}_{} where Name='{}'".format(db,sec,name))
            ar=mycursor.fetchall()
            no=mycursor.rowcount
            for i in ar:
                for j in i:
                    all_adm.remove(j)
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("DELETE FROM {}_{} WHERE Name='{}'".format(db,sec,name))
            mydb.commit()
            print(f'{no} Records of Name: {name} deleted!')
            with open ('Under Usage.dat','wb+') as f:
                all_adm=pickle.dump(all_adm,f)
        except Exception as e:
            print(e)
    elif ch=='3':
        roll=int(input('Enter Roll no to delete: '))
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("select Adm_no from {}_{} where Roll_no={}".format(db,sec,roll))
            ar=mycursor.fetchall()
            no=mycursor.rowcount
            for i in ar:
                for j in i:
                    all_adm.remove(j)
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("DELETE FROM {}_{} WHERE Roll_no={}".format(db,sec,roll))
            mydb.commit()
            print(f'{no} Records with roll no: {roll} deleted!')
            with open ('Under Usage.dat','wb+') as f:
                all_adm=pickle.dump(all_adm,f)
        except Exception as e:
            print(e)
        
    elif ch=='4':
        club=input('Enter club to delete: ')
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("select Adm_no from {}_{} where Club='{}'".format(db,sec,club))
            ar=mycursor.fetchall()
            no=mycursor.rowcount
            for i in ar:
                for j in i:
                    all_adm.remove(j)
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("DELETE FROM {}_{} WHERE Club='{}'".format(db,sec,club))
            mydb.commit()
            print(f'{no} Records with club: {club} deleted!')
            with open ('Under Usage.dat','wb+') as f:
                all_adm=pickle.dump(all_adm,f)
        except Exception as e:
            print(e)
    elif ch=='5':
        # Like those who fail should be deleted for next year
        remark=input('Enter remark to delete: ')
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("select Adm_no from {}_{} where Remarks='{}'".format(db,sec,remark))
            ar=mycursor.fetchall()
            no=mycursor.rowcount
            for i in ar:
                for j in i:
                    all_adm.remove(j)
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("DELETE FROM {}_{} WHERE Remarks='{}'".format(db,sec,remark))
            mydb.commit()
            print(f'{no} Records with remark: {remark} deleted!')
            with open ('Under Usage.dat','wb+') as f:
                all_adm=pickle.dump(all_adm,f)
        except Exception as e:
            print(e)
    else:
        print('Enter valid choice!')
    

def display_whole_school():
    l1=['I','II','III','IV','V']
    l2=['VI','VII','VIII','IX','X','XI','XII']
    sec=['A','B','C','D']
    print()
    x = PrettyTable()
    x.field_names = ['Adm no','Name',"Father's Name",'Class','Club','TotMid','TotFinal','Overall','Remarks']    
    for i in l1:
        for j in sec:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=i)
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM {}_{}".format(i,j))
            rec=mycursor.fetchall()
            for k in rec :
                cls=f'{i}-{j}'
                x.add_row([k[0],k[1],k[3],cls,k[4],k[10],k[16],k[17],k[18]])
    for i in l2:
        for j in sec:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=i)
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM {}_{}".format(i,j))
            rec=mycursor.fetchall()
            for k in rec :
                cls=f'{i}-{j}'
                x.add_row([k[0],k[1],k[3],cls,k[4],k[15],k[26],k[27],k[28]])
    x.align['Name']='l'
    x.align["Father's Name"]='l'
    print(x.get_string(title="SCHOOL RECORDS"))




def see_full_records(db):
    print()
    l1=['I','II','III','IV','V']
    l2=['VI','VII','VIII','IX','X']
    if db.upper()=='XI' or db.upper=='XII':
        print(f'Class {db} unsupported for whole class records display. You can display records using sections!')
    elif db.upper() in l1:
        print(f'RECORDS FOR CLASS {db}')
        l3=['A','B','C','D']
        x = PrettyTable()
        x.field_names = ['Adm no','Name','Class','Engm','Hinm','Matm','Scim','EVSm','TotMid','Engf','Hinf','Matf','Scif','EVSf','TotFinal','Overall','Remarks']
        for i in l3:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM {}_{}".format(db,i))
            rec=mycursor.fetchall()
            for j in rec:
                cls=f'{db}-{i}'
                x.add_row([j[0],j[1],cls,j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],j[15],j[16],j[17],j[18]])
        x.align['Name'] ='l'
        print(x)
    elif db.upper() in l2:
        print(f'RECORDS FOR CLASS {db}')
        l4=['A','B','C','D']
        x = PrettyTable()
        x.field_names = ['Adm no','Name','Class','Engm','Hinm','Matm','Scim','SocScim','TotMid','Engf','Hinf','Matf','Scif','SocScif','TotFinal','Overall','Remarks']
        for i in l4:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM {}_{}".format(db,i))
            rec=mycursor.fetchall()
            for j in rec:
                clas=f'{db}-{i}'
                x.add_row([j[0],j[1],cls,j[5]+j[6],j[7]+j[8],j[9]+j[10],j[11]+j[12],j[13]+j[14],j[15],j[16]+j[17],j[18]+j[19],j[20]+j[21],j[22]+j[23],j[24]+j[25],j[26],j[27],j[28]])
        x.align['Name'] ='l'
        print(x.get_string(title=f"RECORDS FOR CLASS {db}"))
    else:
        print('Class not found!')


def see_part_sec(db):
    print()
    l1=['I','II','III','IV','V']
    l2=['VI','VII','VIII','IX','X']
    l3=['XI','XII']
    sec=input('Enter Section: ')
    sec=sec.upper()
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM {}_{}".format(db,sec))
        rec=mycursor.fetchall()
        x = PrettyTable()
        if db.upper() in l1:
            x.field_names = ['Adm no','Name','Roll no','Club','Engm','Hinm','Matm','Scim','EVSm','TotMid','Engf','Hinf','Matf','Scif','EVSf','TotFinal','Overall','Remarks']
            for j in rec:
                x.add_row([j[0],j[1],j[2],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],j[15],j[16],j[17],j[18]])
        elif db.upper() in l2:
            x.field_names = ['Adm no','Name','Roll no','Club','Engm','Hinm','Matm','Scim','SocScim','TotMid','Engf','Hinf','Matf','Scif','SocScif','TotFinal','Overall','Remarks']
            for j in rec:
                x.add_row([j[0],j[1],j[2],j[4],j[5]+j[6],j[7]+j[8],j[9]+j[10],j[11]+j[12],j[13]+j[14],j[15],j[16]+j[17],j[18]+j[19],j[20]+j[21],j[22]+j[23],j[24]+j[25],j[26],j[27],j[28]])
        elif db.upper() in l3:
            if sec in ' A ':
                x.field_names = ['Adm no','Name','Roll no','Club','Engm','Sociom','Psychom','Geogrm','Ecom','TotMid','Engf','Sociof','Psychof','Geogrf','Ecof','TotFinal','Overall','Remarks']
                for j in rec:
                    x.add_row([j[0],j[1],j[2],j[4],j[5]+j[6],j[7]+j[8],j[9]+j[10],j[11]+j[12],j[13]+j[14],j[15],j[16]+j[17],j[18]+j[19],j[20]+j[21],j[22]+j[23],j[24]+j[25],j[26],j[27],j[28]])
            elif sec.upper() in ' B':
                x.field_names = ['Adm no','Name','Roll no','Club','Engm','Matm','Phym','Chemm','Biom','TotMid','Engf','Matf','Phyf','Chemf','Biof','TotFinal','Overall','Remarks']
                for j in rec:
                    x.add_row([j[0],j[1],j[2],j[4],j[5]+j[6],j[7]+j[8],j[9]+j[10],j[11]+j[12],j[13]+j[14],j[15],j[16]+j[17],j[18]+j[19],j[20]+j[21],j[22]+j[23],j[24]+j[25],j[26],j[27],j[28]])
            elif sec.upper() in ' C ':
                x.field_names = ['Adm no','Name','Roll no','Club','Engm','Matm','Phym','Chemm','Compm','TotMid','Engf','Matf','Phyf','Chemf','Compf','TotFinal','Overall','Remarks']
                for j in rec:
                    x.add_row([j[0],j[1],j[2],j[4],j[5]+j[6],j[7]+j[8],j[9]+j[10],j[11]+j[12],j[13]+j[14],j[15],j[16]+j[17],j[18]+j[19],j[20]+j[21],j[22]+j[23],j[24]+j[25],j[26],j[27],j[28]])
            elif sec.upper() in ' D ':
                x.field_names = ['Adm no','Name','Roll no','Club','Engm','Matm','Busim','Accountsm','Ecom','TotMid','Engf','Matf','Busif','Accountsf','Ecof','TotFinal','Overall','Remarks']
                for j in rec:
                    x.add_row([j[0],j[1],j[2],j[4],j[5]+j[6],j[7]+j[8],j[9]+j[10],j[11]+j[12],j[13]+j[14],j[15],j[16]+j[17],j[18]+j[19],j[20]+j[21],j[22]+j[23],j[24]+j[25],j[26],j[27],j[28]])
        x.align['Name'] ='l'
        print(x.get_string(title=f"RECORDS FOR CLASS {db}-{sec}"))
    except Exception as e :
        print(e)

def see_part_student(db):
    l1=['I','II','III','IV','V']
    l2=['VI','VII','VIII','IX','X']
    l3=['XI','XII']
    sec=input('Enter section of student: ')
    adm=int(input('Enter adm no of student: '))
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd=q,database=db)
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM {}_{} WHERE Adm_no={}".format(db,sec,adm))
        rec=mycursor.fetchall()
        if db.upper() in l1:
            for i in rec:
                print('========================================================================================')
                print("                                 ST. MARK'S SCHOOL")
                print('========================================================================================')
                print('Name: ',i[1],' '*(40-len(i[1])),'Admission no.: ',i[0])
                print("Father's Name: ",i[3],' '*(31-len(i[3])),'Roll no.: ',i[2])
                print('Club: ',i[4],' '*(43-len(i[1])),'Class: ',db,'-',sec)
                x = PrettyTable()
                x.field_names = ['Subject','Mid Theory','Final Theory','Overall']
                x.add_row(['English',i[5],i[11],round((i[5]*0.3)+(i[11]*0.7)) ])
                x.add_row(['Hindi',i[6],i[12],round((i[6]*0.3)+(i[12]*0.7),2)  ])
                x.add_row(['Mathematics',i[7],i[13],round((i[7]*0.3)+(i[13]*0.7),2) ])
                x.add_row(['Science',i[8],i[14],round((i[8]*0.3)+(i[14]*0.7),2) ])
                x.add_row(['Envir. Studies',i[9],i[15],round((i[9]*0.3)+(i[15]*0.7),2)  ])
                x.align['Subject']='l'
                print(x)
                print('Overall percentage: ',i[17])
                print('Remarks: ',i[18])
                if i[18]=='PASS':
                    print('Insight:  Well done, Keep it up')
                elif i[18]=='FAIL':
                    print('Insight:  Keep Improving')
                print('========================================================================================')
        elif db.upper() in l2:
            for i in rec:
                print('================================================================================================')
                print("                                 ST. MARK'S SCHOOL")
                print('================================================================================================')
                print('Name: ',i[1],' '*(40-len(i[1])),'Admission no.: ',i[0])
                print("Father's Name: ",i[3],' '*(31-len(i[3])),'Roll no.: ',i[2])
                print('Club: ',i[4],' '*(43-len(i[1])),'Class: ',db,'-',sec)
                x = PrettyTable()
                x.field_names = ['Subject','Mid Theory','Mid Practical','Mid','Final Theory','Final Practical','Final','Overall']
                x.add_row(['English',i[5],i[6],i[5]+i[6],i[16],i[17],i[16]+i[17],round((((i[5]+i[6])*0.3)+((i[16]+i[17])*0.7)),2) ])
                x.add_row(['Hindi',i[7],i[8],i[7]+i[8],i[18],i[19],i[18]+i[19],round((((i[7]+i[8])*0.3)+((i[18]+i[19])*0.7)),2)  ])
                x.add_row(['Mathematics',i[9],i[10],i[9]+i[10],i[20],i[21],i[20]+i[21] ,round((((i[9]+i[10])*0.3)+((i[20]+i[21])*0.7)),2) ])
                x.add_row(['Science',i[11],i[12],i[11]+i[12],i[22],i[23],i[22]+i[23],round((((i[11]+i[12])*0.3)+((i[22]+i[23])*0.7)),2)  ])
                x.add_row(['Social Science',i[13],i[14],i[13]+i[14],i[24],i[25],i[24]+i[25],round((((i[13]+i[14])*0.3)+((i[24]+i[25])*0.7)),2)  ])
                x.align['Subject']='l'
                print(x)
                print('Overall percentage: ',i[27])
                print('Remarks: ',i[28])
                if i[28]=='PASS':
                    print('Insight:  Well done, Keep it up')
                elif i[28]=='FAIL':
                    print('Insight:  Keep Improving')
                print('================================================================================================')
        elif db.upper() in l3:
            for i in rec:
                if sec.upper() in ' A ':
                    print('================================================================================================')
                    print("                                 ST. MARK'S SCHOOL")
                    print('================================================================================================')
                    print('Name: ',i[1],' '*(30-len(i[1])),'Admission no.: ',i[0])
                    print("Father's Name: ",i[3],' '*(21-len(i[3])),'Roll no.: ',i[2])
                    print('Club: ',i[4],' '*(33-len(i[1])),'Class: ',db,'-',sec)
                    x = PrettyTable()
                    x.field_names = ['Subject','Mid Theory','Mid Practical','Mid','Final Theory','Final Practical','Final','Overall']
                    x.add_row(['English',i[5],i[6],i[5]+i[6],i[16],i[17],i[16]+i[17],round((((i[5]+i[6])*0.3)+((i[16]+i[17])*0.7)),2) ])
                    x.add_row(['Sociology',i[7],i[8],i[7]+i[8],i[18],i[19],i[18]+i[19],round((((i[7]+i[8])*0.3)+((i[18]+i[19])*0.7)),2)  ])
                    x.add_row(['Psychology',i[9],i[10],i[9]+i[10],i[20],i[21],i[20]+i[21] ,round((((i[9]+i[10])*0.3)+((i[20]+i[21])*0.7)),2) ])
                    x.add_row(['Geography',i[11],i[12],i[11]+i[12],i[22],i[23],i[22]+i[23],round((((i[11]+i[12])*0.3)+((i[22]+i[23])*0.7)),2)  ])
                    x.add_row(['Economics',i[13],i[14],i[13]+i[14],i[24],i[25],i[24]+i[25],round((((i[13]+i[14])*0.3)+((i[24]+i[25])*0.7)),2)  ])
                    x.align['Subject']='l'
                    print(x)
                    print('Overall percentage: ',i[27])
                    print('Remarks: ',i[28])
                    if i[28]=='PASS':
                        print('Insight:  Well done, Keep it up')
                    elif i[28]=='FAIL':
                        print('Insight:  Keep Improving')
                    print('================================================================================================')
                elif sec.upper() in ' B ':
                    print('================================================================================================')
                    print("                                 ST. MARK'S SCHOOL")
                    print('================================================================================================')
                    print('Name: ',i[1],' '*(30-len(i[1])),'Admission no.: ',i[0])
                    print("Father's Name: ",i[3],' '*(21-len(i[3])),'Roll no.: ',i[2])
                    print('Club: ',i[4],' '*(33-len(i[1])),'Class: ',db,'-',sec)
                    x = PrettyTable()
                    x.field_names = ['Subject','Mid Theory','Mid Practical','Mid','Final Theory','Final Practical','Final','Overall']
                    x.add_row(['English',i[5],i[6],i[5]+i[6],i[16],i[17],i[16]+i[17],round((((i[5]+i[6])*0.3)+((i[16]+i[17])*0.7)),2) ])
                    x.add_row(['Mathematics',i[7],i[8],i[7]+i[8],i[18],i[19],i[18]+i[19],round((((i[7]+i[8])*0.3)+((i[18]+i[19])*0.7)),2)  ])
                    x.add_row(['Physics',i[9],i[10],i[9]+i[10],i[20],i[21],i[20]+i[21] ,round((((i[9]+i[10])*0.3)+((i[20]+i[21])*0.7)),2) ])
                    x.add_row(['Chemistry',i[11],i[12],i[11]+i[12],i[22],i[23],i[22]+i[23],round((((i[11]+i[12])*0.3)+((i[22]+i[23])*0.7)),2)  ])
                    x.add_row(['Biology',i[13],i[14],i[13]+i[14],i[24],i[25],i[24]+i[25],round((((i[13]+i[14])*0.3)+((i[24]+i[25])*0.7)),2)  ])
                    x.align['Subject']='l'
                    print(x)
                    print('Overall percentage: ',i[27])
                    print('Remarks: ',i[28])
                    if i[28]=='PASS':
                        print('Insight:  Well done, Keep it up')
                    elif i[28]=='FAIL':
                        print('Insight:  Keep Improving')
                    print('================================================================================================')
                elif sec.upper() in ' C ':
                    print('================================================================================================')
                    print("                                 ST. MARK'S SCHOOL")
                    print('================================================================================================')
                    print('Name: ',i[1],' '*(30-len(i[1])),'Admission no.: ',i[0])
                    print("Father's Name: ",i[3],' '*(21-len(i[3])),'Roll no.: ',i[2])
                    print('Club: ',i[4],' '*(33-len(i[1])),'Class: ',db,'-',sec)
                    x = PrettyTable()
                    x.field_names = ['Subject','Mid Theory','Mid Practical','Mid','Final Theory','Final Practical','Final','Overall']
                    x.add_row(['English',i[5],i[6],i[5]+i[6],i[16],i[17],i[16]+i[17],round((((i[5]+i[6])*0.3)+((i[16]+i[17])*0.7)),2) ])
                    x.add_row(['Mathematics',i[7],i[8],i[7]+i[8],i[18],i[19],i[18]+i[19],round((((i[7]+i[8])*0.3)+((i[18]+i[19])*0.7)),2)  ])
                    x.add_row(['Physics',i[9],i[10],i[9]+i[10],i[20],i[21],i[20]+i[21] ,round((((i[9]+i[10])*0.3)+((i[20]+i[21])*0.7)),2) ])
                    x.add_row(['Chemistry',i[11],i[12],i[11]+i[12],i[22],i[23],i[22]+i[23],round((((i[11]+i[12])*0.3)+((i[22]+i[23])*0.7)),2)  ])
                    x.add_row(['Computer Science',i[13],i[14],i[13]+i[14],i[24],i[25],i[24]+i[25],round((((i[13]+i[14])*0.3)+((i[24]+i[25])*0.7)),2)  ])
                    x.align['Subject']='l'
                    print(x)
                    print('Overall percentage: ',i[27])
                    print('Remarks: ',i[28])
                    if i[28]=='PASS':
                        print('Insight:  Well done, Keep it up')
                    elif i[28]=='FAIL':
                        print('Insight:  Keep Improving')
                    print('================================================================================================')
                elif sec.upper() in ' D ':
                    print('================================================================================================')
                    print("                                 ST. MARK'S SCHOOL")
                    print('================================================================================================')
                    print('Name: ',i[1],' '*(30-len(i[1])),'Admission no.: ',i[0])
                    print("Father's Name: ",i[3],' '*(21-len(i[3])),'Roll no.: ',i[2])
                    print('Club: ',i[4],' '*(33-len(i[1])),'Class: ',db,'-',sec)
                    x = PrettyTable()
                    x.field_names = ['Subject','Mid Theory','Mid Practical','Mid','Final Theory','Final Practical','Final','Overall']
                    x.add_row(['English',i[5],i[6],i[5]+i[6],i[16],i[17],i[16]+i[17],round((((i[5]+i[6])*0.3)+((i[16]+i[17])*0.7)),2) ])
                    x.add_row(['Mathematics',i[7],i[8],i[7]+i[8],i[18],i[19],i[18]+i[19],round((((i[7]+i[8])*0.3)+((i[18]+i[19])*0.7)),2)  ])
                    x.add_row(['Business Studies',i[9],i[10],i[9]+i[10],i[20],i[21],i[20]+i[21] ,round((((i[9]+i[10])*0.3)+((i[20]+i[21])*0.7)),2) ])
                    x.add_row(['Accounts',i[11],i[12],i[11]+i[12],i[22],i[23],i[22]+i[23],round((((i[11]+i[12])*0.3)+((i[22]+i[23])*0.7)),2)  ])
                    x.add_row(['Economics',i[13],i[14],i[13]+i[14],i[24],i[25],i[24]+i[25],round((((i[13]+i[14])*0.3)+((i[24]+i[25])*0.7)),2)  ])
                    x.align['Subject']='l'
                    print(x)
                    print('Overall percentage: ',i[27])
                    print('Remarks: ',i[28])
                    if i[28]=='PASS':
                        print('Insight:  Well done, Keep it up')
                    elif i[28]=='FAIL':
                        print('Insight:  Keep Improving')
                    print('================================================================================================')
        else:
            print('Enter valid CLass !')
    except Exception as e:
        print(e)
def modify_roll(db,sec,adm):#=====================================MODIFY Rollno===
    s=input("Enter new rollno. of the student : ")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
    mycursor=mydb.cursor()
    q=(" update {}_{} set Roll_no={} where Adm_no={}".format(db,sec,s,adm))
    mycursor.execute(q)
    mydb.commit()
    print("SUCCESSFULLY modified for ",mycursor.rowcount," students ! ")
def modify_father(db,sec,adm):#=====================================MODIFY Father name===
    s=input("Enter new name of father of the student : ")
    mydb=mysql.connecor.connect(host="localhost",user="root",passwd=bla,database=db)
    mycursor=mydb.cursor()
    q=(" update {}_{} set Father_name='{}' where Adm_no={}".format(db,sec,s,adm))
    mycursor.execute(q)
    mydb.commit()
    print("SUCCESSFULLY modified for ,",mycursor.rowcount," students ! ")
def modify_club(db,sec,adm):#=====================================MODIFY Club===
    s=input("Enter new club of the student : ")
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
    mycursor=mydb.cursor()
    mycursor.execute("UPDATE {}_{} SET Club='{}' WHERE Adm_no={}".format(db,sec,s,adm))
    mydb.commit()
    print("Successful modified for ,",mycursor.rowcount," students!")
def modify_batch_club(db,sec,adm):#=====================================MODIFY Club from prev club===
    prev=input('Enter current club: ')
    new=input('Enter new club: ')
    try:
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='python',database=db)
        mycursor=mydb.cursor()
        mycursor.execute(f"UPDATE {db}_{sec} SET Club='{new}' WHERE Club='{prev}'")
        mydb.commit()
        print(f'Batch edit club Successful for {mycursor.rowcount} students!')
    except Exception as e:
        print(e)

def updating_record(db,sec,adm):      #To update remarks,mid,final,etc. after updating marks
    if db in ("I","II","III","IV","V"):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
        mycursor=mydb.cursor()
        q=("Select English1,Hindi1,Maths1,Science1,EVS1 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
        mycursor.execute(q)
        x=mycursor.fetchone()
        mid=sum(x)//5
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
        mycursor=mydb.cursor()
        q=("Select English2,Hindi2,Maths2,Science2,EVS2 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
        mycursor.execute(q)
        x1=mycursor.fetchone()
        final=sum(x1)//5
        Overall=(mid*0.3+final*0.7)
        if Overall>33:
            Remarks="PASS"
        else:
            Remarks="FAIL"
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
        mycursor=mydb.cursor()
        s=("Update {}_{} set Total_mid={},Total_final={},Overall={},Remarks='{}' WHERE Adm_no={}").format(db,sec,mid,final,Overall,Remarks,adm)
        mycursor.execute(s)
        mydb.commit()
    elif db in ("VI","VII","VIII","VIII","IX","X") :
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
        mycursor=mydb.cursor()
        q=("Select English1,Prac_Eng1,Hindi1,Prac_Hindi1,Maths1,Prac_Maths1,Science1,Prac_Scien1,Social_Sc1,Prac_Soc1 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
        mycursor.execute(q)
        x=mycursor.fetchone()
        mid=sum(x)//5
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
        mycursor=mydb.cursor()
        q=("Select English2,Prac_Eng2,Hindi2,Prac_Hindi2,Maths2,Prac_Maths2,Science2,Prac_Scien2,Social_Sc2,Prac_Soc2 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
        mycursor.execute(q)
        x1=mycursor.fetchone()
        final=sum(x1)//5
        mydb.commit()
        if Overall>33:
            remark="PASS"
        else:
            remark="FAIL"
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
        mycursor=mydb.cursor()
        s=("Update {}_{} set Total_mid={},Total_final={},Overall={},Remarks='{}' WHERE Adm_no={}").format(db,sec,mid,final,Overall,remark,adm)
        mycursor.execute(s)
        mydb.commit()
    elif db in ("XI","XII") :
        mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
        mycursor=mydb.cursor()
        if c==1:     # Error c not defined
            q=("Select English1,Prac_Eng1,Sociology1,Prac_Soc1,Psycology1,Prac_Psy1,Geography1,Prac_Geo1,Economics1,Prac_Eco1 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mycursor.execute(q)
            x=mycursor.fetchall()
            mid=sum(x)//5
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
            mycursor=mydb.cursor()
            q=("Select English2,Prac_Eng2,Sociology2,Prac_Soc2,Psycology2,Prac_Psy2,Geography2,Prac_Geo2,Economics2,Prac_Eco2 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mycursor.execute(q)
            x1=mycursor.fetchall()
            final=sum(x1)//5
            if Overall>33:
                remark="PASS"
            else:
                remark="FAIL"
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
            mycursor=mydb.cursor()
            s=("Update {}_{} set Total_mid={},Total_final={},Overall={},Remarks='{}' WHERE Adm_no={}").format(db,sec,mid,final,Overall,remark,adm)
            mycursor.execute(s)
            mydb.commit()
        elif c==2:#PCMC
            q=("Select English1,Prac_Eng1,Maths1,Prac_Maths1,Physics1,Prac_Physics1,Chemistry1,Prac_Chemistry1,Comp_Sc1,Prac_Comp1 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mycursor.execute(q)
            x=mycursor.fetchall()
            mid=sum(x)//5
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
            mycursor=mydb.cursor()
            q=("Select English2,Prac_Eng2,Maths2,Prac_Maths2,Physics2,Prac_Physics2,Chemistry2,Prac_Chemistry2,Comp_Sc1,Prac_Comp2 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mycursor.execute(q)
            x1=mycursor.fetchall()
            final=sum(x1)//5
            if Overall>33:
                remark="PASS"
            else:
                remark="FAIL"
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
            mycursor=mydb.cursor()
            s=("Update {}_{} set Total_mid={},Total_final={},Overall={},Remarks='{}' WHERE Adm_no={}").format(db,sec,mid,final,Overall,remark,adm)
            mycursor.execute(s)
            mydb.commit()
        elif c==3:#PCMB
            q=("Select English1,Prac_Eng1,Maths1,Prac_Math1,Physics1,Prac_Phy1,Chemistry1,Prac_Chem1,Biology1,Prac_Bio1 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mycursor.execute(q)
            x=mycursor.fetchall()
            mid=sum(x)//5
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
            mycursor=mydb.cursor()
            q=("Select English2,Prac_Eng2,Maths2,Prac_Math2,Physics2,Prac_Phy2,Chemistry2,Prac_Chem2,Biology2,Prac_Bio2 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mycursor.execute(q)
            x1=mycursor.fetchall()
            final=sum(x1)//5
            if Overall>33:
                remark="PASS"
            else:
                remark="FAIL"
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
            mycursor=mydb.cursor()
            s=("Update {}_{} set Total_mid={},Total_final={},Overall={},Remarks='{}' WHERE Adm_no={}").format(db,sec,mid,final,Overall,remark,adm)
            mycursor.execute(s)
            mydb.commit()
        elif c==4:#Commerce
            q=("Select English1,Prac_Eng1,Maths1,Prac_Maths1,Bus_Studies1,Prac_Bus1,Accounts1,Prac_Acc1,Economics1,Prac_Eco1 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mycursor.execute(q)
            x=mycursor.fetchall()
            mid=sum(x)//5
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
            mycursor=mydb.cursor()
            q=("Select English2,Prac_Eng2,Maths2,Prac_Maths2,Bus_Studies2,Prac_Bus2,Accounts2,Prac_Acc2,Economics2,Prac_Eco2 from {}_{} WHERE Adm_no={}".format(db,sec,adm))
            mycursor.execute(q)
            x1=mycursor.fetchall()
            final=sum(x1)//5
            if Overall>33:
                remark="PASS"
            else:
                remark="FAIL"
            mydb=mysql.connector.connect(host="localhost",user="root",passwd=bla,database=db)
            mycursor=mydb.cursor()
            s=("Update {}_{} set Total_mid={},Total_final={},Overall={},Remarks='{}'").format(db,sec,mid,final,Overall,remark)
            mycursor.execute(s)
            mydb.commit()

def modify_subject(db,sec,adm):#=====================================MODIFY MARKS===
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=bla,database=db)
    mycursor=mydb.cursor()
    s=db
    l1=['I','II','III','IV','V']
    l2=['VI','VII','VIII','IX','X']
    l3=['XI','XII']
    if s in l1:
        a1=print('''
+--------------------------------------------------------------------------------------+
| Subjects marks modify choice for classes I to V                                      |
+--------------------------------------------------------------------------------------+
| 1) English     | 2) Hindi     | 3) Maths    | 4) Science    | 5) EVS                 |
+--------------------------------------------------------------------------------------+  ''')
        a1=int(input("Enter the subject of which you want to modify the marks  : "))
        if a1==1:
            q1=int(input("Enter new english marks : "))
            z=input("Which term of which you want to modify the marks  (m/f) : ")
            if z=="m":
                mycursor.execute("UPDATE {}_{} set English1={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
            elif z=="f":
                mycursor.execute("UPDATE {}_{} set English2={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
        elif a1==2:
            q1=int(input("Enter new Hindi marks : "))
            z=input("Which term of which you want to modify the marks  (m/f) : ")
            if z=="m":
                mycursor.execute("UPDATE {}_{} set Hindi1={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
            elif z=="f":
                mycursor.execute("UPDATE {}_{} set Hindi2={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
        elif a1==3:
            q1=int(input("Enter new Maths marks : "))
            z=input("Which term of which you want to modify the marks  (m/f) : ")
            if z=="m":
                mycursor.execute("UPDATE {}_{} set Maths1={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
            elif z=="f":
                mycursor.execute("UPDATE {}_{} set Maths2={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
        elif a1==4:
            q1=int(input("Enter new Science marks : "))
            z=input("Which term of which you want to modify the marks  (m/f) : ")
            if z=="m":
                mycursor.execute("UPDATE {}_{} set Science1={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
            elif z=="f":
                mycursor.execute("UPDATE {}_{} set Science2={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
        elif a1==5:
            q1=int(input("Enter new EVS marks : "))
            z=input("Which term of which you want to modify the marks  (m/f) : ")
            if z=="m":
                mycursor.execute("UPDATE {}_{} set EVS1={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
            elif z=="f":
                mycursor.execute("UPDATE {}_{} set EVS2={} where Adm_no={}".format(db,sec,q1,adm))
                mydb.commit()
    elif s in l2:
        a1=int(input('''
+-----------------------------------------------------------------------------+
| Subjects marks modify choice for classes VI to X                            |
+-----------------------------------------------------------------------------+
| 1) English   | 2) Hindi   | 3) Maths   | 4) Science   | 5) SST              |
+-----------------------------------------------------------------------------+ : \n which subject marks do you want to modify : '''))
        z=input("Enter which marks you want to modify (p=prac/t=theory) : ")
        if a1==1:
            if z=="p":
                q1=int(input("Enter new English practical marks out of 20 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set Prac_Eng1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{sec} set Prac_Eng2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
            elif z=="t":
               q1=int(input("Enter new English theory marks out of 80: "))
               z1=input("Enter the term of which you want to modify the marks (m/f) : ")
               if z1=="m":
                   mycursor.execute("UPDATE {}_{} set English1={} where Adm_no={}".format(db,sec,q1,adm))
                   mydb.commit()
               elif z1=="f":
                   mycursor.execute("UPDATE {}_{} set English2={} where Adm_no={}".format(db,sec,q1,adm))
                   mydb.commit()
        elif a1==2:
            if z=="p":
                q1=int(input("Enter new Hindi practical marks out of 20 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set Prac_Hindi1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{} set Prac_Hindi2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
            elif z=="t":
                q1=int(input("Enter new Hindi theory marks out of 80 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set English1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{} set English2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
        elif a1==3:
            if z=="p":
                q1=int(input("Enter new Maths practical marks out of 20 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set Prac_Maths1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{} set Prac_Math2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
            elif z=="t":
                q1=int(input("Enter new Maths theory marks out of 80 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set Maths1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{} set Math2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
        elif a1==4:
            if z=="p":
                q1=int(input("Enter new Science practical marks out of 20 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set Prac_Scien1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{} set Prac_Scien2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
            elif z=="t":
                q1=int(input("Enter new Hindi theory marks out of 80 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set Science1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{} set Science2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
        elif a1==5:
            if z=="p":
                q1=int(input("Enter new SST practical marks out of 20 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set Prac_Soc1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{} set Prac_Soc2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
            elif z=="t":
                q1=int(input("Enter new SST theory marks out of 80 : "))
                z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                if z1=="m":
                    mycursor.execute("UPDATE {}_{} set Social_Sc1={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
                elif z1=="f":
                    mycursor.execute("UPDATE {}_{} set Social_Sc2={} where Adm_no={}".format(db,sec,q1,adm))
                    mydb.commit()
    elif s in l3:
        c=int(input('''
+--------------------------------+
| Choice for stream              |
+--------------------------------+
| 1) Arts                        |
| 2) PCMC                        |
| 3) PCMB                        |
| 4) Commerce                    |
+--------------------------------+ /n Enter his stream : '''))
        if c==1:
            print('''
+------------------------------------------------------------------------------------------+
| Subjects marks modify choice for classes XI to XII     (Arts)                            |
+------------------------------------------------------------------------------------------+
| 1) English   | 2) Sociology  | 3) Psycology  | 4) Geography  | 5) Economics              |
+------------------------------------------------------------------------------------------+ \n which subject marks do you want to modify : ''')
            z=input("Enter which marks you want to modify (p=prac/t=theory) : ")
            z1=input("Enter the term of which you want to modify the marks (m/f) : ")
            if a1==1:
                if z=="p":
                            q1=int(input("Enter new English practical marks out of 20 : "))
                            if z1=="m":
                                mycursor.execute("UPDATE {}_{} set Prac_Eng1={} where Adm_no={}".format(db,sec,q1,adm))
                                mydb.commit()
                            elif z1=="f":
                                mycursor.execute("UPDATE {}_{} set Prac_Eng2={} where Adm_no={}".format(db,sec,q1,adm))
                                mydb.commit()
                elif z=="t":
                           q1=int(input("Enter new English theory marks out of 80: "))
                           if z1=="m":
                               mycursor.execute("UPDATE {}_{} set English1={} where Adm_no={}".format(db,sec,q1,adm))
                               mydb.commit()
                           elif z1=="f":
                               mycursor.execute("UPDATE {}_{} set English2={} where Adm_no={}".format(db,sec,q1,adm))
                               mydb.commit()
            elif a1==2:
                if z=="p":
                          q1=int(input("Enter new sociology practical marks out of 20 : "))
                          if z1=="m":
                               mycursor.execute("UPDATE {}_{} set Prac_Soc1={} where Adm_no={}".format(db,sec,q1,adm))
                               mydb.commit()
                          elif z1=="f":
                               mycursor.execute("UPDATE {}_{} set Prac_Soc2={} where Adm_no={}".format(db,sec,q1,adm))
                               mydb.commit()
                elif z=="t":
                          q1=int(input("Enter new sociology theory marks out of 80: "))
                          if z1=="m":
                              mycursor.execute("UPDATE {}_{} set Sociology1={} where Adm_no={}".format(db,sec,q1,adm))
                          elif z1=="f":
                              mycursor.execute("UPDATE {}_{} set Sociology2={} where Adm_no={}".format(db,sec,q1,adm))
            elif a1==3:
                if z=="p":
                          q1=int(input("Enter new psycology practical marks out of 20 : "))
                          if z1=="m":
                               mycursor.execute("UPDATE {}_{} set Prac_Psy1={} where Adm_no={}".format(db,sec,q1,adm))
                               mydb.commit()
                          elif z1=="f":
                               mycursor.execute("UPDATE {}_{} set Prac_Psy2={} where Adm_no={}".format(db,sec,q1,adm))
                               mydb.commit()
                elif z=="t":
                          q1=int(input("Enter new psycology theory marks out of 80: "))
                          if z1=="m":
                              mycursor.execute("UPDATE {}_{} set Psycology1={} where Adm_no={}".format(db,sec,q1,adm))
                              mydb.commit()
                          elif z1=="f":
                              mycursor.execute("UPDATE {}_{} set Psycology2={} where Adm_no={}".format(db,sec,q1,adm))
                              mydb.commit()
            elif a1==4:
                if z=="p":
                          q1=int(input("Enter new geography practical marks out of 20 : "))
                          if z1=="m":
                               mycursor.execute("UPDATE {}_{} set Prac_Geo1={} where Adm_no={}".format(db,sec,q1,adm))
                               mydb.commit()
                          elif z1=="f":
                               mycursor.execute("UPDATE {}_{} set Prac_Geo2={} where Adm_no={}".format(db,sec,q1,adm))
                               mydb.commit()
                elif z=="t":
                          q1=int(input("Enter new English theory marks out of 80: "))
                          if z1=="m":
                              mycursor.execute("UPDATE {}_{} set Geography1={} where Adm_no={}".format(db,sec,q1,adm))
                              mydb.commit()
                          elif z1=="f":
                              mycursor.execute("UPDATE {}_{} set Geography2={} where Adm_no={}".format(db,sec,q1,adm))
                              mydb.commit()
            elif a1==5:
                if z=="p":
                    q1=int(input("Enter new economics practical marks out of 20 : "))
                    if z1=="m":
                         mycursor.execute("UPDATE {}_{} set Prac_Eco1={} where Adm_no={}".format(db,sec,q1,adm))
                         mydb.commit()
                    elif z1=="f":
                         mycursor.execute("UPDATE {}_{} set Prac_Eco2={} where Adm_no={}".format(db,sec,q1,adm))
                         mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new English theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Economics1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Economics2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
        elif c==2:
            print('''
+--------------------------------------------------------------------------------------+
| Subjects marks modify choice for classes XI to XII       (PCMB)                      |
+--------------------------------------------------------------------------------------+
| 1) English    | 2) Maths     | 3) Physics    | 4) Chemistry    | 5) Biology          |
+--------------------------------------------------------------------------------------+ \n which subject marks do you want to modify : ''')
            if a1==1:
                z=input("Enter which marks you want to modify (p=prac/t=theory) : ")
                if z=="p":
                    z1=input("Enter the term of which you want to modify the marks (m/f) : ")
                    q1=int(input("Enter new English practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Eng1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Eng2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new English theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set English1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set English2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==2:
                if z=="p":
                    q1=int(input("Enter new maths practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Math1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Math2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new maths theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Maths1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Maths2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==3: 
                if z=="p":
                    q1=int(input("Enter new Physics practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Phy1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Phy2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new Physics theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Physics1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Physics2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==4:
                if z=="p":
                    q1=int(input("Enter new chemistry practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Chem1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Chem2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new chemistry theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Chemistry1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Chemistry2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==5:
                if z=="p":
                    q1=int(input("Enter new Biology practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Bio1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Bio2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new Bio theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Biology1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Biology2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
        elif c==3:
            print('''
+--------------------------------------------------------------------------------------+
| Subjects marks modify choice for classes XI to XII       (PCMC)                      |
+--------------------------------------------------------------------------------------+
| 1) English   | 2) Maths   | 3) Physics   | 4) Chemistry   | 5) ComputerScience       |
+--------------------------------------------------------------------------------------+ \n which subject marks do you want to modify : ''')
            z=input("Enter which marks you want to modify (p=prac/t=theory) : ")
            z1=input("Enter the term of which you want to modify the marks (m/f) : ")
            if a1==1:
                if z=="p":
                    q1=int(input("Enter new English practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Eng1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Eng2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new English theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set English1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set English2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==2:
                if z=="p":
                    q1=int(input("Enter new maths practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Math1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Math2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new maths theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Maths1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Maths2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==3: 
                if z=="p":
                    q1=int(input("Enter new Physics practical marks out of 20 : "))
                    if z1=="m":
                        q=("UPDATE {}_{} set Prac_Phy1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        q=("UPDATE {}_{} set Prac_Phy2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new Physics theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Physics1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Physics2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==4:
                if z=="p":
                    q1=int(input("Enter new chemistry practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Chem1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Chem2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new chemistry theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Chemistry1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Chemistry2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==5:
                if z=="p":
                    q1=int(input("Enter new Computer practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Comp1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Comp2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new Computer theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Comp_Sc1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Comp_Sc2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
        elif c==4:
            print('''
+-----------------------------------------------------------------------------+
| Subjects marks modify choice for classes XI to XII       (Commerce)         |
+-----------------------------------------------------------------------------+
| 1) English | 2) Maths | 3) BuisnessStudies | 4) Accounts | 5) Economics     |
+-----------------------------------------------------------------------------+ \n which subject marks do you want to modify : ''')
            z=input("Enter which marks you want to modify (p=prac/t=theory) : ")
            z1=input("Enter the term of which you want to modify the marks (m/f) : ")
            if a1==1:
                if z=="p":
                    q1=int(input("Enter new English practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Eng1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Eng2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new English theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set English1={} where Adm_no={}".formatdb,sec,(q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set English2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==2:
                if z=="p":
                    q1=int(input("Enter new maths practical marks out of 20 : "))
                    if z1=="m":
                         mycursor.execute("UPDATE {}_{} set Prac_Maths1={} where Adm_no={}".format(db,sec,q1,adm))
                         mydb.commit()
                    elif z1=="f":
                         mycursor.execute("UPDATE {}_{} set Prac_Maths2={} where Adm_no={}".format(db,sec,q1,adm))
                         mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new maths theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Maths1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Maths2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
            elif a1==3: 
                if z=="p":
                    q1=int(input("Enter new BuisnessStudies practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Bus1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Bus2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new BuisnessStudies theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Bus_Studies1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Bus_Studies2={} where Adm_no={}".formatdb,sec,(q1,adm))
                        mydb.commit()
            elif a1==4:
                if z=="p":
                    q1=int(input("Enter new accounts practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Acc1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Acc2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new accounts theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Accounts1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{sec} set Accounts2={} where Adm_no={}".formatdb,sec,(q1,adm))
                        mydb.commit()
            elif a1==5:
                if z=="p":
                    q1=int(input("Enter new Economics practical marks out of 20 : "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Prac_Eco1={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Prac_Eco2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                elif z=="t":
                    q1=int(input("Enter new Economics theory marks out of 80: "))
                    if z1=="m":
                        mycursor.execute("UPDATE {}_{} set Economics1={}where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
                    elif z1=="f":
                        mycursor.execute("UPDATE {}_{} set Economics2={} where Adm_no={}".format(db,sec,q1,adm))
                        mydb.commit()
    print()
    updating_record(db,sec,adm)
    print(' Data modified SUCCESSFULLY for ',mycursor.rowcount,' student ! ' )
    print()


def menu():
    print()
    db=input('Enter the database/class to use: ')           # This is the class(I,II,II..)
    x='y'
    while x=='y':
        x1=input('''
+-----------------------------+
|    Menu for editing         |
+-----------------------------+
| 1) Add records              |
| 2) Delete record            |
| 3) Modify records           |
| 4) Show records             |
| 5) Exit                     |
+-----------------------------+

Enter your choice.(1/2/3/4/5).: ''')
        if x1=='1':
            add_records(db)
        elif x1=='2':
            delete_record(db)
        elif x1=='3':
            see_full_records(db)
            sec=input('Enter Section of student you want to modify : ')
            x2=input('''
+----------------------------------+                              
| 1) Roll no                       |
| 2) Father's Name                 |
| 3) Club                          |
| 4) Batch edit club               |
| 5) Any one subject marks         |
| 6) Exit                          |
+----------------------------------+
What do you want to modify ? : ''')            
            if x2=='1':
                adm=int(input('Enter Adm no of student: '))
                modify_roll(db,sec,adm)
            elif x2=='2':
                adm=int(input('Enter Adm no of student: '))
                modify_father(db,sec,adm)
            elif x2=='3':
                adm=int(input('Enter Adm no of student: '))
                modify_club(db,sec,adm)
            elif x2=='4':
                modify_batch_club(db,sec,adm)
            elif x2=='5':
                adm=int(input('Enter Adm no of student: '))
                modify_subject(db,sec,adm)
            else:
                x='y'
        elif x1=='4':
            x3=input('''
+------------------------------------+
| 1) See Records for whole class     |
|     (valid for I-X)                |
| 2) See record for                  |
|     particular Section             |
| 3) See record for                  |
|     particular student             |
+------------------------------------+
=> Enter your choice.(1/2/3).: ''')
            if x3=='1':
                see_full_records(db)
            elif x3=='2':
                see_part_sec(db)
            elif x3=='3':
                see_part_student(db)
            else:
                x='y'
        else:
            x='n'


r='y'
while r=='y':
    print('''
+---------------------------------+
|    Features:-                   |
+---------------------------------+
| 1) Create database              |
| 2) Create table                 |
| 3) Go to menu                   |
| 4) Display records of           |
|    whole school                 |
| 5) Exit Program                 |
+---------------------------------+
    ''')
    r1=input('Enter your choice.(1/2/3/4/5).: ')
    if r1=='1':
        create_database()
    elif r1=='2':
        create_table_I_X()
        create_table_X_XII()
    elif r1=='3':
        menu()
    elif r1=='4':
        display_whole_school()
    else:
        print('GOOD BYE!')
        r='n'
