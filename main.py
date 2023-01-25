# imports
from datetime import datetime
import json


# Defining the general structure of a product
class Product:
    def __init__(self, name, price, quantity, brand, unique_id):  # each product must have the following attributes
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unique_id = unique_id
        self.brand = brand


# Subclasses of product initialised using the super() method to include all attributes of Product
class Clothing(Product):
    def __init__(self, name, price, quantity, brand, unique_id, size, materials):
        super().__init__(name, price, quantity, brand, unique_id)
        self.size = size
        self.materials = materials

    # to_json will generate a json representation of the product
    def to_json(self):
        clothing_json = {"price": self.price,
                         "quantity": self.quantity,
                         "brand": self.brand,
                         "unique id": self.unique_id,
                         "size": self.size,
                         "materials": self.materials
                         }
        return clothing_json


class Food(Product):
    def __init__(self, name, price, quantity, brand, unique_id, expiry_date, gluten_free, suitable_for_vegans):
        super().__init__(name, price, quantity, brand, unique_id)
        self.expiry_date = expiry_date
        self.gluten_free = gluten_free
        self.suitable_for_vegans = suitable_for_vegans

    # to_json will generate a json representation of the product
    def to_json(self):
        datetime_as_str = self.expiry_date.strftime("%d/%m/%Y")  # date is not a jsonable format so change to string
        food_json = {"price": self.price,
                     "quantity": self.quantity,
                     "brand": self.brand,
                     "unique id": self.unique_id,
                     "expiry date": datetime_as_str,
                     "gluten free": self.gluten_free,
                     "suitable for vegan": self.suitable_for_vegans
                     }
        return food_json


class Toys(Product):
    def __init__(self, name, price, quantity, brand, unique_id, minimum_age, gender):
        super().__init__(name, price, quantity, brand, unique_id)
        self.gender = gender
        self.minimum_age = minimum_age

    # to_json will generate a json representation of the product
    def to_json(self):
        toys_json = {"price": self.price,
                     "quantity": self.quantity,
                     "brand": self.brand,
                     "unique id": self.unique_id,
                     "gender": self.gender,
                     "minimum_age": self.minimum_age
                     }
        return toys_json

# a class which stores what products are in and out of the shopping cart
class ShoppingCart:
    def __init__(self, cart_list=[], number_of_products=0):
        self.cart_list = cart_list  # we store the products in a list
        self.number_of_products = number_of_products  # counts the number of products within the cart

    """
    addProduct method will get a product of type class Product and will add it to the cart list
    and will add 1 to the number of products
    """

    def addProduct(self, p):
        self.cart_list.append(p)
        self.number_of_products = self.number_of_products + 1

    """
    removeProduct method will get a product of type class Product and will remove it from the cart list
    and will remove 1 to the number of products
    """

    def removeProduct(self, p):
        for cart_product in self.cart_list:  # iterate over all products
            if cart_product.name == p:  # check if product is current product
                self.cart_list.remove(cart_product)
                self.number_of_products = self.number_of_products - 1

    """
    getContents method will return the current contents of the ShoppingCart
    """

    def getContents(self):
        print("This is the total of the expenses:")
        i = 1
        total_cost = 0
        for item in self.cart_list:
            if item.quantity == 1:  # if there is only one of the product in the cart then print a certain way
                print("\t{} - {} = £{}".format(i, item.name, item.price))
                total_cost = total_cost + item.price  # add to total cost
            else:  # if there is more than one of the product in the cart print a different way
                indiv_cost = item.quantity * item.price
                print("\t{} - {} * {} = £{}".format(i, item.quantity, item.name, indiv_cost))
                total_cost = total_cost + indiv_cost  # add to total cost

            i = i + 1  # print out the number in the cart

        print("\tTotal = £{}".format((total_cost)))  # print total cost

    def changeProductQuantity(self, p, q):  # change the quantity, q of product, p in the cart
        for item in self.cart_list:
            if item.name == p:
                item.quantity = q

    def checkProductExist(self, p):  # check product p exists in the cart
        for item in self.cart_list:
            if item.unique_id == p:
                return True
        print("This product does not exist")
        print("These are the items in your list:")
        for item in self.cart_list:
            print("\tName: {} - \t - \tUnique ID: {}".format(item.name, item.unique_id))
        return False

    def checkListLength(self):  # check the length of the list
        return len(self.cart_list)


