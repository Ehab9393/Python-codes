# Dictionary containing trivia questions and answers
trivia_questions = {
    "12": "How many items are in a dozen? ",
    "Canberra": "What is the capital city of Australia? ",
    "India": "What is the largest country on Earth by population? ",
    "Tokyo": "Before Paris this year, what city hosted the previous summer Olympic Games? ",
    "CERN": "At what European organization was the World Wide Web first created? "
}

print("Welcome to trivia. You must answer 5 questions correctly to win.")
correct_answers = 0

# Iterate through each question and answer pair in the dictionary
for answer, question in trivia_questions.items():
    # Get user input and convert it to lowercase for case-insensitive comparison
    user_answer = input(question).lower()

    # Compare the user's answer to the correct answer (converted to lowercase)
    if user_answer == answer.lower():
        print("Correct.")
        correct_answers += 1
    else:
        print(f"Incorrect. The answer is {answer}.")
        break

# Display the final result
print(f"Game over. Total number of correct answers was {correct_answers}.")



#Write a program that creates a class called Product that has the following attributes:
#•	store: This is a class attribute and is set to “My Corner Store”
#•	name: An instance attribute that is the name of the product
#	  weight: An instance attribute that represents the weight of the product in grams
#•	health_rating: An instance attribute that represents a 0-5 health rating (0.5 ratings are allowed)
#•	cost: An instance attribute that represents the cost of the product
#You program should allow the user to enter 3 items names, weights, health ratings and costs and create an object for each item. Store these objects by appending them to a list.
#Once all the items have been entered, writing a heading that includes the store name, and then the information about each of the 3 items.
#At the end, add a summary with the total and average cost of the items.
#REQUIREMENTS
#•	Your program must create an object of class Product for each product item, and store them in a list.
#•	Your program must get the store name from the class attribute for the heading.
#•	You must use the __str__ function to format the output for printing.
#•	The user input is always correct (input verification is not required).
#•	Your code must be based only on the materials covered in weeks 1 to 9 of the course.
#•	Your output must appear exactly like the following example (the text in red bold indicates the user input).
#Sample Output:
#Enter item 1 name: Vegemite
#Enter item 1 weight (g): 300
#Enter item 1 health rating (0-5): 3.5
#Enter item 1 cost: 4.65
#Enter item 2 name: Cheese
#Enter item 2 weight (g): 250
#Enter item 2 health rating (0-5): 3
#Enter item 2 cost: 3.5
#Enter item 3 name: Bread
#Enter item 3 weight (g): 150
#Enter item 3 health rating (0-5): 4.5
#Enter item 3 cost: 2

#Items from My Corner Store:
#Vegemite (300g) with health rating of 3.5 and cost of $4.65
#Cheese (250g) with health rating of 3 and cost of $3.50
#Bread (150g) with health rating of 4.5 and cost of $2.00
#Total cost of products is $10.15
#Average cost of products is $3.38

class Product:
    store = "My Corner Store"   #class attribute

    def __init__(self, name, weight, health_rating, cost):
        self.name = name
        self.weight = weight
        self.health_rating = health_rating
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.weight}g) with health rating of {self.health_rating} and cost of ${self.cost:.2f}"

products = []
for i in range(1, 4):
        name = input(f"Enter item {i} name: ")
        weight = int(input(f"Enter item {i} weight (g): "))
        health_rating = float(input(f"Enter item {i} health rating (0-5): "))
        cost = float(input(f"Enter item {i} cost: "))
        products.append(Product(name, weight, health_rating, cost))
print()
print(f"Items from {Product.store}:")

total_cost = 0
num_0f_products = 0  # to count the number of products

for p in products:
    print(p)
    total_cost += p.cost  # add the cost of each product to the total
    num_0f_products += 1  # increment the counter for each product

average_cost = total_cost / num_0f_products  # calculate the average using the counter
print(f"Total cost of products is ${total_cost:.2f}")
print(f"Average cost of products is ${average_cost:.2f}")


