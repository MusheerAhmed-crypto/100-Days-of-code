# # # states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
# # #                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
# # #                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
# # #                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
# # #                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
# # #                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
# # #                      "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # # # Using len() to find the number of items in a List
# # # num_states = len(states_of_america)
# # # print(states_of_america[num_states - 1])


# # # # dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
# # # # "Tomatoes", "Celery", "Potatoes"]

# # # fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# # # vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# # # dirty_dozen = [fruits, vegetables]
# # # print(dirty_dozen)

# # import random

# # rock = '''    _______
# # ---'   ____)
# #       (_____)
# #       (_____)
# #       (____)
# # ---.__(___)'''
# # paper = '''   _______
# # ---'   ____)____
# #           ______)
# #           _______)
# #          _______)
# # ---.__________)'''
# # scissors = '''   _______
# # ---'   ____)____
# #           ______)
# #        __________)
# #       (____)
# # ---.__(___)0'''

# # game_images = [rock, paper, scissors]

# # user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# # if user_choice < 0 or user_choice > 2:
# #     print("Invalid choice!")
# # else:
# #     computer_choice = random.randint(0, 2)

# #     print("You chose:")
# #     print(game_images[user_choice])

# #     print("Computer chose:")
# #     print(game_images[computer_choice])

# #     if user_choice == computer_choice:
# #         print("It's a draw!")
# #     elif user_choice == 0 and computer_choice == 2:
# #         print("You win!")
# #     elif user_choice == 2 and computer_choice == 0:
# #         print("You lose!")
# #     elif user_choice > computer_choice:
# #         print("You win!")
# #     else:
# #         print("You lose!")

# fruits = ["apple", "banana", "orange", "mango", "grapes", "pineapple"]
# vegetables = ["carrot", "potato", "tomato", "onion", "cabbage", "spinach"]
# grocessry_list = [fruits, vegetables]
# print(grocessry_list)
