import random
import copy

# define defaults

full_deck = {'2♧':2,'2♢':2,'2♡':2,'2♤':2,
            '3♧':3,'3♢':3,'3♡':3,'3♤':3,
            '4♧':4,'4♢':4,'4♡':4,'4♤':4,
            '5♧':5,'5♢':5,'5♡':5,'5♤':5,
            '6♧':6,'6♢':6,'6♡':6,'6♤':6,
            '7♧':7,'7♢':7,'7♡':7,'7♤':7,
            '8♧':8,'8♢':8,'8♡':8,'8♤':8,
            '9♧':9,'9♢':9,'9♡':9,'9♤':9,
            '10♧':10,'10♢':10,'10♡':10,'10♤':10,
            'J♧':10,'J♢':10,'J♡':10,'J♤':10,
            'Q♧':10,'Q♢':10,'Q♡':10,'Q♤':10,
            'K♧':10,'K♢':10,'K♡':10,'K♤':10,
            'A♧':11,'A♢':11,'A♡':11,'A♤':11}

wallet = 100

# define functions

def placeBet():
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
                print('Your bet is $' + str(bet))
                break
        except ValueError:
            print('You must bet in dollars only.')

def evaluate():
    global p_val
    global d_val
    p_val = sum(p_hand.values())
    d_val = sum(d_hand.values())

def deal():
    global round_status
    while len(p_hand) < 2 and len(d_hand) < 2:
        card = random.choice(list(deck))
        p_hand[card] = deck.get(card)
        del deck[card]

        card = random.choice(list(deck))
        d_hand[card] = deck.get(card)
        del deck[card]
    print('You were dealt the hand: ' +str(list(p_hand)))
    print('The dealer is showing: ' + list(d_hand)[0])
    evaluate()
    if d_val == 21:
        print('The dealer has a BlackJack')
        round_status = 'L'
    elif p_val == 21:
        print('BLACKJACK!!!')
        round_status = 'W'
        

def hit():
    global round_status
    card = random.choice(list(deck))
    p_hand[card] = deck.get(card)
    del deck[card]
    print('You were dealt ' + card)
    print('Your hand is now: '+str(list(p_hand)))
    evaluate()
    if p_val > 21:
        print('You BUST, IDIOT!!')
        round_status = 'L'

def houseFinish():
    global d_val
    global p_val
    global round_status
    while True:
        if round_status == 'L':
            break
        elif d_val < 16 and d_val < p_val:
            card = random.choice(list(deck))
            d_hand[card] = deck.get(card)
            del deck[card]
            print('The dealer flips: ' + card)
            print('The dealers hand is: '+str(list(d_hand)))
            evaluate()
            continue
        else:
            evaluate()
            if d_val > 21:
                print('The dealer BUST!')
                round_status = 'W'
            elif d_val < p_val:
                round_status = 'W'
            elif d_val > p_val:
                round_status = 'L'
            break

def playerAction():
    global round_status
    while True:
        if round_status != '':
            break
        else:
            move = input('Would you like to Hit or Stay? ')
            move = move.lower()
            if move == 'hit':
                hit()
                move = ''
                continue
            elif move == 'stay':
                break
            else:
                print('You must choose either Hit or Stay. What would you like to do? ')
                move = ''
                continue


# round start

while True:
    if wallet > 0:
        deck = full_deck.copy()
        p_hand = {}
        d_hand = {}
        round_status = ''
        move = ''
        placeBet()
        deal()
        while True:
            if round_status == 'W':
                print('You win the hand!')
                wallet = wallet +(bet*2)
                break
            elif round_status == 'L':
                print('You lost the hand...')
                break
            else:
                playerAction()
                houseFinish()
                continue
            print('You have $'+str(wallet)+' remaining in your wallet.')
            continue
    elif wallet == 0:
        print('You are out of money. Game over....')
        print('Thanks for playing.')
        break