#Write code to create a class called MathQuestion and the method __init__
#to initialise the following instance attributes in this order:
#-number1 (an integer)
#-number2 (an integer)
#-operation (a string)
#-solution  (an integer)
class MathQuestion:
  def __init__(self, number1, number2, operation, solution):
    self.number1= number1
    self.number2= number2
    self.operation= operation
    self.solution= solution
  def str (self):
   return "{0} {2} {1} = {3}".format(
self.number1,
self.number2,
self.operation,
self.solution
)
  def __repr__(self):
   return "MathQuestion({0}, {1}, '{2}', {3})".format(
self.number1,
self.number2,
self.operation,
self.solution
)
  def __init__(self, number1, number2, operation, solution):
  #{
    self.number1 = number1
    self.number2 = number2
    self.operation = operation
    self.solution = solution
  #}

  def question_text(self):
   """return the question text (without the solution)
   """
   return "{0} {2} {1} = ".format(
       self.number1,
       self.number2,
       self.operation
   )
  def check_answer(self,answer):
    """return true if the answer is equal to the solution
    """
    if(answer== self.solution):
      return "Correct"
    else:
      return "Not correct"
questionObj1= MathQuestion(3, 5, "+", 8)
questionObj2= MathQuestion(7, 5, "-", 2)
questionObj3= MathQuestion(20, 5, "X", 100)
questionObj4= MathQuestion(20, 5, "/", 4)

print(str(questionObj1))
print(str(questionObj2))
print(str(questionObj3))
print(str(questionObj4))

print(repr(questionObj1))
print(repr(questionObj2))
print(repr(questionObj3))
print(repr(questionObj4))

print(questionObj1.check_answer(8))
print(questionObj2.check_answer(1))
print(questionObj3.check_answer(15))
print(questionObj4.check_answer(2))

print(questionObj1.question_text())
print(questionObj2.question_text())
print(questionObj3.question_text())
print(questionObj4.question_text())

class MathQuestion:
    def __init__(self, number1, number2, operation, solution):
        self.number1 = number1
        self.number2 = number2
        self.operation = operation
        self.solution = solution

# create objects:
questionObj1 = MathQuestion(20, 5, '+', 25)
questionObj2 = MathQuestion(20, 5, '-', 15)
questionObj3 = MathQuestion(20, 5, 'x', 100)
questionObj4 = MathQuestion(20, 5, '/', 4)

# To verify the created objects, you can print them out:
print(f"Question 1: {questionObj1.number1} {questionObj1.operation} {questionObj1.number2} = {questionObj1.solution}")
print(f"Question 2: {questionObj2.number1} {questionObj2.operation} {questionObj2.number2} = {questionObj2.solution}")
print(f"Question 3: {questionObj3.number1} {questionObj3.operation} {questionObj3.number2} = {questionObj3.solution}")
print(f"Question 4: {questionObj4.number1} {questionObj4.operation} {questionObj4.number2} = {questionObj4.solution}")

class MathQuestion:
  def __init__(self, number1, number2, operation, solution):
  #{
    self.number1 = number1
    self.number2 = number2
    self.operation = operation
    self.solution = solution
  #}

  def question_text(self):
   """return the question text (without the solution)
   """
   return "{0} {2} {1} = ".format(
       self.number1,
       self.number2,
       self.operation
   )
questionObj1 = MathQuestion(20, 5, '+', 25)
questionObj2 = MathQuestion(20, 5, '-', 15)
questionObj3 = MathQuestion(20, 5, 'x', 100)
questionObj4 = MathQuestion(20, 5, '/', 4)
print(questionObj1.question_text())
print(questionObj2.question_text())
print(questionObj3.question_text())
print(questionObj4.question_text())


import random
class MathQuestion:
  def __init__(self, number1, number2, operation, solution):
    self.number1 = number1
    self.number2 = number2
    self.operation = operation
    self.solution = solution
  def generate_question_add():
    """generate a random addition question
    """
    operation="+"
    number1=random.randint(0,20)
    number2= random.randint(0,20)
    solution= number1 + number2
    return MathQuestion(number1,number2,operation,solution)
    random_question1 = MathQuestion.generate_question()
    print(str(random_question1))

  def generate_question_sub():
    """generate a random subtraction question
    """
    operation="-"
    number1=random.randint(0,20)
    number2= random.randint(0,20)
    solution= number1 - number2
    return MathQuestion(number1,number2,operation,solution)

  def generate_question_multiply():
    """generate a random multiplication question
    """
    operation="X"
    number1=random.randint(0,20)
    number2= random.randint(0,20)
    solution= number1 * number2
    return MathQuestion(number1,number2,operation,solution)

  def generate_question_div():
    """generate a random division question
    """
    operation="/"
    number1=random.randint(0,20)
    number2= random.randint(0,20)
    solution= number1 / number2
    return MathQuestion(number1,number2,operation,solution)
