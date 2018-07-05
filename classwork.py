from random import randint
from pprint import pprint


def huuuh_sonny():
    while True:
        response = input('You: ')
        if response == 'BYE':
            print('GRANDMA: BYE SONNY')
            break
        elif response.isupper():
            print('Grandma: NO, NOT SINCE {}!'.format(randint(1930, 1950)))
        else:
            print(
                'Grandma: HUUUH!!?....WHAT THE HECK YOU SAYIN,SPEAK UP...SONNY!!!'
            )


def grader():
    grades = []
    while True:
        grade = input('Your Grade: ').strip()
        if grade == 'quit':
            break
        else:
            grades.append(int(grade))
    average = round(sum(grades) / len(grades))
    print(average)

    if average >= 90:
        print('Your grade is: A')
    elif average >= 80:
        print('Your grade is: B')
    elif average >= 70:
        print('Your grade is: C')
    elif average >= 65:
        print('Your grade is: D')
    elif average <= 64:
        print('Your grade is: F, and you failed stupid!!!')


def what_you_doin():
    while True:
        name = input(
            '\nWhat is your name?(first,last name.): ').strip().lower()
        if name == 'nate clark':
            print('\nI am the Technical Director.')
        if name == 'sean anthony':
            print('\nI am the Director.')
        if name == 'kagan coughlin':
            print('\nI am a co-founder')
        if name == 'sage nichols':
            print('\nI am a Founding Trustee')
        if name == 'edgar guzman':
            print('\nI was in the graduated class 0f 2017')
        if name == 'daniel peterson':
            print('\nI am a current student, and is gonna be the best!!!!')
        if name == 'cody vander poel':
            print('\nI am a current student and I am from Charleston.')
        elif name == 'done':
            break


def two_player_war():

    from random import randint, shuffle

    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12,
        13, 13, 13, 13, 14, 14, 14, 14
    ]
    shuffle(deck)

    Daniels_hand = deck[:26]

    Rays_hand = deck[26:]

    Daniels_pile = []

    Rays_pile = []

    deck = []

    treasure_cards = []

    while True:
        if len(Daniels_hand) == 0:
            if len(Daniels_pile) == 0:
                print('Big Razzor wins!')
                break
            Daniels_hand.extend(Daniels_pile)
            Daniels_pile = []
        daniels_card = Daniels_hand.pop()
        if len(Rays_hand) == 0:
            if len(Rays_pile) == 0:
                print('Dannyp wins!')
                break
            Rays_hand.extend(Rays_pile)
            Rays_pile = []
        rays_card = Rays_hand.pop()
        deck.extend([daniels_card, rays_card])

        print('\nDaniel: drew {} \nRay: drew {}'.format(
            daniels_card, rays_card))
        shuffle(deck)
        input()

        if daniels_card > rays_card:
            print('\tThe Danny P wins!')
            Daniels_pile.append(daniels_card)
            Daniels_pile.append(rays_card)
            Daniels_pile.extend(treasure_cards)
            treasure_cards = []

        elif rays_card > daniels_card:
            print('\tOne more for Raynard!')
            Rays_pile.append(rays_card)
            Rays_pile.append(daniels_card)
            Rays_pile.extend(treasure_cards)
            treasure_cards = []
        else:
            treasure_cards.append(daniels_card)

            treasure_cards.append(rays_card)

            if len(Daniels_hand) == 0:
                if len(Daniels_pile) == 0:
                    print('Big Razzor wins!')
                    break
                Daniels_hand.extend(Daniels_pile)
                Daniels_pile = []

            dp_cards = Daniels_hand.pop()

            treasure_cards.append(dp_cards)

            if len(Daniels_hand) == 0:
                if len(Daniels_pile) == 0:
                    print('Big Razzor wins!')
                    break
                Daniels_hand.extend(Daniels_pile)
                Daniels_pile = []

            dp_cards = Daniels_hand.pop()

            treasure_cards.append(dp_cards)

            if len(Daniels_hand) == 0:
                if len(Daniels_pile) == 0:
                    print('Big Razzor wins!')
                    break
                Daniels_hand.extend(Daniels_pile)
                Daniels_pile = []

            dp_cards = Daniels_hand.pop()

            treasure_cards.append(dp_cards)

            if len(Rays_hand) == 0:
                if len(Rays_pile) == 0:
                    print('Dannyp wins!')
                    break
                Rays_hand.extend(Rays_pile)
                Rays_pile = []

            rt_cards = Rays_hand.pop()

            treasure_cards.append(rt_cards)

            if len(Rays_hand) == 0:
                if len(Rays_pile) == 0:
                    print('Dannyp wins!')
                    break
                Rays_hand.extend(Rays_pile)
                Rays_pile = []

            rt_cards = Rays_hand.pop()

            treasure_cards.append(rt_cards)

            if len(Rays_hand) == 0:
                if len(Rays_pile) == 0:
                    print('Dannyp wins!')
                    break
                Rays_hand.extend(Rays_pile)
                Rays_pile = []

            rt_cards = Rays_hand.pop()

            treasure_cards.append(rt_cards)
        # print('D:', Daniels_hand, Daniels_pile)
        # print('R:', Rays_hand, Rays_pile)
        # print('T:', treasure_cards)


