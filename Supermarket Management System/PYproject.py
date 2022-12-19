'''            ## SUPER MARKET##        '''

'''prepared by,
   #1. Bhargav Kargatiya  :AU2140121
   #2. Dhruv Gajjar       :AU2140123
   #3. priyank patel      :AU2140129
   #4. Darshan Vasani     :AU2140184   
'''

import colorama
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import os
import shutil
from datetime import date

from pip import main

colorama.init(autoreset=True)
columns = shutil.get_terminal_size().columns
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
itemAvailableDict={}
basket={}


########## ADMIN ##########

#-----> See previous Record

def pre_bill():
    with open("bill.txt",'r') as f:
        print(f.read())  
    adm_key=input((color.BOLD + 'Enter Any key For EXIT:' + color.END))
    if (True):
        os.system('cls')
        mainadmin()


#-----> Change The Price
def change_dict(file_name):
    itemchangeDict={}
    file=open(file_name)
    itemAvailablegr=file.readlines()
    file.close()
    for  item in itemAvailablegr:
                name=item.split()[0]
                price=item.split()[1]
                itemchangeDict.update({name:float(price)})
                print(f"{name} {price}")
    print(Style.NORMAL+Back.LIGHTBLUE_EX+Fore.CYAN+"\n#",end=" ")
    change_name=input("     Enter product name:")
    if change_name.title() in itemchangeDict:
        try:
            print(Style.NORMAL+Back.LIGHTBLUE_EX+Fore.CYAN+"\n#",end=" ")
            change_price=int(input("     Enter Product's new price:"))
            itemchangeDict[change_name.title()]=change_price
            print("\nYou successfully changed the price of the product")
        except:
            print("please Enter Correct price !") 
            sleep(3)
            os.system('cls')
            change_dict(file_name)
  

    else:
        print("Enter correct item.")    
        sleep(3)
        os.system('cls')
        change_dict(file_name)

    with open(file_name,"w") as f:
            for key,Value in itemchangeDict.items():
                f.write('%s %s\n' %(key, Value))
    sleep(3)
    os.system('cls')            
    mainadmin()


def change_prc():
    print((color.BOLD + '::In which Categories you want to Change Price::' + color.END).center(columns))
    display_menu()

    print(Style.NORMAL+Back.LIGHTCYAN_EX +Fore.CYAN+"\n#",end=" ")
    admin_chg_prc=(input("Enter the Category number:"))   

    if (admin_chg_prc=='1'):  
        os.system('cls')
        change_dict('Grocery.txt')

    elif(admin_chg_prc=='2'):
        os.system('cls')
        change_dict('dairy and frozen.txt') 

    elif(admin_chg_prc=='3'):
        os.system('cls')
        change_dict('Bed and Bath.txt')

    elif(admin_chg_prc=='4'):
        os.system('cls')
        change_dict('Crockery.txt')

    elif(admin_chg_prc=='5'):
        os.system('cls')
        change_dict("Kitchen Essentials.txt")  

    elif(admin_chg_prc=='6'):
        os.system('cls')
        change_dict("Clothes.txt")

    elif(admin_chg_prc=='7'):
        os.system('cls')
        change_dict("Daily Essentials.txt") 

    elif(admin_chg_prc=='8'):
        os.system('cls')
        change_dict("Home And personal care.txt")

    elif(admin_chg_prc=='9'):
        os.system('cls')
        change_dict("Electrical items.txt")   

    elif(admin_chg_prc=='10'):
        os.system('cls')
        change_dict("Footware.txt")

    elif(admin_chg_prc=='11'):
        os.system('cls')
        change_dict("Toys And Games.txt")  

    elif(admin_chg_prc=='12'):
        os.system('cls')
        change_dict("Fruits And Vagetables.txt") 

    elif(admin_chg_prc=='13'):
        os.system('cls')
        mainadmin()     
    else:
        print("Enter right choise!")   
        sleep(3)
        os.system('cls')
        remove_item()

