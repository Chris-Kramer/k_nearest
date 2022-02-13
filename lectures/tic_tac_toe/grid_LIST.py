"""
Offers functions for creating and maintaining a grid for playing tic-tac-toe.
"""

_empty = ' '

_players = ['O','X']

def empty_grid():
  """
  Returns an empty grid.
  """
  return [ _empty ] * 9
  

def is_empty(grid,pos):
  """
  Returns True if the specified position of the given grid is empty, False
  otherwise.
  """
  return grid[pos - 1] == _empty

def remaining_turns(grid):
  """
  Returns the number of turns that can be played on the given grid (i.e., the
  number of empty positions).
  """
  return grid.count(_empty)  

def played_turns(grid):
  """
  Returns the number of turns that have been played on the given grid (i.e., the
  number of positions marked with O or X).
  """
  # return 9 - remaining_turns(grid)
  # -- or --
  # accumulator = 0
  # for x in grid:
  #   if x in _players:
  #     accumulator += 1
  # return accumulator
  # -- or --
  return grid.count(_players[0]) + grid.count(_players[1])

def next_player(grid):
  """
  Return the marking (O or X) of the player that must play next on the given grid.
  """
  return turn_player(played_turns(grid))  

def turn_player(turn):
  """
  Return the marking (O or X) of the player that must play during the given turn.
  """
  return _players[ turn % 2 ]

def is_position(pos):
  """
  Returns True if the argument is a position, False otherwise.
  """
  return 1 <= pos <= 9
  
def is_grid(grid):
  """
  Returns True if the argument is a grid, False otherwise.
  """
  return 9 == len(grid) and \
         9 == remaining_turns(grid) + played_turns(grid) and \
         0 <= grid.count(_players[0]) - grid.count(_players[1]) <= 1

def mark_position(grid,pos):
  """
  The current player marks the given position on the grid.

  Assumption: pos points to an empty spot on the grid.
  """
  grid[pos - 1] = next_player(grid)

def wins_grid(grid,pos):
  """
  Checks whether the current player wins after marking the given position.
  """
  return _wins_row(grid,pos) or \
         _wins_col(grid,pos) or \
         _wins_diag(grid,pos) or \
         _wins_anti_diag(grid,pos)

def _to_row(pos):
  return (pos - 1) // 3

def _to_col(pos):
  return (pos - 1) % 3

def _wins_row(grid,pos):
  row = _to_row(pos)
  return grid[row * 3] == grid[row * 3 + 1] == grid[row * 3 + 2]

def _wins_col(grid,pos):
  col = _to_col(pos)
  return grid[col] == grid[3 + col] == grid[6 + col]

def _wins_diag(grid,pos):
  row = _to_row(pos)
  col = _to_col(pos)
  return row == col and grid[0] == grid[4] == grid[8]

def _wins_anti_diag(grid,pos):
  row = _to_row(pos)
  col = _to_col(pos)
  return row + col == 2 and grid[2] == grid[4] == grid[6]

def check_position(pos):
  """
  Checks if the argument is a position and raises a ValueError otherwise.
  """
  if not is_position(pos):
    raise ValueError(f"invalid position: '{pos}'")

def input_position(message):
  """
  Reads a position from the standard input displaying the given message.
  If the input is not a valid position, the user is prompt to try again.
  """
  pos = input(message)
  try:
    pos = int(pos)
    check_position(pos)
    return pos
  except ValueError:
    print('Invalid input: expected a position.')
    print_positions()
    return input_position(message)

def print_positions():
  """
  Prints a help message showing how each position in the grid is identified.
  """
  print(' ┌─┬─┬─┐ ')
  line = ' ├─┼─┼─┤ '
  print(' │1│2│3│ ')
  print(line)
  print(' │4│5│6│ ')
  print(line)
  print(' │7│8│9│ ')
  print(' └─┴─┴─┘ ')

def print_grid(grid):
  """
  Prints the given grid.
  """
  print(' ┌─┬─┬─┐ ')
  line = ' ├─┼─┼─┤ '
  print(' │' + '│'.join(grid[0:3]) + '│')
  print(line)
  print(' │' + '│'.join(grid[3:6]) + '│')
  print(line)
  print(' │' + '│'.join(grid[6:9]) + '│')
  print(' └─┴─┴─┘ ')
