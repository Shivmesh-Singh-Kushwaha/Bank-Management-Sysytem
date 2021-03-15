# --------------------------BANK MANAGEMENT SYSTEM----------------------------

import mysql.connector as db
mydb=db.connect(host="localhost",user="root",passwd="",database="bank1")

def openAccount():
    name=input("Enter Name: ")
    acc=input("Enter Account No.: ")
    dob=input("Enter D.O.B: ")
    ph=input("Enter Phone: ")
    add=input("enter Address: ")
    opbal=int(input("Enter Opening Balance: "))
    data1=(name,acc,dob,add,ph,opbal)
    data2=(name,acc,opbal)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=mydb.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()
def displayAccount():
    acc=input("Enter Account no.: ")
    a="select * from account where acno = %s"
    data=(acc,)
    c=mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i, end=" ")
    main()
def withdrawlAmount():
    am=int(input("Enter Amount: "))
    acc=input("Enter Account No.:")
    a="select balance from amount where acno = %s"
    data=(acc,)
    c=mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql="update amount set balance = %s where acno = %s"
    d=(tam,acc)
    c.execute(sql,d)
    mydb.commit()
    main()
def closeAccount():
    acc=input("Enter Account no.: ")
    sql1="delete from account where acno = %s"
    sql2="delete from amount where acno = %s"
    data=(acc,)
    c=mydb.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    mydb.commit()
    main()

def balanceEq():
    acc=input("Enter Account No.: ")
    a="select balance from amount where acno = %s"
    data=(acc,)
    c=mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balance for Account :",acc," is ",myresult[0])
    main()



def depositAmount():
    am=int(input("Enter Amount: "))
    acc=input("Enter Account No: ")
    a="select balance from amount where acno = %s"
    data=(acc,)
    c=mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set balance = %s where acno = %s"
    d=(tam,acc)
    c.execute(sql,d)
    mydb.commit()
    main()

def main():
    print('''
    1.Open New Account
    2.Deposit Amount
    3.Withdraw Amount
    4.Balance Enquiry
    5.Display Customer Details
    6.Close an Account
    ''')
    choice=input("Enter Task no.: ")
    if(choice=='1'):
        openAccount()
    elif (choice=='2'):
        depositAmount()
    elif (choice=='3'):
        withdrawlAmount()
    elif (choice=='4'):
        balanceEq()
    elif (choice=='5'):
        displayAccount()
    elif (choice=='6'):
        closeAccount()
    else:
        print("Wrong Choice.......")
    
#__main__
print("                           _____________________________________________")
print("                          |           BANK MANAGEMENT SYSTEM            |")
print("                          |_____________________________________________|")
main()