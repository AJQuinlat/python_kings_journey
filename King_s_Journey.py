import os
import random
import time
import copy

def startScreen():
    print(
    '''
♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚
♚                                                          █╗             ♔
♔  ====================================================== ███╗ ========== ♚
♚                                                         ╚█╔╝            ♔
♔        ██╗  ██╗██╗███╗   ██╗ ██████╗  █╗███████╗  ████╗██ ██╗████╗      ♚
♚        ██║ ██╔╝██║████╗  ██║██╔════╝ ██║██╔════╝ █║║║║█║║█║║█║║║║█╗     ♔
♔        █████╔╝ ██║██╔██╗ ██║██║  ███╗╚═╝███████╗ ╚█║║║║█║█║█║║║║█╔╝     ♚
♚        ██╔═██╗ ██║██║╚██╗██║██║   ██║   ╚════██║  ╚█║║██║█║██║║█╔╝      ♔
♔        ██║  ██╗██║██║ ╚████║╚██████╔╝   ███████║  ███████████████╗      ♚
♚        ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚══════╝  ╚══════════════╝      ♔
♔         ██╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗███████╗██╗   ██╗        ♚
♚         ██║██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝╚██╗ ██╔╝        ♔
♔         ██║██║   ██║██║   ██║██████╔╝██╔██╗ ██║█████╗   ╚████╔╝         ♚
♚    ██   ██║██║   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══╝    ╚██╔╝          ♔
♔    ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║███████╗   ██║           ♚
♚     ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝           ♔
♔  ====================================================================== ♚
♚                                                                         ♔ 
♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚ ♔ ♚
    ''')

def congratulations():
    print('''
    ██╗    ██╗███████╗██╗     ██╗         ██████╗  ██████╗ ███╗   ██╗███████╗██╗
    ██║    ██║██╔════╝██║     ██║         ██╔══██╗██╔═══██╗████╗  ██║██╔════╝██║
    ██║ █╗ ██║█████╗  ██║     ██║         ██║  ██║██║   ██║██╔██╗ ██║█████╗  ██║
    ██║███╗██║██╔══╝  ██║     ██║         ██║  ██║██║   ██║██║╚██╗██║██╔══╝  ╚═╝
    ╚███╔███╔╝███████╗███████╗███████╗    ██████╔╝╚██████╔╝██║ ╚████║███████╗██╗
     ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝ 
    ''')

def clear():
    os.system('cls')

def new_game(load_file):
    game_state = []
    game_file = open(load_file, "r", encoding='utf-8')
    for line in game_file:
        data = line.split(",")
        game_state.append(data)
    
    game_file.close()

    return game_state

def load_game(load_file):
    game_state = []
    game_file = open(load_file, "r", encoding='utf-8')
    for line in game_file:
        data = line.split(",")
        game_state.append(data)
    
    game_file.close()
    
    move_count = int(game_state.pop()[0])
    king = game_state.pop()
    moves = []

    for i in king:
        i = i.replace("[","").replace("]","").replace(" ","")
        moves.append(str(i))
    king = []
    moves.pop()
    for index,value in enumerate(moves):
        if index % 2 == 0:
            king.append([str(value), str(moves[index+1])])

    return game_state,king,move_count     

def save_game(current_game, file_name):
    fileHandle = open(file_name,"w")
    for row in current_game:
        for column in row:
            if column != row[-1]:
                fileHandle.write(column + ",")
            else:
                fileHandle.write(column)
    fileHandle.write("\n")
    for i in king:
        fileHandle.write(str(i) + ",")
    fileHandle.write("\n")
    fileHandle.write(str(move_count))

    fileHandle.close()

def move(king_x,king_y,player_x,player_y):
    x,y=0,0
    x = king_x+player_x
    y = king_y+player_y
    if x >= 0 and x <= 6 and y >= 0 and y <= 6:
        global move_count
        move_count+=1 
        if move_count < 10:
            move = "0" + str(move_count)
        elif move_count >= 10:
            move = str(move_count)
        
        current_game[x][y] = move
        if current_game[x][y] == board1[x][y]:  
            return [x,y]
        else:
            current_game[x][y] = backup[x][y]
            return [11,11]

    else:
        print("[Invalid move!]")
        king.pop()
        time.sleep(1)

def move_translate(player_action):
    if player_action == "a":
        return -1,0
    elif player_action == "b":
        return -1,1
    elif player_action == "c":
        return 0,1
    elif player_action == "d":
        return 1,1
    elif player_action == "e":
        return 1,0
    elif player_action == "f":
        return 1,-1
    elif player_action == "g":
        return 0,-1
    elif player_action == "h":
        return -1,-1

def king_position():
    if move_count < 10:
        move = "0" + str(move_count)
    elif move_count >= 10:
        move = str(move_count)
    
    if len(king) > 0:
        for i in current_game:
            for index, value in enumerate(i):
                if value == move:
                    king.append([current_game.index(i),index])
                    x,y = king[move_count-1][0],king[move_count-1][1]
                    
    if len(king) == 0: 
        for i in current_game:
            for index, value in enumerate(i):
                if value == "01":
                    king.append([current_game.index(i),index])
                    x,y = king[move_count-1][0],king[move_count-1][1]
                    
    return [x,y]


