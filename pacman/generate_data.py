from pacman import *
import pacman
import layouts
import math
import textDisplay
import os
from ghostAgents import *

board_sizes = [(8,4),(9,5),(10,6),(11,7),(12,8),(13,9),(14,10)]
weight_combos=[(10,10), (1,1), (math.sqrt(2),math.sqrt(2)), (3,3), (1,10),
                (math.sqrt(2),math.sqrt(1.5)) ,(math.sqrt(1.5),math.sqrt(2)) ]

Astar = False
Astar13by9A = False
Astar13by9B = False
Astar13by9C = False
Astar14by10A = False
Astar14by10B = False
Astar14by10C = False
WAstar = False
IMHA = False
SMHA = False

######################
######   ASTAR  ######
######################

if Astar:
    board_size_counter = 1
    idx = 0
    for board in sorted(os.listdir("layouts")):
        if board == ".DS_Store":
            continue
        print("\n"+"#"*(len(board)+8))
        print("### " + board + " ###")

        if board_size_counter == 1:
            results_file = open("pacman_results_file.txt", "a")
            results_file.write("Astar"+str(board_sizes[idx])+"\n")
            results_file.close()
        board_size_counter += 1
        if board_size_counter == 4:
            idx+=1
            board_size_counter = 1

        pacman.runGames(layout.getLayout(board),AStarFoodSearchAgent(), RandomGhost(0), textDisplay.PacmanGraphics(),1,False)
        if idx == 5: # does not run Astar for 13x9 and 14x10, they are too long
            break
if Astar13by9A:
    pacman.runGames(layout.getLayout("F1allfoodsearch13x9.lay"), AStarFoodSearchAgent(), RandomGhost(0), textDisplay.PacmanGraphics(), 1,
                    False)
if Astar13by9B:
    print("Astar 13x9 Layout B")
    pacman.runGames(layout.getLayout("F2allfoodsearch13x9two.lay"), AStarFoodSearchAgent(), RandomGhost(0), textDisplay.PacmanGraphics(), 1,
                    False)
if Astar13by9C:
    print("Astar 13x9 layout C")
    pacman.runGames(layout.getLayout("F3allfoodsearch13x9three.lay"), AStarFoodSearchAgent(), RandomGhost(0), textDisplay.PacmanGraphics(), 1,
                    False)
if Astar14by10A:
    print("Astar 14x10 layout A")
    pacman.runGames(layout.getLayout("G1allfoodsearch14x10.lay"), AStarFoodSearchAgent(), RandomGhost(0), textDisplay.PacmanGraphics(), 1,
                    False)
if Astar14by10B:
    print("Astar 14x10 layout B")
    pacman.runGames(layout.getLayout("G2allfoodsearch14x10two.lay"), AStarFoodSearchAgent(), RandomGhost(0), textDisplay.PacmanGraphics(), 1,
                    False)
if Astar14by10C:
    print("Astar 14x10 layout C")
    pacman.runGames(layout.getLayout("G3allfoodsearch14x10three.lay"), AStarFoodSearchAgent(), RandomGhost(0), textDisplay.PacmanGraphics(), 1,
                    False)

######################
######  WASTAR  ######
######################

if WAstar:
    board_size_counter = 1
    idx = 0
    for w1, w2 in weight_combos:
        if (w1 == w2) and (w2 == 1):
            continue
        if (w1==w2) and (w2==10):
            continue
        print("Weight Combo: ", w1, ", ", w2)
        for board in sorted(os.listdir("layouts")):
            if board == ".DS_Store":
                continue
            print("#"*(len(board)+8))
            print("### " + board + " ###")

            if board_size_counter == 1:
                results_file = open("pacman_results_file.txt", "a")
                results_file.write("WAstar," + str(board_sizes[idx])+",w1="+str(w1) +",w2="+str(w2)+",w="+str(w1*w2)+"\n")
                results_file.close()
            board_size_counter += 1
            if board_size_counter == 4:
                idx += 1
                board_size_counter = 1

            pacman.runGames(layout.getLayout(board),WAStarFoodSearchAgent(w1*w2), RandomGhost(0), textDisplay.PacmanGraphics(),1,False)
        idx = 0


######################
###### IMHASTAR ######
######################

if IMHA:
    board_size_counter = 1
    idx = 0
    for w1, w2 in weight_combos:
        print("Weight Combo: ", w1, ", ", w2)
        for board in sorted(os.listdir("layouts")):
            if board == ".DS_Store":
                continue
            print("#" * (len(board) + 8))
            print("### " + board + " ###")

            if board_size_counter == 1:
                results_file = open("pacman_results_file.txt", "a")
                results_file.write("IMHAstar," + str(board_sizes[idx])+",w1="+str(w1) +",w2="+str(w2)+",w="+str(w1*w2)+"\n")
                results_file.close()
            board_size_counter += 1
            if board_size_counter == 4:
                idx += 1
                board_size_counter = 1

            pacman.runGames(layout.getLayout(board), IMHAStarFoodSearchAgent(w1,w2), RandomGhost(0),
                            textDisplay.PacmanGraphics(), 1, False)
        idx = 0


######################
###### SMHASTAR ######
######################

if SMHA:
    board_size_counter = 1
    idx = 0
    for w1, w2 in weight_combos:
        print("Weight Combo: ", w1, ", ", w2)
        for board in sorted(os.listdir("layouts")):
            if board == ".DS_Store":
                continue
            print("#" * (len(board) + 8))
            print("### " + board + " ###")

            if board_size_counter == 1:
                results_file = open("pacman_results_file.txt", "a")
                results_file.write("SMHAstar," + str(board_sizes[idx])+",w1="+str(w1) +",w2="+str(w2)+",w="+str(w1*w2)+"\n")
                results_file.close()
            board_size_counter += 1
            if board_size_counter == 4:
                idx += 1
                board_size_counter = 1

            pacman.runGames(layout.getLayout(board), SMHAStarFoodSearchAgent(w1, w2), RandomGhost(0),
                            textDisplay.PacmanGraphics(), 1, False)
        idx = 0

