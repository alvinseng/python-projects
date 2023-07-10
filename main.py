############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
from art import logo
import random 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deckValue = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'A' : 11,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}

#Creating a list from the dictionary key then shuffling it 
keys = list(deckValue.keys())
random.shuffle(keys)

#player's start hand
userCards = []
compCards = []

#deals the card out to the players
def dealCard():
    #shuffling the keys and drawing 2 keys out of the list
    userCards.extend(random.sample(keys, k=2))
    compCards.extend(random.sample(keys, k=2))
    #dealing cards
    print(f'\nPlayer Cards : \n{userCards}')
    print(f'Computer Cards : \n{compCards}')
    
pTotal = 0
cTotal = 0

#Calculates both the User & Computer scores to "21" / '0'
def calculateScore(userHand, compHand):
    global pTotal
    global cTotal
    pTotal = sum(deckValue[card] for card in userCards)
    cTotal = sum(deckValue[card] for card in compCards)
    if 'A' in userCards and pTotal > 21:
        # deckValue['A'] = 1
        pTotal -= 10
    if 'A' in compCards and cTotal > 21:
        # deckValue['A'] = 1
        cTotal -= 10

def hitCard():
    global pTotal
    global cTotal
    #note: add this to calculateScores to call hitcards()
    if pTotal <= 15:
        hitC = input("Would you like another card?\n")
        if hitC.lower() == 'y':
            userCards.extend(random.choice(keys))  
            print(f'\nPlayer Card : \n{userCards}')
            # print(f"{pTotal}") #Debugging
        elif hitC.lower() == 'n':
            print(f"Player's Card: \n{userCards}")
            # print(f"{pTotal}") #Debugging
    if cTotal > 15:
        f'Computer Cards: \n{compCards}'
        # print(f"{cTotal}") #Debugging
    elif cTotal <= 15:
        compCards.extend(random.choice(keys))
        print(f'Computer cards: \n{compCards}')
        # print(f"{pTotal}") #Debugging

def compare(playerScore, comScore):
    if playerScore == comScore or playerScore > 21 and comScore > 21:
        print("\nTry Again")
    elif comScore <= 21 and comScore > playerScore or playerScore > 21 and comScore < 21:
        print("\nComputer Wins")
    elif playerScore <= 21 and playerScore > comScore or comScore > 21 and playerScore < 21:
        print("\nPlayer WIns")
        
print(logo)
gameInput = input("Start Game? Y/N\n")
if gameInput.lower() == 'y':
    dealCard()

hitCard()
calculateScore(userCards,compCards)
print(f" \nPlayer: {pTotal} \nComputer: {cTotal}" )
compare(pTotal, cTotal)