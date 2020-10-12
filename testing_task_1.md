### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 

```python

class CardGame:
#no mention of suit?
#where is def __init__(self)?

  def checkforAce(self, card):
    if card.value == 1:
      return true
    else
      return false
#value == 1
#else missing :

  def highest_card(self, card1 card2):
    if card1.value > card2.value:
      return card1
    else
      return card2
#def instead of dif
#return card1
#missing : after first line
#missing : after
#card 1 and card 2 don't have comma
#else mssing :
#:missing after card2) on first line

 def cards_total(self, cards):
   total
   for card in cards:
     total += card.value
     return "You have a total of" + total
#(self, cards)
#will total not be included in string and needs to be changed to string?
#total = 0
#indentation of return to leave function
```
