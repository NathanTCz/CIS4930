from __future__ import print_function
import threading
from socket import *
import re
from game import Game
import personnel

def handle_client(c):
    c.send('Enter your character\'s name: ')
    name = c.recv(15)
    name = str(name[:-2])
    c.send('Are you a CodeWarrior or 1337H4x0r? Enter [c] or [h]: ')
    player_class = c.recv(4)

    if player_class[0] == 'c':
        player = personnel.CodeWarrior(name)
    elif player_class[0] == 'h':
        player = personnel.Hax0r(name)

    game = Game(player, c)
    #game.print_grid()
    go_regex = re.compile('go ([A-Z]*)')

    while not game.over:
        c.send('> ')
        choice = c.recv(15)

        if go_regex.match(choice[0:4]):
            m = go_regex.search(choice)
            game.move_player( m.group()[3].lower() )
            game.player.go()
        elif choice[0:4] == 'quit':
            game.player.quit(c)
            game.over = True
        elif choice[0:6] == 'attack':
            game.fight()
        elif choice[0:6] == 'health':
            game.player.health(c)
        elif choice[0:4] == 'help':
            game.player.help(c)

        #game.print_grid()
    c.close()
    return

if __name__ == '__main__':
    socket = socket(AF_INET, SOCK_STREAM)
    socket.bind(('', 9000))
    socket.listen(5)
    print('listening on localhost:9000')
    while True:
        c,a = socket.accept()
        thread = threading.Thread(target=handle_client, args=(c,))
        thread.start()
