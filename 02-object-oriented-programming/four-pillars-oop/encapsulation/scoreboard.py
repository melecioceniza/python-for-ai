# Challenge: Encapsulation

# Instruction
# Create a class ScoreBoard
# Add an __init__ with a score parameter and store it as a private attribute
# Add a methoed called get_score that returns the private score
# Create an object s1 with a score of 0
# Print the score of s1


# Start here
# Create the scoreboard class
class ScoreBoard:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


# Create an object
scoreboard = ScoreBoard(99)

# Print the score
print(scoreboard.get_score())
