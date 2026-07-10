#!/usr/bin/env python
# -*-coding: utf-8-*-

# ========================================================
#                       methods
# ========================================================
def turn_of_the_gamer():
    global matches_to_remove, matches, is_turn_finished, \
           number_of_remaining_matches

    while not is_turn_finished:  # tant que le tour n'est pas fini
        matches_to_remove = int(input(MESSAGE))

        while not (1 <= matches_to_remove <= 4):    # tant que les allumettes ne sont pas entre 1 et 4
            matches_to_remove = int(input(MESSAGE))

        number_of_remaining_matches = matches - matches_to_remove   # calcul du nombre d'allumettes restantes
        print(f"There are {number_of_remaining_matches} matches left.")
        is_turn_finished = True


# ========================================================
#                         main
# ========================================================
if __name__ == '__main__':

    is_game_finished = False
    is_turn_finished = False
    matches_to_remove = 0
    matches = 21
    number_of_remaining_matches = 0
    MESSAGE = "Which matches do you want to remove?"
    last_match = False
    gamer1_name = input("Gamer1 :Enter your name: ")
    gamer2_name = input("Gamer2 :Enter your name: ")
    gamer_start = input("who start the game ? (your name)")

    print("Welcome to NIM Game")
    while not is_game_finished:  # tant que la partie n'est pas terminé
        if gamer_start == gamer1_name:  # tour du joueur 1
            print("Player 1's turn")
            turn_of_the_gamer()
            








