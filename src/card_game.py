### Testing task 2 code:

# Carry out dynamic testing on the code below.
# Correct the errors below that you spotted in task 1.

class CardGame:

  # def __init__(self):
  #   self.cards = []
  # does this need set up?

  # def add_card(self, card):
  #   card = []
  #   self.card.append(card)


  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False
#_ between check for ace and decapitalise A in ace.

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
      return card1
    else:
      return card2
 

  def cards_total(self, cards):
      total = 0
      for card in cards:
          total += card.value
      return "You have a total of " + str(total)