import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
def year() :
    print("--------------------------------------------------------------------")
    print("1. 2017")
    print("2. 2018")
    print("3. 2019")
    print("4. 2020")
    print("5. Return to companies")
    print("--------------------------------------------------------------------")
def company() :
    print("--------------------------------------------------------------------")
    print("A. AUDI")
    print("B. BMW")
    print("C. HONDA")
    print("D. NISSAN")
    print("E. ROLLSROYCE")
    print("F. TATA")
    print("G. TESLA")
    print("H. VOLKSWAGEN")
    print("J. RETURN TO MAIN MENU")
    print("--------------------------------------------------------------------")
def functions() :
    print("--------------------------------------------------------------------")
    print("Functions to perform")
    print("1. Display the data of each car company per year :")
    print("2. Comparing the Data using graphs")
    print("3. Comparing the volume using graphs")
    print("4. Compare companies overall stock market trading")
    print("5. Enter records")
    print("6. Deleting Data")
    print("7. Candle Stick chart")
    print("8. Statiscal Analysis")
    print("Please select the option according to the index in front of option")
    print("--------------------------------------------------------------------")
df_AUDI=pd.read_csv("C:\\Top EV Company\\Audi\\audi.csv")
df_BMW=pd.read_csv("C:\\Top EV Company\\BMW\\bmw.csv")
df_HONDA=pd.read_csv("C:\\Top EV Company\\Honda\\honda.csv")
df_LUCIDMOTORS=pd.read_csv("C:\\Top EV Company\\Lucid Motors\\lucid motors.csv")
df_NIO=pd.read_csv("C:\\Top EV Company\\NIO\\NIO.csv")
df_NISSAN=pd.read_csv("C:\\Top EV Company\\Nissan\\nissan.csv")
df_ROLLSROYCE=pd.read_csv("C:\\Top EV Company\\Rolls Royces\\rolls royces.csv")
df_TATA=pd.read_csv("C:\\Top EV Company\\Tata\\tata.csv")
df_TESLA=pd.read_csv("C:\\Top EV Company\\Tesla\\tesla.csv")
df_VOLKSWAGEN=pd.read_csv("C:\\Top EV Company\\Volkswagen\\Volkswagen.csv")
AUDI={"Date":pd.DatetimeIndex(df_AUDI.Date[91:1097]),"Open":df_AUDI.Open[91:1097],"High":df_AUDI.High[91:1097],"Low":df_AUDI.Low[91:1097],"Close":df_AUDI.Close[91:1097],"Volume":df_AUDI.Volume[91:1097]}
AUDI=pd.DataFrame(AUDI).set_index("Date")
BMW={"Date":pd.DatetimeIndex(df_BMW.Date[91:1103]),"Open":df_BMW.Open[91:1103],"High":df_BMW.High[91:1103],"Low":df_BMW.Low[91:1103],"Close":df_BMW.Close[91:1103],"Volume":df_BMW.Volume[91:1103]}
BMW=pd.DataFrame(BMW).set_index("Date")
HONDA={"Date":pd.DatetimeIndex(df_HONDA.Date[90:1097]),"Open":df_HONDA.Open[90:1097],"High":df_HONDA.High[90:1097],"Low":df_HONDA.Low[90:1097],"Close":df_HONDA.Close[90:1097],"Volume":df_HONDA.Volume[90:1097]}
HONDA=pd.DataFrame(HONDA).set_index("Date")
NISSAN={"Date":pd.DatetimeIndex(df_NISSAN.Date[87:1084]),"Open":df_NISSAN.Open[87:1084],"High":df_NISSAN.High[87:1084],"Low":df_NISSAN.Low[87:1084],"Close":df_NISSAN.Close[87:1084],"Volume":df_NISSAN.Volume[87:1084]}
NISSAN=pd.DataFrame(NISSAN).set_index("Date")
ROLLSROYCE={"Date":pd.DatetimeIndex(df_ROLLSROYCE.Date[90:1102]),"Open":df_ROLLSROYCE.Open[90:1102],"High":df_ROLLSROYCE.High[90:1102],"Low":df_ROLLSROYCE.Low[90:1102],"Close":df_ROLLSROYCE.Close[90:1102], "Volume":df_ROLLSROYCE.Volume[90:1102]}
ROLLSROYCE=pd.DataFrame(ROLLSROYCE).set_index("Date")
TATA={"Date":pd.DatetimeIndex(df_TATA.Date[87:1075]),"Open":df_TATA.Open[87:1075],"High":df_TATA.High[87:1075],"Low":df_TATA.Low[87:1075],"Close":df_TATA.Close[87:1075],"Volume":df_TATA.Volume[87:1075]}
TATA=pd.DataFrame(TATA).set_index("Date")
TESLA={"Date":pd.DatetimeIndex(df_TESLA.Date[90:1097]),"Open":df_TESLA.Open[90:1097],"High":df_TESLA.High[90:1097],"Low":df_TESLA.Low[90:1097],"Close":df_TESLA.Close[90:1097],"Volume":df_TESLA.Volume[90:1097]}
TESLA=pd.DataFrame(TESLA).set_index("Date")
VOLKSWAGEN={"Date":pd.DatetimeIndex(df_VOLKSWAGEN.Date[91:1103]),"Open":df_VOLKSWAGEN.Open[91:1103],"High":df_VOLKSWAGEN.High[91:1103],"Low":df_VOLKSWAGEN.Low[91:1103],"Close":df_VOLKSWAGEN.Close[91:1103],"Volume":df_VOLKSWAGEN.Volume[91:1103]}
VOLKSWAGEN=pd.DataFrame(VOLKSWAGEN).set_index("Date")
choice="Y"
while choice=="Y" :
    functions()
    ch=int(input("Enter your choice : "))
    A="N"
    while A=="N" :#"A" variable to create while loop for company()
        if ch==1 :
            company()
            print("Select the stocks you want to display")
            x=input("Enter your choice : ").upper()
            if x=="A":
                B="N"
                while B=="N":#"B" variable to create while loop for year()
                    print("Stocks of AUDI")
                    year()
                    y=int(input("Enter the year : "))
                    if y==1 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(AUDI.loc["2017-01-01":"2017-12-31"]) 
                    elif y==2 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(AUDI.loc["2018-01-01":"2018-12-31"])
                    elif y==3 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(AUDI.loc["2019-01-01":"2019-12-31"])
                    elif y==4 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(AUDI.loc["2020-01-01":"2020-12-31"])
                    elif y==5 :
                        B=input("Do you want return").upper()
                    else :
                        print("Select a valid option!")
                    B="Y"
            elif x=="B" :
                B="N"
                while B=="N" :
                    print("Stocks of BMW")
                    year()
                    y=int(input("Enter the year : "))
                    if y==1 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(BMW.loc["2017-01-01":"2017-12-31"]) 
                    elif y==2 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(BMW.loc["2018-01-01":"2018-12-31"])
                    elif y==3 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(BMW.loc["2019-01-01":"2019-12-31"])
                    elif y==4 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(BMW.loc["2020-01-01":"2020-12-31"])
                    elif y==5 :
                        B=input("Do you want return").upper()
                    else :
                        print("Select a valid option!")
                    B="Y"
            elif x=="C" :
                B="N"
                while B=="N" :
                    print("Stocks of HONDA")
                    year()
                    y=int(input("Enter the year : "))
                    if y==1 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(HONDA.loc["2017-01-01":"2017-12-31"]) 
                    elif y==2 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(HONDA.loc["2018-01-01":"2018-12-31"])
                    elif y==3 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(HONDA.loc["2019-01-01":"2019-12-31"])
                    elif y==4 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(HONDA.loc["2020-01-01":"2020-12-31"])
                    elif y==5 :
                        B=input("Do you want return").upper()
                    else :
                        print("Select a valid option!")
                    B="Y"
            elif x=="D" :
                B="N"
                while B=="N" :
                    print("Stocks of NISSAN")
                    year()
                    y=int(input("Enter the year : "))
                    if y==1 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(NISSAN.loc["2017-01-01":"2017-12-31"]) 
                    elif y==2 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(NISSAN.loc["2018-01-01":"2018-12-31"])
                    elif y==3 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(NISSAN.loc["2019-01-01":"2019-12-31"])
                    elif y==4 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(NISSAN.loc["2020-01-01":"2020-12-31"])
                    elif y==5 :
                        B=input("Do you want return").upper()
                    else :
                        print("Select a valid option!")
                    B="Y"
            elif x=="E" :
                B="N"
                while B=="N" :
                    print("Stocks of ROLLSROYCE")
                    year()
                    y=int(input("Enter the year : "))
                    if y==1 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(ROLLSROYCE.loc["2017-01-01":"2017-12-31"]) 
                    elif y==2 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(ROLLSROYCE.loc["2018-01-01":"2018-12-31"])
                    elif y==3 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(ROLLSROYCE.loc["2019-01-01":"2019-12-31"])
                    elif y==4 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(ROLLSROYCE.loc["2020-01-01":"2020-12-31"])
                    elif y==5 :
                        B=input("Do you want return").upper()
                    else :
                        print("Select a valid option!")
                    B="Y"
            elif x=="F" :
                B="N"
                while B=="N" :
                    print("Stocks of TATA")
                    year()
                    y=int(input("Enter the year : "))
                    if y==1 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(TATA.loc["2017-01-01":"2017-12-31"]) 
                    elif y==2 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(TATA.loc["2018-01-01":"2018-12-31"])
                    elif y==3 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(TATA.loc["2019-01-01":"2019-12-31"])
                    elif y==4 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(TATA.loc["2020-01-01":"2020-12-31"])
                    elif y==5 :
                        B=input("Do you want return").upper()
                    else :
                        print("Select a valid option!")
                    B="Y"
            elif x=="G" :
                B="N"
                while B=="N" :
                    print("Stocks of TESLA")
                    year()
                    y=int(input("Enter the year : "))
                    if y==1 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(TESLA.loc["2017-01-01":"2017-12-31"]) 
                    elif y==2 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(TESLA.loc["2018-01-01":"2018-12-31"])
                    elif y==3 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(TESLA.loc["2019-01-01":"2019-12-31"])
                    elif y==4 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(TESLA.loc["2020-01-01":"2020-12-31"])
                    elif y==5 :
                        B=input("Do you want return").upper()
                    else :
                        print("Select a valid option!")
                    B="Y"
            elif x=="H" :
                B="N"
                while B=="N" :
                    print("Stocks of VOLKSWAGEN")
                    year()
                    y=int(input("Enter the year : "))
                    if y==1 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(VOLKSWAGEN.loc["2017-01-01":"2017-12-31"]) 
                    elif y==2 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(VOLKSWAGEN.loc["2018-01-01":"2018-12-31"])
                    elif y==3 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(VOLKWAGEN.loc["2019-01-01":"2019-12-31"])
                    elif y==4 :
                        pd.set_option("max_rows",None)
                        pd.set_option("max_columns",None)
                        pd.set_option("max_colwidth",None)
                        print(VOLKSWAGEN.loc["2020-01-01":"2020-12-31"])
                    elif y==5 :
                        B=input("Do you want return").upper()
                    else :
                        print("Select a valid option!")
                    B="Y"
            elif x=="J" :
                A="Y"
            else :
                print("Select a valid option!")
            A="Y"
        elif ch==2 :
            print("Closing amount is the price at which the stock market closes for the day")
            a=["2017-01-01","2017-03-01","2017-05-01","2017-07-01","2017-09-01","2017-11-01"]
            b=["2018-01-01","2018-03-01","2018-05-01","2018-07-01","2018-09-01","2018-11-01"]
            c=["2019-01-01","2019-03-01","2019-05-01","2019-07-01","2019-09-01","2019-11-01"]
            d=["2020-01-01","2020-03-01","2020-05-01","2020-07-01","2020-09-01","2020-11-01"]
            choice="Y"
            while choice=="Y" :
                print("Select the Stocks you want to compare : ")
                company()
                x=input("Enter the company for which you want graph : ").upper()
                if x=="A" :
                    year()
                    y=int(input("Select the year you want display : "))
                    if y==1 :
                        plt.plot(AUDI.Close["2017-01-01":"2017-12-31"],label="AUDI 2017")
                        plt.xticks(a)
                    elif y==2 :
                        plt.plot(AUDI.Close["2018-01-01":"2018-12-31"],label="AUDI 2018")
                        plt.xticks(b)
                    elif y==3 :
                        plt.plot(AUDI.Close["2019-01-01":"2019-12-31"],label="AUDI 2019")
                        plt.xticks(c)
                    elif y==4 :
                        plt.plot(AUDI.Close["2020-02-01":"2020-12-31"],label="AUDI 2020")
                        plt.xticks(d)
                    else :
                        print("Select a valid option!")
                elif x=="B" :
                    year()
                    y=int(input("Select the year you want display : "))
                    if y==1 :
                        plt.plot(BMW.Close["2017-01-01":"2017-12-31"],label="BMW 2017")
                        plt.xticks(a)
                    elif y==2 :
                        plt.plot(BMW.Close["2018-01-01":"2018-12-31"],label="BMW 2018")
                        plt.xticks(b)
                    elif y==3 :
                        plt.plot(BMW.Close["2019-01-01":"2019-12-31"],label="BMW 2019")
                        plt.xticks(c)
                    elif y==4 :
                        plt.plot(BMW.Close["2020-02-01":"2020-12-31"],label="BMW 2020")
                        plt.xticks(d)
                    else :
                        print("Select a valid option!")
                elif x=="C" :
                    year()
                    y=int(input("Select the year you want to display : "))
                    if y==1 :
                        plt.plot(HONDA.Close["2017-01-01":"2017-12-31"],label="HONDA 2017")
                        plt.xticks(a)
                    elif y==2 :
                        plt.plot(HONDA.Close["2018-01-01":"2018-12-31"],label="HONDA 2018")
                        plt.xticks(b)
                    elif y==3 :
                        plt.plot(HONDA.Close["2019-01-01":"2019-12-31"],label="HONDA 2019")
                        plt.xticks(c)
                    elif y==4 :
                        plt.plot(HONDA.Close["2020-02-01":"2020-12-31"],label="HONDA 2020")
                        plt.xticks(d)
                    else :
                        print("Select a valid option!")
                elif x=="D" :
                    year()
                    y=int(input("Select the year you want to display : "))
                    if y==1 :
                        plt.plot(NISSAN.Close["2017-01-01":"2017-12-31"],label="NISSAN 2017")
                        plt.xticks(a)
                    elif y==2 :
                        plt.plot(NISSAN.Close["2018-01-01":"2018-12-31"],label="NISSAN 2018")
                        plt.xticks(b)
                    elif y==3 :
                        plt.plot(NISSAN.Close["2019-01-01":"2019-12-31"],label="NISSAN 2019")
                        plt.xticks(c)
                    elif y==4 :
                        plt.plot(NISSAN.Close["2020-02-01":"2020-12-31"],label="NISSAN 2020")
                        plt.xticks(d)
                    else :
                        print("Select a valid option!")
                elif x=="E" :
                    year()
                    y=int(input("Select the year you want to display : "))
                    if y==1 :
                        plt.plot(ROLLSROYCE.Close["2017-01-01":"2017-12-31"],label="ROLLS ROYCE 2017")
                        plt.xticks(a)
                    elif y==2 :
                        plt.plot(ROLLSROYCE.Close["2018-01-01":"2018-12-31"],label="ROLLS ROYCE 2018")
                        plt.xticks(b)
                    elif y==3 :
                        plt.plot(ROLLSROYCE.Close["2019-01-01":"2019-12-31"],label="ROLLS ROYCE 2019")
                        plt.xticks(c)
                    elif y==4 :
                        plt.plot(ROLLSROYCE.Close["2020-02-01":"2020-12-31"],label="ROLLS ROYCE 2020")
                        plt.xticks(d)
                    else :
                        print("Select a valid option!")
                elif x=="F" :
                    year()
                    y=int(input("Select the year you want to display : "))
                    if y==1 :
                        plt.plot(TATA.Close["2017-01-01":"2017-12-31"],label="TATA 2017")
                        plt.xticks(a)
                    elif y==2 :
                        plt.plot(TATA.Close["2018-01-01":"2018-12-31"],label="TATA 2018")
                        plt.xticks(b)
                    elif y==3 :
                        plt.plot(TATA.Close["2019-01-01":"2019-12-31"],label="TATA 2019")
                        plt.xticks(c)
                    elif y==4 :
                        plt.plot(TATA.Close["2020-01-01":"2020-12-31"],label="TATA 2020")
                        plt.xticks(d)
                    else :
                        print("Select a valid option!")
                elif x=="G" :
                    year()
                    y=int(input("Select the year you want to display : "))
                    if y==1 :
                        plt.plot(TESLA.Close["2017-01-01":"2017-12-31"],label="TESLA 2017")
                        plt.xticks(a)
                    elif y==2 :
                        plt.plot(TESLA.Close["2018-01-01":"2018-12-31"],label="TESLA 2018")
                        plt.xticks(b)
                    elif y==3 :
                        plt.plot(TESLA.Close["2019-01-01":"2019-12-31"],label="TESLA 2019")
                        plt.xticks(c)
                    elif y==4 :
                        plt.plot(TESLA.Close["2020-01-01":"2020-12-31"],label="TESLA 2020")
                        plt.xticks(d)
                    else :
                        print("Select a valid option!")
                elif x=="H" :
                    year()
                    y=int(input("Select the year you want to display : "))
                    if y==1 :
                        plt.plot(VOLKSWAGEN.Close["2017-01-01":"2017-12-31"],label="VOLKSWAGEN 2017")
                        plt.xticks(a)
                    elif y==2 :
                        plt.plot(VOLKSWAGEN.Close["2018-01-01":"2018-12-31"],label="VOLKSWAGEN 2018")
                        plt.xticks(b)
                    elif y==3 :
                        plt.plot(VOLKSWAGEN.Close["2019-01-01":"2019-12-31"],label="VOLKSWAGEN 2019")
                        plt.xticks(c)
                    elif y==4 :
                        plt.plot(VOLKSWAGEN.Close["2020-01-01":"2020-12-31"],label="VOLKSWAGEN 2020")
                        plt.xticks(d)
                    else :
                        print("Select a valid option!")
                choice=input("Do you want to continue ? ").upper()
            plt.title("Comparing the closing value of stocks over time")
            plt.ylabel("Close amount of stocks")
            plt.xlabel("Date")
            plt.legend()
            plt.show()
            A="Y"
        elif ch==3 :
            print("Select the company")
            company()
            x=input("Enter your choice : ").upper()
            m=[2017,2018,2019,2020]
            while A=="N" :
                if x=="A" :
                    a=sum(AUDI.Volume["2017-01-01":"2017-12-31"])
                    b=sum(AUDI.Volume["2018-01-01":"2018-12-31"])
                    c=sum(AUDI.Volume["2019-01-01":"2019-12-31"])
                    d=sum(AUDI.Volume["2020-01-01":"2020-12-31"])
                    plt.bar(m[0],a,label="AUDI 2017")
                    plt.bar(m[1],b,label="AUDI 2018")
                    plt.bar(m[2],c,label="AUDI 2019")
                    plt.bar(m[3],d,label="AUDI 2020")
                elif x=="B" :
                    a=sum(BMW.Volume["2017-01-01":"2017-12-31"])
                    b=sum(BMW.Volume["2018-01-01":"2018-12-31"])
                    c=sum(BMW.Volume["2019-01-01":"2019-12-31"])
                    d=sum(BMW.Volume["2020-01-01":"2020-12-31"])
                    plt.bar(m[0],a,label="BMW 2017")
                    plt.bar(m[1],b,label="BMW 2018")
                    plt.bar(m[2],c,label="BMW 2019")
                    plt.bar(m[3],d,label="BMW 2020")
                elif x=="C" :
                    a=sum(HONDA.Volume["2017-01-01":"2017-12-31"])
                    b=sum(HONDA.Volume["2018-01-01":"2018-12-31"])
                    c=sum(HONDA.Volume["2019-01-01":"2019-12-31"])
                    d=sum(HONDA.Volume["2020-01-01":"2020-12-31"])
                    plt.bar(m[0],a,label="HONDA 2017")
                    plt.bar(m[1],b,label="HONDA 2018")
                    plt.bar(m[2],c,label="HONDA 2019")
                    plt.bar(m[3],d,label="HONDA 2020")
                elif x=="D" :
                    a=sum(NISSAN.Volume["2017-01-01":"2017-12-31"])
                    b=sum(NISSAN.Volume["2018-01-01":"2018-12-31"])
                    c=sum(NISSAN.Volume["2019-01-01":"2019-12-31"])
                    d=sum(NISSAN.Volume["2020-01-01":"2020-12-31"])
                    plt.bar(m[0],a,label="NISSAN 2017")
                    plt.bar(m[1],b,label="NISSAN 2018")
                    plt.bar(m[2],c,label="NISSAN 2019")
                    plt.bar(m[3],d,label="NISSAN 2020")
                elif x=="E" :
                    a=sum(ROLLSROYCE.Volume["2017-01-01":"2017-12-31"])
                    b=sum(ROLLSROYCE.Volume["2018-01-01":"2018-12-31"])
                    c=sum(ROLLSROYCE.Volume["2019-01-01":"2019-12-31"])
                    d=sum(ROLLSROYCE.Volume["2020-01-01":"2020-12-31"])
                    plt.bar(m[0],a,label="ROLLS ROYCE 2017")
                    plt.bar(m[1],b,label="ROLLS ROYCE 2018")
                    plt.bar(m[2],c,label="ROLLS ROYCE 2019")
                    plt.bar(m[3],d,label="ROLLS ROYCE 2020")
                elif x=="F" :
                    a=sum(TATA.Volume["2017-01-01":"2017-12-31"])
                    b=sum(TATA.Volume["2018-01-01":"2018-12-31"])
                    c=sum(TATA.Volume["2019-01-01":"2019-12-31"])
                    d=sum(TATA.Volume["2020-01-01":"2020-12-31"])
                    plt.bar(m[0],a,label="TATA 2017")
                    plt.bar(m[1],b,label="TATA 2018")
                    plt.bar(m[2],c,label="TATA 2019")
                    plt.bar(m[3],d,label="TATA 2020")
                elif x=="G" :
                    a=sum(TESLA.Volume["2017-01-01":"2017-12-31"])
                    b=sum(TESLA.Volume["2018-01-01":"2018-12-31"])
                    c=sum(TESLA.Volume["2019-01-01":"2019-12-31"])
                    d=sum(TESLA.Volume["2020-01-01":"2020-12-31"])
                    plt.bar(m[0],a,label="TESLA 2017")
                    plt.bar(m[1],b,label="TESLA 2018")
                    plt.bar(m[2],c,label="TESLA 2019")
                    plt.bar(m[3],d,label="TESLA 2020")
                elif x=="H" :
                    a=sum(VOLKSWAGEN.Volume["2017-01-01":"2017-12-31"])
                    b=sum(VOLKSWAGEN.Volume["2018-01-01":"2018-12-31"])
                    c=sum(VOLKSWAGEN.Volume["2019-01-01":"2019-12-31"])
                    d=sum(VOLKSWAGEN.Volume["2020-01-01":"2020-12-31"])
                    plt.bar(m[0],a,label="VOLKSWAGEN 2017")
                    plt.bar(m[1],b,label="VOLKSWAGEN 2018")
                    plt.bar(m[2],c,label="VOLKSWAGEN 2019")
                    plt.bar(m[3],d,label="VOLKSWAGEN 2020")
                
                else :
                    print("Select a valid option!")
                print("Volume is the overall purchasing and selling of the stock")
                print("It is a reliable indicator of market strength of a particular stock")
                plt.title("Stock Comparison by volume")
                plt.xticks(m)
                plt.legend()
                plt.show()
                A=input("Do you want to continue?")
                A="Y"
        elif ch==4 :
            a=sum(AUDI.Volume["2017-01-01":"2020-12-31"])
            b=sum(BMW.Volume["2017-01-01":"2020-12-31"])
            c=sum(HONDA.Volume["2017-01-01":"2020-12-31"])
            d=sum(NISSAN.Volume["2017-01-01":"2020-12-31"])
            e=sum(ROLLSROYCE.Volume["2017-01-01":"2020-12-31"])
            f=sum(TATA.Volume["2017-01-01":"2020-12-31"])
            g=sum(TESLA.Volume["2017-01-01":"2020-12-31"])
            h=sum(VOLKSWAGEN.Volume["2017-01-01":"2020-12-31"])
            print("AUDI Stock Market Trading gross volume : ",a)
            print("BMW Stock Market Trading gross volume : ",b)
            print("HONDA Stock Market Trading gross volume : ",c)
            print("NISSAN Stock Market Trading gross volume : ",d)
            print("ROLLS ROYCE Stock Market Trading gross volume : ",e)
            print("TESLA Stock Market Trading gross volume : ",f)
            print("TATA Stock Market Trading gross volume : ",g)
            print("VOLKSWAGEN Stock Market Trading gross volume : ",h)
            x=input("Do you wish to see pie chart presentation of following data ? ").upper()
            if x=="Y" :
                col=[a,b,c,d,e,f,g,h]
                companies=["AUDI","BMW","HONDA","NISSAN","ROLLS ROYCE","TATA","TESLA","VOLKSWAGEN"]
                plt.axis("equal")
                plt.pie(col,labels=companies,autopct="%05.2f%%")
                plt.title("Volume traded over the year 2017-2020")
                plt.show()
            else :
                print("OK")
        elif ch==5 :
            company()
            x=input("Select the company : ").upper()
            A="N"
            while A=="N" :
                if x=="A" :
                    d=input("Enter Date : ")
                    o=float(input("Enter the opening value of stock : "))
                    h=float(input("Enter the highest value attained by the stock on that day : "))
                    l=float(input("Enter the lowest value attained by the stock on that day : "))
                    c=float(input("Enter the closing value of stock : "))
                    Ac=float(input("Enter the Adjclosing value of stock : " ))
                    v=float(input("Enter the volume : "))
                    AUDI=AUDI.append({"Date":d,"Open":o,"High":h,"Low":l,"Close":c,"Adjclose":Ac,"Volume":v},ignore_index=True)
                elif x=="B" :
                    d=input("Enter Date : ")
                    o=float(input("Enter the opening value of stock : "))
                    h=float(input("Enter the highest value attained by the stock on that day : "))
                    l=float(input("Enter the lowest value attained by the stock on that day : "))
                    c=float(input("Enter the closing value of stock : "))
                    Ac=float(input("Enter the Adjclosing value of stock : " ))
                    v=float(input("Enter the volume : "))
                    BMW=BMW.append({"Date":d,"Open":o,"High":h,"Low":l,"Close":c,"Adjclose":Ac,"Volume":v},ignore_index=True)
                elif x=="C" :
                    d=input("Enter Date : ")
                    o=float(input("Enter the opening value of stock : "))
                    h=float(input("Enter the highest value attained by the stock on that day : "))
                    l=float(input("Enter the lowest value attained by the stock on that day : "))
                    c=float(input("Enter the closing value of stock : "))
                    Ac=float(input("Enter the Adjclosing value of stock : " ))
                    v=float(input("Enter the volume : "))
                    HONDA=HONDA.append({"Date":d,"Open":o,"High":h,"Low":l,"Close":c,"Adjclose":Ac,"Volume":v},ignore_index=True)
                elif x=="D" :
                    d=input("Enter Date : ")
                    o=float(input("Enter the opening value of stock : "))
                    h=float(input("Enter the highest value attained by the stock on that day : "))
                    l=float(input("Enter the lowest value attained by the stock on that day : "))
                    c=float(input("Enter the closing value of stock : "))
                    Ac=float(input("Enter the Adjclosing value of stock : " ))
                    v=float(input("Enter the volume : "))
                    NISSAN=NISSAN.append({"Date":d,"Open":o,"High":h,"Low":l,"Close":c,"Adjclose":Ac,"Volume":v},ignore_index=True)
                elif x=="E" :
                    d=input("Enter Date : ")
                    o=float(input("Enter the opening value of stock : "))
                    h=float(input("Enter the highest value attained by the stock on that day : "))
                    l=float(input("Enter the lowest value attained by the stock on that day : "))
                    c=float(input("Enter the closing value of stock : "))
                    Ac=float(input("Enter the Adjclosing value of stock : " ))
                    v=float(input("Enter the volume : "))
                    ROLLSROYCE=ROLLSROYCE.append({"Date":d,"Open":o,"High":h,"Low":l,"Close":c,"Adjclose":Ac,"Volume":v},ignore_index=True)
                elif x=="F" :
                    d=input("Enter Date : ")
                    o=float(input("Enter the opening value of stock : "))
                    h=float(input("Enter the highest value attained by the stock on that day : "))
                    l=float(input("Enter the lowest value attained by the stock on that day : "))
                    c=float(input("Enter the closing value of stock : "))
                    Ac=float(input("Enter the Adjclosing value of stock : " ))
                    v=float(input("Enter the volume : "))
                    TESLA=TESLA.append({"Date":d,"Open":o,"High":h,"Low":l,"Close":c,"Adjclose":Ac,"Volume":v},ignore_index=True)
                elif x=="G" :
                    d=input("Enter Date : ")
                    o=float(input("Enter the opening value of stock : "))
                    h=float(input("Enter the highest value attained by the stock on that day : "))
                    l=float(input("Enter the lowest value attained by the stock on that day : "))
                    c=float(input("Enter the closing value of stock : "))
                    Ac=float(input("Enter the Adjclosing value of stock : " ))
                    v=float(input("Enter the volume : "))
                    TATA=TATA.append({"Date":d,"Open":o,"High":h,"Low":l,"Close":c,"Adjclose":Ac,"Volume":v},ignore_index=True)
                elif x=="H" :
                    d=input("Enter Date : ")
                    o=float(input("Enter the opening value of stock : "))
                    h=float(input("Enter the highest value attained by the stock on that day : "))
                    l=float(input("Enter the lowest value attained by the stock on that day : "))
                    c=float(input("Enter the closing value of stock : "))
                    Ac=float(input("Enter the Adjclosing value of stock : " ))
                    v=float(input("Enter the volume : "))
                    VOLKSWAGEN=VOLKSWAGEN.append({"Date":d,"Open":o,"High":h,"Low":l,"Close":c,"Adjclose":Ac,"Volume":v},ignore_index=True)
                elif x=="J" :
                    A="Y"
                else :
                    print("Select a valid option!")
                print("Record added successfully")
                A="Y"
        elif ch==6 :
            company()
            x=input("Select the company : ").upper()
            if x=="A" :
                d=input("Enter Date for which you want to delete record : ")
                df_AUDI=df_AUDI[df_AUDI["Date"]!=d]
            elif x=="B" :
                d=input("Enter Date for which you want to delete record : ")
                df_BMW=df_BMW[df_BMW["Date"]!=d]
            elif x=="C" :
                d=input("Enter Date for which you want to delete record : ")
                df_HONDA=df_HONDA[df_HONDA["Date"]!=d]
            elif x=="D" :
                d=input("Enter Date for which you want to delete record : ")
                df_NISSAN=df_NISSAN[df_NISSAN["Date"]!=d]
            elif x=="E" :
                d=input("Enter Date for which you want to delete record : ")
                df_ROLLSROYCE=df_ROLLSROYCE[df_ROLLSROYCE["Date"]!=d]
            elif x=="F" :
                d=input("Enter Date for which you want to delete record : ")
                df_TATA=df_TATA[df_TATA["Date"]!=d]
            elif x=="G" :
                d=input("Enter Date for which you want to delete record : ")
                df_TESLA=df_TESLA[df_TESLA["Date"]!=d]
            elif x=="H" :
                d=input("Enter Date for which you want to delete record : ")
                df_VOLKSWAGEN=df_VOLKSWAGEN[df_VOLKSWAGEN["Date"]!=d]    
            else :
                print("Select a valid option!")
            print("record deleted")
        elif ch==7 :
            print("The candle stick chart is useful in depicting all four values : OPEN , CLOSE , HIGH , LOW for a particular day")
            print("The real body represents the price range between the open and close of that day's trading")
            print("The basic difference between the bar chart and the candle stick chart is the wicks or shadows just above and below the real body")
            print("The above wick is the high price and the below wick is the down price")
            print("If closing amount is higher than opening amount the candle is of green colour")
            print("If closing amount is lesser than opening amount the candle is of red colour")
            company()
            x=input("Select the company : ").upper()
            if x=="A" :
                year()
                y=int(input("Enter the year : "))
                if y==1 :
                    mpf.plot(AUDI.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==2 :
                    mpf.plot(AUDI.loc["2018-01-01":"2018-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==3 :
                    mpf.plot(AUDI.loc["2019-01-01":"2019-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==4 :
                    mpf.plot(AUDI.loc["2020-01-01":"2020-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                else :
                    print("Select a valid option!")
            elif x=="B" :
                year()
                y=int(input("Enter the year : "))
                if y==1 :
                    mpf.plot(BMW.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==2 :
                    mpf.plot(BMW.loc["2018-01-01":"2018-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==3 :
                    mpf.plot(BMW.loc["2019-01-01":"2019-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==4 :
                    mpf.plot(BMW.loc["2020-01-01":"2020-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                else :
                    print("Select a valid option!")
            elif x=="C" :
                year()
                y=int(input("Enter the year : "))
                if y==1 :
                    mpf.plot(HONDA.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==2 :
                    mpf.plot(HONDA.loc["2018-01-01":"2018-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==3 :
                    mpf.plot(HONDA.loc["2019-01-01":"2019-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)        
                elif y==4:
                    mpf.plot(HONDA.loc["2020-01-01":"2020-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                else :
                    print("Select a valid option!")
            elif x=="D" :
                year()
                y=int(input("Enter the year : "))
                if y==1 :
                    mpf.plot(NISSAN.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==2 :
                    mpf.plot(NISSAN.loc["2018-01-01":"2018-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==3 :
                    mpf.plot(NISSAN.loc["2019-01-01":"2019-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)        
                elif y==4 :
                    mpf.plot(NISSAN.loc["2020-01-01":"2020-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)        
                else :
                    print("Select a valid option!")
            elif x=="E" :
                year()
                y=int(input("Enter the year : "))
                if y==1 :
                    mpf.plot(ROLLSROYCE.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==2 :
                    mpf.plot(ROLLSROYCE.loc["2018-01-01":"2018-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==3 :
                    mpf.plot(ROLLSROYCE.loc["2019-01-01":"2019-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==4 :
                    mpf.plot(ROLLSROYCE.loc["2020-01-01":"2020-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                else :
                    print("Select a valid option!")
            elif x=="F" :
                year()
                y=int(input("Enter the year : "))
                if y==1 :
                    mpf.plot(TATA.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==2 :
                    mpf.plot(TATA.loc["2018-01-01":"2018-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==3 :
                    mpf.plot(TATA.loc["2019-01-01":"2019-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==4 :
                    mpf.plot(TATA.loc["2020-01-01":"2020-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                else :
                    print("Select a valid option!")
            elif x=="G" :
                year()
                y=int(input("Enter the year : "))
                if y==1 :
                    mpf.plot(TESLA.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==2 :
                    mpf.plot(TESLA.loc["2018-01-01":"2018-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==3 :
                    mpf.plot(TESLA.loc["2019-01-01":"2019-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==4 :
                    mpf.plot(TESLA.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                else :
                    print("Select a valid option!")
            elif x=="H" :
                year()
                y=int(input("Enter the year : "))
                if y==1 :
                    mpf.plot(VOLKSWAGEN.loc["2017-01-01":"2017-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                elif y==2 :
                    mpf.plot(VOLKSWAGEN.loc["2018-01-01":"2018-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
        
                elif y==3 :
                    mpf.plot(VOLKSWAGEN.loc["2019-01-01":"2019-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)

                elif y==4 :
                    mpf.plot(VOLKSWAGEN.loc["2020-01-01":"2020-12-31"],type="candle",style="charles",show_nontrading=False,mav=2,volume=False)
                else :
                    print("Select a valid option!")
            else :
                print("Select a valid option!")
            mpf.show()        
        elif ch==8 :
            print("A. State top 3 and bottom 3 companies by the volume")
            print("B. Data of all stocks")
            x=input("Enter your choice : ").upper()
            if x=="A" :
                a=sum(AUDI.Volume["2017-01-01":"2020-12-31"])
                b=sum(BMW.Volume["2017-01-01":"2020-12-31"])
                c=sum(HONDA.Volume["2017-01-01":"2020-12-31"])
                d=sum(NISSAN.Volume["2017-01-01":"2020-12-31"])
                e=sum(ROLLSROYCE.Volume["2017-01-01":"2020-12-31"])
                f=sum(TATA.Volume["2017-01-01":"2020-12-31"])
                g=sum(TESLA.Volume["2017-01-01":"2020-12-31"])
                h=sum(VOLKSWAGEN.Volume["2017-01-01":"2020-12-31"])
                Volume=[a,b,c,d,e,f,g,h]
                df=pd.Series(Volume,index=["AUDI","BMW","HONDA","NISSAN","ROLLSROYCE","TATA","TESLA","VOLKSWAGEN"])
                df=df.sort_values(ascending=False)
                print("Top 3 companies")
                print(df.head(3))
                print("Bottom 3 companies")
                print(df.tail(3))
            elif x=="B" :
                company()
                y=input("Enter your choice : ").upper()
                if y=="A" :
                    print(AUDI["2017-01-01":"2020-12-31"].describe())
                elif y=="B" :
                    print(BMW["2017-01-01":"2020-12-31"].describe())
                elif y=="C" :
                    print(HONDA["2017-01-01":"2020-12-31"].describe())
                elif y=="D" :
                    print(NISSAN["2017-01-01":"2020-12-31"].describe())
                elif y=="E" :
                    print(ROLLSROYCE["2017-01-01":"2020-12-31"].describe())
                elif y=="F" :
                    print(TATA["2017-01-01":"2020-12-31"].describe())
                elif y=="G" :
                    print(TESLA["2017-01-01":"2020-12-31"].describe())
                elif y=="H" :
                    print(VOLKSWAGEN["2017-01-01":"2020-12-31"].describe())
                else :
                    print("Please select a valid option!")
            else :
                print("Please select a valid option!")
        else :
            print("Please select a valid option!")
        A="Y"
    choice=input("Do you want to continue?(Y/N)").upper()    
else :
    print("Thank You")


