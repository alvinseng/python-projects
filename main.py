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
