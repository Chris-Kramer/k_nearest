import geometry2D
import geometry3D


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
    print('Bye')
  else:
    print('Option \'' + option + '\' not recognised, please enter a number that corresponds to one of the options displayed.')
    menu_main()    

def menu_2d():
  option = input('''Select one of the following:
  1) Compute the area of a circle
  2) Compute the area of a square
  9) Back to the main menu.
Enter your choice: ''')
  if option == '1':
    r = float(input('Enter a value for the radius: '))
    print(geometry2D.circle_area(r))
    menu_2d()
  elif option == '2':
    s = float(input('Enter a value for the side: '))
    print(geometry2D.square_area(s))
    menu_2d()
  elif option == '9':
    menu_main()
  else:
    print('Unrecognised option, please enter a number for one of the options diplayed.')
    menu_2d()

def menu_3d():
  option = input('''Select one of the following:
  1) Compute the volume of a cilinder
  2) Compute the volume of a square prism
  9) Back to the main menu.
Enter your choice: ''')
  if option == '1':
    r = float(input('Enter a value for the radius: '))
    h = float(input('Enter a value for the height: '))
    print(geometry3D.cilinder_volume(r,h))
    menu_3d()
  elif option == '2':
    s = float(input('Enter a value for the side: '))
    h = float(input('Enter a value for the height: '))
    print(geometry3D.square_prism_volume(s,h))
    menu_3d()
  elif option == '9':
    menu_main()
  else:
    print('Unrecognised option, please enter a number for one of the options diplayed.')
    menu_3d()
    
menu_main()
