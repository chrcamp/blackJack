import random
import copy

# define defaults

deck = ['02♧','02♢','02♡','02♤',
        '03♧','03♢','03♡','03♤',
        '04♧','04♢','04♡','04♤',
        '05♧','05♢','05♡','05♤',
        '06♧','06♢','06♡','06♤',
        '07♧','07♢','07♡','07♤',
        '08♧','08♢','08♡','08♤',
        '09♧','09♢','09♡','09♤',
        '10♧','10♢','10♡','10♤',
        'J♧','J♢','J♡','J♤',
        'Q♧','Q♢','Q♡','Q♤',
        'K♧','K♢','K♡','K♤',
        'A♧','A♢','A♡','A♤']

card_val = {'02♧':2,'02♢':2,'02♡':2,'02♤':2,
            '03♧':3,'03♢':3,'03♡':3,'03♤':3,
            '04♧':4,'04♢':4,'04♡':4,'04♤':4,
            '05♧':5,'05♢':5,'05♡':5,'05♤':5,
            '06♧':6,'06♢':6,'06♡':6,'06♤':6,
            '07♧':7,'07♢':7,'07♡':7,'07♤':7,
            '08♧':8,'08♢':8,'08♡':8,'08♤':8,
            '09♧':9,'09♢':9,'09♡':9,'09♤':9,
            '10♧':10,'10♢':10,'10♡':10,'10♤':10,
            'J♧':10,'J♢':10,'J♡':10,'J♤':10,
            'Q♧':10,'Q♢':10,'Q♡':10,'Q♤':10,
            'K♧':10,'K♢':10,'K♡':10,'K♤':10,
            'A♧':11,'A♢':11,'A♡':11,'A♤':11}

wallet = 100
player_hand = []
dealer_hand = []
round_status = ''

# define functions

def bet():
    global wallet
    global bet
    while True:
        try:
            bet = int(input('You currently have $' + str(wallet) + '. Enter your bet: '))
            if bet <= 0:
                print('You must bet at least $1.')
                continue
            elif bet > wallet:
                print('You do not have enough money')
                continue
            else:
                wallet = wallet - bet
                print('Your bet is $' + str(bet) + '. You have $' + str(wallet) + ' remaining')
                break
        except ValueError:
            print('You must bet in dollars only.')

def deal():
    while len(player_hand) < 2 and len(dealer_hand) < 2:
        card = str(deck[random.randint(0,len(deck)-1)])
        player_hand.append(card)
        deck.remove(card)

        card = str(deck[random.randint(0,len(deck)-1)])
        dealer_hand.append(card)
        deck.remove(card)

def hit():
    global hand_val
    global move
    while move == 'hit':
        card = str(deck[random.randint(0,len(deck)-1)])
        player_hand.append(card)
        deck.remove(card)
        print('You were dealt: ' + card + '. Your hand is now: ' + str(player_hand))
        hand_val = hand_val + card_val[card]
        move = ''
        if hand_val > 21:
            print('YOU BUST, IDIOT!!!! Dealer wins the hand.')
            round_status = 'L'

def house_finish():
    global house_val
    global hand_val
    while house_val < 16 and house_val < hand_val:
        card = str(deck[random.randint(0,len(deck)-1)])
        dealer_hand.append(card)
        deck.remove(card)
        print('The dealer flips: ' + card)
        house_val = house_val + card_val[card]
        if house_val > 21:
            print('The Dealer bust. You win the hand!')
            round_status = 'W'

# round start

bet()
deal()

house_val = card_val[dealer_hand[0]] + card_val[dealer_hand[1]]
hand_val = card_val[player_hand[0]] + card_val[player_hand[1]]

if house_val == 21:
    print('You were dealt the hand: '+ str(player_hand))
    print('The dealer has: '+ str(dealer_hand))
    print('Dealer has a Blackjack, you lose the hand.')
    round_status = 'L'
elif hand_val == 21:
    print('You were dealt the hand: '+ str(player_hand))
    print('The dealer has: '+ str(dealer_hand))
    print('Blackjack!! You win the hand!')
    round_status = 'W'
else:
    print('You were dealt the hand: '+ str(player_hand))
    print('The dealer has '+str(dealer_hand[0])+' showing.')
    move = input('Would you like to Hit or Stay?   ')
    move = move.lower()
    if move == 'hit':
        hit()
        move = ''
    elif move == 'stay':
        house_finish()
    else:
        print('Your options are Hit or Stay. Which would you like to do?')

if hand_val > house_val:
    print('You beat the dealer!')
    round_status = 'W'
else:
    print('The dealer beat you...')
    round_status = 'L'



# figure out if python convention uses camelCase or under_score for variable names. Also, stop giving variables dumb names.

# figure out a way to make the Ace value dynamic--i.e. 1 or 11
# end hand by printing player_hand and dealer_hand for final reveal/results
# refine hit() fn. can only hit once. need better loop to give you 2+ decisions
# build decision() fn loop to streamline hit() stay(). consider split() double()
# simplify round. use round_status as round end/rest indicator.
# make complete game loop with aggregate wallet until a Loss with $0 left. Game currently ends after 1 hand.
# for complete game loop, decide whether or not to use a fresh deck. consider using 3 decks simultaneously.
# consider importing time module to add a 1 second delay between output. the instant response/processing somehow pisses me off...

# long-term: learn a python gui --probably pygame or tkinter-- and migrate.



