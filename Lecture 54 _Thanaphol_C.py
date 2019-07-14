def login():
    username = input("Username:")
    password = input("Password:")
    while username != "hon" or password != "1234":
       print("Username or Password Incorrect")
       username = input("Username:")
       password = input("Password:")
    showMenu()

def showMenu():
    print("----Calculate Program----")
    print("Choose 1----> Calculate Vat")
    print("Choose 2----> Calculate Price")
    menuSelect()

def menuSelect():
    Select=(int(input("Choose number :")))
    if Select == 1:
        print("Vat = ",Vatcalculate(float(input("Enter price:"))))
    else :
        print("Totalprice = ",Pricecalculate(price1 = float(input("First Product:")),price2 = float(input("Second Product:"))))
    return Select

def Vatcalculate(Price):
    VAT = Price * 7 / 100
    return VAT

def Pricecalculate(price1,price2):
    Total = price1+price2
    Totalprice = Total+(Total*7/100)
    return Totalprice

login()




