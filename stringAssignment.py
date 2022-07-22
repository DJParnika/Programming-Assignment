# This class handles string related tasks as given below -
# 1. Extraction of data in given string
# 2. Reverse the given string
# 3. Convert the given string to upper case and split it
# 4. Convert the given string to lower case
# 5. Capitalise the in given string
# 6. Expand the in given string


import logging

logging.basicConfig(filename="stringHandling.log", level=logging.DEBUG)


class StringHandling:

    def __init__(self, inputString):
        self.inputString = inputString
        logging.info("This is constructor to accept given input string")
        print(inputString)

    def extract_with_given_range(self):
        # Try to extract data from index one to index 300 with a jump of 3
        try:
            logging.info("The given input string is - %s", inputString)
            extracted_string = inputString[1:300:3]
            logging.info("The extracted string from index 1 to 300 with jump of 3 is = %s", extracted_string)
        except Exception as e:
            logging.exception("Exception while handling extraction of given string is = \n %s", str(e))

    def reverse_string(self):
        # This function revesrses the given string
        try:
            logging.info("The given input string is - %s ", inputString)
            reverse_string = inputString[::-1]
            logging.info("The reverse string is : \n %s", reverse_string)
        except Exception as e:
            logging.exception("Exception while handling extraction of given string is = %s", str(e))

    def set_upper_split(self):
        # Convert the given string to upper case and split it
        try:
            logging.info("The given input string is - %s ", inputString)
            upperSplit = inputString.upper().split(' ')
            logging.info("The string after set to upper and split : \n %s", upperSplit)
        except Exception as e:
            logging.exception("Exception while handling upper and split function of given string is = %s", str(e))

    def set_lower(self):
        # Convert the given string to lower case
        try:
            logging.info("The given input string is - %s ", inputString)
            lowerString = inputString.lower()
            logging.info("The string after converting to lower case : \n %s", lowerString)
        except Exception as e:
            logging.exception("Exception while handling upper and split function of given string is = %s", str(e))

    def capitalise_string(self):
        # Capitalise the given string
        try:
            logging.info("The given input string is - %s ", inputString)
            capitaliseString = inputString.capitalize()
            logging.info("The string after capitalising given string: \n %s", capitaliseString)
        except Exception as e:
            logging.exception("Exception while handling capitalising given string is = %s", str(e))

    def expand_string(self):
        # expand the given string with tab spaces
        try:
            logging.info("The given input string is - %s ", inputString)
            expandString = inputString.expandtabs()
            logging.info("The string after expanding the given string: \n %s", expandString)
            print(expandString)
        except Exception as e:
            logging.exception("Exception while expanding the given string is = %s", str(e))


inputString = "This is string handling and 1" \
              "this is My First Python programming class and i am learNING python string and its function"

objStrHandling = StringHandling(inputString)
objStrHandling.extract_with_given_range()
objStrHandling.reverse_string()
objStrHandling.set_upper_split()
objStrHandling.set_lower()
objStrHandling.capitalise_string()
objStrHandling.expand_string()
