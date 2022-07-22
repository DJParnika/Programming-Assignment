#1. Write a Python program to print &quot;Hello Python&quot;?
#2. Write a Python program to do arithmetical operations addition and division.?
#3. Write a Python program to find the area of a triangle?
#4. Write a Python program to swap two variables?
#5. Write a Python program to generate a random number?

import logging
import random

logging.basicConfig(filename="assignment1.log", level=logging.DEBUG)

class Assignment1 :

    def __init__(self):
        #1. print "Hello Python";
        logging.info("This is constructor and it says 'Hello Python'")

    def swap(self):
        #This function swap two variables
        try:
            logging.info("************ Inside Swap function **************")
            x = input("Enter first variable to swap= ")
            logging.info("First variable entered is : {}".format(x))
            y = input("Enter Second variable to swap = ")
            logging.info("Second variable entered is : {}".format(y))

            # swapping the values
            temp_var = x
            x = y
            y = temp_var

            logging.info('The value of x after swapping is :{}'.format(x))
            logging.info('The value of y after swapping is :{}'.format(y))

        except Exception as e:
            logging.exception("This is exception while swapping variables \n %s",e)

    def validate_input(self, num):
        #This function validate given input
        logging.info("*********** Validating given input number **********")
        try:
            while not num.isnumeric():
                num = input("Please enter valid number again : ")
            return int(num)
        except Exception as e:
            logging.exception("This is exception while validating input from user \n %s", e)

    def get_input_from_user(self):
        #This function is used to get input for arithmetical operation addition
         logging.info("************* Getting input from user *************")
         try:
             #get and check first number
             num1 = input("Enter first variable  = ")
             number1 = objAssignment1.validate_input(num1)
             logging.info("First variable entered is : {}".format(number1))

             # get and check second number
             num2 = input("Enter Second variable  = ")
             number2 = objAssignment1.validate_input(num2)
             logging.info("Second variable entered is : {}".format(number2))

             objAssignment1.addition(number1, number2)
             objAssignment1.division(number1, number2)

         except Exception as e:
             logging.exception("This is exception while getting input from user \n %s", e)

    def addition(self, number1, number2):
        # addition of given values
        logging.info("*************Inside addition function**************")
        try:
            ans = number1 + number2
            logging.info("The addition of given number {0} and {1}  is: {2}".format(number1, number2, ans))
        except Exception as e:
            logging.exception("This is exception while adding variables is \n %s ", e)

    def division(self, number1, number2):
        # division of given values
        logging.info("*************Inside division function**************")
        try:
            ans = number1 / number2
            logging.info("The division of given number {0} and {1}  is: {2}".format(number1, number2, ans))
        except Exception as e:
            logging.exception("This is exception while dividing variables is \n %s ", e)
        except ZeroDivisionError as err:
            logging.ERROR(err)

    def area_of_triangle(self):
        try:
            # get and check first number
            num1 = input("Enter base of triangle (b)  = ")
            base = objAssignment1.validate_input(num1)
            logging.info("Base of triangle entered is : {}".format(base))

            # get and check second number
            num2 = input("Enter height of triangle  = ")
            height = objAssignment1.validate_input(num2)
            logging.info("Second variable entered is : {}".format(height))

            #calculating area of triangle
            area = (base * height)/2
            logging.info("The area of triangle is : {}".format(area))

        except Exception as e:
            logging.exception("This is exception while adding variables is \n %s ", e)
        except ZeroDivisionError as err:
            logging.ERROR(err)

    def generate_random_num(self):
        #This funcion generates random number within given range
        try:
            num = random.randint(10, 100)
            logging.info("This is system generated random number : {}".format(num))
        except Exception as e:
            logging.exception("Random generated exception \n %s ",e)

objAssignment1 = Assignment1()
objAssignment1.swap()
objAssignment1.get_input_from_user()
objAssignment1.area_of_triangle()
objAssignment1.generate_random_num()




