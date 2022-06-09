def successors(stable):
  # find empty spot
  empty = stable.index('E');
  print('Empty:', empty)
  # generate list of unfiltered candidates
  candidates = [empty-2, empty-1, empty+1, empty+2]
  print('First:', candidates)
  # Keep only those who are inside the stable
  candidates = [c for c in candidates if c >= 0 and c < len(stable)]
  print('Second:', candidates)
  # Cows can always move right, Sheep move left, and from two fields away, they can move in opposite direction
  candidates = [c for c in candidates
    if stable[c:c+2] == ['C', 'E'] # cows can move right
    or stable[c-1:c+1] == ['E', 'S'] # sheep can move left
    or stable[c:c+3] == ['C', 'S', 'E'] # cow jumps over sheep
    or stable[c-2:c+1] == ['E', 'C', 'S'] # sheep jumps over cow
  ]
  print('Third:', candidates)

  # Make sure that all the entries are occupied
  # (not necessary for operation, just better style)
  assert not [c for c in candidates if stable[c] == 'E']

  for c in candidates:
    new_stable = stable[:] # make a copy
    # move the candidates into empty  position
    new_stable[c], new_stable[empty] = new_stable[empty], new_stable[c]
    yield new_stable # remember where we were
pass

goal_stable = ['S','S','S','S','E','C','C','C','C'];
def solution(stable):
  if stable == goal_stable:
    return [stable];

  # dept first search
  for new_stable in successors(stable):
    print('New Stable', new_stable)
    sol = solution(new_stable)
    if sol:
      return [stable] + sol

list(solution(['C','C','C','C','E','S','S','S','S']))

