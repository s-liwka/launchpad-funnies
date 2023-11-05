import random
import novation_launchpad as launchpad
import time

lp = launchpad.Launchpad()
if lp.Open():
    print("yay")

else:
    print(":(((")
    exit()

lp.Reset()

board_size = 150
board = [None] * board_size
mem_board = [None] * board_size
neighbor_board = [0] * board_size
neighbor_board_mem1 = [0] * board_size
neighbor_board_mem2 = [0] * board_size
#allowed_indexes = [0,1,2,3,4,5,6,7, 8,16,17,18,19,20,21,22,23, 24,32,33,34,35,36,37,38,39, 40,48,49,50,51,52,53,54,55, 56,64,65,66,67,68,69,70,71, 72,80,81,82,83,84,85,86,87, 88,96,97,98,99,100,101,102,103, 104,112,113,114,115,116,117,118,119,120]
allowed_indexes = [0,1,2,3,4,5,6,7,16,17,18,19,20,21,22,23,32,33,34,35,36,37,38,39,48,49,50,51,52,53,54,55,64,65,66,67,68,69,70,71,80,81,82,83,84,85,86,87,96,97,98,99,100,101,102,103,112,113,114,115,116,117,118,119]
def generate_board():
    for i in range(board_size):
        if i in allowed_indexes:
            if random.random() < 0.35:
                board[i] = 1
            else:
                board[i] = 0



def print_board():
    for i in range(board_size):
        if i in allowed_indexes:
            print(board[i], end=' ')
        else:
            pass
        
        if (i + 1) % 16 == 0:
            print()

def print_neighbor_board():
    for i in range(board_size):
        if i in allowed_indexes:
            print(neighbor_board[i], end=' ')
        else:
            pass
        
        if (i + 1) % 16 == 0:
            print()


def display_on_launchpad(display_old=False):
    for i in range(board_size):

        if display_old:
            if mem_board[i] is not None and mem_board[i] != 0:
                lp.LedCtrlRaw(i, 0, 1)
                
        if board[i] is not None and board[i] != 0:
            lp.LedCtrlRaw(i, 3, 0)
        else:
            continue

def check_for_neighbors():
    for i in range(board_size):
        neigbors = 0
        if i in allowed_indexes:
            # S
            try:
                if board[i + 16] == 1:
                    neigbors += 1
            except IndexError:
                pass

            # SE
            try:
                if board[i + 17] == 1:
                    neigbors += 1
            except IndexError:
                pass

            # SW
            try:
                if board[i + 15] == 1:
                    neigbors += 1
            except IndexError:
                pass

            # N
            try:
                if board[i - 16] == 1:
                    neigbors += 1
            except IndexError:
                pass

            # NE
            try:
                if board[i - 15] == 1:
                    neigbors += 1
            except IndexError:
                pass

            # NW
            try:
                if board[i - 17] == 1:
                    neigbors += 1
            except IndexError:
                pass

            # E
            try:
                if board[i + 1] == 1:
                    neigbors += 1
            except IndexError:
                pass

            # W
            try:
                if board[i - 1] == 1:
                    neigbors += 1
            except IndexError:
                pass

            neighbor_board[i] = neigbors


def update_population():
    for i in range(board_size):
        if neighbor_board[i] < 2 and board[i] == 1:
            board[i] = 0
        elif (neighbor_board[i] == 2 or neighbor_board[i] == 3) and board[i] == 1:
            board[i] = 1
        elif neighbor_board[i] > 3 and board[i] == 1:
            board[i] = 0
        elif neighbor_board[i] == 3 and board[i] == 0:
            board[i] = 1

