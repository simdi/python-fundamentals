# state = (
#   {
#     ('kick', 1): 'left',
#     ('kick', 2): 'left',
#     ('kick', 3): 'left',
#     ('hero', 1): 'left',
#     ('hero', 1): 'left',
#     ('hero', 1): 'left',
#   },
#   'left'
# )

from typing_extensions import Self

class Hero:
  def start(self):
    # where everybody is, where the boat is
    return {
      (person, index): 'left'
      for person in ['hero', 'kick']
      for index in [1,2,3]
    }, 'left'

  def goal(self, state):
    person_side, _ = state
    # is everybody on the right?
    return set(person_side[person] for person in person_side) == { 'right'}
    # person_side.values() should also work

  def successor(self, state):
    # who can move
    person_side, boat = state
    # collect all people on the side of the boat
    person_with_boat = [person for person in person_side if person_side[person] == boat]

    for traveler_group in select_traveler(person_with_boat):
      new_side = person_side.copy() # never change the original

      for traveler in traveler_group:
        # the traveler moves to the other side
        new_side[traveler] = other_side[person_side[traveler]]

      new_side = new_side, other_side[boat]

      if safe(new_side):
        yield new_side

def select_traveler(candidates):
  # select 1 or 2 traveler
  # since there are only two cases,
  # choose pedestrian approach rather than recursion

  #one traveler
  for first in range(len(candidates)):
    yield [candidates[first]]

  # two travelers
  for first in range(len(candidates)):
    for second in range(first+1, len(candidates)):
      yield [candidates[first], candidates[second]]

other_side = { 'left': 'right', 'right': 'left' }

def safe(state):
  # never leave your sidekick alone with another hero

  person_side, _ = state
  for side in ['left', 'right']:
    # check all sidekick on given side with a their hero
    lone_kick = [
      index for (person, index) in person_side
      if person == 'kick'
      if person_side[person, index] == side
      if person_side['hero', index] != side
    ]

    # collect all heros on the current side (they are the bad ones!)
    present_hero = [
      index for (person,index) in person_side
      if person == 'kick'
      if person_side[person, index] == side
    ]

    # if there is a lone kick and another hero, there is problem
    if lone_kick and present_hero:
      return False

  return True

state = Hero.start(Self)
for succ in Hero.successor(Self, state):
  print(succ);
