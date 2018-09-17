def saveTransaction(credit_card, price, description):
    file = open("transaction.txt","a")
    #io.UnsupportedOperation: not writable
    file.write("%16s%07d%s\n" % (credit_card, price * 100, description))
    file.close()

items = ["DONUT","LATTE","FILTER","MUFFIN"]
prices = [1.50, 2.0, 1.80, 1.20]
running = True
while running:
    option = 1
    for choice in items:
        print(str(option)+". "+choice)
        option += 1
    print(str(option)+". Quit")

    choice = int(input("tell me the number of your option:"))
    if choice == option:
        running = False
    elif choice<len(items):
        #credit_number = input("input your credit card number:")
        credit_number = str(4325031994082256)
        saveTransaction(credit_number,prices[choice-1], items[choice-1])
    else:
        print("we don't have this option")