"""Output"""
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [3, 5]
# New Stable ['C', 'C', 'C', 'E', 'C', 'S', 'S', 'S', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [2, 5]
# New Stable ['C', 'C', 'E', 'C', 'C', 'S', 'S', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [1]
# New Stable ['C', 'E', 'C', 'C', 'C', 'S', 'S', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: [0]
# New Stable ['E', 'C', 'C', 'C', 'C', 'S', 'S', 'S', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: []
# New Stable ['C', 'C', 'C', 'S', 'C', 'E', 'S', 'S', 'S']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: [4, 6]
# New Stable ['C', 'C', 'C', 'S', 'E', 'C', 'S', 'S', 'S']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [2, 6]
# New Stable ['C', 'C', 'E', 'S', 'C', 'C', 'S', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [1, 3]
# New Stable ['C', 'E', 'C', 'S', 'C', 'C', 'S', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: [0, 3]
# New Stable ['E', 'C', 'C', 'S', 'C', 'C', 'S', 'S', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: []
# New Stable ['C', 'S', 'C', 'E', 'C', 'C', 'S', 'S', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [2]
# New Stable ['C', 'S', 'E', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [0]
# New Stable ['E', 'S', 'C', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: [1]
# New Stable ['S', 'E', 'C', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: []
# New Stable ['C', 'C', 'S', 'E', 'C', 'C', 'S', 'S', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [1]
# New Stable ['C', 'E', 'S', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: [0, 2]
# New Stable ['E', 'C', 'S', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: [2]
# New Stable ['S', 'C', 'E', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [1]
# New Stable ['S', 'E', 'C', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: []
# New Stable ['C', 'S', 'E', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [0]
# New Stable ['E', 'S', 'C', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: [1]
# New Stable ['S', 'E', 'C', 'C', 'C', 'C', 'S', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: []
# New Stable ['C', 'C', 'C', 'S', 'S', 'C', 'E', 'S', 'S']
# Empty: 6
# First: [4, 5, 7, 8]
# Second: [4, 5, 7, 8]
# Third: [5, 7]
# New Stable ['C', 'C', 'C', 'S', 'S', 'E', 'C', 'S', 'S']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: [7]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'C', 'E', 'S']
# Empty: 7
# First: [5, 6, 8, 9]
# Second: [5, 6, 8]
# Third: [6, 8]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'E', 'C', 'S']
# Empty: 6
# First: [4, 5, 7, 8]
# Second: [4, 5, 7, 8]
# Third: [8]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'S', 'C', 'E']
# Empty: 8
# First: [6, 7, 9, 10]
# Second: [6, 7]
# Third: [7]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'S', 'E', 'C']
# Empty: 7
# First: [5, 6, 8, 9]
# Second: [5, 6, 8]
# Third: []
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'C', 'S', 'E']
# Empty: 8
# First: [6, 7, 9, 10]
# Second: [6, 7]
# Third: [6]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'E', 'S', 'C']
# Empty: 6
# First: [4, 5, 7, 8]
# Second: [4, 5, 7, 8]
# Third: [7]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'S', 'E', 'C']
# Empty: 7
# First: [5, 6, 8, 9]
# Second: [5, 6, 8]
# Third: []
# New Stable ['C', 'C', 'C', 'S', 'S', 'C', 'S', 'E', 'S']
# Empty: 7
# First: [5, 6, 8, 9]
# Second: [5, 6, 8]
# Third: [5, 8]
# New Stable ['C', 'C', 'C', 'S', 'S', 'E', 'S', 'C', 'S']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: [6]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'E', 'C', 'S']
# Empty: 6
# First: [4, 5, 7, 8]
# Second: [4, 5, 7, 8]
# Third: [8]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'S', 'C', 'E']
# Empty: 8
# First: [6, 7, 9, 10]
# Second: [6, 7]
# Third: [7]
# New Stable ['C', 'C', 'C', 'S', 'S', 'S', 'S', 'E', 'C']
# Empty: 7
# First: [5, 6, 8, 9]
# Second: [5, 6, 8]
# Third: []
# New Stable ['C', 'C', 'C', 'S', 'S', 'C', 'S', 'S', 'E']
# Empty: 8
# First: [6, 7, 9, 10]
# Second: [6, 7]
# Third: []
# New Stable ['C', 'C', 'C', 'S', 'C', 'S', 'E', 'S', 'S']
# Empty: 6
# First: [4, 5, 7, 8]
# Second: [4, 5, 7, 8]
# Third: [4, 7]
# New Stable ['C', 'C', 'C', 'S', 'E', 'S', 'C', 'S', 'S']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [2, 5]
# New Stable ['C', 'C', 'E', 'S', 'C', 'S', 'C', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [1, 3]
# New Stable ['C', 'E', 'C', 'S', 'C', 'S', 'C', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: [0, 3]
# New Stable ['E', 'C', 'C', 'S', 'C', 'S', 'C', 'S', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: []
# New Stable ['C', 'S', 'C', 'E', 'C', 'S', 'C', 'S', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [2, 5]
# New Stable ['C', 'S', 'E', 'C', 'C', 'S', 'C', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [0]
# New Stable ['E', 'S', 'C', 'C', 'C', 'S', 'C', 'S', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: [1]
# New Stable ['S', 'E', 'C', 'C', 'C', 'S', 'C', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: []
# New Stable ['C', 'S', 'C', 'S', 'C', 'E', 'C', 'S', 'S']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: [4, 7]
# New Stable ['C', 'S', 'C', 'S', 'E', 'C', 'C', 'S', 'S']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [2]
# New Stable ['C', 'S', 'E', 'S', 'C', 'C', 'C', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [0, 3]
# New Stable ['E', 'S', 'C', 'S', 'C', 'C', 'C', 'S', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: [1]
# New Stable ['S', 'E', 'C', 'S', 'C', 'C', 'C', 'S', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: [3]
# New Stable ['S', 'S', 'C', 'E', 'C', 'C', 'C', 'S', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [2]
# New Stable ['S', 'S', 'E', 'C', 'C', 'C', 'C', 'S', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: []
# New Stable ['C', 'S', 'S', 'E', 'C', 'C', 'C', 'S', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: []
# New Stable ['C', 'S', 'C', 'S', 'C', 'S', 'C', 'E', 'S']
# Empty: 7
# First: [5, 6, 8, 9]
# Second: [5, 6, 8]
# Third: [6, 8]
# New Stable ['C', 'S', 'C', 'S', 'C', 'S', 'E', 'C', 'S']
# Empty: 6
# First: [4, 5, 7, 8]
# Second: [4, 5, 7, 8]
# Third: [4, 8]
# New Stable ['C', 'S', 'C', 'S', 'E', 'S', 'C', 'C', 'S']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [2, 5]
# New Stable ['C', 'S', 'E', 'S', 'C', 'S', 'C', 'C', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [0, 3]
# New Stable ['E', 'S', 'C', 'S', 'C', 'S', 'C', 'C', 'S']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: [1]
# New Stable ['S', 'E', 'C', 'S', 'C', 'S', 'C', 'C', 'S']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: [3]
# New Stable ['S', 'S', 'C', 'E', 'C', 'S', 'C', 'C', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [2, 5]
# New Stable ['S', 'S', 'E', 'C', 'C', 'S', 'C', 'C', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: []
# New Stable ['S', 'S', 'C', 'S', 'C', 'E', 'C', 'C', 'S']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: [4]
# New Stable ['S', 'S', 'C', 'S', 'E', 'C', 'C', 'C', 'S']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [2]
# New Stable ['S', 'S', 'E', 'S', 'C', 'C', 'C', 'C', 'S']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [3]
# New Stable ['S', 'S', 'S', 'E', 'C', 'C', 'C', 'C', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: []
# New Stable ['C', 'S', 'S', 'E', 'C', 'S', 'C', 'C', 'S']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [5]
# New Stable ['C', 'S', 'S', 'S', 'C', 'E', 'C', 'C', 'S']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: [4]
# New Stable ['C', 'S', 'S', 'S', 'E', 'C', 'C', 'C', 'S']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: []
# New Stable ['C', 'S', 'C', 'S', 'S', 'E', 'C', 'C', 'S']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: []
# New Stable ['C', 'S', 'C', 'S', 'C', 'S', 'S', 'C', 'E']
# Empty: 8
# First: [6, 7, 9, 10]
# Second: [6, 7]
# Third: [7]
# New Stable ['C', 'S', 'C', 'S', 'C', 'S', 'S', 'E', 'C']
# Empty: 7
# First: [5, 6, 8, 9]
# Second: [5, 6, 8]
# Third: []
# New Stable ['C', 'S', 'C', 'S', 'C', 'S', 'C', 'S', 'E']
# Empty: 8
# First: [6, 7, 9, 10]
# Second: [6, 7]
# Third: [6]
# New Stable ['C', 'S', 'C', 'S', 'C', 'S', 'E', 'S', 'C']
# Empty: 6
# First: [4, 5, 7, 8]
# Second: [4, 5, 7, 8]
# Third: [4, 7]
# New Stable ['C', 'S', 'C', 'S', 'E', 'S', 'C', 'S', 'C']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [2, 5]
# New Stable ['C', 'S', 'E', 'S', 'C', 'S', 'C', 'S', 'C']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [0, 3]
# New Stable ['E', 'S', 'C', 'S', 'C', 'S', 'C', 'S', 'C']
# Empty: 0
# First: [-2, -1, 1, 2]
# Second: [1, 2]
# Third: [1]
# New Stable ['S', 'E', 'C', 'S', 'C', 'S', 'C', 'S', 'C']
# Empty: 1
# First: [-1, 0, 2, 3]
# Second: [0, 2, 3]
# Third: [3]
# New Stable ['S', 'S', 'C', 'E', 'C', 'S', 'C', 'S', 'C']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [2, 5]
# New Stable ['S', 'S', 'E', 'C', 'C', 'S', 'C', 'S', 'C']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: []
# New Stable ['S', 'S', 'C', 'S', 'C', 'E', 'C', 'S', 'C']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: [4, 7]
# New Stable ['S', 'S', 'C', 'S', 'E', 'C', 'C', 'S', 'C']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [2]
# New Stable ['S', 'S', 'E', 'S', 'C', 'C', 'C', 'S', 'C']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [3]
# New Stable ['S', 'S', 'S', 'E', 'C', 'C', 'C', 'S', 'C']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: []
# New Stable ['S', 'S', 'C', 'S', 'C', 'S', 'C', 'E', 'C']
# Empty: 7
# First: [5, 6, 8, 9]
# Second: [5, 6, 8]
# Third: [6]
# New Stable ['S', 'S', 'C', 'S', 'C', 'S', 'E', 'C', 'C']
# Empty: 6
# First: [4, 5, 7, 8]
# Second: [4, 5, 7, 8]
# Third: [4]
# New Stable ['S', 'S', 'C', 'S', 'E', 'S', 'C', 'C', 'C']
# Empty: 4
# First: [2, 3, 5, 6]
# Second: [2, 3, 5, 6]
# Third: [2, 5]
# New Stable ['S', 'S', 'E', 'S', 'C', 'S', 'C', 'C', 'C']
# Empty: 2
# First: [0, 1, 3, 4]
# Second: [0, 1, 3, 4]
# Third: [3]
# New Stable ['S', 'S', 'S', 'E', 'C', 'S', 'C', 'C', 'C']
# Empty: 3
# First: [1, 2, 4, 5]
# Second: [1, 2, 4, 5]
# Third: [5]
# New Stable ['S', 'S', 'S', 'S', 'C', 'E', 'C', 'C', 'C']
# Empty: 5
# First: [3, 4, 6, 7]
# Second: [3, 4, 6, 7]
# Third: [4]
# New Stable ['S', 'S', 'S', 'S', 'E', 'C', 'C', 'C', 'C']