print("welcome to math: ")
while True:
  question = MathQuestion. generate_question_add()
# get the question text and prompt the user to answer the question
  question = MathQuestion. generate_question_add()
# ask user to enter solution or quit
  user_input = input(question)
# check if student want to quit
  if(user_input == "q"):
   print("Good bye!")
  break
# user don't want to quit - translate string to integer for answer
  answer = int(user_input)
# check user answer correct or not
  correct = question. check_answer(answer)
  if(correct):
   print("Correct")
  else:
   print("Incorrect")



import random

class MathQuestion:
    def __init__(self, number1, number2, operation, solution):
        self.number1 = number1
        self.number2 = number2
        self.operation = operation
        self.solution = solution

    def __repr__(self):
        return f"{self.number1} {self.operation} {self.number2}"

# Function to generate a random math question
def generate_random_question():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    operation = random.choice(['+', '-', 'x', '/'])

    # Calculating the correct solution based on the operation
    if operation == '+':
        solution = number1 + number2
    elif operation == '-':
        solution = number1 - number2
    elif operation == 'x':
        solution = number1 * number2
    else:
        # Ensure no division by zero and keep it integer division
        number2 = random.randint(1, 50) or 1  # Avoid zero
        solution = number1 / number2

    return MathQuestion(number1, number2, operation, solution)

# Generate four random math questions
questions = [generate_random_question() for _ in range(4)]

# Iterate over each question to ask the user and check the answer
for question in questions:
    print(f"Question: {repr(question)} = ?")
    user_answer = int(input("Enter your answer: "))

    if user_answer == question.solution:
        print("Correct!")
    else:
        print("Not correct. The correct answer is:", question.solution)


#Below is a code snippet of a class called MathQuestion is given.
#Your task is to write the method check_answer(self, answer) so that
#it returns True if the argument answer is equal to the object's attribute solution,
#otherwise, it returns False.
class MathQuestion:
#{
  def __init__(self, number1, number2, operation, solution):
  #{
    self.number1 = number1
    self.number2 = number2
    self.operation = operation
    self.solution = solution
  #}

  def check_answer(self, answer):
  #{
    # Returns true if the answer is equal to the solution
  #}
#}
   """
   Returns true if the answer is equal to the solution
   """
   if(answer == self.solution):
    return True
   else:
    return False
question1 = MathQuestion(4, 6, "+", 10)
question2 = MathQuestion(17, 10, "-", 7)
question3 = MathQuestion(5, 3, "x", 15)
question4 = MathQuestion(35, 5, "/", 7)
print(question1.check_answer(10))
print(question2.check_answer(1))
print(question3.check_answer(15))
print(question4.check_answer(2))


#Create a program with a class called Sport and the following instance (object) attributes:
#-	name
#-	number_players_team
#-	number_players_world
#Create 2 objects, one for “football” (11 players in a team) and one for “basketball” (5 players in a team)
#but leave the number of players worldwide as 0.
#Then ask the user to input the number of players worldwide for football,
#nd then for basketball. Print out the sport names from their object, not as a literal string.
#Then print out the details for each sport (making sure you code __str__).
class Sport:
    def __init__(self, name, number_players_team, number_players_world):
        self.name = name
        self.number_players_team = number_players_team
        self.number_players_world = number_players_world

    # Define the __str__ method to format the output
    def __str__(self):
        return (f"Sport: {self.name}\n"
                f"Number of Players in a Team: {self.number_players_team}\n"
                f"Number of Players Worldwide: {self.number_players_world}")

# Create objects for football and basketball
football = Sport("football", 11, 0)
basketball = Sport("basketball", 5, 0)

# Ask the user to input the number of players worldwide for each sport
football.number_players_world = int(input(f"Enter the number of players worldwide for {football.name}: "))
basketball.number_players_world = int(input(f"Enter the number of players worldwide for {basketball.name}: "))

# Print out the sport names from the object attributes
print(f"\nSport names from objects: {football.name} and {basketball.name}")

# Print out the details for each sport
print("\nDetails for each sport:")
print(football)
print(basketball)


#Write a program to create a series of objects that contain two fields,
#city and country. Create 8 objects listing different cities and which countries they belong to.
#Create a trivia game where you give the user a city and ask them to enter the correct country.
#Keep score of how many questions that the user gets right and give them a total at the end of the game.
import random
class countery:
  def __init__(self, city, country):
    self.city=city
    self.country=country
