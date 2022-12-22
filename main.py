# ________________________________Special Function - COUPONS AND DISCOUNTS________________________________________
def coupon(total):
    if total >= 100:
        user_input = ""
        user_input = input("You are eligible to use a 10% coupon.\n" "Please follow us on instagram to enjoy the discount, yes / no:\t")
        if user_input.lower() == "yes":
            print ()
            print ("Please follow @sid_kts , @fatty_brian , @rlsh1017 , @jas.ele.t")
            print ("Enjoy the coupon!")
            print ()
            amount_to_pay = total - ((10/100) * total)
            return(amount_to_pay)

        elif user_input.lower() == "no":
            amount_to_pay = total
            return (amount_to_pay)

        else:
            print("Please choose an option: yes / no", "to try again.")
            coupon(total)
    else:
        return total
#___________________________Part 4 - VIEW SALES INFORMATION_________________________________________________________
def sales_read(choice):
    """This is the function to display the records that were requested by user"""
    import datetime
    fob = open("sales.txt", "r")
    read = fob.readlines()
    current_time = datetime.datetime.now() # obtaining the current date and time from the system using module
    count = 0 # to count the number of records in the final output
    if choice == 1: # Daily report
        print ("{0:6} | {1:7} | {2:5} |{3:14}\n". format("Year", "Month", "Day", "Total_Amount")) # repeating header row for the output 
        for i in read:
            i = i.split( ",")
            # comparing the years, months and days to find the records of the same day as the system
            if i[0] == str(current_time.year) and i[1] == str(current_time.month) and i[2] == str(current_time.day):
                print ("{0:6} | {1:7} | {2:5} |{3:14}". format(i[0], i[1], i[2], i[3]))
                count = count + 1
    elif choice == 2: # Weekly report
        print ("{0:6} | {1:7} | {2:5} |{3:14}\n". format("Year", "Month", "Day", "Total_Amount"))
        for i in read:
            i = i.split( ",")
            date = datetime.datetime(int(i[0]), int(i[1]), int(i[2])) # converting the dates in the file into a datetime object
            if (current_time - date).days <=7: #obtaining the days from the resultant timedelta object obtained from subtraction and comparing with the number 7
                print ("{0:6} | {1:7} | {2:5} |{3:14}". format(i[0], i[1], i[2], i[3]))
                count = count + 1
    
    elif choice == 3:  # Monthly Report
        print ("{0:6} | {1:7} | {2:5} |{3:14}\n". format("Year", "Month", "Day", "Total_Amount"))
        for i in read:
            i = i.split( ",")
            if i[0] == str(current_time.year) and i[1] == str(current_time.month): # chacking if the year and month are same
                print ("{0:6} | {1:7} | {2:5} |{3:14}". format(i[0], i[1], i[2], i[3]))
                count = count + 1     
    elif choice == 4: # Yearly Report (Annual)
        print ("{0:6} | {1:7} | {2:5} |{3:14}\n". format("Year", "Month", "Day", "Total_Amount"))
        for i in read:
            i = i.split( ",")
            if i[0] == str(current_time.year): #Just checking if the year is similar to the current system year for the record
                print ("{0:6} | {1:7} | {2:5} |{3:14}". format(i[0], i[1], i[2], i[3]))
                count = count + 1
    elif choice == 5: # Custom date range
        print ("To find records within the given time period, please provide the following details")
        # obtaining the date information from the user step by step to avoid confusions
        y1 = int(input("Enter required starting year:\t"))
        m1 = int(input("Enter required starting month:\t"))
        d1 = int(input("Enter the starting date:\t"))
        y2 = int(input("Enter required ending year:\t"))
        m2 = int(input("Enter required ending month:\t"))
        d2 = int(input("Enter the ending date:\t"))
        date1 = datetime.datetime(y1,m1,d1) # converting the obtained dates into datetime objects
        date2 = datetime.datetime(y2,m2,d2) # same as above
        print ("The records between", date1,"and", date2,"are:")
        print ()
        print ("{0:6} | {1:7} | {2:5} |{3:14}\n". format("Year", "Month", "Day", "Total_Amount"))
        for i in read:
            i = i.split( ",")
            date = datetime.datetime(int(i[0]), int(i[1]), int(i[2])) # converting the present record into a datetime object
            if date>= date1 and date <= date2: #comparing the datetime objects to check if the present record is in range
                print ("{0:6} | {1:7} | {2:5} |{3:14}". format(i[0], i[1], i[2], i[3]))
                count = count + 1
        
    else:
        print ("invalid input")  
        
    if count == 0:
        print ("No records founds for the stipulated time period.")
        print ()
    else: 
        print ("Total no. of records found =", count)
        print ()

def sales_write(total):
    """This is a function that is used to update the sales records in the sales.txt file"""
    import datetime 
    fob = open("sales.txt", "a")
    current_time = datetime.datetime.now()
    #year, month, day, amount
    text = str(current_time.year)+","+ str(current_time.month)+","+ str(current_time.day)+","+str(total)+"\n"
    fob.write(text)
    fob.close()

