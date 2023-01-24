import numpy as np
import matplotlib.pyplot as plt
from sys import exit

matrix_A = np.matrix('1 1 1 1 1; 1 0 0 0 1; 1 1 1 1 1; 1 0 0 0 1; 1 0 0 0 1')
matrix_B = np.matrix('1 1 1 1 0; 1 0 0 0 1; 1 1 1 1 0; 1 0 0 0 1; 1 1 1 1 0')
matrix_C = np.matrix('1 1 1 1 1; 1 0 0 0 0; 1 0 0 0 0; 1 0 0 0 0; 1 1 1 1 1')
matrix_D = np.matrix('1 1 1 1 0; 1 0 0 0 1; 1 0 0 0 1; 1 0 0 0 1; 1 1 1 1 0')
matrix_E = np.matrix('1 1 1 1 1; 1 0 0 0 0; 1 1 1 1 0; 1 0 0 0 0; 1 1 1 1 1')
matrix_F = np.matrix('1 1 1 1 1; 1 0 0 0 0; 1 1 1 0 0; 1 0 0 0 0; 1 0 0 0 0')
matrix_G = np.matrix('1 1 1 1 1; 1 0 0 0 0; 1 0 0 1 1; 1 0 0 0 1; 1 1 1 1 1')
matrix_H = np.matrix('1 0 0 0 1; 1 0 0 0 1; 1 1 1 1 1; 1 0 0 0 1; 1 0 0 0 1')
matrix_I = np.matrix('1 1 1 1 1; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 1 1 1 1 1')
matrix_J = np.matrix('1 1 1 1 1; 0 0 1 0 0; 0 0 1 0 0; 1 0 1 0 0; 1 1 1 0 0')
matrix_K = np.matrix('1 0 0 1 1; 1 0 1 0 0; 1 1 0 0 0; 1 0 1 0 0; 1 0 0 1 1')
matrix_L = np.matrix('1 0 0 0 0; 1 0 0 0 0; 1 0 0 0 0; 1 0 0 0 0; 1 1 1 1 1')
matrix_M = np.matrix('1 0 0 0 1; 1 1 0 1 1; 1 0 1 0 1; 1 0 0 0 1; 1 0 0 0 1')
matrix_N = np.matrix('1 0 0 0 1; 1 1 0 0 1; 1 0 1 0 1; 1 0 0 1 1; 1 0 0 0 1')
matrix_O = np.matrix('1 1 1 1 1; 1 0 0 0 1; 1 0 0 0 1; 1 0 0 0 1; 1 1 1 1 1')
matrix_P = np.matrix('1 1 1 1 0; 1 0 0 0 1; 1 1 1 1 0; 1 0 0 0 0; 1 0 0 0 0')
matrix_Q = np.matrix('1 1 1 1 1; 1 0 0 0 1; 1 0 1 0 1; 1 0 0 1 1; 1 1 1 1 1')
matrix_R = np.matrix('1 1 1 1 1; 1 0 0 0 1; 1 1 1 1 1; 1 1 1 0 0; 1 0 0 1 1')
matrix_S = np.matrix('0 1 1 1 1; 1 0 0 0 0; 0 1 1 1 0; 0 0 0 0 1; 1 1 1 1 0')
matrix_T = np.matrix('1 1 1 1 1; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0')
matrix_U = np.matrix('1 0 0 0 1; 1 0 0 0 1; 1 0 0 0 1; 1 0 0 0 1; 0 1 1 1 0')
matrix_V = np.matrix('1 0 0 0 1; 1 0 0 0 1; 0 1 0 1 0; 0 1 0 1 0; 0 0 1 0 0')
matrix_W = np.matrix('1 0 0 0 1; 1 0 0 0 1; 1 0 1 0 1; 1 1 0 1 1; 1 0 0 0 1')
matrix_X = np.matrix('1 0 0 0 1; 0 1 0 1 0; 0 0 1 0 0; 0 1 0 1 0; 1 0 0 0 1')
matrix_Y = np.matrix('1 0 0 0 1; 0 1 0 1 0; 0 0 1 0 0; 0 0 1 0 0; 0 0 1 0 0')
matrix_Z = np.matrix('1 1 1 1 1; 0 0 0 1 0; 0 0 1 0 0; 0 1 0 0 0; 1 1 1 1 1')


matrix_alphabet = {"A" : matrix_A, "B" : matrix_B, "C" : matrix_C, "D" : matrix_D, 
                   "E" : matrix_E, "F" : matrix_F, "G" : matrix_G, "H" : matrix_H, 
                   "I" : matrix_I, "J" : matrix_J, "K" : matrix_K, "L" : matrix_L,
                   "M" : matrix_M, "N" : matrix_N, "O" : matrix_O, "P" : matrix_P, 
                   "Q" : matrix_Q, "R" : matrix_R, "S" : matrix_S, "T" : matrix_T, 
                   "U" : matrix_U, "V" : matrix_V, "W" : matrix_W, "X" : matrix_X,
                   "Y" : matrix_Y, "Z" : matrix_Z}


KEYSTRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def add_border(matrix):
  border_row = np.matrix('0 0 0 0 0')
  border_col = np.matrix('0;0;0;0;0;0;0')

  matrix = np.vstack((matrix, border_row))
  matrix = np.vstack((border_row, matrix))
  matrix = np.hstack((matrix, border_col))
  matrix = np.hstack((border_col, matrix))

  return matrix


