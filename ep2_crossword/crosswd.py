import numpy as np


def get_grid_possibilities_with_next_word(grid_state, word_array, remaining_grid_possibilities):
    """Computes possible grids for a given original grid state and word

        Args:
            grid_state (char array): Defines the initial content of the grid
            word_array (char array): The word to add in the grid
            remaining_grid_possibilities (dict): A dictionary of free word positions in the grid

        Returns:
            next_step_options ([char array, dict]): A list containing couples of new grid state with the word
            in it and remaining free word position for the given grid
    """

    next_step_options = []
    # Length of current word to fit
    word_len = len(word_array)
    # Filter of possible ways to write word in grid, based on size only
    good_len_pos = remaining_grid_possibilities[word_len]

    # Loop through all word possibilities
    for current_key in good_len_pos.keys():
        for possible_pos in good_len_pos[current_key]:
            # Does the word fit?
            grid_state_at_chosen_position = grid_state[possible_pos]
            test_word_fit = word_can_fit_check(grid_state_at_chosen_position, word_array)
            # If word fit, return grid with updated word and updated list of grid remaining possibilities
            if test_word_fit:
                # update grid
                grid_state_with_word = grid_state.copy()
                grid_state_with_word[possible_pos] = word_array
                # update possible positions
                remaining_grid_possition_good_len = good_len_pos.copy()
                remaining_grid_possibilities_with_word = remaining_grid_possibilities.copy()
                del remaining_grid_possition_good_len[current_key]
                remaining_grid_possibilities_with_word[word_len] = remaining_grid_possition_good_len
                # Add the possibility to the next step option
                next_step_options.append([grid_state_with_word, remaining_grid_possibilities_with_word])
    return next_step_options


def word_can_fit_check(local_grid_state, word_array):
    """Checks if a word fits at a given grid position

        Args:
            local_grid_state (char array): Value of the grid at the position the word is being checked
            word_array (char array): The word to add in the grid

        Returns:
            test_global (bool): Can the word fit? True for success, False otherwise.
    """

    # For each letter, it is compatible with the grid if the same letter is already in the grid
    # or if the grid is empty '#' at this position.
    test_by_char = (local_grid_state == '#') | (local_grid_state == word_array)
    test_global = np.all(test_by_char)
    return test_global


def solve_grid(grid_state, words_to_place, dict_grid_possibilities, word_id):
    """Recursive function called to solve the grid

            Args:
                grid_state (char array): Initial content of the grid
                words_to_place (string array): List of words to be placed in the grid
                dict_grid_possibilities (dict): Available free position in the current grid state
                word_id (int): Index number of the current word to be placed

            Returns:
                None
    """

    # Get all feasible grid configurations with the current word being placed
    all_current_pos = get_grid_possibilities_with_next_word(grid_state,
                                                            list(words_to_place[word_id]),
                                                            dict_grid_possibilities)
    # If no feasible configurations exist, return 0
    if len(all_current_pos) == 0:
        return 0
    # If possible configurations exist, then:
    else:
        # If the word is the last word to place. Print the completed grid. Display a happy message.
        if word_id == (len(words_to_place)-1):
            print('VICTORY')
            print(all_current_pos[0][0])
            return 0
        # If the word is not the last one to place; for all possibilities to place it, make a recursive call
        # to the solve_grid function.
        else:
            for checked_pos in all_current_pos:
                # This print allows rough estimation of the solving speed
                if word_id == 0:
                    print('TIC')
                solve_grid(checked_pos[0], words_to_place, checked_pos[1], word_id+1)


if __name__ == '__main__':
    # Initializes the grid as empty
    defGrid = np.array(list('#'*(9*13)))
    # Defines words positions in the grid
    grid_configuration = {4: {0: [[0, 1, 2, 3], [3, 2, 1, 0]],
                              1: [[27, 28, 29, 30], [30, 29, 28, 27]],
                              2: [[45, 46, 47, 48], [48, 47, 46, 45]],
                              3: [[68, 69, 70, 71], [71, 70, 69, 68]],
                              4: [[86, 87, 88, 89], [89, 88, 87, 86]],
                              5: [[113, 114, 115, 116], [116, 115, 114, 113]],
                              6: [[0, 9, 18, 27], [27, 18, 9, 0]],
                              7: [[45, 54, 63, 72], [72, 63, 54, 45]],
                              8: [[29, 38, 47, 56], [56, 47, 38, 29]],
                              9: [[3, 12, 21, 30], [30, 21, 12, 3]],
                              10: [[86, 95, 104, 113], [113, 104, 95, 86]],
                              11: [[60, 69, 78, 87], [87, 78, 69, 60]],
                              12: [[44, 53, 62, 71], [71, 62, 53, 44]],
                              13: [[89, 98, 107, 116], [116, 107, 98, 89]]
                             },
                          5: {14: [[12, 13, 14, 15, 16], [16, 15, 14, 13, 12]],
                              15: [[40, 41, 42, 43, 44], [44, 43, 42, 41, 40]],
                              16: [[56, 57, 58, 59, 60], [60, 59, 58, 57, 56]],
                              17: [[72, 73, 74, 75, 76], [76, 75, 74, 73, 72]],
                              18: [[100, 101, 102, 103, 104], [104, 103, 102, 101, 100]],
                              19: [[73, 82, 91, 100, 109], [109, 100, 91, 82, 73]],
                              20: [[48, 57, 66, 75, 84], [84, 75, 66, 57, 48]],
                              21: [[32, 41, 50, 59, 68], [68, 59, 50, 41, 32]],
                              22: [[7, 16, 25, 34, 43], [43, 34, 25, 16, 7]]
                              }
                          }
    # Defines words to place in the grid
    word_list = ['ABLE', 'AXIS', 'CALF', 'EVEN', 'LAWN', 'PAIR', 'PILL', 'TIDY', 'TUBA', 'TURF', 'ZEST', 'ZINC',
                 'BHAJI', 'CIVIL', 'EQUAL', 'IRISH', 'MANIC', 'QUICK', 'SITAR', 'YACHT']

    # Solve for the grid
    solve_grid(defGrid, word_list, grid_configuration, 0)
