# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_word1 = 0 # Creating this variable for storing total "TRUE" word characters
total_word2 = 0 # Creating this variable for storing total "LOVE" word characters

#--------------------------------------------------------------------------------
# This portion calculates the 'T' Character in both words and suming the count.

if 't' in name1 or 't' in name2:
  word1 = name1.count('t')
  word2 = name2.count('t')
  total_word1 = word1 + word2
#  print(f"'T' word count is {word1 + word2}")
#else:
#  print("'T' word count is 0")

#--------------------------------------------------------------------------------
# This portion calculates the 'R' Character in both words and suming the count.

if 'r' in name1 or 'r' in name2:
  word1 = name1.count('r')
  word2 = name2.count('r')
  total_word1 += word1 + word2
#  print(f"'R' word count is {word1 + word2}")
#else:
#  print("'R' word count is 0")

#--------------------------------------------------------------------------------
# This portion calculates the 'U' Character in both words and suming the count.

if 'u' in name1 or 'u' in name2:
  word1 = name1.count('u')
  word2 = name2.count('u')
  total_word1 += word1 + word2
#  print(f"'U' word count is {word1 + word2}")
#else:
#  print("'U' word count is 0")

#--------------------------------------------------------------------------------
# This portion calculates the 'E' Character in both words and suming the count.

if 'e' in name1 or 'e' in name2:
  word1 = name1.count('e')
  word2 = name2.count('e')
  total_word1 += word1 + word2
#  print(f"'E' word count is {word1 + word2}")
#else:
#  print("'E' word count is 0")

#print(f"Total characts of word 'TRUE' is {total_word1}")  #Printing total "TRUE" word characters

#--------------------------------------------------------------------------------
# This portion calculates the 'L' Character in both words and suming the count.

if 'l' in name1 or 'l' in name2:
  word3 = name1.count('l')
  word4 = name2.count('l')
  total_word2 += word3 + word4
#  print(f"'L' word count is {word3 + word4}")
#else:
#  print("'L' word count is 0")

#--------------------------------------------------------------------------------
# This portion calculates the 'U' Character in both words and suming the count.

if 'o' in name1 or 'o' in name2:
  word3 = name1.count('o')
  word4 = name2.count('o')
  total_word2 += word3 + word4
#  print(f"'O' word count is {word3 + word4}")
#else:
#  print("'O' word count is 0")

#--------------------------------------------------------------------------------
# This portion calculates the 'E' Character in both words and suming the count.

if 'v' in name1 or 'v' in name2:
  word3 = name1.count('v')
  word4 = name2.count('v')
  total_word2 += word3 + word4
#  print(f"'V' word count is {word3 + word4}")
#else:
#  print("'V' word count is 0")

#--------------------------------------------------------------------------------
# This portion calculates the 'E' Character in both words and suming the count.

if 'e' in name1 or 'e' in name2:
  word3 = name1.count('e')
  word4 = name2.count('e')
  total_word2 += word3 + word4
#  print(f"'U' word count is {word3 + word4}")
#else:
#  print("'E' word count is 0")

#print(f"Total characts of word 'LOVE' is {total_word2}")

#concatinating total characters of both words to find the score
str_love_score = str(total_word1) + str(total_word2)

#Converting the score from string to integer for next if condition
love_score = int(str_love_score)
#print(love_score)

#--------------------------------------------------------------------------------
# If condition to check what's the score for printing the appropriate message

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")