#________________________________________PART 3 - MENU CHANGES (UPDATE/DELETE/ADD)_________________________________________________________
def function_3():
    # making the update function
    def update_function(menu_list):
        choose_dish = input("Please indicate which dish you wish to update (as integer) whilst referring to the column below: ")
        print("You have chosen to update the dish: ", menu_list[int(choose_dish)][1])
        dish_action = input("Please choose the following options to update the dish, Name or Price: ")
        if dish_action.lower() == "name":
            new_name = input("Please type the new name of the dish: ")
            menu_list[int(choose_dish)][1] = new_name
        elif dish_action.lower() == "price":
            new_price = input("Please type the new price of the dish: ")
            menu_list[int(choose_dish)][2] = new_price
        else:
            print("Invalid input, please try again")
            update_function(menu_list)
        
        # change data type to str type
        New_str = ""
        for i in menu_list:
            New_str += ",".join(i)
            
        # write the new data to the file
        write_new_list = open("Asian confusion menu.txt", "w")
        for i in New_str:
            write_new_list.write(str(i))
        write_new_list.close()

        # displaying the updated menu
        print("The information has been updated successfully")
        Open = open("Asian confusion menu.txt", "r")
        view = Open.readlines()
        for line in view:
            cells = line.split(",")
            print ("{0:5} {1:24} {2:7}". format(cells[0], cells[1], cells[2]))
            print()
  
    # making the add function
    def add_function(menu_list):
        count = 0
        dish_name = input("Please type the name of the new dish: ")
        dish_price = input("Please type the price of the new dish: ")
        new_dish_no = len(menu_list) + count
        count = count + 1
        new_dish = str(new_dish_no) + "," + dish_name + "," + str(dish_price) + "," + "0"+"\n"
        add_new_item = open("Asian confusion menu.txt", "a")
        add_new_item.write(new_dish)
        add_new_item.close()

        # displaying the new menu with addition
        print("The dish has been successfully added")
        Open = open("Asian confusion menu.txt", "r")
        view = Open.readlines()
        for line in view:
            cells = line.split(",")
            print ("{0:5} {1:24} {2:7}". format(cells[0], cells[1], cells[2]))
            print()
    # making the delete function
    def delete_function(menu_list):
        dish_name = input("Please type the number of the dish you wish to delete: ")
        print("You have chosen to delete the dish: ", menu_list[int(dish_name)][1])
        confirm = input("Are you sure you want to delete this dish? Yes or No: ")
        if confirm.lower() == "yes":
            Pop = menu_list.pop(int(dish_name))
            Pop = int(Pop[0])
            
            for i in menu_list[Pop::]:
                i[0] = int(i[0])
                i[0] -= 1
                i[0] = str(i[0])

            # change data type to str type
            New_str = ""
            for i in menu_list:
                New_str += ",".join(i)
                    
            # write the new data to the file
            write_new_list = open("Asian confusion menu.txt", "w")
            for i in New_str:
                write_new_list.write(str(i))
            write_new_list.close()

            # displaying the new menu with deletion
            print("The dish has been successfully deleted")
            Open = open("Asian confusion menu.txt", "r")
            view = Open.readlines()
            for line in view:
                cells = line.split(",")
                print ("{0:5} {1:24} {2:7}". format(cells[0], cells[1], cells[2]))
                print()

        elif confirm.lower() == "no":
            print ("Deletion proces has been terminated.")
    
    # Function 3 main body_
    # making a list version of the menu, in my opinion elements are easier to access with a list
    Open = open("Asian confusion menu.txt", "r")
    view = Open.readlines()
    menu_list = []
    count = 0
    for line in view:
        cells = line.split(",")
        print ("{0:>5} {1:24} {2:7}". format (cells[0], cells[1], cells[2]))
        menu_list.append(cells)
    # ask the user to choose course of action
    print("These are the available actions to perform: Update, Add, Delete, Exit")
    choice = input("Please type the action you wish to perform: ")
    if choice.lower() == "update":
        update_function(menu_list)
    elif choice.lower() == "add":
        add_function(menu_list)
    elif choice.lower() == "delete":
        delete_function(menu_list)
    elif choice.lower() == "exit":
        main()
    else:
        print("Invalid input, please try again")
        function_3()
 
#_____________________________________________PART 2 - DISH RANKING___________________________________________________
def dish_ranking():
    fob = open ("Asian confusion menu.txt", "r")
    lines = fob.readlines()

    for i in range (1,len(lines)-1):
        for j in range (1,len(lines)-i):
            list1 = lines[j].split(",")
            list2= lines[j+1].split(",")
            num1 = int(list1[-1])
            num2 = int(list2[-1])
            if num1>num2:
                lines[j], lines[j+1] = lines[j+1], lines[j]
        
    print ("{0:>6} {1:24} {2:7}". format("RANK", "DISH", "COUNT"))       
    for i in range(-1, -(len(lines)), -1):
        line = lines[i].strip("\n")
        line = line.split(",")
        print ("{0:6} {1:24} {2:7}". format(abs(i), line[1], line[-1]))# check this line something is wrong
        


