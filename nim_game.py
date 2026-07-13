#!/usr/bin/env python
# -*-coding: utf-8-*-

# ========================================================
#                       methods
# ========================================================

def turn_finished():
    global is_turn_finished
    # turn  doesn't finish if number_of_remaining_matches not equal to 0
    if number_of_remaining_matches != 0:
        is_turn_finished = False


def turn_of_the_gamer(total_count_of_matches_after_turn):
    global matches_to_remove, matches, is_turn_finished

    if not is_turn_finished:  # tant que le tour n'est pas fini
        matches_to_remove = int(input(MESSAGE))

        # tant que les allumettes ne sont pas entre 1 et 4 à être choisies
        while not (1 <= matches_to_remove <= 4):
            matches_to_remove = int(input(MESSAGE))

        # calcul du nombre d'allumettes restantes
        total_count_of_matches_after_turn = total_count_of_matches_after_turn - matches_to_remove
        print(f"There are {total_count_of_matches_after_turn} matches left.")
        is_turn_finished = True
        return total_count_of_matches_after_turn
    return total_count_of_matches_after_turn


def check_matches_to_remove_under_number_of_remaining_matches():
    global matches_to_remove
    while matches_to_remove > number_of_remaining_matches:
        print("You cannot remove more matches than there are.")
        matches_to_remove = int(input(MESSAGE))


def game_is_finished():
    global is_game_finished
    if number_of_remaining_matches == 0:
        print("You lose")
        is_game_finished = True
        return is_game_finished
    else:
        is_game_finished = False
        return is_game_finished


# ========================================================
#                         main
# ========================================================
if __name__ == '__main__':

    is_game_finished = False
    is_turn_finished = False
    matches_to_remove = 0
    matches = 21
    number_of_remaining_matches = matches
    MESSAGE = "Which matches do you want to remove?"
    last_match = False

    print("Welcome to NIM Game")
    gamer1_name = input("Gamer1 :Enter your name: ")
    gamer2_name = input("Gamer2 :Enter your name: ")
    gamer_start = input("who start the game ? (your name)")

    while not is_game_finished:  # tant que la partie n'est pas terminé
        if gamer_start == gamer1_name:  # si le nom du joueur est celui qui commence
            # tour du joueur 1
            turn_finished()
            print("Player 1's turn")
            number_of_remaining_matches = turn_of_the_gamer(number_of_remaining_matches)
            check_matches_to_remove_under_number_of_remaining_matches()
            is_game_finished = game_is_finished()
            gamer_start = gamer2_name

        else:
            if gamer_start == gamer2_name:  # tour du joueur 2
                print("Player 2's turn")
                turn_finished()
                number_of_remaining_matches = turn_of_the_gamer(number_of_remaining_matches)
                check_matches_to_remove_under_number_of_remaining_matches()
                is_game_finished = game_is_finished()
                gamer_start = gamer1_name

    print("Thanks for playing.")
