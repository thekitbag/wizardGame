import random
deck = []
suits = ["a", "b", "c", "d"]

gameId = 0
pile = []
hands= {}
numberOfEntrants=4
Scoreboard = {
	"playerOne": 0,
	"playerTwo": 0,
	"playerThree": 0,
	"playerFour": 0,
	"playerFive": 0,
	"playerSix": 0,
}

def buildDeck():
	for i in range(1,14):
		for j in suits:
			card = str(i)+j
			deck.append(card)
	for i in range(4):
		deck.append("0J")
		deck.append("0W")



def setPlaces(players):
	for i in range(players):		
		hands['player_hand_{}'.format(i)]=[]

def dealCards(roundNumber):
	for i in range(roundNumber):
		for j in hands:
			nextCard = deck.pop(random.randint(0,len(deck)-1))
			hands[j].append(nextCard)
	

def clearHands():
	for i in range(len(hands['player_hand_1'])):
		for j in hands:
			cards = hands[j].pop()
			deck.append(cards)


def playGame(entrants):
	currentRound = 1
	buildDeck()
	setPlaces(entrants)	
	dealCards(currentRound)
	print hands
	print deck
	print len(deck)
	clearHands()	
	print"----------------"
	currentRound +=1		
	dealCards(currentRound)
	print hands
	print deck
	print len(deck)
	clearHands()
	print"----------------"
	currentRound +=1		
	dealCards(currentRound)
	print hands
	print deck
	print len(deck)
	
	
	

playGame(numberOfEntrants)




