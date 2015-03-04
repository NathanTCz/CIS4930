from __future__ import print_function
import re
from game import Game
import personnel

if __name__ == '__main__':
    name = raw_input('Enter your character\'s name: ')
    player_class = raw_input('Are you a CodeWarrior or 1337H4x0r? Enter [c] or [h]: ')

    if player_class == 'c':
        player = personnel.CodeWarrior(name)
    elif player_class == 'h':
        player = personnel.Hax0r(name)

    game = Game(player)
    game.print_grid()
    go_regex = re.compile('go ([A-Z]*)')

    while not game.over:
        choice = raw_input('> ')

        if go_regex.match(choice):
            m = go_regex.search(choice)
            game.move_player( m.group()[3].lower() )
            game.player.go()
        elif choice == 'quit':
            game.player.quit()
            game.over = True
        elif choice == 'attack':
            game.fight()
        elif choice == 'health':
            game.player.health()
        elif choice == 'help':
            game.player.help()

        game.print_grid()
