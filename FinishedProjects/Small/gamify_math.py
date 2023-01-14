from random import randint, choice

# A small terminal-based tool to practice some math
# namely, converting between C and F and
# converting hex and binary to decimal, and vice versa

def convert_temperature(input_temperature: float, scale_name: str) -> tuple:
  '''
  Take a number and a scale and return the converted value in the other scale.
  Assuming the only scales used are Fahrenheit or Celsius.

  input_temperature - the given temperature value to be converted
  scale_name - the name of the temperature scale of the given value (expect Fahrenheit or Celsius)

  Output - tuple:
  output_temperature - the converted temperature value
  scale_name - the name of the temperature scale of the output_temperature value
  ''' 
  scale_name = scale_name.lower()
  if ("c" in scale_name):
    output_temperature = (input_temperature * 9.0 / 5.0) + 32.0
    scale_name = "Fahrenheit"

  elif ("f" in scale_name):
    output_temperature = (input_temperature - 32.0) * 5.0 / 9.0
    scale_name = "Celsius"

  else:
    output_temperature = -999
    scale_name = "Invalid temperature scale"
    print("Specify either 'Fahrenheit' or 'Celsius' as your temperature scale")
  
  return (output_temperature, scale_name)


def convert_number_hex_bin_dec(input_number: int, conversion: str) -> tuple:
  '''
  Define and answer the conversion for the user to compare their answer to.

  Example: input_number = 255, conversion = "xd",
    tell the user "convert 0xff to decimal?"
           input_number = 4, conversion = "db",
    ask the user "what is 0d4 in binary?"

  input_number - integer value that will either be converted to bin/hex or passed through the function
  conversion - string characters "dx", "xd", "db", "bd", indicating the type of conversion
                       "dx" - convert decimal to hex
                       "bd" - convert binary to decimal
                       etc.
  Output - tuple:
  value_to_convert - a string the user is asked to convert
  converted_value - a string of the correct converted value
  converted_base - a string indicating the base of the converted_value
  '''
  input_as_hex = hex(input_number) #type: str
  input_as_bin = bin(input_number) #type: str
  input_as_dec = "0d" + str(input_number) 

  if conversion == "dx":
    value_to_convert = input_as_dec
    converted_value =  input_as_hex
    converted_base = "hexadecimal"

  elif conversion == "db":
    value_to_convert = input_as_dec
    converted_value =  input_as_bin
    converted_base = "binary"

  elif conversion == "xd":
    value_to_convert = input_as_hex
    converted_value =  input_as_dec
    converted_base = "decimal"

  elif conversion == "bd":
    value_to_convert = input_as_bin
    converted_value  = input_as_dec
    converted_base = "decimal"

  return (value_to_convert, converted_value, converted_base)


def compare_values(correct_answer: str, user_answer: str, exact: bool=False, tolerance: float=0.10) -> str:
  '''
  Compare the correct answer and user answer and determine if they are the same.

  correct_answer - supplied from a function
  user_answer - supplied from user input
  exact - require answers to match exactly, default behavior is to accept answers within 5%
  '''
  if exact and ((user_answer == correct_answer) or (user_answer == correct_answer[2:])):
    print(f"{user_answer} is correct!")
    return True

  elif not exact and (abs(float(correct_answer) - float(user_answer))/100. <= tolerance):
    print(f"{user_answer} is correct! Exact Answer: {correct_answer}")
    return True

  else:
    print(f"{user_answer} is not correct! Correct Answer: {correct_answer}")
    return False


if __name__ == "__main__":

  print("Bienvenue! Let's do some practice math... Input 'q' at any time to quit")
  mode = input("Please specify 'binary', 'hex', or 'temperature' mode: ")

  correct_tally = 0
  incorrect_tally = 0
  available_mode = "b" in mode or "h" in mode or "t" in mode
  if not available_mode:
    print("Please restart the program and select a valid mode.")
  while True:

    # (re)initialize
    user_temperature = user_binary = user_hex = ""

    # temperature conversion mode
    if "t" in mode: 
      exact_flag = False
      number_to_convert = randint(-100, 451) # Bounds of interesting conversions (bounds from Fahrenheit scale)
      scale_to_convert = choice(["F", "C"])       # randomly choose either Fahrenheit or Celsius scale
      correct_value, scale_name = convert_temperature(number_to_convert, scale_to_convert)
      user_value = input(f"Convert {number_to_convert} {scale_to_convert} : ")

    # hex and binary conversion modes
    if ("b" in mode or "h" in mode):
      exact_flag = True
      number_to_convert = randint(0, 256) # don't care about working on negative numbers for now
      if "h" in mode:
        conversion = choice(["dx", "xd"])
      if "b" in mode:
        conversion = choice(["db", "bd"])
      value_to_convert, correct_value, converted_base = convert_number_hex_bin_dec(number_to_convert, conversion)
      user_value = input(f"Convert {value_to_convert} to {converted_base} : ")
      print(user_value[2:])

    if "q" in user_value: break
    correct = compare_values(str(correct_value), user_value, exact_flag)

    if correct: correct_tally += 1
    else: incorrect_tally += 1

  # give a score at the end
  if available_mode:
    print("#"*20)
    print("Here are your stats!")
    print(f"Correct: {correct_tally}")
    print(f"Incorrect: {incorrect_tally}")
    if ((correct_tally + incorrect_tally) > 0):
     print(f"Percentage: {correct_tally*100/(correct_tally+incorrect_tally)}%")
    print("#"*20)