city_country_list = [
    ("Paris", "France"),
    ("Tokyo", "Japan"),
    ("Cairo", "Egypt"),
    ("Sydney", "Australia"),
    ("New York", "USA"),
    ("Moscow", "Russia"),
    ("Rio de Janeiro", "Brazil"),
    ("Berlin", "Germany")
]
random.shuffle(city_country_list)
score=0
print("welcome to trivia game: ")
for city,country in city_country_list:
  user_answer= input(f"What country does {city} belongs to: ")
  if user_answer.lower() == country.lower():
    print("correct")
    score+=1
  else:
    print("incorrect")
print(f"game over you got score of {score}")


#Write a program to create a list of students using inheritance. The parent class should be called Student and have the fields “name” and “age”.
#There should be 2 child classes. The first should be called “Domestic” and have the field “state”, while the second should be called “International” and have the field “country”.
#Allow the user to enter any number of students into the list, and then print a list of student names indicating for each one whether they are a domestic or international student, and which state or country they are from.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Domestic(Student):
    def __init__(self, name, age, state):
        super().__init__(name, age)
        self.state = state

class International(Student):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

students = []

while True:
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    student_type = input("Is the student Domestic or International? (d/i): ").lower()

    if student_type == 'd':
        state = input("Enter the state: ")
        students.append(Domestic(name, age, state))
    elif student_type == 'i':
        country = input("Enter the country: ")
        students.append(International(name, age, country))
    else:
        print("Invalid type. Please enter 'd' for Domestic or 'i' for International.")
        continue

    another = input("Add another student? (yes/no): ").lower()
    if another != 'yes':
        break

print("\nList of Students:")
for student in students:
    if isinstance(student, Domestic):
        print(f"{student.name}, Age: {student.age}, Domestic Student from {student.state}")
    elif isinstance(student, International):
        print(f"{student.name}, Age: {student.age}, International Student from {student.country}")


#Create a program with a class called Sport and the following instance (object) attributes:
#-	name
#-	number_players_team
#-	number_players_world
#Create 2 objects, one for “football” (11 players in a team) and one for “basketball” (5 players in a team) but leave the number of players worldwide as 0.
#Then ask the user to input the number of players worldwide for football, and then for basketball. Print out the sport names from their object, not as a literal string.
#Then print out the details for each sport (making sure you code __str__).
class Sport:
  def __init__(self, name, number_players_team, number_players_world=0):
    self.name=name
    self.number_players_team=number_players_team
    self.number_players_world=number_players_world

  def __str__(self):
    return (f"Sport: {self.name}\n"
                f"Number of Players per Team: {self.number_players_team}\n"
                f"Number of Players Worldwide: {self.number_players_world}")
football= Sport(name="Football", number_players_team=11)
basketball= Sport(name="Basketball", number_players_team=5)

football.number_players_world= int(input("input the football number_players_team: "))
basketball.number_players_world= int(input("input the basketball number_players_team: "))

print(f"sports names from objects: {football.name}, {basketball.name}")

print(football)
print()
print(basketball)


#Write a class Animal with a method speak() that prints "Animal sound". Create a subclass Dog that overrides the speak() method to print "Woof!".
#Instantiate both classes and call their speak() methods.
class Animal:
  def speak(self):
    print("Animal sound")
class Dog(Animal):
  def speak(self):
    print("Woof! ")
animal= Animal()
dog= Dog()
animal.speak()
dog.speak()

