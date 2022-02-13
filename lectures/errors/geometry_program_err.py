import geometry2D
import geometry3D
import sys

def input_positive_float(message):
  x = input(message)
  try:
    x = float(x)
    if x > 0:
      return x
    else:
      print('Please enter a positive number, you entered ' + x + '.')
      return input_positive_float(message)
  except ValueError:
    print('Please enter a positive number, you entered ' + x + '.')
    return input_positive_float(message)

def menu_main():
  option = input('''Select one of the following:
  1) 2D geometry
  2) 3D geometry
  9) Quit.
Enter your choice: ''')
  if option == '1':
    menu_2d()
  elif option == '2':
    menu_3d()
  elif option == '9':
    sys.exit()
  else:
    print('Option \'' + option + '\' not recognised, please enter a number that corresponds to one of the options displayed.')
    menu_main()    

def menu_2d():
  option = input('''Select one of the following:
  1) Compute the area of a circle.
  2) Compute the area of a square.
  8) Go back to the main menu.
  9) Quit.
Enter your choice: ''')
  if option == '1':
    r = input_positive_float('Enter a value for the radius: ')
    print('area =',geometry2D.circle_area(r))
    menu_2d()
  elif option == '2':
    s = input_positive_float('Enter a value for the side: ')
    print('area =',geometry2D.square_area(s))
    menu_2d()
  elif option == '8':
    menu_main()
  elif option == '9':
    sys.exit()
  else:
    print('Unrecognised option, please enter a number for one of the options diplayed.')
    menu_2d()

def menu_3d():
  option = input('''Select one of the following:
  1) Compute the volume of a cilinder.
  2) Compute the volume of a square prism.
  8) Go back to the main menu.
  9) Quit.
Enter your choice: ''')
  if option == '1':
    r = input_positive_float('Enter a value for the radius: ')
    h = input_positive_float('Enter a value for the height: ')
    print('volume =',geometry3D.cilinder_volume(r,h))
    menu_3d()
  elif option == '2':
    s = input_positive_float('Enter a value for the side: ')
    h = input_positive_float('Enter a value for the height: ')
    print('volume =',geometry3D.square_prism_volume(s,h))
    menu_3d()
  elif option == '8':
    menu_main()
  elif option == '9':
    sys.exit()
  else:
    print('Unrecognised option, please enter a number for one of the options diplayed.')
    menu_3d()
    
if __name__ == '__main__':
   menu_main()