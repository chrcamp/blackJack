#blackJack.py
# Use Python 3

import random, copy, time

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
    global wallet, bet
    while True:
        try:
            bet = int(input('You have $' + str(wallet) + ' in your wallet. \nPlace your bet: $'))
            if bet <= 0:
                print('You must bet at least $1.')
                continue
            elif bet > wallet:
                print('You do not have enough money')
                continue
            else:
                wallet = wallet - bet
                break
        except ValueError:
            print('You must bet in dollars only.')

def evaluate():
    global player_value, dealer_value
    while True:
        player_value = sum(player_hand.values())
        if player_value > 21 and 'A♧' in player_hand:
            del player_hand['A♧']
            player_hand['a♧'] = 1
            continue
        elif player_value > 21 and 'A♢' in player_hand:
            del player_hand['A♢']
            player_hand['a♢'] = 1
            continue
        elif player_value > 21 and 'A♡' in player_hand:
            del player_hand['A♡']
            player_hand['a♡'] = 1
            continue
        elif player_value > 21 and 'A♤' in player_hand:
            del player_hand['A♤']
            player_hand['a♤'] = 1
            continue
        else:
            break
    while True:
        dealer_value = sum(dealer_hand.values())
        if dealer_value > 21 and 'A♧' in dealer_hand:
            del dealer_hand['A♧']
            dealer_hand['a♧'] = 1
            continue
        elif dealer_value > 21 and 'A♢' in dealer_hand:
            del dealer_hand['A♢']
            dealer_hand['a♢'] = 1
            continue
        elif dealer_value > 21 and 'A♡' in dealer_hand:
            del dealer_hand['A♡']
            dealer_hand['a♡'] = 1
            continue
        elif dealer_value > 21 and 'A♤' in dealer_hand:
            del dealer_hand['A♤']
            dealer_hand['a♤'] = 1
            continue
        else:
            break

def deal():
    global round_status
    while len(player_hand) < 2 and len(dealer_hand) < 2:
        card = random.choice(list(deck))
        player_hand[card] = deck.get(card)
        del deck[card]

        card = random.choice(list(deck))
        dealer_hand[card] = deck.get(card)
        del deck[card]
    print('\n\tYou were dealt the hand: ' + (' '.join(list(player_hand))))
    time.sleep(0.25)
    print('\tThe dealer is showing: ' + list(dealer_hand)[0]+'\n')
    time.sleep(0.25)
    evaluate()
    if dealer_value == 21:
        print('\tThe dealer has a BlackJack')
        round_status = 'L'
    elif player_value == 21:
        print('\t' + '*'*18 + '\n\t** BLACKJACK!!! **\n\t' + '*'*18 + '\n')
        round_status = 'B'
        

def hit():
    global round_status
    card = random.choice(list(deck))
    player_hand[card] = deck.get(card)
    del deck[card]
    print('\tYou were dealt ' + card)
    time.sleep(0.25)
    print('\tYour hand is now: '+ (' '.join(list(player_hand)))+'\n')
    time.sleep(0.25)
    evaluate()
    if player_value > 21:
        print('\tYou BUST, IDIOT!!')
        round_status = 'L'

def houseFinish():
    global dealer_value, player_value, round_status
    while True:
        if round_status == 'L':
            break
        elif dealer_value < 16 and dealer_value < player_value:
            card = random.choice(list(deck))
            dealer_hand[card] = deck.get(card)
            del deck[card]
            print('\tThe dealer flips: ' + card)
            time.sleep(0.25)
            evaluate()
            continue
        else:
            evaluate()
            if dealer_value > 21:
                print('\tThe dealer BUST!')
                round_status = 'W'
            elif dealer_value < player_value:
                round_status = 'W'
            elif dealer_value >= player_value:
                round_status = 'L'
            break

def playerAction():
    global round_status
    while True:
        if round_status != '':
            break
        else:
            move = input('\tWould you like to Hit or Stay? ')
            move = move.lower()
            if move == 'hit':
                hit()
                move = ''
                continue
            elif move == 'stay':
                break
            else:
                print('\tYou must choose either Hit or Stay. What would you like to do? ')
                move = ''

def results():
    print('\n\tYour hand: \n\t' + (' '.join(list(player_hand))))
    print('\n\tDealer\'s hand: \n\t' + (' '.join(list(dealer_hand)))+'\n')


# round start

while True:
    if wallet > 0:
        deck = full_deck.copy()
        player_hand = {}
        dealer_hand = {}
        round_status = ''
        move = ''
        placeBet()
        time.sleep(0.5)
        deal()
        while True:
            if round_status == 'W':
                print('You win the hand!\n')
                print('~~*'*30+'\n')
                wallet = wallet +(bet*2)
                break
            elif round_status == 'B':
                print('You win the hand!\n')
                print('~~*'*30+'\n')
                wallet = wallet +(bet*3)
                break
            elif round_status == 'L':
                print('You lost the hand...\n')
                print('-'*90+'\n')
                break
            else:
                playerAction()
                houseFinish()
                results()
                continue
    elif wallet == 0:
        print('You are out of money. Game over....')
        print('Thanks for playing.')
        break
