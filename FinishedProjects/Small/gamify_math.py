from random import randint, choice

# A small terminal-based tool to practice some math
# namely, converting between C and F and
# converting binary to decimal

def convert_temperature(input_temperature: float, scale_name: str) -> tuple:
  '''
  Take a number and a scale and return the converted value in the other scale.
  Assuming the only scales used are Fahrenheit or Celsius.

  input_temperature - the given temperature value to be converted
  scale - the name of the temperature scale of the given value (expect Fahrenheit or Celsius)
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


def compare_values(correct_answer: str, user_answer: str, exact: bool=False, tolerance: float=0.10) -> str:
  '''
  Compare the correct answer and user answer and determine if they are the same.

  correct_answer - supplied from a function
  user_answer - supplied from user input
  exact - require answers to match exactly, default behavior is to accept answers within 5%
  '''
  if exact and (correct_answer == user_answer):
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
  while True:

    # (re)initialize
    user_temperature = user_binary = user_hex = ""

    # temperature conversion mode
    if "t" in mode: 
      number_to_convert = randint(-100, 451) # Bounds of interesting conversions (bounds from Fahrenheit scale)
      scale_to_convert = choice([" F", " C"])       # randomly choose either Fahrenheit or Celsius scale
      correct_value, scale_name = convert_temperature(number_to_convert, scale_to_convert)
      user_value = input(f"Convert {number_to_convert}{scale_to_convert} : ")

    # binary mode
    if "b" in mode:
      number_to_convert = randint(0, 65) # don't care about working on negative numbers for now
      correct_value = bin(number_to_convert)
      user_value = input(f"Convert 0d{number_to_convert} : ")

    # hex mode
    if "h" in mode:
      number_to_convert = randint(0, 65)
      correct_value = hex(number_to_convert)
      user_value = input(f"Convert 0d{number_to_convert} : ")

    # quit if user says to
    if "q" in user_value: break

    # otherwise, check answer
    if ("b" in mode or "h" in mode):
      correct = compare_values(str(correct_value), user_value, exact=True)
    else:
      correct = compare_values(str(correct_value), user_value)

    if correct: correct_tally += 1
    else: incorrect_tally += 1

  # something to give a score at the end
  print("#"*20)
  print("Here are your stats!")
  print(f"Correct: {correct_tally}")
  print(f"Incorrect: {incorrect_tally}")
  print(f"Percentage: {correct_tally*100/(correct_tally+incorrect_tally)}%")
  print("#"*20)