# This function will print out all possibilities the user can choose from
def print_help():
    print("The program supports the following command")
    print("\t[A] - Add a new product to the cart")
    print("\t[R] - Remove product from the cart")
    print("\t[S] - Print a summary from the cart")
    print("\t[Q] - Change the quantity of a product")
    print("\t[E] - Export a JSON version of the cart")
    print("\t[T] - Terminate the program")
    print("\t[H] - List the supported commands")


"""
As we will be receiving a lot of user inputs, we must ensure that the program can process these inputs.
Therefore, we must complete quite a lot of validation and formatting.
The following 13 functions handle these inputs. They will either validate the input or format it for the
program to handle them.
Normally these would be stored in a separate file for clarity.
"""


def type_validation(input_value):
    if not string_check(input_value):  # check that the input is a string
        return False

    input_value = input_string_formatting(input_value)  # formatting string to standard type

    if input_value in ['Food', 'Clothing', 'Toys']:  # if type is accepted return True otherwise return false
        return True
    else:  # otherwise return that the type entered is false
        print("Please enter a valid type [Food, Clothing, Toys]")
        return False


def size_validation(size):  # check that it is a valid size
    if size.upper() in ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL']:
        return True
    else:
        print("Please enter a valid size [XXS, XS, S, M, L, XL, XXL]! ")


def gender_validation(gender):  # check that the gender is a valid input
    if gender.lower() in ['m', 'f']:  # .lower() means that we can handle uppercase and lowercase
        return True
    else:
        print("Please enter either 'f' or 'm'.")
        return False


def string_check(test_string):
    if not isinstance(test_string, str):  # checking if string
        print("Please enter a string.")
    return isinstance(test_string, str)  # will return True if it is a string and false if it is not


def int_check(test_int):  # testing to see if a value is an integer
    if isinstance(test_int, int):  # making sure value is an integer
        if int(test_int) < 1:  # we make sure that the input is not negative
            print("Please enter a number bigger than 0")
            return False
        else:
            return True
    else:
        print("Please enter an Integer")
        return False


def float_check(test_float):  # testing the input is a float
    if isinstance(test_float, float):  # check if input is float
        if float(test_float) <= 0:  # making sure that the input is positive
            print("Please enter a floating point number bigger than 0")
            return False
        else:
            return True
    else:
        print("Please enter a number")
        return False


def product_id_check(test_id):  # this function is to check whether or not an id already exists in the cart
    id_exists = 0
    if isinstance(test_id, int):  # make sure input is an integer
        if len(str(test_id)) == 13:  # make sure length of the id is 13
            for item in cart.cart_list:  # go through all items to test their ids
                if item.unique_id == test_id:  # if id is existant, change id_exists to 1
                    id_exists = 1
            if id_exists != 0:  # if id_exists is 1 print that it exists and return False (the input is not vali)
                print("This ID number already exists!")
                return False
            else:
                return True
        else:
            print("Please make sure the ID number is 13 digits")
            return False
    else:
        print("Please enter an Integer")
        return False


def date_check(test_date):  # checking that date is in the right format
    try:
        datetime.strptime(test_date, "%d/%m/%Y")
        if datetime.strptime(test_date,
                             "%d/%m/%Y") < datetime.today():  # making sure that the product has not expired yet
            print("This product has expired! Enter a date in the future.")
            return False
        else:
            return True
    except ValueError:
        print("Please enter in the correct format")
        return False


def input_string_formatting(input_string):  # standardizing the formatting of a string
    input_value = input_string.title()  # changing to format
    output_value = input_value.strip()  # stripping spaces
    return output_value


def input_int_formatting(input_int):  # will check if input can be formatted as integer and then format it as such
    try:
        int(input_int)
        is_int = True
    except ValueError:
        is_int = False

    if is_int:
        return int(input_int)
    else:
        return input_int


def input_float_formatting(input_float):  # will check if input can be formatted as float and then format it as such
    try:
        float(input_float)
        is_float = True
    except ValueError:
        is_float = False

    if is_float:
        return float(input_float)
    else:
        return input_float


def input_bool_formatting(input_bool):  # will check a few different accepted values for bools
    if input_bool.lower() in ['true', '1', 't', 'y', 'yes']:  # if in this accepted value for bools return true
        return True
    if input_bool.lower() in ['false', '0', 'f', 'n', 'no']:  # if in this accepted value for bools return false
        return False
    else:
        print("Please enter a Boolean value (True\False)")
        return


