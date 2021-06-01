class Dish:


  def __init__ (self, dish_name, price):
    self.dish_name = dish_name
    self.price = price
    self.spice_level = 0

  def str(self):
    return self.dish_name + ", Spice Level: " + str(self.spice_level) + ", cost: $" + str(self.price)


  def printme(self):
    print("  "+self.dish_name+"          "+self.price)

def get_user_input_alt():
    usr_input=False
    ccontinue=True
    total=0.0
    while ccontinue:
        ccontinue = input("Do you want to add a dish? Type 'no' if not, anything else for yes : ")
        if ccontinue =="no":
            print('Thank you for visiting us')
            print("The total is : "+str(total))
            ccontinue=False
        else:
            usr_input=small_list()
            print("the user input is "+usr_input)
            if usr_input=="1":
                total=total+printing_list(Dim_Sum,"DISH")
            if usr_input=="2":
                total=total+printing_list(Baked_and_Fried,"Baked and Fried")
            if usr_input=="3":
                total=total+printing_list(Steamed_Rice_Rolls,"Steamed Rice Rolls")
            if usr_input=="4":
                total=total+printing_list(Congee,"Congee")
            if usr_input=="5":
                total=total+printing_list(Dessert,"Dessert")
            print("")

def small_list():
    print("what dish do you like to order?")
    print("")
    print("1- DISH")
    print("2- Baked and Fried")
    print("3- Steamed Rice Rolls")
    print("4- Congee")
    print("5- Dessert")
    dish_type = input("Type here a number from 1 to 5: ")
    return dish_type

def printing_list(b, name):
    i=1
    print("       "+name+"      ")
    for element in b:
        printable=str(element.price)
        e=str(i)
        print(e+"-"+"     "+element.dish_name+"          "+printable)
        i=i+1
    print("")
    selection= input("what dish you will pick?")
    result=pick_product(b,selection)
    
    return result

def pick_product(arr, number):
    true_number=int(number)
    true_number=true_number-1
    picked=arr[true_number]
    return picked.price


def shoping_list():
  for dish in Dim_Sum:
    print(dish.str())
  for dish in Baked_and_Fried:
    print(dish.str())
  for dish in Steamed_Rice_Rolls:
      print(dish.str())
  for dish in Congee:
    print(dish.str())
  for dish in Dessert:
    print(dish.str())

Dim_Sum = [Dish("Seafood Dumpling in Soup with Bird’s Nest", 25.99),
Dish("Goose Liver & Caviar Siu Mai", 12.99),
Dish("Steamed Chicken Feet with Chef’s Sauce", 8.99),
Dish("Chicken with Ginger Bun", 6.99),
Dish("Beef Ball with Preserved Orange Peel", 11.99),
Dish("BBQ Pork Bun", 5.99)]

Baked_and_Fried = [Dish("Pan Fried Chive Shrimp", 7.99),
Dish("Pan Fried Beef Ribs with Maggi Sauce", 7.99),
Dish("Deep Fried Sticky Dumpling with Chicken", 5.99),
Dish("Deep Fried Shrimp Roll", 6.99),
Dish("Crispy Taro with Mushroom Dumpling", 4.99),
Dish("Baked Eel Puff Pastry", 5.99)]

Steamed_Rice_Rolls = [Dish("Steamed Shrimp & Veggie Rice Roll", 13.99),
Dish("Rice Noodle Wrapped with Pork & Shrimp", 15.99),
Dish("BBQ Pork Rice Roll", 11.99),
Dish("Beef Rice Noodle with Perigord Black Truffle", 14.99),
Dish("Mix Mushroom Rice Roll", 10.99),
Dish("Spicy XO Sauce with Scallop Rice Roll", 12.99)]

Congee = [Dish("Fish Maw Congee", 18.99),
Dish("Pumpkin & Sweet Corn Congee", 15.99),
Dish("Chicken & Duck Meat Congee", 16.99),
Dish("Seafood Supreme Super Bowl Congee", 23.99),
Dish("Vegetarian Super Bowl Congee", 17.99),
Dish("Avalone Clam & Fish Super Bowl Congee", 21.99)]

Dessert = [Dish("Baked Salted Egg Yolk Paste Bun", 6.99),
Dish("Milk Tart with Bird’s Nest", 7.99),
Dish("Steamed Milk Pudding with Ginger Juice", 11.99),
Dish("Baked Tapioca & Lotus Paste", 13.99),
Dish("Sweet Egg Yolk Paste Layer Cake", 7.99),
Dish("Cold Coconut Cake", 5.99)]


tax = 1.13
tip = 1.1
get_user_input_alt()