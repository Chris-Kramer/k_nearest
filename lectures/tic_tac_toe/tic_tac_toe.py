from grid import *

def play_round():
  grid = empty_grid()
  print_grid(grid)
  playing = True
  while playing:
    player = next_player(grid)
    pos = input_position(f"Enter a position {player}: ")
    while not is_empty(grid,pos):
      print("Please, select an empty position in the grid.")
      print_grid(grid)
      pos = input_position(f"Enter a position {player}: ")
    assert is_empty(grid,pos)
    mark_position(grid,pos)
    print_grid(grid)
    if wins_grid(grid,pos):
      print(f"{player} won.")
      playing = False
    elif played_turns(grid) == 9:
      print("draw.")
      playing = False

def input_yes_no(message):
    ans = input(message + ' (yes/no) ')
    if ans == 'y' or ans == 'yes':
      return True
    elif ans == 'n' or ans == 'no':
      return False
    else:
      print("Invalid input. Please enter 'yes', 'y', 'no', or 'n'.") 
      return input_yes_no(message)

if __name__ == '__main__':
  playing = True
  while playing:
    play_round()
    playing = input_yes_no('Would you like to play again?')
