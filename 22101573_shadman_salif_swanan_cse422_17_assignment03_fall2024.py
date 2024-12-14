# -*- coding: utf-8 -*-
"""22101573_Shadman Salif Swanan_CSE422_17_Assignment03_Fall2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cO61ydbAle0VU9M576tidq_WX9yV0rBN

# **PART 1**
"""

MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, isMaximizingPlayer, scores, alpha, beta):
    if depth == 5:
        return scores[nodeIndex]

    if isMaximizingPlayer:
        best = MIN
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, scores, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, scores, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


starting_player = int(input('Enter Starting Player: ').strip())


rounds = []
current_player = starting_player
scores = [-1, 1] * 16


for _ in range(3):
    result = minimax(0, 0, current_player == 0, scores, MIN, MAX)
    winner = 0 if result == -1 else 1
    rounds.append(winner)
    current_player = 1 - current_player

game_winner = 0 if rounds.count(0) > rounds.count(1) else 1


print(f"Game Winner: {'Scorpion' if game_winner == 0 else 'Sub-Zero'}")
print(f"Total Rounds Played: {len(rounds)}")
for i, winner in enumerate(rounds, 1):
    print(f"Winner of Round {i}: {'Scorpion' if winner == 0 else 'Sub-Zero'}")

"""# **PART 2**"""

leaf_nodes = [3, 6, 2, 3, 7, 1, 2, 0]

def compute_minimax_with_special_power(cost, use_special_power):

    if use_special_power:

        left_tree_value = max(leaf_nodes[0:4]) - cost
        right_tree_value = max(leaf_nodes[4:]) - cost
    else:

        left_subtree_max1 = max(leaf_nodes[0:2])
        left_subtree_max2 = max(leaf_nodes[2:4])
        left_tree_value = min(left_subtree_max1, left_subtree_max2)

        right_subtree_max1 = max(leaf_nodes[4:6])
        right_subtree_max2 = max(leaf_nodes[6:])
        right_tree_value = min(right_subtree_max1, right_subtree_max2)

    return max(left_tree_value, right_tree_value)

def alpha_beta_search(current_depth, is_maximizing, alpha, beta, values, range_start, range_end):


    if current_depth == 3:
        return values[range_start]

    if is_maximizing:
        max_value = float('-inf')
        step = (range_end - range_start) // 2
        for i in range(range_start, range_end, step):
            subtree_value = alpha_beta_search(current_depth + 1, False, alpha, beta, values, i, i + step)
            max_value = max(max_value, subtree_value)
            alpha = max(alpha, subtree_value)
            if beta <= alpha:
                break
        return max_value
    else:
        min_value = float('inf')
        step = (range_end - range_start) // 2
        for i in range(range_start, range_end, step):
            subtree_value = alpha_beta_search(current_depth + 1, True, alpha, beta, values, i, i + step)
            min_value = min(min_value, subtree_value)
            beta = min(beta, subtree_value)
            if beta <= alpha:
                break
        return min_value


power_cost = int(input("Enter the cost of using the special power: "))


value_without_power = alpha_beta_search(0, True, float('-inf'), float('inf'), leaf_nodes, 0, len(leaf_nodes))


value_with_power = compute_minimax_with_special_power(power_cost, True)


if value_with_power > value_without_power:
    best_strategy = "Pacman goes to the right and uses the special power"
else:
    best_strategy = "Pacman does not use the special power"


final_minimax_value = max(value_with_power, value_without_power)
print(f"The new minimax value is {final_minimax_value}. {best_strategy}")