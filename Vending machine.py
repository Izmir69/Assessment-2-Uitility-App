drinks_menu = [
    { 
    'itemname' : 'Pepsi',
    'itemno' : 1,
    'price' : 3,
    'qty' : 4,
     },

         { 
    'itemname' : 'Coca-Cola',
    'itemno' : 2,
    'price' : 3,
    'qty' : 2,
     },

         { 
    'itemname' : 'Fanta',
    'itemno' : 3,
    'price' : 3,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Sprite',
    'itemno' : 4,
    'price' : 3,
    'qty' : 3,
     },
     
              { 
    'itemname' : '7UP',
    'itemno' : 5,
    'price' : 3,
    'qty' : 1,
     },
     
         { 
    'itemname' : 'Sparkling Water',
    'itemno' : 6,
    'price' : 5,
    'qty' : 4,
     },

         { 
    'itemname' : 'Water',
    'itemno' : 7,
    'price' : 1,
    'qty' : 7,
     },

         { 
    'itemname' : 'Chocolate Milk',
    'itemno' : 8,
    'price' : 3,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Strawberry Milk',
    'itemno' : 9,
    'price' : 3,
    'qty' : 12,
     },
     
              { 
    'itemname' : 'Mango Juice',
    'itemno' : 10,
    'price' : 3,
    'qty' : 9,
     },
         { 
    'itemname' : 'Belvita Biscuits',
    'itemno' : 11,
    'price' : 3,
    'qty' : 4,
     },

         { 
    'itemname' : 'Pringles Chips Salt',
    'itemno' : 12,
    'price' : 3,
    'qty' : 2,
     },

         { 
    'itemname' : 'Pringles Chips Cheese',
    'itemno' : 13,
    'price' : 3,
    'qty' : 14,
     },
     
              { 
    'itemname' : 'Doritos Chips Spicy',
    'itemno' : 14,
    'price' : 3,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Lotte Choco-pie',
    'itemno' : 15,
    'price' : 5,
    'qty' : 6,
     },

         { 
    'itemname' : 'KitKat',
    'itemno' : 16,
    'price' : 2,
    'qty' : 4,
     },

         { 
    'itemname' : 'Oreo',
    'itemno' : 17,
    'price' : 2,
    'qty' : 2,
     },

         { 
    'itemname' : 'Lotus Biscoff',
    'itemno' : 18,
    'price' : 2,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Galaxy Bar Chocolate',
    'itemno' : 19,
    'price' : 3,
    'qty' : 1,
     },
     
              { 
    'itemname' : 'Galaxy Bar Hazelnut',
    'itemno' : 20,
    'price' : 6,
    'qty' : 8,
     },
]

#printing drinks and logo
def drinks():
  print("==========BSUMART-Vending-Machine========")
  print("=================DRINKS================")
  drinks = {
    "01 Pepsi" : "3 AED", 
    "02 Coca-Cola" : "3 AED",
    "03 Fanta" : "3 AED",
    "04 Sprite" : "3 AED",
    "05 7UP" : "3 AED",
    "06 Sparkling Water" : "5 AED",
    "07 Water" : "1 AED",
    "08 Chocolate Milk" : "3 AED",
    "09 Strawberry Milk" : "3 AED",
    "10 Mango Juice" : "3 AED",
}
  for item, price in drinks.items():
    print(f" {item:30} {price}")

#printing snacks
def snacks():
  print("=================SNACKS================")
  snacks_items = {
    "11 Belvita Biscuit" : "3 AED", 
    "12 Pringles Salt" : "3 AED",
    "13 Pringles Cheese" : "3 AED",
    "14 Doritos Spicy" : "3 AED",
    "15 Lotte Choco-pie" : "5 AED",
    "16 KitKat" : "2 AED",
    "17 Oreo" : "2 AED",
    "18 Lotus Biscoff" : "2 AED",
    "19 Galaxy Bar Chocolate" : "3 AED",
    "20 Galaxy Bar Hazelnut" : "6 AED",
}
#A for loop system that prints out the dictionary like a menu
  for item, price in snacks_items.items():
    print(f" {item:30} {price}")
  print()


#printing the menu function
def menu():
  drinks()
  snacks()

#the main ordering system
def order():

  #A while loop that starts the function
  while True:
    
    #prints the menu
    menu()

    #asks user input of the credits
    credits = int(input('Please insert an amount to proceed to buy an item in the vending machine:\n'))

    #invalid amount
    if credits <= 0:
      print('Please enter a valid amount\n')
      order()

    #asks user input of the displayed items
    iteminput = int(input('Please input the number of your desired item\n'))

    #product does not exist message
    if iteminput >= 21 or iteminput <= 0:
      print('Product does not exist or is invalid')
      
    cart = []
    total_sum = []

    for i in drinks_menu:

          #insufficient funds
          if iteminput == i['itemno'] and credits <= i['price'] :
            print('Insufficient funds, please kindly re-enter the appropriate amount\n')
            order()

          #out of stock
          if iteminput == i['itemno'] and i['qty'] <= 0:
            print(f"{i['itemname']} is currently out of stock please choose another item \n")
            order()

          #inputting the item 
          if iteminput == i['itemno'] and credits >= i['price']:

            #displays the item the user picked
            print('=======================================\n')
            print(f"You picked {i['itemname']}\n")
            print('=======================================\n')

            #reduces the stock quantity by 1
            i['qty'] = i.get('qty', 0) - 1

            #appends the price into the list of total_sum
            total_sum.append(i.get('price'))
            
            #appends the item into the cart
            cart.append(i.get('itemname'))

            #prints the remaining stock of the item
            print(f"Amount of {i['itemname']} remaining: {i['qty']}\n")

            #prints the the item being dispensed
            print('=======================================\n')
            print("You may now proceed a receive the following items that have been dispensed:\n")

            #prints the cart
            print(cart, '\n')
            print('=======================================\n')

            #prints the total
            total=sum(total_sum)
            print("And here is your total amount:\n\n\t", total, "AED\n")

            #prints the change
            change = credits - total
            print("And your change is:\n\n\t", change, "AED\n")

            #prints the final message
            print('=======================================\n')
            print("Thank you for choosing BSUMART!\n")
            print('=======================================\n')

            #breaks the for loop function and starts over again
            break

#renaming the function to vending machine
def vendingmachine():
  order()

#output:
vendingmachine()