def make_board(board):
    for i in board1:
        for index, value in enumerate(i):
            if value == "01" or value =="49":
                player_board[board1.index(i)][index] = board1[board1.index(i)][index]

    for i in range(random.randint(18,20)):
        x,y = random.randint(0,6), random.randint(0,6)
        player_board[x][y] = board1[x][y]
    
    return board

def undo_move():
    global king
    global move_count
    king_position()
    if move_count > 1:
        if len(king) > 0:
            last = king[-1]
            king.remove(king[-1])
            king.remove(king[-1])
            current_game[last[0]][last[1]] = backup[last[0]][last[1]]
            move_count-=1
            clear()
            display()
    elif move_count == 1:
        king.clear()
        print("[Can't Undo Anymore]")
        time.sleep(1)
    else:
        print("[Can't Undo Anymore]")
        time.sleep(1)

def display():
    clear()
    print("\n\n                       K I N G ' S   J O U R N E Y\n           ==================================================")
    for i in current_game:
        if i[0] == "00":
            print("           |      |", end="")
        else:
            print("           |  " + str(i[0]) + "  |", end="")
        for j in range(1,7):
            if i[j] == "00":
                print("      |", end="")
            else:
                print("  " + str(i[j]) + "  |", end="")
        print("\n           ==================================================")
    
    print('''           ||                                              ||
           ||      h.) ⇖         a.) ⇑         b.) ⇗       ||
           ||      g.) ⇐                       c.) ⇒       ||
           ||      f.) ⇙         e.) ⇓         d.) ⇘       ||
           ||                                              ||          ''')  
    print("           ==================================================")
    print("           u.) Undo Move | s.) Save Game | q.) Quit Game")
    print("           ==================================================")
    print("\n                   Move Count: " + str(move_count) + "            ", end="")

def game_over():
    clear()
    decision = input('''
             ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .           ▌ ▐·▄▄▄ .▄▄▄  
            ▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▪     ▪█·█▌▀▄.▀·▀▄ █·
            ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ 
            ▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌
            ·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀      ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀
    
                                Continue? 
                                [1]Yes
                                [0]No
        
                   ''')

    return decision

def recap():
    global move_count
    global current_game
    global backup
    current_game=backup.copy()
    for k in range(50):
        if k < 10:
            sq = "0" + str(k)
        elif k >= 10:
            sq = str(k)

        for i in board1:
            for index,value in enumerate(i):
                if value == sq:
                    clear()
                    current_game[board1.index(i)][index] = board1[board1.index(i)][index]
                    display()
                    time.sleep(0.75)
    move_count=0
    king.clear()

def play_game():
    clear()
    global current_game
    while True:
        display()
        player_action = input("Move: ").lower()
        if player_action == 'q':
            global move_count
            move_count = 1
            king.clear()
            clear()
            break
        elif player_action == 's':
            save_game(current_game,input("Save File Name: "))
            clear()
        elif player_action == 'u':
            undo_move()
        else:
            if player_action in choices:
                kingp = king_position()
                player = move_translate(player_action)
                state = move(kingp[0],kingp[1],player[0],player[1])
                if state == [11,11]:
                    decision = game_over()
                    if decision == "1":
                        clear()
                        move_count-=1 
                        king.pop()
                    else:
                        recap()
                        for i in range(5,0,-1):
                            print(i,end="-")
                            time.sleep(1)
                        print("\n\n                 [Thank You For Playing!]")
                        time.sleep(1.5)
                        break
            else:
                print("[Please enter a valid action!]")
                time.sleep(1)
                clear()
                display()

        if move_count==49:
            congratulations()
            time.sleep(3)
            current_game.clear() 
            current_game = backup
            recap()
            print("\n\n                 [Thank You For Playing!]")
            time.sleep(1.5)
            break
    
board1 = [["43","44","49","35","34","05","04"],
          ["42","45","36","48","33","06","03"],
          ["41","37","46","47","32","02","07"],
          ["40","39","38","31","01","09","08"],
          ["25","26","30","29","11","10","14"],
          ["24","22","27","28","12","13","15"],
          ["23","21","20","19","18","17","16"]]

choices = ("a","b","c","d","e","f","g","h")
king = []
current_game = []
move_count = 1
while True:
    clear()
    startScreen()
    start = input(
    '''
                                [1] New Game
                                [2] Load Game
                                [0] Quit
                                ''')
    if start == "0":
        print("\n                           [Thank You For Playing!]")
        time.sleep(1.5)
        clear()
        break
    elif start == "1":
        player_board = new_game('new_game.txt')
        current_game = make_board(player_board)
        backup = copy.deepcopy(current_game)
        play_game()
        break
    elif start == "2":
        try:
            player_board,king,move_count = load_game(input("\n                     Please enter the file to use: "))
            current_game = player_board
            backup = copy.deepcopy(current_game)
            play_game()
            break
        except FileNotFoundError:
            print("\n                           [File Non-existent!]")
            time.sleep(1)
            continue
        else:
            break
    else:
        print("\n                           [Please enter valid action!]")
        time.sleep(1)