def input_date_formatting(input_date):  # formats the date if possible to a value which can be processed by program
    try:
        datetime.strptime(input_date, "%d/%m/%Y")
        return datetime.strptime(input_date, "%d/%m/%Y")
    except ValueError:
        print("Incorrect data format, should be DD/MM/YYY")
        return input_date


def create_product():  # creating a new product from thin air
    print("Adding a new product:")
    type_is_valid = False

    while not type_is_valid:  # This code will run as long as the inputted type is not a valid type
        new_product_type = input("Insert its type: ")  # gets input
        type_is_valid = type_validation(new_product_type)  # checks if type is within the allowed types

    new_product_type = input_string_formatting(new_product_type)  # reset formatting
    if new_product_type == 'Clothing':  # branch depending on product type, create an object of the product class
        create_clothing()
    if new_product_type == 'Food':
        create_food()
    if new_product_type == 'Toys':
        create_toys()


"""
The following functions create objects of the type product. They all follow a similar structure
1. get standard inputs that all products must have 
2. set input validity to false
3. get inputs for each of the extra attributes specific to that product type
4. if inputs are all valid create an object of that product and add it to our shopping list
I will comment the first one as the others follow a similar sturcture
"""


def create_clothing():  # create object of clothing type
    clothing_name, clothing_price, clothing_quantity, clothing_brand, clothing_ID = standardProductInputs()  # first get the inputs for a regular product

    size_is_valid = False  # set the input validities to false
    material_is_valid = False

    while not size_is_valid:  # will run while the input is not valid
        clothing_size = input("Insert its Size: ")  # get input
        clothing_size = clothing_size.strip()  # first formatting
        clothing_size = clothing_size.upper()  # second formatting
        size_is_valid = size_validation(clothing_size)  # check validitiy, if True move on, else run again
    while not material_is_valid:
        clothing_material = input("Insert its material: ")
        clothing_material = input_string_formatting(clothing_material)
        material_is_valid = string_check(clothing_material)

    cart.addProduct(Clothing(clothing_name, clothing_price, clothing_quantity, clothing_brand, clothing_ID,
                             clothing_size, clothing_material))  # Once all inputs have been received, create an object
    # of the given type and add it to the shopping list
    print("The product {} was added to the cart".format(clothing_name))
    print("The cart contains {} products".format(cart.number_of_products))


def create_food():
    food_name, food_price, food_quantity, food_brand, food_ID = standardProductInputs()

    expiry_date_is_valid = False
    gf_is_valid = 12
    vegan_suitable_is_valid = 12

    while not expiry_date_is_valid:
        expiry_date = input("Insert its expiry date in the format DD/MM/YYYY: ")
        expiry_date_is_valid = date_check(expiry_date)
        expiry_date = input_date_formatting(expiry_date)
    while gf_is_valid == 12:
        food_gf = input("Is the item gluten free: ")
        food_gf = input_string_formatting(food_gf)
        gf_is_valid = input_bool_formatting(food_gf)
        food_gf = input_bool_formatting(food_gf)
    while vegan_suitable_is_valid == 12:
        food_vegan = input("Is the item suitable for vegans: ")
        food_vegan = input_string_formatting(food_vegan)
        vegan_suitable_is_valid = input_bool_formatting(food_vegan)
        food_vegan = input_bool_formatting(food_vegan)

    cart.addProduct(Food(food_name, food_price, food_quantity, food_brand, food_ID,
                         expiry_date, food_gf, food_vegan))
    print("The product {} was added to the cart".format(food_name))
    print("The cart contains {} products".format(cart.number_of_products))


def create_toys():
    toy_name, toy_price, toy_quantity, toy_brand, toy_ID = standardProductInputs()
    is_gender_valid = False
    is_mini_int = False

    while not is_gender_valid:  # this is an example, not a statement on our current political climate
        toys_recommended_gender = input("Insert the recommended gender (m/f): ")
        toys_recommended_gender = input_string_formatting(toys_recommended_gender)
        is_gender_valid = gender_validation(toys_recommended_gender)
    while not is_mini_int:
        minimum_age = input("Insert the minimum age: ")
        minimum_age = input_int_formatting(minimum_age)
        is_mini_int = int_check(minimum_age)

    cart.addProduct(Toys(toy_name, toy_price, toy_quantity, toy_brand, toy_ID,
                         minimum_age, toys_recommended_gender))
    print("The product {} was added to the cart".format(toy_name))
    print("The cart contains {} products".format(cart.number_of_products))


