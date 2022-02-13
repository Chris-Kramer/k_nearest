"""
Offers functions for creating and maintaining a grid for playing tic-tac-toe.
"""

_empty = ' '

_players = ['O','X']

def empty_grid():
  """
  Returns an empty grid.
  """
  return [ [ _empty for col in range(3) ] for row in range(3) ]  

def is_empty(grid,pos):
  """
  Returns True if the specified position of the given grid is empty, False
  otherwise.
  """
  return grid[_to_row(pos)][_to_col(pos)] == _empty

def _count(grid,e):
  # accumulator = 0
  # for row in grid:
  #   for x in row:
  #     if x == e:
  #       accumulator += 1
  # return accumulator
  return sum( row.count(e) for row in grid)

def remaining_turns(grid):
  """
  Returns the number of turns that can be played on the given grid (i.e., the
  number of empty positions).
  """
  # accumulator = 0
  # for row in grid:
  #   for x in row:
  #     if x == _empty:
  #       accumulator += 1
  # return accumulator
  return _count(grid,_empty)

def played_turns(grid):
  """
  Returns the number of turns that have been played on the given grid (i.e., the
  number of positions marked with O or X).
  """
  # return 9 - remaining_turns(grid)
  # -- or --
  # accumulator = 0
  # for row in grid:
  #   for x in row:
  #     if x in _players:
  #       accumulator += 1
  # return accumulator
  # -- or --
  return _count(grid,_players[0]) + _count(grid,_players[1])

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

def _to_row(pos):
  """
  Converts a position (in the format exposed by the module) to the internal
  representation (row by column) returning the corresponding row.
  """
  return (pos - 1) // 3

def _to_col(pos):
  """
  Converts a position (in the format exposed by the module) to the internal
  representation (row by column) returning the corresponding column.
  """
  return (pos - 1) % 3

def is_position(pos):
  """
  Returns True if the argument is a position, False otherwise.
  """
  return 1 <= pos <= 9
  
def is_grid(grid):
  """
  Returns True if the argument is a grid, False otherwise.
  """
  return 3 == len(grid) == len(grid[0]) == len(grid[1]) == len(grid[2]) and \
         9 == remaining_turns(grid) + played_turns(grid) and \
         0 <= _count(grid,_players[0]) - grid.count(grid,_players[1]) <= 1

def mark_position(grid,pos):
  """
  The current player marks the given position on the grid.

  Assumption: pos points to an empty spot on the grid.
  """
  grid[_to_row(pos)][_to_col(pos)] = next_player(grid)

def wins_grid(grid,pos):
  """
  Checks whether the current player wins after marking the given position.
  """
  return _wins_row(grid,pos) or \
         _wins_col(grid,pos) or \
         _wins_diag(grid,pos) or \
         _wins_anti_diag(grid,pos)

def _wins_row(grid,pos):
  row = _to_row(pos)
  return grid[row][0] == grid[row][1] == grid[row][2]
# row = grid[_to_row(pos)]
# return row[0] == row[1] == row[2]

def _wins_col(grid,pos):
  col = _to_col(pos)
  return grid[0][col] == grid[1][col] == grid[2][col]

def _wins_diag(grid,pos):
  row = _to_row(pos)
  col = _to_col(pos)
  return row == col and grid[0][0] == grid[1][1] == grid[2][2]

def _wins_anti_diag(grid,pos):
  row = _to_row(pos)
  col = _to_col(pos)
  return row + col == 2 and grid[0][2] == grid[1][1] == grid[2][0]

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
  print(' │' + '│'.join(grid[0]) + '│')
  print(line)
  print(' │' + '│'.join(grid[1]) + '│')
  print(line)
  print(' │' + '│'.join(grid[2]) + '│')
  print(' └─┴─┴─┘ ')
