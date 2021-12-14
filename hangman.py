import random

word_list=["number","sleep","piano","study","funny","music"]
random_word=random.choice(word_list)
word=[]
for j in random_word:
    word.append(j)
#print(word)
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives =len(random_word)-1

display = []

for i in random_word:

    display += "_"
       
end_game = True
while  end_game==True:

    guess = str(input("enter a letter :"))


        
    for position in range(len(random_word)):
        
        letter=random_word[position]
        
        if letter == guess:
            display[position] = letter
            print(display)
        
    if guess not in random_word:
        
        
        if lives == 0:
            end_game=False
            print("you lose")
        print(stages[lives])
    lives -= 1
    if "_" not in display:
        end_game=False
        print("you win ")
