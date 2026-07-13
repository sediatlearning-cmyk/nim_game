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


def calculate_number_of_matches_by_turn(removes_matches: int, total_count_of_matches_after_turn):
    global is_turn_finished
    # calcul du nombre d'allumettes restantes
    total_count_of_matches_after_turn = total_count_of_matches_after_turn - removes_matches
    print(f"There are {total_count_of_matches_after_turn} matches left.")
    if total_count_of_matches_after_turn < 0:
        is_turn_finished = True
        return total_count_of_matches_after_turn
    return total_count_of_matches_after_turn


def turn_of_the_gamer(total_count_of_matches_after_turn):
    global matches_to_remove, matches, is_turn_finished

    if not is_turn_finished:  # tant que le tour n'est pas fini
        matches_to_remove = int(input(MESSAGE))

        # tant que les allumettes ne sont pas entre 1 et 4 à être choisies
        while not (1 <= matches_to_remove <= 4):
            matches_to_remove = int(input(MESSAGE))

        total_count_of_matches_after_turn = (
            calculate_number_of_matches_by_turn(
                matches_to_remove,
                total_count_of_matches_after_turn))
        return total_count_of_matches_after_turn
    return total_count_of_matches_after_turn


def check_matches_to_remove_under_number_of_remaining_matches(total_count_of_matches_after_turn):
    global matches_to_remove
    number_of_matches_to_remain = total_count_of_matches_after_turn
    if matches_to_remove > total_count_of_matches_after_turn:
        print("The only digit you could write is 1, so:")
        if 2 <= matches_to_remove <= 3:
            matches_to_remove = int(input(MESSAGE))
            number_of_matches_to_remain = calculate_number_of_matches_by_turn(
             matches_to_remove,
             total_count_of_matches_after_turn)

        if 0 >= number_of_matches_to_remain >= 1:
            print("The game is finished")
            game_is_finished()


def game_is_finished():
    global is_game_finished
    if number_of_remaining_matches <= 1:
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
    gamer1_name = input("Gamer1 : Enter your name: ")
    gamer2_name = input("Gamer2 : Enter your name: ")
    gamer_start = input("Who start the game ? (your name) : ")

    while not is_game_finished:  # tant que la partie n'est pas terminé
        if gamer_start == gamer1_name:  # si le nom du joueur est égal à celui qui commence
            # tour du joueur 1
            turn_finished()
            print(f"Player {gamer1_name}, it's your turn")
            number_of_remaining_matches = turn_of_the_gamer(number_of_remaining_matches)
            check_matches_to_remove_under_number_of_remaining_matches(number_of_remaining_matches)
            is_game_finished = game_is_finished()
            gamer_start = gamer2_name

        else:
            if gamer_start == gamer2_name:  # tour du joueur 2
                print(f"Player {gamer2_name}, it's your turn")
                turn_finished()
                number_of_remaining_matches = turn_of_the_gamer(number_of_remaining_matches)
                check_matches_to_remove_under_number_of_remaining_matches(number_of_remaining_matches)
                is_game_finished = game_is_finished()
                gamer_start = gamer1_name

    print("Thanks for playing.")
