from counter import Counter

c = Counter()

def menu():
  option = input('''Select an action:
  1) Display the current value of the counter.
  2) Increment the counter.
  3) Reset the counter.
  9) Quit.
Enter your choice: ''')
  if option == '1':
    print('The current value of the counter is ' + str(c.get_value()) + '.')
    menu()
  elif option == '2':
    c.increment()
    print('Counter incremented.')
    menu()
  elif option == '3':
    c.reset()
    print('Counter reset.')
    menu()
  elif option == '9':
    print('Bye.')
  else:
    print('Action \'' + option + '\' not recognised, please enter a number corresponding to one of the actions displayed.')
    menu()

print('This program...counts 😅')
menu()
