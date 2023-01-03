import random
from typing import Dict, List


class Players:
    options = {'scissors': ['rock'], 'paper': ['scissors'], 'rock': ['paper']}

    def __init__(self, name):
        self.score = 0
        self.name = name
        self.choice = ''

    def rating(self):
        return print('Your rating:', self.score)

    def greet(self):
        return print('Hello,', self.name)

    def options_set(options_list):
        if options_list == ['']:
            pass
        else:
            Players.options = {}
            for i in range(len(options_list)):
                if i == len(options_list) - 1:
                    Players.options[options_list[i]] = options_list[0:len(options_list) // 2]
                else:
                    if i <= len(options_list) // 2:
                        Players.options[options_list[i]] = options_list[i + 1:i + len(options_list) // 2 + 1]
                    elif i > len(options_list) // 2:
                        Players.options[options_list[i]] = options_list[i - len(options_list) + 1:] + options_list[:i - len(options_list) // 2]
        return print("Okay, let's start")


    def computer_choice():
        return random.choice(list(Players.options))

    def set_choice(self, user_input):
        if user_input == '!rating':
            self.choice = '!rating'
            self.rating()
        elif user_input == '!exit':
            self.choice = '!exit'
            print('Bye!')
        elif user_input not in Players.options:
            self.choice = 'Invalid input'
            print('Invalid input')
        elif user_input in Players.options:
            self.choice = user_input

    def play(self):
        computer_option = Players.computer_choice()
        player_option = self.choice
        if computer_option == player_option:
            self.score += 50
            print(f"There is a draw ({player_option})")
        elif computer_option in Players.options[player_option]:
            print(f"Sorry, but the computer chose {computer_option}")
        else:
            self.score += 100
            print(f"Well done. The computer chose {computer_option} and failed")



initial_users_rating = {}
with open('rating.txt', 'r') as rating:
    for line in rating:
        name, score = line.strip().split(' ')
        initial_users_rating[name] = int(score)



# print('Enter your name: ')
player = Players(input('Enter your name: '))
Players.greet(player)
Players.options_set(input().split(','))

if player.name in initial_users_rating.keys():
    player.score = initial_users_rating[player.name]


while True:
    player.set_choice(input())
    if player.choice == '!exit':
        break
    elif player.choice == 'Invalid input':
        continue
    elif player.choice == '!rating':
        continue
    elif player.choice in Players.options:
        player.play()