#----->Remove Items
def removedict_item(file_name):
    removeDict={}
    file=open(file_name)
    itemAvailablegr=file.readlines()
    file.close()
    for  item in itemAvailablegr:
            name=item.split()[0]
            price=item.split()[1]
            print(f"{name} {price}")
    print(Style.NORMAL+Back.LIGHTBLUE_EX+Fore.CYAN+"\n#",end=" ")
    remove_itm=str(input("     Enter item which you want to Remove:"))
    if (remove_itm.lower()=='exit'):
        remove_item()
    else:    
        try:
            for item in itemAvailablegr:  
                name=item.split()[0]
                price=item.split()[1] 
                removeDict.update({name:float(price)})
            remove_itm=remove_itm.title()
            del removeDict[remove_itm]
            with open(file_name,"w") as f:
                for key,Value in removeDict.items():
                    f.write('%s %s\n' %(key, Value))
            print(f"\n{remove_itm} was Removed!")   
        except:
            print("Item not found!")  
            sleep(3)
            os.system('cls')
            removedict_item(file_name)  
        sleep(3)
        os.system('cls')     
        mainadmin()
    
def remove_item():
    print((color.BOLD + '::In which Categories you want to Remove item::' + color.END).center(columns))
    display_menu()

    print(Style.NORMAL+Back.LIGHTCYAN_EX +Fore.CYAN+"\n#",end=" ")
    admin_add=(input("Enter the Category number:"))   

    if (admin_add=='1'):  
        os.system('cls')
        removedict_item('Grocery.txt')

    elif(admin_add=='2'):
        os.system('cls')
        removedict_item('dairy and frozen.txt') 

    elif(admin_add=='3'):
        os.system('cls')
        removedict_item('Bed and Bath.txt')

    elif(admin_add=='4'):
        os.system('cls')
        removedict_item('Crockery.txt')

    elif(admin_add=='5'):
        os.system('cls')
        removedict_item("Kitchen Essentials.txt") 

    elif(admin_add=='6'):
        os.system('cls')
        removedict_item("Clothes.txt")

    elif(admin_add=='7'):
        os.system('cls')
        removedict_item("Daily Essentials.txt")   

    elif(admin_add=='8'):
        os.system('cls')
        removedict_item("Home And personal care.txt")

    elif(admin_add=='9'):
        os.system('cls')
        removedict_item("Electrical items.txt")

    elif(admin_add=='10'):
        os.system('cls')
        removedict_item("Footware.txt")

    elif(admin_add=='11'):
        os.system('cls')
        removedict_item("Toys And Games.txt")  

    elif(admin_add=='12'):
        os.system('cls')
        removedict_item("Fruits And Vagetables.txt") 

    elif(admin_add=='13'):
        os.system('cls')
        mainadmin()     
    else:
        print("Enter right choise!")   
        sleep(3)
        os.system('cls')
        remove_item()

#---->Add Items

def write(file_name):

        choise_  = input("  To go to main menu enter 'Exit', for continue Enter 'yes':") 
        if(choise_.lower() == "yes"):
            print(Style.NORMAL+Back.LIGHTBLUE_EX+Fore.CYAN+"\n#",end=" ")
            add_item_name=input("     Enter item name:")
            print(Style.NORMAL+Back.LIGHTBLUE_EX+Fore.CYAN+"\n#",end=" ")
            add_item_price=input("     Enter item price:")
            try:
                if int(add_item_price)<0:
                        print("Enter correct price")
                        sleep(3)
                        os.system('cls') 
                        add_itme()
                else:
                        with open(file_name,"a") as f:
                            f.write(f"\n{add_item_name.title()} {add_item_price}")
                        print("\nItem added Succesfully")
                        sleep(3)
                        os.system('cls')     
                        mainadmin()
            except:
                print("Please Enter Numeric number in the Price.")  
                sleep(3)
                os.system('cls')
                add_itme()  
        else:
            mainadmin() 

def add_itme():
    print((color.BOLD + '::In which Categories you want to add item::' + color.END).center(columns))
    display_menu()
   
    print(Style.NORMAL+Back.LIGHTCYAN_EX +Fore.CYAN+"\n#",end=" ")
    admin_add=(input("Enter the Category number:"))   
    if (admin_add=='1'):  
        os.system('cls')
        write("grocery.txt")
    elif(admin_add=='2'):
        os.system('cls')
        write("dairy and frozen.txt")
    elif(admin_add=='3'):
        os.system('cls')
        write("Bed and Bath.txt")
    elif(admin_add=='4'):
        os.system('cls')
        write("Crockery.txt")
    elif(admin_add=='5'):
        os.system('cls')
        write("Kitchen Essentials.txt")                 
    elif(admin_add=='6'):
        os.system('cls')
        write("Clothes.txt")
    elif(admin_add=='7'):
        os.system('cls')
        write("Daily Essentials.txt")
    elif(admin_add=='8'):
        os.system('cls')
        write("Home And personal care.txt")
    elif(admin_add=='9'):
        os.system('cls')
        write("Electrical items.txt")     
    elif(admin_add=='10'):
        os.system('cls')
        write("Footware.txt")
    elif(admin_add=='11'):
        os.system('cls') 
        write("Toys And Games.txt") 
    elif(admin_add=='12'):
        os.system('cls')
        write("Fruits And Vagetables.txt")
    elif(admin_add=='13'):
        os.system('cls')  
        mainadmin()  
    else:
        print("Enter right choise!")   
        sleep(3)
        os.system('cls')  
        add_itme()
    