def add_border_to_alphabet():
  for entry, letter in enumerate(KEYSTRING):
    matrix_alphabet[letter] = add_border(matrix_alphabet[letter])


# take every letter and multiply it by itself
def square_alphabet():
  for entry, letter in enumerate(KEYSTRING):
    matrix_alphabet[letter] = matrix_alphabet[letter]*matrix_alphabet[letter]


def turn_off_axes(axis_object):
  axis_object.get_xaxis().set_visible(False)
  axis_object.get_yaxis().set_visible(False)


def print_five_letters(letters):
  fig = plt.figure()
  ax1 = fig.add_subplot(151)
  ax2 = fig.add_subplot(152)
  ax3 = fig.add_subplot(153)
  ax4 = fig.add_subplot(154)
  ax5 = fig.add_subplot(155)
  list_of_axes = [ax1, ax2, ax3, ax4, ax5]

  for entry, ax in enumerate(list_of_axes):
    turn_off_axes(ax)
    ax.imshow(matrix_alphabet[letters[entry]])

  plt.show()


def print_all_letters(letters):

  fig = plt.figure()
  ax0 = plt.subplot2grid((3, 9), (0, 0))
  ax1 = plt.subplot2grid((3, 9), (0, 1))
  ax2 = plt.subplot2grid((3, 9), (0, 2))
  ax3 = plt.subplot2grid((3, 9), (0, 3))
  ax4 = plt.subplot2grid((3, 9), (0, 4))
  ax5 = plt.subplot2grid((3, 9), (0, 5))
  ax6 = plt.subplot2grid((3, 9), (0, 6))
  ax7 = plt.subplot2grid((3, 9), (0, 7))
  ax8 = plt.subplot2grid((3, 9), (0, 8))

  ax9 = plt.subplot2grid((3, 9), (1, 0))
  ax10 = plt.subplot2grid((3, 9), (1, 1))
  ax11 = plt.subplot2grid((3, 9), (1, 2))
  ax12 = plt.subplot2grid((3, 9), (1, 3))
  ax13 = plt.subplot2grid((3, 9), (1, 4))
  ax14 = plt.subplot2grid((3, 9), (1, 5))
  ax15 = plt.subplot2grid((3, 9), (1, 6))
  ax16 = plt.subplot2grid((3, 9), (1, 7))
  ax17 = plt.subplot2grid((3, 9), (1, 8))

  ax18 = plt.subplot2grid((3, 9), (2, 0))
  ax19 = plt.subplot2grid((3, 9), (2, 1))
  ax20 = plt.subplot2grid((3, 9), (2, 2))
  ax21 = plt.subplot2grid((3, 9), (2, 3))
  ax22 = plt.subplot2grid((3, 9), (2, 4))
  ax23 = plt.subplot2grid((3, 9), (2, 5))
  ax24 = plt.subplot2grid((3, 9), (2, 6))
  ax25 = plt.subplot2grid((3, 9), (2, 7))

  list_of_axes = [ax0,  ax1,  ax2,  ax3,  ax4,  ax5,  ax6,  ax7,  ax8,  ax9,
                  ax10, ax11, ax12, ax13, ax14, ax15, ax16, ax17, ax18, ax19,
                  ax20, ax21, ax22, ax23, ax24, ax25]

  for entry, ax in enumerate(list_of_axes):
    turn_off_axes(ax)
    ax.imshow(matrix_alphabet[letters[entry]])

  plt.show()


def matrix_operation(matrix_1, matrix_2, operation, print_output=False):

  if (operation == "+"):
    matrix_output = matrix_1 + matrix_2

  elif (operation == "-"):
    matrix_output = matrix_1 - matrix_2

  elif (operation == "*"):
    matrix_output = matrix_1 * matrix_2

  elif (operation == "|"):
    matrix_output = matrix_1 | matrix_2

  elif (operation == "&"):
    matrix_output = matrix_1 & matrix_2

  else:
    print(f"operation \"{operation}\" not understood or permitted. Exiting...")
    exit()

  if (print_output):
    fig = plt.figure()
    ax_1 = plt.subplot2grid((1, 3), (0, 0))
    ax_2 = plt.subplot2grid((1, 3), (0, 1))
    ax_output = plt.subplot2grid((1, 3), (0, 2))
  
    ax_1.imshow(matrix_1)
    ax_2.imshow(matrix_2)
    ax_output.imshow(matrix_output)
  
    plt.show()

  return matrix_output

def print_matrix(matrix):
  plt.imshow(matrix)
  plt.show()


def print_alphabet_operation(user_operation = ""):
  operation = user_operation
  output_matrix = matrix_operation(matrix_alphabet["A"], matrix_alphabet["B"], operation)
  for entry, letter in enumerate(KEYSTRING):
    if (letter in "AB"):
      pass
    else:
      output_matrix = matrix_operation(output_matrix, matrix_alphabet[letter], operation)
  
  print_matrix(output_matrix)
  

if __name__ == "__main__":

  # always add a border for aesthetic purposes
  add_border_to_alphabet()

  # see entire alphabet before and after an operation
  #print_all_letters(list(KEYSTRING))
  #square_alphabet()
  #print_all_letters(list(KEYSTRING))

  #new_matrix = matrix_operation(matrix_alphabet["A"], matrix_alphabet["B"], "|")
  #newer_matrix = matrix_operation(new_matrix, matrix_alphabet["T"], "|")

  print_alphabet_operation()





