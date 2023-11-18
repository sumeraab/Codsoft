# -*- coding: utf-8 -*-
"""Tasks 1,2,4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tbhd8ZOA6OVDghxD58K56ps6I2kpXLBQ
"""

#TASK 1

#Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This will give you a basic understanding of natural language processing and conversation flow.

import random

def sumera_chatbot():
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            responses = ["Hi there!", "Hey, how can I help you!", "Hello! What's on your mind?"]
            print("Bot:", random.choice(responses))

        elif "how are you" in user_input:
            responses = ["I'm just a bot, but I'm doing well. How about you?", "I'm good, thank you. What can I do for you?"]
            print("Bot:", random.choice(responses))

        elif "bye" in user_input:
            responses = ["Goodbye!", "See you later!", "Bye! Have a great day!"]
            print("Bot:", random.choice(responses))
            break

        elif "recommend me something" in user_input or "suggest" in user_input:
            responses = ["Sure! What type of recommendations are you looking for?", "Of course! Movies, books, or something else?"]
            print("Bot:", random.choice(responses))

        elif "thank you" in user_input:
            responses = ["You're welcome!", "Anytime!", "Glad I could help!"]
            print("Bot:", random.choice(responses))

        else:
            responses = ["Sorry, I didn't quite get that.", "I'm not sure I understand. Could you rephrase?", "I'm still learning!"]
            print("Bot:", random.choice(responses))

if __name__ == "__main__":
    print("Bot: Hello! Ask me anything or say 'bye' to exit.")
    sumera_chatbot()

#TASK 2

#Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable. This project will help you understand game theory and basic search algorithms.
import math

def print_board(b):
    for r in b:
        print(" ".join(r))
    print()

def evaluate(b):
    for r in range(3):
        if b[r][0] == b[r][1] == b[r][2] != '-':
            return 10 if b[r][0] == 'X' else -10
    for c in range(3):
        if b[0][c] == b[1][c] == b[2][c] != '-':
            return 10 if b[0][c] == 'X' else -10
    if b[0][0] == b[1][1] == b[2][2] != '-':
        return 10 if b[0][0] == 'X' else -10
    if b[0][2] == b[1][1] == b[2][0] != '-':
        return 10 if b[0][2] == 'X' else -10
    return 0

def is_moves_left(b):
    return any('-' in r for r in b)

def minimax(b, d, is_max):
    score = evaluate(b)

    if score == 10:
        return score - d
    if score == -10:
        return score + d
    if not is_moves_left(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == '-':
                    b[i][j] = 'X'
                    best = max(best, minimax(b, d + 1, not is_max))
                    b[i][j] = '-'
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == '-':
                    b[i][j] = 'O'
                    best = min(best, minimax(b, d + 1, not is_max))
                    b[i][j] = '-'
        return best

def find_best_move(b):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if b[i][j] == '-':
                b[i][j] = 'X'
                move_val = minimax(b, 0, False)
                b[i][j] = '-'

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def play_game():
    b = [['-' for _ in range(3)] for _ in range(3)]
    print("Let's play Tic-Tac-Toe! You are 'O', and I am 'X'.")
    print_board(b)

    while is_moves_left(b):
        h_move = tuple(map(int, input("Enter your move (row and column): ").split()))
        b[h_move[0]][h_move[1]] = 'O'
        print_board(b)

        if evaluate(b) == -10:
            print("You win!")
            return

        if not is_moves_left(b):
            print("It's a draw!")
            return

        print("My turn...")
        a_move = find_best_move(b)
        b[a_move[0]][a_move[1]] = 'X'
        print(f"I placed my 'X' at {a_move}")
        print_board(b)

        if evaluate(b) == 10:
            print("I win!")
            return

if __name__ == "__main__":
    play_game()

#TASK 4

#Create a simple recommendation system that suggests items to users based on their preferences. You can use techniques like collaborative filtering or content-based filtering to recommend movies, books, or products to users.

u_ratings = {'Sumera': {'Heart of stone': 5, 'Gone Girl': 4, 'The Creator': 5},
             'Aina': {'Heart of stone': 4, 'Gone Girl': 5, 'The Conjuring': 4},
             'Reem': {'Gone Girl': 5, 'The Creator': 4, 'The Conjuring': 5},
             'Damia': {'Heart of stone': 5, 'Gone Girl': 4, 'The Conjuring': 5},
             'Ahmed': {'Gone Girl': 5, 'The Creator': 4, 'The Conjuring': 5}}

your_ratings = {'The Conjuring': 4, 'Heart of stone': 5}

similar_users = [u for u, r in u_ratings.items() if set(r.keys()) & set(your_ratings.keys())]

suggested_movies = {}
for u in similar_users:
    for m, rt in u_ratings[u].items():
        if m not in your_ratings:
            suggested_movies[m] = (suggested_movies.get(m, 0) + rt) / 2

sorted_suggestions = sorted(suggested_movies.items(), key=lambda x: x[1], reverse=True)
print("Based on your ratings, you might like:")
for m, rt in sorted_suggestions[:5]:
    print(f"- {m}")