def standardProductInputs():  # standard product input will get the inputs for each product and will return it to the
    # the given create_product() function
    name_not_string = False
    price_not_float = False
    quantity_not_int = False
    brand_not_string = False
    id_not_13digInt = False

    while not name_not_string:
        product_name = input("Insert its name: ")
        product_name = input_string_formatting(product_name)
        name_not_string = string_check(product_name)
    while not price_not_float:
        product_price = input("Insert its price (£): ")
        product_price = input_float_formatting(product_price)
        price_not_float = float_check(product_price)
    while not quantity_not_int:
        product_quantity = input("Insert its quantity: ")
        product_quantity = input_int_formatting(product_quantity)
        quantity_not_int = int_check(product_quantity)
    while not brand_not_string:
        product_brand = input("Insert its brand: ")
        product_brand = input_string_formatting(product_brand)
        brand_not_string = string_check(product_brand)
    while not id_not_13digInt:
        product_ID = input("Insert its ID Number: ")
        product_ID = input_int_formatting(product_ID)
        id_not_13digInt = product_id_check(product_ID)

    return product_name, product_price, product_quantity, product_brand, product_ID


# main loop

print('The program has started.')
cart = ShoppingCart()  # initialise shopping cart for this session

terminated = False
while not terminated:  # continue to run as long as terminated hasn't been switched to true
    c = input("Insert your next command (H for help): ")
    c = c.upper()  # format for comparison reasons

    if c == "A":  # allow the user to add a product to the cart
        create_product()

    elif c == "R":  # allow the user to remove an item
        if cart.checkListLength() == 0:  # if there are no items we cannot remove anything
            print("There are no items to remove.")
        else:  # otherwise check inputs and if the id number exists in the cart and is valid, remove product from cart
            input_valid = False
            product_exists = False
            while (not input_valid) and (not product_exists):
                product_to_remove = input("What product would you like to remove [ID number]: ")
                product_to_remove = input_int_formatting(product_to_remove)
                input_valid = product_id_check(product_to_remove)
                product_exists = cart.checkProductExist(product_to_remove)

            cart.removeProduct(product_to_remove)

    elif c == "S":  # allow the user to show the shopping cart
        if len(cart.cart_list) > 0:  # as long as the cart list has an object return summary
            cart.getContents()
        else:
            print("There are no items in the cart. To add items select 'A'.")

    elif c == "Q":  # allow user to change quantity of item
        if cart.checkListLength() == 0:  # make sure there is an item in the cart
            print("There are no items to remove.")

        else:  # if there are items, set input validities to false
            input_valid = False
            product_exists = False
            quantity_is_int = False

            while not input_valid:
                while not product_exists:  # check input is valid and that the product exists in the cart
                    product_to_edit = input("What product would you like to edit [ID number]: ")
                    product_to_edit = input_int_formatting(product_to_edit)
                    input_valid = product_id_check(product_to_edit)
                    product_exists = cart.checkProductExist(product_to_edit)

            while not quantity_is_int:  # check that the quantity being changed to is an int
                new_product_quantity = input("Change the quantity to: ")
                new_product_quantity = input_int_formatting(new_product_quantity)
                quantity_is_int = int_check(new_product_quantity)

            if new_product_quantity > 0:  # as long as the new product quantity is more than 0 then change the quantity
                cart.changeProductQuantity(product_to_edit, new_product_quantity)

    elif c == "E":  # generates a summary of the cart as a JSON formatted data dump
        file_name = input("Please enter a file name: ")  # filename to save as
        json_file = {}
        for item in cart.cart_list:  # dump each item to json
            json_file[item.name] = json.dumps(item.to_json())

        data = json.dumps(json_file)  # store dump
        with open("{}.json".format(file_name), "w") as f:
            f.write(data)  # write to json

    elif c == "T":  # terminate script
        terminated = True

    elif c == "H":  # print help
        print_help()

    else:
        print("Command not recognised. Please try again.")

print('Goodbye.')

# End of Code