def chores_assigner():
    from random import randint, shuffle

    students = [
        'Cody Vander Poel:', 'Desma Hervey:', 'Daniel Peterson:',
        'Tim Bowling:', 'Henry Moore:', 'Ray Turner:', 'Justice Taylor:',
        'Ginger Keys:', 'Logan Harrell:', 'Irma Patton:', 'Cole Anderson:',
        'Matt Lipsey:', 'John Morgan:', 'Andrew Wheeler:',
        'Jakylan Standifer:', 'Myisha Madkins:'
    ]
    chores = [
        'Monday Lunch set-up/clean up', 'Tuesday Lunch set-up/clean up',
        'Wednesday Lunch set-up/clean up', 'Thursday Lunch set-up/clean up',
        'Friday Lunch set-up/clean up',
        'Check trash and sweep classroom floor DAILY',
        'Take kitchens trash out DAILY', 'Sweep stairs DAILY',
        'Friday sweep hallways', 'Keep classroom organized DAILY',
        'Restock water when needed', 'Friday clean bathroom 1',
        'Friday clean bathroom 2', 'Take trash out of bathrooms',
        'Take boxes to trash', 'Help others'
    ]
    shuffle(students)
    for student in students:
        print()
        print(student, chores.pop())


def black_jack():
    from random import shuffle
    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11
    ]
    shuffle(deck)
    blackjack_deck = []
    dealer_deck = []
    total = 0
    while True:
        blackjack_deck.append(deck.pop())
        dealer_deck.append(deck.pop())
        blackjack_deck.append(deck.pop())
        dealer_deck.append(deck.pop())
        while True:
            print('Your hand:', blackjack_deck)
            print('Dealer top card:', dealer_deck[0])
            choice = input('would you like to hit or stay????')
            if choice == 'hit':
                blackjack_deck.append(deck.pop())
            if choice == 'stay':
                break

    while sum(blackjack_deck) < 22 and sum(dealer_deck) < 22:
        if sum(dealer_deck) < 17:
            dealers_deck.append(deck.pop())
            print('Dealer Hits.')
        elif sum(dealer_deck) >= 17:
            print('Dealer Stays')
            break

    if score_of(dealer_deck) <= score_of(blackjack_deck):
        print('The Dealer Wins!!!!')
    else:
        print('Player wins!!!')

    deck.extend(blackjack_deck)
    blackjack_deck.clear()


def hey_you():
    name = input('What is your name sir/mam??')
    print('Whats up, ' + name)


def main():
    black_jack()
    # hey_you()
    # what_you_doin()
    # grader()
    # huuuh_sonny()
    # two_player_war()
    # chores_assigner()


if __name__ == '__main__':
    main()
