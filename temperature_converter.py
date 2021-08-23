# Problem 1
# Max Zinski

def main():
    initial_prompt = (f"Enter a temperature in fahrenheit: ")
    user_input = input(initial_prompt)

    converted_number = validate_and_convert_to_float(user_input)
    while(not converted_number):
        recurring_prompt = "Please enter the temperature in farhenheit:"
        user_input = input(recurring_prompt)
        converted_number = validate_and_convert_to_float(user_input)

    c_temp = convert_fahr_to_cels(converted_number)
    print(f"The temperature is {round(c_temp, 2)} in Celsius.")

"""
an input is valid if it is a number greater than absolute zero (-456.7 degress Fahrenheit). 
https://en.wikipedia.org/wiki/Absolute_zero
# if it's valid, return the number as a float
# if not, return False
"""
def validate_and_convert_to_float(user_input):
    if isinstance(user_input, str) and len(user_input) == 0:
        return False
    try:
        temp_fahrenheit = float(user_input)
        assert temp_fahrenheit >= -456.7
    except:
        print("The temperature you entered is not a valid number. A valid temperature in Fahreneheit is a number greater than -456.7.")
        return False
    else:
        return temp_fahrenheit

# https://www.almanac.com/content/temperature-conversion c = (f - 32) * 5/9
# either returns a float or return False (not a valid type)
def convert_fahr_to_cels(fahr_temp):
    converted_number = validate_and_convert_to_float(fahr_temp)

    # number was not valid, return False. Second expression is necessary because 0.0 == False evaluates to True in Python
    if converted_number == False and type(converted_number) == bool:
        return False
        
    return (converted_number - 32) * 5/9

if __name__ == "__main__":
    main()