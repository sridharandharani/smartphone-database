import sqlite3

folder = sqlite3.connect("mobile.db")

listoftables = folder.execute(" select name from sqlite_master where type = 'table' and name = 'smartphones' ").fetchall()

if listoftables != []:
    print("Table already exist !")
else:
    folder.execute(''' create table smartphones(
                   id integer primary key autoincrement,
                   brand text,
                   modelname text,
                   serialnum integer,
                   manuyear integer,
                   manumonth integer,
                   price integer);  ''')
    print("Table has created")

while True:
    print("Select an option from the menu :")
    print("1. Add a new mobile")
    print("2. view all the mobilephones")
    print("3. Search for the mobilephone using serial num:")
    print("4. Update for the mobilephone using serial num:")
    print("5. Delete for the mobilephone using serial num:")
    print("6. EXIT")

    choice = int(input("Enter the choice :"))
    if choice == 1:
        getbrand = input("Enter the brand :")
        getmodelname = input("Enter the model name :")
        getserial = input("Enter the serial num: :")
        getyear = input("Enter the manufactured year :")
        getmonth = input("Enter the manufactured month :")
        getprice = input("Enter the manufactured price :")

        folder.execute("insert into smartphones(brand,modelname,serialnum,manuyear,manumonth,price) \
        values('"+getbrand+"','"+getmodelname+"',"+getserial+","+getyear+","+getmonth+","+getprice+")")
        folder.commit()
        print("inserted sucessfully")

    elif choice == 2:
        result = folder.execute("select * from smartphones ")
        for i in result:
            print("id",i[0])
            print("brand",i[1])
            print("model name",i[2])
            print("serial num",i[3])
            print("manufactured year",i[4])
            print("manufactured month",i[5])
            print("price",i[6])

    elif choice == 3:
        getserial = input("Enter the serial number :")
        result = folder.execute("select * from smartphones where serialnum ="+getserial)
        for i in result:
            print("id",i[0])
            print("brand",i[1])
            print("model name",i[2])
            print("serial num",i[3])
            print("manufactured year",i[4])
            print("manufactured month",i[5])
            print("price",i[6])

    elif choice == 4:
        getserial = input("Enter the serial number :")

        getbrand = input("Enter the brand :")
        getmodelname = input("Enter the model name :")
        getyear = input("Enter the manufactured year :")
        getmonth = input("Enter the manufactured month :")
        getprice = input("Enter the manufactured price :")
        folder.execute("update smartphones set \
        brand = '"+getbrand+"',modelname = '"+getmodelname+"',manuyear = "+getyear+",manumonth = "+getmonth+",price = "+getprice+"\
        where serialnum = "+getserial)
        folder.commit()
        print("updated sucessfully")

    elif choice == 5:
        getserial = input("Enter the serial number to be deleted :")
        folder.execute("delete from smartphones where serialnum = "+getserial)
        folder.commit()
        print("deleted")

    elif choice == 6:
        break
    else:
        print("invalid choice")