def binary_generation_display(generation):
    generation = [int(bit) for bit in bin(generation)[2:]]
    print(generation)

    try:
        if generation[0] == 1:
            lp.LedCtrlRaw(200, 3, 3)
        elif generation[0] == 0:
            lp.LedCtrlRaw(200, 0, 1)

        if generation[1] == 1:
            lp.LedCtrlRaw(201, 3, 3)
        elif generation[1] == 0:
            lp.LedCtrlRaw(201, 0, 1)

        if generation[2] == 1:
            lp.LedCtrlRaw(202, 3, 3)
        elif generation[2] == 0:
            lp.LedCtrlRaw(202, 0, 1)

        if generation[3] == 1:
            lp.LedCtrlRaw(203, 3, 3)
        elif generation[3] == 0:
            lp.LedCtrlRaw(203, 0, 1)

        if generation[4] == 1:
            lp.LedCtrlRaw(204, 3, 3)
        elif generation[4] == 0:
            lp.LedCtrlRaw(204, 0, 1)

        if generation[5] == 1:
            lp.LedCtrlRaw(205, 3, 3)
        elif generation[5] == 0:
            lp.LedCtrlRaw(205, 0, 1)

        if generation[6] == 1:
            lp.LedCtrlRaw(206, 3, 3)
        elif generation[6] == 0:
            lp.LedCtrlRaw(206, 0, 1)

        if generation[7] == 1:
            lp.LedCtrlRaw(207, 3, 3)
        elif generation[7] == 0:
            lp.LedCtrlRaw(207, 0, 1)

        if generation[8] == 1:
            lp.LedCtrlRaw(8, 3, 3)
        elif generation[8] == 0:
            lp.LedCtrlRaw(8, 0, 1)
        
        if generation[9] == 1:
            lp.LedCtrlRaw(24, 3, 3)
        elif generation[9] == 0:
            lp.LedCtrlRaw(24, 0, 1)

        if generation[10] == 1:
            lp.LedCtrlRaw(40, 3, 3)
        elif generation[10] == 0:
            lp.LedCtrlRaw(40, 0, 1)

        if generation[11] == 1:
            lp.LedCtrlRaw(56, 3, 3)
        elif generation[11] == 0:
            lp.LedCtrlRaw(56, 0, 1)

        if generation[12] == 1:
            lp.LedCtrlRaw(72, 3, 3)
        elif generation[12] == 0:
            lp.LedCtrlRaw(72, 0, 1)
        
        if generation[13] == 1:
            lp.LedCtrlRaw(88, 3, 3)
        elif generation[13] == 0:
            lp.LedCtrlRaw(88, 0, 1)

        if generation[14] == 1:
            lp.LedCtrlRaw(104, 3, 3)
        elif generation[14] == 0:
            lp.LedCtrlRaw(104, 0, 1)

        if generation[15] == 1:
            lp.LedCtrlRaw(120, 3, 3)
        elif generation[15] == 0:
            lp.LedCtrlRaw(120, 0, 1)







    except IndexError:
        return


    

generation = 0
generate_board()
display_old = False
while True:
    try:
        generation += 1
        lp.Reset()
        display_on_launchpad(display_old=False)
        binary_generation_display(generation)
        time.sleep(0.25)

        # Make a copy of the current board
        current_board = board.copy()
        if display_old:
            mem_board = board.copy()

        check_for_neighbors()
        update_population()

        if not 1 in board:
            print(generation)
            lp.Reset()
            lp.LedCtrlRaw(33, 3, 3)
            lp.LedCtrlRaw(38, 3, 3)
            lp.LedCtrlRaw(97, 3, 3)
            lp.LedCtrlRaw(102, 3, 3)
            for i in range(82, 86):
                lp.LedCtrlRaw(i, 3, 3)
            binary_generation_display(generation)

            time.sleep(1)
            lp.Reset()
            generate_board()
            generation = 0

        if current_board == neighbor_board_mem1 or current_board == neighbor_board_mem2:
        #if 0 == 1:
            print(generation)
            lp.Reset()
            lp.LedCtrlRaw(33, 0, 3)
            lp.LedCtrlRaw(38, 0, 3)
            lp.LedCtrlRaw(97, 0, 3)
            lp.LedCtrlRaw(102, 0, 3)
            for i in range(82, 86):
                lp.LedCtrlRaw(i, 0, 3)
            binary_generation_display(generation)

            time.sleep(1)
            lp.Reset()
            generate_board()
            generation = 0

        neighbor_board_mem2 = neighbor_board_mem1.copy()
        neighbor_board_mem1 = current_board

    except KeyboardInterrupt:
        lp.Reset()
        lp.Close()

