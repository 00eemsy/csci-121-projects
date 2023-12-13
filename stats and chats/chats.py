#
# CSCI 121 Fall 2022
#
# Project 2, Part 2
#
# chats.py
#
# Process a text and distill statistics about the bi-gram and tri-gram
# word occurrences in the entered text. It does this by using a dictionary
# of words and bi-grams. Each dictionary entry gives the list of words
# in the text that follow that word/bi-gram (and possibly a count of the
# number of times each follower does so).
#
# The code then generates random text based on these statistics.
#
#
# Usage: python3 chats.py
#
# This command processes a series of lines of text, looking for
# contiguous runs of alphabetic characters treating them each as a
# word. For each such word, it keeps a count of the number of its
# occurrences in the text.
#
# To end text entry hit RETURN and then CTRL-d.  It then generates
# a random text that tries to mimic the text it just processed.
#
#
# Alternative usage: python3 chats.py < textfile.txt
#
# The above instead processes the text of the file in 'textfile.txt'.
#

from socket import INADDR_LOOPBACK
import sys
import random

STOPPERS   = [".", "!", "?"]
WHITESPACE = [" ","\n","\r","\t"]

def simplifyWord(word):
    """Returns the given string with only certain chars and lowercase.

    This "simplifies" a word so that it only contains a sequence of
    lower case letters and apostrophes, making uppercase letters
    lowercase, and skipping others.  It returns the "simplified" word.
    If, upon simplifying a word, all the characters are skipped, the 
    function returns None.
    
    In normal use, this would convert a word like "Ain't" into the
    word "ain't" and return it. It also would take a text string like
    "it105%s" and give back the string "its".

    This particular function behavior is somewhat arbitrary, written
    to be "good enough" just to handle the spurious other characters
    that might arise in the kinds of free texts from things like
    Project Gutenberg. Sadly, this also strips out accented characters
    and non-Roman alphabetic characters.
    """

    # Scan the word for a-z or ' characters.
    convertedWord = "";
    for c in word:
        if 'A' <= c and  c <= 'Z':
            c = c.lower()
        if ('a' <= c and c <= 'z') or c == '\'':
            convertedWord += c;

    # If we added any such characters, return that word.
    if len(convertedWord) > 0:
        return convertedWord
    else:
        # Otherwise, return None.
        return None

def readWordsFromInput():
    """Returns the contents of console input as a list of words.

    Process the console input as consisting of lines of words. Return
    a list of all the words along with the strings that are "stoppers." 
    Each non-stopper word in the list will be lowercase consisting only
    of the letters 'a'-'z' and also apostrophe. All other characters are
    stripped from the input. Stopper words are specified by the variable
    STOPPERS.
    """
     
    def spacedAround(text,c):
        """Returns modified text with spaces around any occurrence of c.

        Helper function that replaces any string `text` that has the
        character `c` so that all the occurrences of `c` are replaced
        with the substring " c ".
        """
        
        splits = text.split(c)
        return (" "+c+" ").join(splits)

    def spaceInsteadOf(text,c):
        """Returns modified text with space replacing any c.

        Helper function that replaces any string `text` that has the
        character `c` so that all the occurrences of `c` are replaced
        with a space.
        """
        
        splits = text.split(c)
        return (" ").join(splits)
    
    # Read the text into one (big) string.
    textChars = sys.stdin.read()

    # Add spaces around each "stopper" character.
    for stopper in STOPPERS: 
        textChars = spacedAround(textChars,stopper)
        
    # Replace each whitespace character with a space.
    for character in WHITESPACE: 
        textChars = spaceInsteadOf(textChars,character)

    # Split the text according to whitespace.
    rawWords = textChars.split(" ")

    # Process the raw words, simplifying them in the process by
    # skipping any characters that we don't currently handle.
    # We treat the "end of sentence"/"stopper" words specially,
    # including them in the list as their own strings.
    words = []
    for word in rawWords:
        if word not in STOPPERS:
            word = simplifyWord(word)
        if word is not None:
            words.append(word)
    return words


def train(wordList):
    """ Your comment goes here. """

    #
    # Your code goes here.
    #
    # ******* emily's code *******
    
    # WORD FOLLOWERS
    # sets up the wordList perfectly slay
    STOPPERS   = [".", "!", "?"]
    
    for i in wordList:
        i.lower()

    count = 0
    while count < len(wordList):
        if wordList[count] == ',':
            wordList[count] = ''
        count += 1 

    for i in wordList:
        for letter in i:
            if letter in STOPPERS:
                i.split(" ")  

    # setting up keys

    wL_copy = list(wordList)
    count = 0
    while count < len(wL_copy):
        if wL_copy[count] in STOPPERS:
            del wL_copy[count]
        count += 1

    count = 0
    count1 = 1

    while count < len(wL_copy):
        count1 = count + 1
        while count1 < len(wL_copy):
            if wL_copy[count] == wL_copy[count1]:
                del wL_copy[count1]
            count1 += 1
        count += 1
    
    biTriDict = {'.':[],'!':[],'?':[]}

    for i in biTriDict:
        biTriDict[i].append(wL_copy[0])

    for i in wL_copy:
        biTriDict[i] = []

    # giving them values lolll
    for i in biTriDict:
        count = 0
        while count < len(wordList):
            if i == wordList[count] and count+1 < len(wordList):
                biTriDict[i].append(wordList[count+1])
            count += 1

    # BIGRAM FOLLOWERS
    count = 0

    while count < len(wordList):
        if count+2 < len(wordList):
            biTriDict[wordList[count] + " " + wordList[count+1]] = [wordList[count+2]]
        count += 1

    return biTriDict
    

    # ****************************

def chat(biTriDict,numLines,lineWidth):
    """ Your comment goes here. """

    #
    # Your code goes here.
    #
    # ******* emily's code *******
    chat = ""

    w1 = ""
    w2 = "."


    count = 1
    firstWord = True
    done = False

    while done == False:
        line = ""
        while len(line) <= lineWidth and done == False:
            if w1 + ' ' + w2 in biTriDict:
                nextWord = random.choice(biTriDict[w1 + " " + w2])
            else:
                if w2 in biTriDict:
                    nextWord = random.choice(biTriDict[w2])
                else:
                    nextWord = random.choice(biTriDict["."])
            
            w1 = w2
            w2 = nextWord

            if firstWord:
                line += " " + w2
            elif w2 not in STOPPERS:
                line += " " + w2
            elif w2 in STOPPERS:
                if w2 in STOPPERS and len(line) == 0:
                    line += " " + w2
                else:
                    line += w2
                if count > numLines:
                    done = True

            firstWord = False
        
        chat += line + "\n"
        count += 1

    print(chat)
    return chat

    # ****************************
    
#
# The main script. This script does the following:
#
# * Processes a series of lines of text input into the console.
#      => The words of the text are put in the list `textWords`
#
# * Scans the text to compute statistics about bi-grams and tri-
# grams that occur in the text. This uses the function `train`.
#
# • Generates a random text from the bi-/tri-gram dictionary
#   using a stochastic process. This uses the procedure 'chat'.
#

if __name__ == "__main__":

    # Read the words of a text (including ".", "!", and "?") into a list.
    print("READING text from STDIN. Hit ctrl-d when done entering text.")
    textWords = readWordsFromInput()
    print("DONE.")

    # Process the words, computing a dictionary.
    biTriDict = train(textWords)
    chat(biTriDict, 10, 10)