def mainadmin():
    print(Style.DIM +Back.LIGHTCYAN_EX +Fore.BLACK+"###### ADMIN MENU ######".center(columns))

    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("1. \tAdd item\n",end="\t\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("2. \tRemove item\n",end="\t\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("3. \tChange The Price\n",end="\t\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("4. \tSee Previous Bills\n",end="\t\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("5. \tEXIT \n",end="\t\t\t\t")
    print(Style.NORMAL+Back.LIGHTBLUE_EX+Fore.CYAN+"\n#",end=" ")

    admin_menu=(input("      Enter your choice :  "))

    if (admin_menu=='1'):
        os.system('cls')  
        add_itme()
    elif (admin_menu=='2'):
        os.system('cls')  
        remove_item()
    elif(admin_menu=='3'):
        os.system('cls')  
        change_prc()  
    elif(admin_menu=='4'):
        os.system('cls')  
        pre_bill()      
    elif(admin_menu=='5'):
        os.system('cls')
        __init__()
        # print("\n Hope To See You Back Soon. :) ")
    else:
        print("Enter correct number.")
        sleep(3)
        os.system('cls')
        mainadmin()

###########  CUSTOMER ##########
def bill():
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    customer_name=input("Enter Customer name: ")
    os.system('cls')
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    f1 = open("bill.txt", "a")  
    f1.write("**************************************************")
    f1.write('\nName:'+customer_name.title())
    f1.write('\nDate:{}\n'.format(d1))
    f1.write("==================================================")
    f1.write('\nProduct Name\tProduct Quantity\tSubtotal\n')
    sum=0
    for key in basket:
        f1.write(f"{key}")
        f1.write(" "*(16-len(key)))
        f1.write(f"{basket[key]['Quantity']}")
        f1.write("\t\t\t\t     ")
        f1.write(f"{basket[key]['Subtotal']}")
        f1.write("\n")
        sum+=basket[key]['Subtotal']
    f1.write("==================================================")    
    f1.write('\n\t\t\t\tTotal')
    f1.write('\t\t\t\tRs.{}'.format(sum)) 
    f1.write("\n**************************************************")
    f1.write("\n-------------------------------------------------------------------------------------------------")
    f1.write("\n \n")   
    f1.close()
    
    print("*"*50)
    print('Name:{}'.format(customer_name.title()),end=" "*(30-len(customer_name)))
    print('Date:{}'.format(d1))
    print('=' * 50)
    print('Product Name\tProduct Quantity\tSubtotal')
    sum=0
    for key in basket:
        print(f"{key}",end="")
        print(" "*(16-len(key)),end="")
        print(f"{basket[key]['Quantity']}",end="")
        print("\t\t\t",end="")
        print(f"{basket[key]['Subtotal']}")
        sum+=basket[key]['Subtotal']
    print('=' * 50)    
    print('\t\t\t\t\tTotal')
    print('\t\t\t\t\tRs.{}'.format(sum)) 
    print("="*50)
    print('\n\t{}\n'.format("Thanks for shopping with us!"))
    print("*"*50)
    sleep(11)


def add(txt):
        file=open(txt)
        itemAvailablegr=file.readlines()
        file.close()
        for  item in itemAvailablegr: 
            name=item.split()[0]
            price=item.split()[1]
            print(f"{name}: {price}")
            itemAvailableDict.update({name:float(price)})
        choice=input(color.BOLD+"To go to main menu enter 'Exit', for continue Enter 'yes':"+color.END)    

        while(choice.lower()=="yes"):
            add_item=input("\nAdd an item: ")
            if add_item.title() in itemAvailableDict:
                try:
                    item_qty=int(input("Add quantity:"))
                    basket.update({add_item:{"Quantity":item_qty,"Subtotal":itemAvailableDict[add_item.title()]*item_qty}})   
                except: 
                    print("\nPlease Enter correct Quantity !")     
            else:
                print("Unable to add item")  
            print(" ")      
            choice=input(color.BOLD+"To go for main menu enter Exit to continue Enter 'yes':"+color.END)    
            
        else:
            if (choice.lower()=="exit"):
                print("You are EXTING ...")     
                sleep(2)
                os.system('cls')
                category()  
            else:
                print("\nWrite right choice.")
                sleep(3) 
                os.system('cls')
                add(txt)   

def rem_basket():
    print((color.BOLD + 'Customer BASKET' + color.END).center(columns))
    for i in basket:
        for j in basket[i]:
            print(i,":",j,"=",basket[i][j])
        print("\n")
    rem_item=input("Do you want to Remove any item?:")
    while (rem_item.lower()=='yes'):
        item_rem=input("Enter specific item:")
        try:
            del basket[item_rem]   
            print("Item removed. ") 
        except:
            print("Item not found in Basket")
        print("\n")    
        rem_item=input("Do you want to Remove any item?:")  
    os.system('cls')
    basket_13()

def basket_13():

        print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
        print("1. \tSee your Basket\n",end="\t\t\t\t")
        print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
        print("2. \tPrint Bill")
        print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
        print("3. \tAdd items in the basket\n")
        print(Style.NORMAL+Back.LIGHTCYAN_EX +Fore.CYAN+"\n#",end=" ")

        cust_ch2=(input("Enter your choice:"))
        
        if (cust_ch2=='1'):
              os.system('cls')
              rem_basket()
        elif(cust_ch2=='2'):
              os.system('cls')
              bill()   
        elif(cust_ch2=='3'):
             os.system('cls')    
             category()  
        else:
            print("Enter Correct Choice.")
            sleep(3) 
            os.system('cls')         
            basket_13()


def category():
    print(Style.DIM +Back.LIGHTCYAN_EX +Fore.BLACK+"###### CUSTOMER MENU ######".center(columns))
    print((color.BOLD + 'Categories' + color.END).center(columns))

    display_menu()
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("14. \tReturn to main menu")
    print(Style.NORMAL+Back.LIGHTCYAN_EX +Fore.CYAN+"\n#",end=" ")

    cust_ch1=(input("Enter the Category number:"))
   
    if  (cust_ch1=='1'):  
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Grocery ######".center(columns))
        add("Grocery.txt")

    elif(cust_ch1=='7'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Daily Essentials ######".center(columns))
        add("Daily Essentials.txt") 

    elif(cust_ch1=='2'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Dairy and Frozen ######".center(columns))
        add("dairy and frozen.txt")

    elif(cust_ch1=='8'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Home And personal care ######".center(columns))
        add("Home And personal care.txt")

    elif(cust_ch1=='3'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Bed and Bath ######".center(columns))
        add("Bed and Bath.txt")   

    elif(cust_ch1=='9'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Electrical items ######".center(columns))
        add("Electrical items.txt")

    elif(cust_ch1=='4'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Crockery ######".center(columns))
        add("Crockery.txt")  

    elif(cust_ch1=='10'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Footware ######".center(columns))
        add("Footware.txt")

    elif(cust_ch1=='5'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Kitchen Essentials ######".center(columns))
        add("Kitchen Essentials.txt")      

    elif(cust_ch1=='11'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Toys And Games ######".center(columns))
        add("Toys And Games.txt")

    elif(cust_ch1=='6'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Clothes ######".center(columns))
        add("Clothes.txt")

    elif(cust_ch1=='12'):
        os.system('cls')
        print(Style.DIM +Back.LIGHTGREEN_EX +Fore.BLACK+"###### Fruits And Vagetables ######".center(columns))
        add("Fruits And Vagetables.txt") 

    elif(cust_ch1=='13'):
        os.system('cls')
        basket_13()
    elif(cust_ch1=='14'):
        os.system('cls')
        __init__()
    else:
        print("Enter right choice!") 
        sleep(3)
        os.system('cls')
        category()

def display_menu():
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("1. \tGrocery",end="\t\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"##",end=" ")
    print("7. \tDaily Essentials")

    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("2. \tDairy & Frozen",end="\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"##",end=" ")
    print("8. \tHome and personal care")

    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("3. \tBed and Bath",end="\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"##",end=" ")
    print("9.\tElectrical things")

    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("4. \tCrockery",end="\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"##",end=" ")
    print("10.\tFootwear")

    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("5. \tKitchen",end="\t\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"##",end=" ")
    print("11.\tToys & Games")

    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("6. \tClothes",end="\t\t\t\t")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"##",end=" ")
    print("12.\tFruits & Vegetables")

    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("13. \tFor Continue...",end="\n")
    
######## Register and Login ##########    
def admin_register():
        db=open("store.txt","r")
        print(Style.DIM +Back.CYAN +Fore.BLACK+"###### ADMIN REGISTERATION ######".center(columns))
        print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
        print(" 1.   Create your name     :- ",end="")
        admin_name=input()
        print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
        print(" 2.   Create your password :- ",end="")
        admin_password=input()
        d=[]
        f=[]
        for i in db:
            a,b=i.split(", ")
            b=b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d,f))    

        if len(admin_password)<6:
            print("password too short,restart")
            sleep(4)                                                                        
            os.system('cls')
            admin_register()
        elif admin_name in d:
            print("Usearname already exists")
            sleep(3)
            os.system('cls')
            admin_register()
        else:
            db=open("store.txt","a")        
            db.write("\n"+admin_name+", "+admin_password)
            print("Success!")
            db.close()
            sleep(3)
            os.system('cls')
            admin_login()
#admin_register()         
            
def admin_login():
        db=open("store.txt","r")
        print(Style.DIM +Back.CYAN +Fore.BLACK+"###### ADMIN LOGIN ######".center(columns))
        print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
        print(" 1.   Enter your name     :- ",end="")
        admin_name=input()
        print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
        print(" 2.   Enter your password :- ",end="")
        admin_password=input()
        if not len(admin_name or admin_password)<1:
            d=[]
            f=[]
            for i in db:
                a,b=i.split(", ")
                b=b.strip()
                d.append(a)
                f.append(b)
            data=dict(zip(d,f)) 
            try:
                if data[admin_name]:
                    try:
                        if admin_password == data[admin_name]:
                            print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n@@",end=" ")
                            print("   Login Succesfully!",end=" ")
                            print("Hi ",admin_name)
                            sleep(3)
                            os.system('cls') 
                            mainadmin()
                        else:
                            print("Password or Username incorrect")
                            sleep(3)
                            os.system('cls') 
                            admin_login()
                    except:
                        print("incorrect  password or username")
                        sleep(3)
                        os.system('cls')
                      
                        admin_login()
                else:
                    print("Username or password incorrect")
                    sleep(3)
                    os.system('cls')
                    admin_login()
            except:
                print("Username incorrect")
                sleep(3)
                os.system('cls')
                admin_login()
        else:
            print("Value is necessary") 
            sleep(3)
            os.system('cls')  
            admin_login()                                      

def admin():
    print(Style.DIM +Back.CYAN +Fore.BLACK+"###### ADMIN ######".center(columns))
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print(" 1.   Register    [For new Admin] ")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print(" 2.   Login       [For Exiting member] \n")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"##",end=" ")
    print(" 3.   Exit        [To go to main window] \n")
    print(Style.NORMAL+Back.LIGHTBLUE_EX+Fore.CYAN+"\n#",end=" ")
    admin_1=(input("      Enter your choice :  "))
    
    if (admin_1=='1'):
        os.system('cls')  
        admin_register()
    elif (admin_1=='2'):
        os.system('cls')  
        admin_login()
    elif (admin_1=='3'):
         os.system('cls')   
         __init__()
    else:
        print("Enter correct number")
        sleep(3)
        os.system('cls')
        admin()

def __init__():
    print(Style.DIM +Back.CYAN +Fore.BLACK+"###### WELCOME TO SUPERMARKET ######".center(columns))
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("   CUSTOMER     -- 1  ")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("   SUPER ADMIN  -- 2  ")
    print(Style.NORMAL+Back.CYAN+Fore.CYAN+"\n##",end=" ")
    print("   Exit         -- 3  ")
    print(Style.NORMAL+Back.LIGHTBLUE_EX  +Fore.CYAN+"\n#",end=" ")
    user_1=(input("   Enter your choice:    "))
    if(user_1=='2'):
        os.system('cls')    #sdfhf
        admin()
    elif(user_1=='1'):
        os.system('cls')
        category()
    elif(user_1=='3'):
        os.system('cls')
        print("Welcome again")    
    else:
        print("Enter correct number!")
        sleep(3)
        os.system('cls')    
        __init__()
__init__()                   


