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


def compare_values(correct_answer: str, user_answer: str, exact: bool=False) -> str:
  '''
  Compare the correct answer and user answer and determine if they are the same.

  correct_answer - supplied from a function
  user_answer - supplied from user input
  exact - require answers to match exactly, default behavior is to accept answers within 5%
  '''
  if exact and (correct_answer == user_answer):
    print(f"{user_answer} is correct!")
    return True

  elif not exact and (abs(correct_answer - user_answer)/100. <= 0.03):
    print(f"{user_answer} is correct! Exact Answer: {correct_answer}")
    return True

  else:
    print(f"{user_answer} is not correct! Correct Answer: {correct_answer}")
    return False


if __name__ == "__main__":
  test_temp, test_name = convert_temperature(50, "f")
  print(test_temp, test_name)

  compare_values(test_temp, 10.0, exact=True)







