# card.py
"""Card class that represents a playing card and its image file name."""

class Card:
  FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
  SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

  def __init__(self, face, suit):
    """Initializes a Card object with a face and suit."""
    self._face = face
    self._suit = suit

  @property
  def face(self):
    """Returns the face of the card."""
    return self._face

  @property
  def suit(self):
    """Returns the suit of the card."""
    return self._suit

  @property
  def image_name(self) -> str:
    """Return the Card's image file name."""
    return str(self).replace(' ', '_').lower() + '.png'

  def __str__(self) -> str:
    return f'{self._face} of {self._suit}'

  def __repr__(self) -> str:
    return f'Card({self._face}, {self._suit})'

  def __format__(self, format) -> str:
    return f'{str(self):{format}}'