

print("-----Welcome To 'The Minion Game'-----")
print("Game Rules")
print("""
1.Both Players are given same string.
2.Both players have to make substrings using the letters of the string.
3.user1 has to make words starting with consonants.
4.user2 has to make words starting with the vowels.
5.The game ends when both players have made all the possible substrings. """)

print()
print("Scoring")
print("""
A player gets +1 point for each occurrence of the substring in the string.""")
user1_score = 0
user2_score = 0
user1 = input("Enter the name of user1:")
user2 = input("Enter the name of user2:")
string = (input("Enter the string:").upper())
print(string)
length = len(string)
for idx, sub in enumerate(string.upper()):
    if sub in ['A', 'E', 'I', 'O', 'U']:
        user1_score += length - idx
    else:
        user2_score += length - idx

if user1_score > user2_score:
    print("user1", user1, user1_score)
elif user1_score < user2_score:
    print("user2", user2, user2_score)
else:
    print("Draw")
