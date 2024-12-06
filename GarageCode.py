import json #so i can process json files

import os # so i can mess with file paths

import time # so i can wait and sos ome animatiosn for no reason







#start menu
MenuOptions = ["1","2","3","4"] 

def StartMenu():
    ClearScreen()
    UserDeciding = True
    while UserDeciding == True:

        SelectedMenuOption = input("Would you like to:\n1)Update Your Items\n2)Log Completed Service\n3)Generate An Invoice\n4)Quit The Program\n")
        if SelectedMenuOption not in MenuOptions:
            NotAnOption()   
        else:
            SelectedMenuOption = int(SelectedMenuOption)
            UserDeciding = False
            if SelectedMenuOption == 1:
                ClearScreen()
                UpdateItemList()
            if SelectedMenuOption == 2:
                ClearScreen()
                ServiceCompleted()
            if SelectedMenuOption == 3:
                ClearScreen()
                GenerateInvoice()
            if SelectedMenuOption == 4:
                Quit()




#tell the user if thats not an option
def NotAnOption():
    print("Sorry This Is Not An Option!\n")






#print initialising LOL
def InitFiles():
    InitMessageList = ["I","N","I","T","I","A","L","I","S","I","N","G"]
    # Print without newline

    for i in InitMessageList:
        print(i, end="")
        time.sleep(0.3)






#####################################################################################################################################################
    #INIT PROGRAM FOLDER
    ProgramFolderPath = 'c:\ProgramData\GarageCalc'
    #Test if the path does not exist
    if not os.path.exists(ProgramFolderPath):

        #if not make the folder
        os.makedirs(ProgramFolderPath)
        #then say youve done so
        print(f"\nFolder '{ProgramFolderPath}' created.")
        time.sleep(0.5)
    else:
        print("\nProgram Folder Present, Please Stand By")
        time.sleep(1)
#####################################################################################################################################################
#BETWEEN THE INIT FOLDER COMMANDS
#####################################################################################################################################################
#init Data folder to c:\ProgramData
    DataFolderPath = 'c:\ProgramData\GarageCalc\Data'

    #Test if the DATA path does not exist
    if not os.path.exists(DataFolderPath):

        #if not make the folder
        os.makedirs(DataFolderPath)
        #then say youve done so
        print(f"Folder '{DataFolderPath}' created.")
        time.sleep(0.5)
    else:
        print("Data Folder Present, Please Stand By\n")
        time.sleep(1)
#####################################################################################################################################################
#BELOW WILL WRITE FILES RATHEWR THAN DATA
#####################################################################################################################################################
#init Data folder to c:\ProgramData
    DataFolderPath = 'c:\ProgramData\GarageCalc\Data'

    #Test if the DATA path does not exist
    if not os.path.exists(DataFolderPath):

        #if not make the folder
        os.makedirs(DataFolderPath)
        #then say youve done so
        print(f"Folder '{DataFolderPath}' created.")
        time.sleep(0.5)
    else:
        print("Data Folder Present, Please Stand By\n")
        time.sleep(1)
#####################################################################################################################################################






#just clears the screen in better english
def ClearScreen():
    os.system('cls')





#Updates the amount of items on the list
def UpdateItemList():
    UserDeciding = True
    while UserDeciding == True:
        IsAddingItem = input("Would you like to add a new item?  (Y/N)\n")
        IsAddingItem = IsAddingItem.lower()

        if "y" in IsAddingItem:
            AddNewItem()
            UserDeciding = False
        elif "n" in IsAddingItem:
            UserSelectItem()
            UserDeciding = False
        else:
            NotAnOption()
            UserDeciding = True
            #Not neccecary to assign this value but looks more readable
    NewCost = UpdateItemCost()
    NewStock = UpdateItemStock()

    print("Your Items Have Been Updated To The System :)\nReturning you to menu!")
    time.sleep(2)
    StartMenu()



#Log it when a service is completed and update stock appropriately
def ServiceCompleted():
    print("Service Completed Not Implemented Yet")
    print("Returning you to menu!")
    time.sleep(2)
    StartMenu()



#takes approproate paramters and 
def GenerateInvoice():
    print("Generate Invoice Not Implemented Yet")
    print("Returning you to menu!")
    time.sleep(2)
    StartMenu()



#quits the thingy
def Quit():
    QuitCheck = input("Are you sure you want to quit? (Y/N)\n")
    QuitCheck = QuitCheck.lower()
    if "n" in QuitCheck:
        StartMenu()
    else:
        print("Have a nice day!\n")



# THESE EXIST TO UPDATE THE ITEM STOCK AND COST I USED TO HAVE THESE AS ONE FUNCTION BUT GOT CONFUSED AND CHANGED IT
def AddNewItem():
    print("New Item Not Implemented Yet")

def UserSelectItem():
    print("Select Item Not Implemented Yet")

def UpdateItemCost():
    NewCost = float(input("What is the cost of this Item?\n"))
    return NewCost

def UpdateItemStock():
    NewStock = float(input("What is the current stock of this Item?\n"))
    return NewStock
# END OF THE UPDATE ITEM FUNCTIONS



InitFiles()
StartMenu()