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