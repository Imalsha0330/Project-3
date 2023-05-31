print("Welcome To The Liquor Store")
#The main heading

print("Please Select The Number For Your Preference")

print("Press Number 1 for Hard Liquor")
print("Press Number 2 for Red Wine")
print("Press Number 3 for White Wine")
print("Press Number 4 for Beer")
#Giving the option to select the prefered number

num = int(input("Please Enter a Number:"))
result = None
#input added to enter the number

if num is 1: #The first If Statement for Hard Liquor
    print("You Have Chosen Hard Liquor")
    print("Below Are Our Options:")
    print("Vodka 750ml 20$,", "Red Label 750ml 25$,", "Jack Daniels 750ml 30$")#Hard Liquor Options
    print("Press 1 For Vodka")#Giving Option to select the prefered one
    print("Press 2 For Red Label")
    print("Press 3 For Jack Daniel")
    num1 = int(input("Please Enter a Number:"))#Input bar to Enter the Number
    result = None
    if num1 == 1:#The nested if statement under Hard Liquor
        print("You Have Chosen Vodka 750ml Bottel")#option what have chosen
        print("Please Select The Quantity")
        quantityhl = int(input("Please Enter Your Quantity:"))#Input bar to enter the quantity
        quantityhl1 = (quantityhl * 20)#multiplying the quantity with the price
        print("Your Total will be")
        print(quantityhl1)#getting the multiplied value
        print("All The Rates Are In US$")
        namehl = str(input("Please Enter Your Name:"))#getting the name
        phhl = str(input ("Please Enter Your Phone Number:"))#getting the phone number
        adhl = str(input("Please Enter Your Address:"))#getting the address
        print("Thank You For Your Order" + " " + namehl)
        print("One Of Our Delivery Agent Will Contact You," + " " + phhl + " " + "On This Number")
        print("And Once We Got an Order Confirmation From Your End, We Will Deliver Your Oder to" + " " + adhl)#confirmation message
        idhl = str(input("Please Enter Your ID Number For Age Verification"))#Id Entering Input bar for age verification
        print("Your ID number" + " " + idhl + " " + "Is Under Age Verification Process")#Message about age verification
        print("We Will Contact You Within 30 Mins After The Age Verification")
        print("Thank you for your oder!")#Final Thank you message.
    elif num1 == 2:#The nested elif statement under Hard Liquor
        print("You Have Chosen Red Label 750ml Bottel")#option what have chosen
        print("Please Select The Quantity")
        quantityhl = int(input("Please Enter Your Quantity:"))#Input bar to enter the quantity
        quantityhl1 = (quantityhl * 25)#multiplying the quantity with the price
        print("Your Total will be")
        print(quantityhl1)#getting the multiplied value
        print("All The Rates Are In US$")
        namehl = str(input("Please Enter Your Name:"))#getting the name
        phhl = str(input ("Please Enter Your Phone Number:"))#getting the phone number
        adhl = str(input("Please Enter Your Address:"))#getting the address
        print("Thank You For Your Order" + " " + namehl)
        print("One Of Our Delivery Agent Will Contact You," + " " + phhl + " " + "On This Number")
        print("And Once We Got an Order Confirmation From Your End, We Will Deliver Your Oder to" + " " + adhl)#confirmation message
        idhl = str(input("Please Enter Your ID Number For Age Verification"))#Id Entering Input bar for age verification
        print("Your ID number" + " " + idhl + " " + "Is Under Age Verification Process")#Message about age verification
        print("We Will Contact You Within 30 Mins After The Age Verification")
        print("Thank you for your oder!")#Final Thank you message.
    elif num1 == 3:#The nested second elif statement under Hard Liquor
        print("You Have Chosen Jack Daniels 750ml Bottel")#option what have chosen
        print("Please Select The Quantity")
        quantityhl = int(input("Please Enter Your Quantity:"))#Input bar to enter the quantity
        quantityhl1 = (quantityhl * 30)#multiplying the quantity with the price
        print("Your Total will be")
        print(quantityhl1)#getting the multiplied value
        print("All The Rates Are In US$")
        namehl = str(input("Please Enter Your Name:"))#getting the name
        phhl = str(input ("Please Enter Your Phone Number:"))#getting the phone number
        adhl = str(input("Please Enter Your Address:"))#getting the address
        print("Thank You For Your Order" + " " + namehl)
        print("One Of Our Delivery Agent Will Contact You," + " " + phhl + " " + "On This Number")
        print("And Once We Got an Order Confirmation From Your End, We Will Deliver Your Oder to" + " " + adhl)#confirmation message
        idhl = str(input("Please Enter Your ID Number For Age Verification"))#Id Entering Input bar for age verification
        print("Your ID number" + " " + idhl + " " + "Is Under Age Verification Process")#Message about age verification
        print("We Will Contact You Within 30 Mins After The Age Verification")
        print("Thank you for your oder!")#Final Thank you message.
    else:#The Else Statement under main if statement
        print("Invalid Number")#If the Number Invalid this message will appear
        print(num1) 
elif num is 2:#The first Elif Statement for Red Wine
    print("You Have Chosen Red Wine")
    print("Below Are Our Options:")
    print("Burn Valley Vineyard Pinot Noir 2021 750ml 40$,", "Lyme Bay Pinot Noir 2020 750ml 45$,", "Denbies Pinot noir 2019 750ml 50$")#Red Wine Options
    print("Press 1 For Burn Valley Vineyard Pinot Noir 2021")#Giving Option to select the prefered one
    print("Press 2 For Lyme Bay Pinot Noir 2020")
    print("Press 3 For Denbies Pinot noir 2019")
    num1 = int(input("Please Enter a Number:"))#Input bar to Enter the Number
    result = None
elif num is 3:#The first Elif Statement for White Wine
    print("You Have Chosen White Wine")
    print("Below Are Our Options:")
    print("Conte Priola Pinot Grigio 750ml 38$,", "Joel Gott Sauvignon Blanc 750ml 42$,", "Whitehaven Sauvignon Blanc 750ml 48$")#White Wine Options
    print("Press 1 For Conte Priola Pinot Grigio")#Giving Option to select the prefered one
    print("Press 2 For Joel Gott Sauvignon Blanc")
    print("Press 3 For Whitehaven Sauvignon Blanc")
    num1 = int(input("Please Enter a Number:"))#Input bar to Enter the Number
    result = None
elif num is 4:#The first Elif Statement for Beer
    print("You Have Chosen Beer")
    print("Below Are Our Options:")
    print("Carlsberg 500ml 10$,", "Heineken 500ml 10$,", "Corona 500ml 10$")#Beer Options
    print("Press 1 For Carlsberg")#Giving Option to select the prefered one
    print("Press 2 For Heineken")
    print("Press 3 For Corona")
    num1 = int(input("Please Enter a Number:"))#Input bar to Enter the Number
    result = None
else:#Else Statement if Entered a wrong value
    print("Invalid Number")
    print(num)