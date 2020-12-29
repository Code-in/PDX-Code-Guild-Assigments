from colorama import Fore, Back, Style
import random
import time


class GameIntro():

    title = r'''
             (                                                                
         )\ )                                   (                      )  
        (()/(   (       )  (  (               ( )\     (     (      ( /(  
         /(_))  )(   ( /(  )\))(  (    (      )((_)   ))\   ))\ (   )\()) 
        (_))_  (()\  )(_))((_))\  )\   )\ )  ((_)_   /((_) /((_))\ (_))/  
         |   \  ((_)((_)_  (()(_)((_) _(_/(   / _ \ (_))( (_)) ((_)| |_   
         | |) || '_|/ _` |/ _` |/ _ \| ' \)) | (_) || || |/ -_)(_-<|  _|  
         |___/ |_|  \__,_|\__, |\___/|_||_|   \__\_\ \_,_|\___|/__/ \__|  
                          |___/                                           
    '''

    dragon = r'''
   ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-
             ~\_        // *******.:|\^^^/|:.******* \\        _/~
                \      / ********.::(>: :<)::.******** \      /
                 \   /  ********.::::\\|//::::.********  \   /
                  \ /   *******.:::::(o o):::::.*******   \ /
                   /.   ******.::::'*|V_V|***`::.******   .\
                     ~~--****.:::'***|___|*****`:.****--~~
                           *.::'***//|___|\\*****`.* 
                           .:'  **/##|___|##\**    .
                          .    (v(VVV)___(VVV)v)     .
'''

        
    def print_intro_test(self):
        text = 'Defeat the dragon, get the treasure!'
        for char in text:
            print(Fore.GREEN + char, end='', flush=True)
            #print(Fore.GREEN + char)
            time.sleep(0.05)
        print(Style.RESET_ALL)
        print()
        return ''


    def __init__(self):
        print(Fore.YELLOW + GameIntro.title + Style.RESET_ALL)
        print(Fore.RED + GameIntro.dragon + Style.RESET_ALL)
        self.print_intro_test()
        


 # parent class which contains a location, character, and health
class Creature:

    def __init__(self, location_x, location_y, character, health, weapon_damage):
        self.location_x = location_x
        self.location_y = location_y
        self.character = character
        self.__health = health
        self.weapon_damage = weapon_damage

    
    def get_x(self):
        return self.location_x

    def get_y(self):
        return self.location_y

    def damage(self, damage):
        self.__health -= damage

    def attack(self):
        return random.randint(0, self.weapon_damage)

    def get_health(self):
        return self.__health 


# player class (which inherits from creature)
# which defaults to having a smiley face as the character and 10 for the health
class Player(Creature):

    def __init__(self, location_x, location_y):
        super().__init__(location_x, location_y, '☺', random.randint(6,10), 5) # invoking the parent class's initializer

    def __str__(self):
        return f"Health:{super().get_health()}"

    def __repr__(self):
        return self.__str__()

# enemy class (which inherits from creature)
# which defaults to having a squiggley as the character and 4 for the health
class Enemy(Creature):

    def __init__(self, location_x, location_y):
        super().__init__(location_x, location_y, '§', random.randint(1,4), 3) # invoking the parent class's initializer

    def __str__(self):
        return f"Health:{super().get_health()}"
    
    def __repr__(self):
        return self.__str__()
    

# board class which represents the board
class Board:

    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        self.grid = [] # list of lists of strings
        self.__creatures = []

        for i in range(self.get_height()):
            row = []
            for j in range(self.get_width()):
                row.append(' ')
            self.grid.append(row)
    
    def add_creature(self, creature):
        self.__creatures.append(creature)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def print_board(self):
        print('  j ', end='')
        for j in range(self.get_width()):
            print(j, end=' ')
        print()
        print('i  ' + '-'*self.get_width()*2)
        # loop over the rows
        for i in range(self.get_height()):
            print(str(i) + ' |', end=' ')
            # loop over the columns
            for j in range(self.get_width()):
                # find out if there's a creature at the given location
                # if there is, print out its character
                # if there isn't, print out a space
                for creature in self.__creatures:
                    if i == creature.location_x and j == creature.location_y and creature.get_health() > 0:
                        print(creature.character, end=' ')
                        break
                else:
                    print(self.grid[i][j], end=' ')  # otherwise print the board square
            print('|')
        print('   ' + '-'*self.get_width()*2)



# class BoardLocation(Board):

#     def get_random_location():
#         x = random(super.get_width())
#         y = random(super.get_height())
#         if()
        




def main():
    # REPL
    board = Board(10, 10)
    player = Player(2, 2)
    board.add_creature(player)
    enemy1 = Enemy(5, 6)
    board.add_creature(enemy1)
    enemy2 = Enemy(1, 3)
    board.add_creature(enemy2)
    enemy3 = Enemy(0, 0)
    board.add_creature(enemy3)
    enemies = [enemy1, enemy2, enemy3]
    gi = GameIntro()
    while True:
        board.print_board()
        print(f"enemies: {enemies}")
        print(f"player: {player}")
        print("Commands: q or quit, l or left, r or right, u or up, d or down")
        command = input('what is your command?')  # get the command from the user
        tmp_location_x = 0
        tmp_location_y = 0
        move_allowed = False
        if command in ['q', 'quit', 'l', 'left', 'r', 'right', 'u', 'up', 'd', 'down']:
            if command in ['q', 'quit']:
                break  # exit the game
            elif command in ['l', 'left']:
                tmp_location_y = -1  # move left
            elif command in ['r', 'right']:
                tmp_location_y = 1  # move right
            elif command in ['u', 'up']:
                tmp_location_x = -1  # move up
            elif command in ['d', 'down']:
                tmp_location_x = 1  # move down
            
            # does the player overlap with any enemy?
            for i in range(len(enemies)):
                enemy = enemies[i]
                if player.get_health() <= 0:
                    print("game over!!!")
                    break
                elif (player.location_x + tmp_location_x) == enemy.location_x and (player.location_y + tmp_location_y) == enemy.location_y:
                    print("attack")
                    enemy.damage(player.attack())
                    if(enemy.get_health() > 0):
                        move_allowed = False
                        print("being attacked")
                        player.damage(enemy.attack())
                        print(f"Player Health: {player.get_health()}")
                    else:
                        move_allowed = True
                    break
                else:
                    print("do nothing")
                    move_allowed = True
            
            if move_allowed:
                print("moving")
                move_allowed = False
                player.location_x += tmp_location_x
                player.location_y += tmp_location_y


main()
