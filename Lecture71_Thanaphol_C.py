menu_list = []
price_list = []
def checkbill():
    price = 0
    print("Product Price")
    for number in range (len(menu_list)):
        print(menu_list[number],price_list[0])
    for count in price_list:
        price += count
    print("total price = ",price)

while True:
    menu_name = input("Enter Menu:")
    if menu_name.lower() == "exit":
        break
    else:
        menu_price = int(input("Enter Price:"))
        menu_list.append(menu_name)
        price_list.append(menu_price)
checkbill()

