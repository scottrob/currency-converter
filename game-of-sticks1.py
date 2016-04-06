import random

def current_player_turn(sticks, name, current_player):
    if current_player == 1:
        return player_one(sticks, name)
    else:
        return player_two(sticks, name)

def player_one(sticks,name):
    number = int(input("Player 1: How many sticks do you take(1-3)? "))
    sticks -= number
    print('{} takes {} sticks'.format(name, number))
    return sticks_a_turn(sticks,name,number)

def player_two(sticks,name):
    number = int(input("Player 2: How many sticks do you take(1-3)? "))
    sticks -= number
    print('{} takes {} sticks'.format(name, number))
    return sticks_a_turn(sticks,name,number)

def sticks_a_turn(sticks,name,number):
    if sticks < 1:
        print('{} takes the last stick and loses'.format(name, number))
    else:
        return sticks

def main():
    print("Welcome to the Game of Sticks!")
    player_one_name = input("Player one enter name > ")
    player_two_name = input("Player two enter name > ")
    sticks = int(input("How many sticks are there (10-100)? "))
    current_player = random.randint(1,2)
    while sticks > 1:
        if current_player == 1:
            print('There are {} sticks on the board'.format(sticks))
            name = player_one_name
            current_player = 2
            sticks = current_player_turn(sticks, name,current_player)
        else:
            print('There are {} sticks on the board'.format(sticks))
            name = player_two_name
            current_player = 1
            sticks = current_player_turn(sticks, name,current_player)
if __name__ == '__main__':
    main()
