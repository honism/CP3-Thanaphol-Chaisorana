User = input("Enter Username:")
Pass = input("Enter Password:")
if User == "hon" and Pass == "1234":
    print("-----WELCOME to Building Electronic&Computer Shop-----")
    print("Order    Product                                           Price")
    print("1.       Ram 8 GB                                       1,600 THB")
    print("2.       Soundcard                                        900 THB")
    print("3.       CPU i5-9400                                    6,900 THB")
    print("4.       Graphic Card                                  12,000 THB")
    print("5.       SSD 500 GB                                     3,200 THB")
    print("6.       HDD 1 TB                                       1,490 THB")
    print("7.       Case                                           2,000 THB")
    print("8.       Monitor 240 Hz                                11,000 THB")
    product = int(input("Select Order(1-8):"))
    if product <1 or product>8:
        print("Enter Order list agian")
        product = int(input("Select Order(1-8):"))
    else:
        if product in range(1,9):
            quant = int(input("Select Quantity(1-10):"))
            if quant < 1 or quant > 11:
                print("Enter Quantity agian")
                quant = int(input("Select Quantity(1-10):"))
            else:
                price = int(input("Enter Price :"))
                total = quant*price
                print("Total Price :",total)