def add_count(set_num,count):
    """Function to update the count values of each item to enable the creation of a ranking"""
    menu = open("Asian confusion menu.txt", "r") 
    sets = menu.readlines()
    new_sets = []
    for cells in sets:
        set = cells.split(",")
        if str(set_num) in set:
            set[3] = str((int(set[3]) + int(count))) +'\n'
        if set !=['\n']:
            string = set[0]+','+set[1]+','+set[2]+','+set[3]
            new_sets.append(string)
    menu.close()
    write = open("Asian confusion menu.txt", "w")
    write.writelines(new_sets)
    write.close()
        

#__________________________________________________PART 1_____________________________________________________________

def view_menu():
    """This function shall read the menu file and display its contents to the user"""
    Open = open("Asian confusion menu.txt", "r")
    view = Open.readlines()
    sizes = [3,22,5,5]
    gapsize = 2
    price = {}
    #count = {}
    for line in view:
        cells = line.split(",")
        price [cells[0]] = cells[2]
        #count[cells[0]] = cells [3]
        for i in range(3):
            print(('{0:' + str(sizes[i] + gapsize) + '}').format(cells[i]), end="")
        print()
        print()
    return (price)


def view_drinks():
    """This function shall open the drinks menu and display its contents to the user"""
    Open = open("Drinks.txt", "r")
    view = Open.readlines()
    sizes = [4,21,5]
    gapsize = 2
    price = {}
    for line in view:
        cells = line.split(",")
        i = 0
        price[cells[0]] = cells[2]
        for cell in cells:
            print(('{0:' + str(sizes[i] + gapsize) + '}').format(cell), end="")
            i += 1
        print()
    return (price)

#_____________________________________MAIN____________________________________________________________________________
def main():
    """The main function that controls the entire program flow"""
    #This is the introduction section / the part the shows what the user may do
    print ("_"*40+"ASIAN CONFUSION"+"_"*40)
    print ("The place where east meets west")
    print ("Here, you can find cuisines from all over Asia. Anything to suit your TasteBuds!")
    print ()
    print ("Please choose from the following options user:")
    print ("\t 1. Place a new order")  # shall display the menus and update the sales
    print ("\t 2. View our Dish Ranking") # show the most popular and least popular dishes
    print ("\t 3. Update the menu") #shall enable the user to edit the menu
    print ("\t 4. View sales information") # displays the sales records of the restaurant to the user
    choice = int(input("Enter your choice:\t"))

    # condiitonal statements to check which of the above functions to execute
    if choice == 1: # for placing a new order
        print()
        print("Please note that every meal set allows the choice of 1 drink (charges are seperate)")
        chc = "y"
        total = 0
        # Looping until the user does not want to order any more items
        # each item must be ordered separately like in VA canteen
        # control flow: The user can choose a combo --> choose a drink --> choose whether more items (y/n)
            # shall display the bill amount after each combo is added so that users may spend wisely
    
        while chc == "y":
            d = view_menu() # multiple assessment to obtain the prices and the purchasing counts of each combo
            print ()
            c1 = input("Please enter the set number that you would wish to purchase:\t")
            if c1 in d:
                total = float(d[c1]) + total # adding to find the bill amount
                add_count(int(c1), 1)
                 
            else:
                print ("Invalid entry, please restart the program")
                break
            print ()
            
            d2 = view_drinks() # calls the drinks menu. Stores the rices of the drinks
            print ()
            c2 = input("Please enter the number for the drink that you would like to purchase: \t")
            if c2 in d2:
                total = float(d2[c2]) + total #dding to the previous amount to calculate total amount of meal
            else:
                print ("Invalid entry, please restart the program")
                total = 0
                break
            
            print (".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.")
            print ("The total billing amount is:\t", total)
            print ()
            chc = input("Do you wish to add more items (y/n):\t") # to keep looping until user decides not to order anymore food
        print ()
        total = coupon(total)
        print ("Your total amount to be paid is:\t$"+ str(total))
        print ()
        print ("Please visit the nearest counter to make the payment. Your food shall be prepared shortly after.")
        print ("Thank you for ordering at Asian Confusion!")
        sales_write(total) # updating the sales information

        print()
        print()
        #menu()
    elif choice == 2:
        print ()
        print ("The dishes ranked as per the number they were sold are given by:\n")
        dish_ranking()
        print ()
        #dish_ranking()
    elif choice == 3:
        print ()
        function_3()
        print ()
        #update()
    elif choice == 4: # to displlay the reports of the transactions that have already been recorded in the restaurant
        print ()
        print ("Please choose from the followng options")
        print ("1. Daily Report")
        print ("2. Weekly Report")
        print ("3. Monthly Report")
        print ("4. Annual Report")
        print ("5. Custom range")
        c = int(input("Enter the choice for sales report generation:\t"))
        sales_read(c) # calls the function to display the sales records
        #view_sales()
    else:
        print ("invalid input, please try again")

#____________________________________________EXECUTION OF PROGRAM__________________________________________
running = "y"
while running == "y":
    main()
    running = input("Would you like to go back to the main menu (y/n):\t")
    