#Write a program to store information for a real estate company.
#The company does two things: sells houses and rent out apartments.
#Your program is to create three classes as shown below.
#You should begin your program by creating your classes and writing some test code to make sure that objects can be created correctly and printed.
#Once you are happy that your classes and objects work, you can delete your test code and start writing your main part of your program.
#Your program is to create an empty list that will be used to store the house and apartment data.
#Your program will loop through a menu and only exit the loop when the user selects to quit. Your menu should look as follows:
#Each menu option should have its own function that you can call.
#The functions you need to write are as follows:
#When creating your program, write one menu option at a time and make sure that it works correctly before moving on to the next menu item. You may need to add some test code to check that your menu item is working, but don’t forget to remove the test code once you are happy that it works.
#Use the __str__() function (called simply by printing the object) to print all houses and to print all apartments. To print all properties, simply print the address and suburb fields directly.
#Exception Handling: You must include exception handling in your program for the selection of the menu option. You must test for ValueError to make sure an integer is entered, and you must create a new exception called RangeError where an error will occur if the user enters a menu option outside the range of 1 to 6.
#Explanation of Terms: The houses have 2 prices. The list price is the price the house is advertised for. The minimum price is the lowest amount that the seller is willing to drop the price to before refusing the sale. The 2 figures for apartments are the amount to be charged as rent per week, and the lease length in months. For example, an apartment might have a weekly rent of $250 for a 6 month lease, so the 2 figures would be 250 and 6.
#REQUIREMENTS
#•	Your program must follow the instructions above.
#•	Your program must use exception handling to test that a valid menu option is entered.
#•	Your code must be based only on the materials covered in weeks 1 to 11 of the course.
#•	Your output must appear exactly like the following example (the text in bold indicates the user input).
#Sample Output:
#Menu:
#1) Add a new house
#2) Add a new apartment
#3) Print all properties
#4) Print all houses
#5) Print all apartments
#6) Quit
#Please select an option: new
#Error: You must enter a number
class Property:
  def __init__ (self, adress, suburb):
    self.address= address
    self.suburb= suburb
  def __str__(self):
    return {0}


class RangeError(Exception):
    """Custom exception for menu range errors."""
    pass

class Properties:         #creating class for properties   (super class)
    def __init__(self, address, suburb):
        self.address = address
        self.suburb = suburb

    def __str__(self):
        return f"{self.address} {self.suburb}"

class House(Properties):                    #creating class for houses (sub class)
    def __init__(self, address, suburb, list_price, min_price):
        super().__init__(address, suburb)
        self.list_price = list_price
        self.min_price = min_price

    def __str__(self):
        return f"{self.address} {self.suburb}"

class Apartment(Properties):                      #creating class for apartments(sub class)
    def __init__(self, address, suburb, rent_per_week, lease_length):
        super().__init__(address, suburb)
        self.rent_per_week = rent_per_week
        self.lease_length = lease_length

    def __str__(self):
        return f"{self.address} {self.suburb}"
# list to store all properties
properties = []

# function to add a new house
def add_house():
    address = input("Enter address: ")
    suburb = input("Enter suburb: ")
    list_price = int(input("Enter list price: "))
    min_price = int(input("Enter minimum price: "))
    properties.append(House(address, suburb, list_price, min_price))

# function to add a new apartment
def add_apartment():
    address = input("Enter address: ")
    suburb = input("Enter suburb: ")
    rent_per_week = int(input("Enter rent per week: "))
    lease_length = int(input("Enter lease length in months: "))
    properties.append(Apartment(address, suburb, rent_per_week, lease_length))
# function to print all properties
def print_all_properties():
    if not properties:
        print("No properties available.")
    else:
        print("Properties available:")
        for prop in properties:
            if isinstance(prop, House):
                print(f"{prop} (house)")
            elif isinstance(prop, Apartment):
                print(f"{prop} (apartment)")
# function to print all houses
def print_all_houses():
    houses = []
    for prop in properties:
        if isinstance(prop, House):
            houses.append(prop)

    if not houses:
        print("No houses available.")
    else:
        print("Houses available:")
        for house in houses:
            print(f"{house.suburb}: {house.address} ${house.list_price}")

# function to print all apartments
def print_all_apartments():
    apartments = []
    for prop in properties:
        if isinstance(prop, Apartment):
            apartments.append(prop)

    if not apartments:
        print("No apartments available.")
    else:
        print("Apartments available:")
        for apartment in apartments:
            print(f"{apartment.address} {apartment.suburb}. Rent: ${apartment.rent_per_week} p/w. Lease in months: {apartment.lease_length}")

# main program logic without using main_menu() function
while True:
    print("\nMenu:")
    print("1) Add a new house")
    print("2) Add a new apartment")
    print("3) Print all properties")
    print("4) Print all houses")
    print("5) Print all apartments")
    print("6) Quit")

    try:
        choice = int(input("Please select an option: "))
        if choice < 1 or choice > 6:
            raise RangeError

        if choice == 1:
            add_house()
        elif choice == 2:
            add_apartment()
        elif choice == 3:
            print_all_properties()
        elif choice == 4:
            print_all_houses()
        elif choice == 5:
            print_all_apartments()
        elif choice == 6:
            print("Goodbye.")
            break

    except ValueError:
        print("Error: You must enter a number")
    except RangeError:
        print("Error: You must selection an option between 1 and 6")





