import math

#unicodes for emojis
crown = '\U0001F451' #after restaurant name
house = '\U0001F3E0' #before address
telephone = '\U0000260E' #before phone number
star = '\U00002B50' #after rating
dollarsign = '\U0001F4B2' #after reviews
book = '\U0001F56E' #before menu
meatballs = '\U0001F9C6' #before dishes
dumpling = '\U0001F95F' #before dim sum
fried_shrimp = '\U0001F364' #before baked and fried
fakericeroll = '\U0001F32F' #before steamed rice rolls
congee = '\U0001F963' #before congee
dessert = '\U0001F370' #before dessert
for_drinks = '\U0001F376' #before drinks
cdrinks = '\U0001F964' #before cold drinks
hdrinks = '\U0001F375' #before hot drinks
crossmark = '\U0000274C' #before error message
money = '\U0001F4B5' #after total
smilingface = '\U0001F600' #after thank you
bye = '\U0001F44B' #after 'have a great day'


#receipt, line 194 & line 286
empty_list = {}


#round to two decimal places (for total)
def truncate(number, decimals=0):
    """Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


#creating object
class Dish:
  """Dish class creates a format for the menu. 

     Attributes:
     dish_name: the name of dishes
     price: the price of dishes
  """
  def __init__(self, dish_name, price):
    """Assigns 'nicknames' for dish_name and price variables. 
       
       Preconditions:
       dish_name - string  
       price - float  

       Parameters:
       dish_name = the name of dishes
       price = the price of dishes

       Postconditions:
       Variables dish_name and price can now be referenced using self.dish_name and self.price. 
    """
    self.dish_name = dish_name
    self.price = price

  def __str__(self):
    """Formats the menu with dish name and price. 
       
       Postconditions:
       Returns objects of the Dish class in a full string in the format of "dish, cost: price". 
    """
    return self.dish_name + ", cost: $" + str(self.price)


#menu
#dishes
Dim_Sum = [Dish("Seafood Dumpling in Soup with Bird’s Nest", 25.99), 
           Dish("Goose Liver & Caviar Siu Mai", 12.99), 
           Dish("Steamed Chicken Feet with Chef’s Sauce", 8.99), 
           Dish("Chicken with Ginger Bun", 6.99), 
           Dish("Beef Ball with Preserved Orange Peel", 11.99), 
           Dish("BBQ Pork Bun", 5.99)]

Baked_and_Fried = [Dish("Pan Fried Beef Ribs with Maggi Sauce", 7.99), 
                   Dish("Deep Fried Sticky Dumpling with Chicken", 5.99), 
                   Dish("Deep Fried Shrimp Roll", 6.99), 
                   Dish("Crispy Taro with Mushroom Dumpling", 4.99), 
                   Dish("Baked Eel Puff Pastry", 5.99)] 

Steamed_Rice_Rolls = [Dish("Steamed Shrimp & Veggie Rice Roll", 13.99), 
                      Dish("Rice Noodle Wrapped with Pork & Shrimp", 15.99), 
                      Dish("BBQ Pork Rice Roll", 11.99), 
                      Dish("Beef Rice Noodle with Perigord Black Truffle", 14.99)]

Congee = [Dish("Fish Maw Congee", 18.99), 
          Dish("Pumpkin & Sweet Corn Congee", 15.99), 
          Dish("Chicken & Duck Meat Congee", 16.99)]

Dessert = [Dish("Baked Salted Egg Yolk Paste Bun", 6.99), 
           Dish("Milk Tart with Bird’s Nest", 7.99), 
           Dish("Steamed Milk Pudding with Ginger Juice", 11.99), 
           Dish("Baked Tapioca & Lotus Paste", 13.99), 
           Dish("Sweet Egg Yolk Paste Layer Cake", 7.99), 
           Dish("Cold Coconut Cake", 5.99)]

#drinks
cold_drinks = [Dish("Diet Coke (can)", 2.49), 
               Dish("Coca-Cola (can)", 2.49), 
               Dish("Coke Zero (can)", 2.49), 
               Dish("Sprite (can)", 2.49)]

hot_drinks = [Dish("Longjing Green Tea (teapot)", 6.99), 
              Dish("Yunnan Black Tea (teapot)", 5.99),
              Dish("Anxi Tieguanyin Oolong Tea (teapot)", 7.99),
              Dish("Gongmei White Tea (teapot)", 5.99)]


#printing restaurant name, address, phone number...
print("Crown Princess Fine Dining", crown)
print(house + " 509 Genius Street, Happyland        " + telephone + " (520)300-1314")
print("5.0 " + star*5 + "        9999 + reviews  " + dollarsign*2)
print("")
print(book, "Menu:")
print("")
print(meatballs, "Dishes:")
print("")


#creating format for dishes, adding number and "-" before dish name
print(dumpling, "DIM SUM:")
for i in range (1, len(Dim_Sum) + 1):
  print(i , "-" , Dim_Sum[i-1])
print("\n")

print(fried_shrimp, "BAKED AND FRIED:")
for i in range (1, len(Baked_and_Fried) + 1):
  print(i , "-" , Baked_and_Fried[i-1])
print("\n")

print(fakericeroll, "STEAMED RICE ROLLS:")
for i in range (1, len(Steamed_Rice_Rolls) + 1):
  print(i , "-" , Steamed_Rice_Rolls[i-1])
print("\n")

print(congee, "CONGEE:")
for i in range (1, len(Congee) + 1):
  print(i , "-" , Congee[i-1])
print("\n")

print(dessert, "DESSERT:")
for i in range (1, len(Dessert) + 1):
  print(i , "-" , Dessert[i-1])
print("\n")

print(for_drinks, "Drinks:")
print("")

#creating format for drinks, adding number and "-" before drink name
print(cdrinks, "COLD DRINKS:")
for i in range (1, len(cold_drinks) + 1):
  print(i, "-", cold_drinks[i-1])
print("\n")

print(hdrinks, "HOT DRINKS:")
for i in range (1, len(hot_drinks) + 1):
  print(i, "-", hot_drinks[i-1])
print("\n")


#getting user input
def get_user_input():
  """
     
     Preconditions:
     there are not preconditions

     this is the main function of the program, in it start the flow of instrucctions, it runs inmediatly
     the programm start, it ends when the program does.

  """
  usr_input = False
  ccontinue = True #can't use 'continue' because it already exist
  tax = 1.13
  total = 0.0
  total_cost = 0
  while ccontinue:
    ccontinue = input("Do you want to add a dish/drink? Type 'no' if not, type anything if yes: ")
    if ccontinue.lower() == "no":
      total_cost = tax * total
      print("")
      print("-------------------- RECEIPT --------------------")
      for key, item in empty_list.items():
        print(key + ", " + str(item))
      print("")
      print("Total" + money + " (tax included): $" + str(truncate(total_cost, 2)))
      print("")
      print("Thank you for visiting us!", smilingface, " Have a great day~", bye)
      ccontinue = False
    else:
        usr_input = small_list()
        print("You chose " + usr_input + ".")
        print("")
        if usr_input == "1":
          total = total + printing_list(Dim_Sum, "DIM SUM")
        elif usr_input == "2":
          total = total + printing_list(Baked_and_Fried, "BAKED AND FRIED")
        elif usr_input == "3":
          total = total + printing_list(Steamed_Rice_Rolls, "STEAMED RICE ROLLS")
        elif usr_input == "4":
          total = total + printing_list(Congee, "CONGEE")
        elif usr_input == "5":
          total = total + printing_list(Dessert, "DESSERT")
          print("")
        elif usr_input == "6":
          total = total + printing_list(cold_drinks, "COLD DRINKS")
          print("")
        elif usr_input == "7":
          total = total + printing_list(hot_drinks, "HOT DRINKS")
          print("")
        else:
          print(crossmark + " That is not a valid number.")


#dish/drink types
def small_list():
  """
     
     Postconditions:

     this is an informative printing method, it display all the dishes/drink list the program offer.

  """
  print("What kind of dish/drink would you like to order?")
  print("")
  print("1 - " + "DIM SUM" + dumpling)
  print("2 - " + "BAKED AND FRIED" + fried_shrimp)
  print("3 - " + "STEAMED RICE ROLLS" + fakericeroll)
  print("4 - " + "CONGEE" + congee)
  print("5 - " + "DESSERT" + dessert)
  print("6 - " + "COLD DRINKS" + cdrinks)
  print("7 - " + "HOT DRINKS" + hdrinks)
  print("")
  dish_type = input("Please type a number from 1-7: ")
  return dish_type


#ordering dish
def printing_list(b, name):
  """
     
     Preconditions:
     b - Array
     name - String

     Parameters:
     b: i'ts and array that contain all dishes/drinks for a determined kind of list
     name: i'ts a String that contain the name of the list

     Postconditions:
     this will print all the content inside a food menu using name: price: format
  """
  i = 0
  menu_name = []
  menu_price = []
  print("What dish/drink would you like to order? ")
  print("")
  print(name)
  for element in b:
    printable = str(element.price)
    i = i + 1
    e = str(i)
    print(e + " - " + element.dish_name + ", cost: $" + printable)
    menu_name.append(element.dish_name)
    menu_price.append(element.price)
  print("")
  dishh = input("Please type the dish/drink number: ")
  if dishh.isdigit() == False or int(dishh) > i or int(dishh) <= 0:
    print(crossmark + " That is not a valid number.\n")
    result = pick_product(0,0)
  else:
    print("You ordered " + menu_name[int(dishh)-1] + ".")
    print("")
    result = pick_product(b, dishh)
    empty_list[menu_name[int(dishh)-1]] = [menu_price[int(dishh)-1]]
  return result


def pick_product(arr, number): 
  """Takes a list as a parameter called 'arr'.
     
     Preconditions:
     arr - list
     number - integer

     Parameters:
     arr: array, where the products are saved, uses true_number as an indexer
     number: the user's input (ordered dish/drink number)

     Postconditions:
     Returns 
  """
  if arr == 0 and number == 0:
    return 0
  else: 
    true_number = int(number)
    true_number = true_number - 1
    picked = arr[true_number]
  return picked.price


get_user_input()