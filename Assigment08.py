# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Lyndsey Holmes,9.1.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
lst_of_products = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Lyndsey Holmes, 9.1.2020,Modified code to complete assignment 8
    """
    # Data -------------------------------------------------------------------- #
    product_name = None
    product_price = None

    # Processing  ------------------------------------------------------------- #
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (Who,When,What)
        RRoot,1.1.2030,Created Class
        Lyndsey Holmes,9.1.2020,Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file

    # Processing  ------------------------------------------------------------- #
    @staticmethod
    def save_data_to_file():
        """
        Description:  This static function saves the list of objects to a file.
        Parameter file_name: The file to save data
        Parameter list_of_product_objects: a list of product objects.
        """
        file = open(strFileName, 'w')
        for row in lstOfProductObjects:
            file.write(row.product_name + ',' + row.product_price + '\n')
            
        file.close()

    

    @staticmethod
    def read_data_from_file():
        """
        Description:  This static function reads data from a file into a list of objects
        Parameter file_name: The name of the file to read from
        Parameter list_of_product_objects: Read data in to a list of product objects
        """
        file = open(strFileName, 'r')

        for row in file:
            name, price = row.split(",")
            product = Product(name.strip(), price.strip())

            lstOfProductObjects.append(product)
        
        file.close()

   
# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes data to and from a file and a list of product objects:

    methods:
        display_menu(): a list of options including show current data, add data, etc

        user_input(): receive data from user

        display_data(): display a list of the current data

        add_product(): allow user to add product and price

    changelog: (Who,When,What)
        RRoot,1.1.2030,Created Class
        Lyndsey Holmes,9.1.2020,Modified code to complete assignment 8
    """

    # Presentation (Input/Output)  -------------------------------------------- #
    @staticmethod
    def display_menu():
        """
        Description:  Displays menu items to user
        No parameters
        """
        print("")
        print("*----------------- Main Menu -----------------*")
        print("")
        print("Please choose number from the following options:")
        print("(1) Show current data.")
        print("(2) Add new product to list.")
        print("(3) Save file.")
        print("(4) Exit Program.")
        
        
    @staticmethod
    def user_input():
        """
        Description: Receives input from user for menu choice.
        No parameters
        Returns: result
        """
        count = 0

        while(True):
            result = input("Enter a number between 1 - 4: ")
            count = count + 1

            try:
                result = int(result)

                if ((result > 0) & (result < 5)):
                    return result
                
                else:
                    print(str(result) + " is not a menu option. Try again")
                    if count > 2:
                        IO.display_menu()
                        count = 0

            except:
                print(str(result) + " is not a menu option. Try again!")
                
                if count > 2:
                    IO.display_menu()
                    count = 0


    @staticmethod
    def display_data():
        """
        Description: Displays current available data
        No parameters
        """
        for product in lstOfProductObjects:
            print(product.product_name + "," + product.product_price)

    @staticmethod
    def add_product():
        """
        Description: Allows a user to add new data to the list of objects.  
        This static function requests user to provide name of product and
        price of product.  Displays it back to the user.  Asks if input is
        correct. And sends to list of objects.
        No parameters
        """
        name= input("Enter name of product to add: ")
        price = input("Enter name of price for product: ")
        
        product = Product(name, price)

        lstOfProductObjects.append(product)
        

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
FileProcessor.read_data_from_file()     # Load data from file into a list of product objects when script starts
while(True):

    IO.display_menu()                       # Show user a menu of options
    result = IO.user_input()                # Get user's menu option choice
    
    if result == 1:                         # Show user current data in the list of product objects
        IO.display_data()

    elif result == 2:                       # Let user add data to the list of product objects
        IO.add_product()

    elif result == 3:
        FileProcessor.save_data_to_file()

    elif result == 4:
        break


    
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

# Test Code --------------------------------------------------------------- #
# Comment out before final run
# IO.display_menu()
# IO.user_input()
# IO.display_menu()
# IO.add_product()