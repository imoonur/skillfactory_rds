"""
    SkillFactory RDS Project 0

    Guess the number game.
    The computer makes an integer from 1 to 100,
    and we need to guess it in the minimum number of attempts. """

BOUND1 = 1  # lower bound number
BOUND2 = 100  # upper bound number

import numpy as np


def game_core_v1(number):
    """
        Just guess at random, without using information about more or less.
        The function takes the requested number
        and returns the number of attempts. """
    count = 0
    while True:
        count += 1
        predict = np.random.randint(BOUND1, BOUND2 + 1)  # estimated number
        if number == predict:
            return count  # exit, if you guessed right


def game_core_v2(number):
    """
        First set any random number, and then decrease or increase it,
        depending on whether it is more or less than what is needed.
        The function takes the requested number and returns the number tried."""
    count = 1
    predict = np.random.randint(BOUND1, BOUND2 + 1)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # exit, if you guessed right


def game_core_v3(number):
    """Use the half division method."""
    count = 1
    bound1, bound2 = BOUND1, BOUND2
    predict = bound1 + ((bound2 - bound1) // 2)
    while number != predict:
        count += 1
        if number > predict:
            bound1 = predict + 1
            predict = bound1 + ((bound2 - bound1) // 2)
        elif number < predict:
            bound2 = predict - 1
            predict = bound1 + ((bound2 - bound1) // 2)
    return count  # exit, if you guessed right


def score_game(game_core):
    """
        Start the game 1000 times to find out
        how quickly the game guesses the number."""
    count_ls = []
    np.random.seed(1)  # fix RANDOM SEED, so that your experiment is reproducible!
    random_array = np.random.randint(BOUND1, BOUND2 + 1, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм {game_core.__name__} угадывает число в среднем '
          f'за {score} попыток')
    return score


# Check
score_game(game_core_v1)
score_game(game_core_v2)
score_game(game_core_v3)
