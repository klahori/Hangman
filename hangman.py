import random
from words import word_list

def get_word():
    word=random.choice(word_list)
    return word.upper()

def play(word):
    word_completion="_"*len(word)
    guessed=False
    guessed_letters=[]
    guesed_words=[]
    tries=6
    print("Time to play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries>0:
        guess=input("Please guess a letter or word: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter")
            elif guess not in word:
                print(guess,"is not in the word")
                tries-=1
            else:
                print("Good job ",guess," is in the word")
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices=[i for i,letter in enumerate(word)if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guesed_words:
                print("You already guessed the word ",guess)
            elif guess!=word:
                print(guess,"is not the word")
                tries-=1
                guesed_words.append(guess)
            else:
                guessed =True
                word_completion=word
        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")    
    if guessed:
        print("Congrats you gussed the the word you WIN")
    else:
        print("Sorry you ran out of tries the word was ",word)
def display_hangman(tries):
    stages = [ """"
                 0
                \|/
                /|\    
    
    
        """,
          """"
                 0
                \|/
                /|   
    
    
        """,""""
                 0
                \|/
                 |    
    
    
        """,""""
                 0
                \|
                 |    
    
    
        """,""""
                 0
                 |
                 |   
    
    
        """,""""
                 0
                
                   
    
    
        """,
        """"



    
    
        """]
    return stages[tries]
def main():
    word = get_word()
    play(word)
    while input("Play Again(Y/N): ").upper()=="Y":
        word=get_word()
        play(word)
if __name__=="__main__":
    main()