# Blues Brothers level
# full quote  = " What kind of music do you usually have here? We have both kinds; country and western! "
bluesBrothersQuote = "What kind of __1__ do you usually have here? We have __2__ kinds; __3__ and __4__ !"
bluesBrothersAnswers = [ "music", "both", "country", "western" ]
replaced = [" this" "is" "a" "placeholder" ]

def createPlaceHolderList(number):  #rather than to create a static list of placeholders for each quiz
                                    # we'll write a function to create them dynamically as needed.
        i = 1  #index
        placeHolderList = []
        while i <= number:
           listMember = "__" + str(i) + "__"
           placeHolderList.append( listMember )
           i += 1
        return placeHolderList 

def presentText( quote , answers): #  Present the original text or replaced text
                                      # based on the number of right answers
    numAnswers = 0     
    numBlanks = len(answers)          # the number for blanks to be filled in, calculated by the length
    wrongAnswers = 0
    rightAnswer = False
    user_input = ""
    evaluationOfInput = []               # This will be a list that will contain as its first element a boolean that
                                            #will tell us of the user input is correct or incorrect. The second
                                            # element will be the modified or unmodifed string
                                        
                                      # of the answer list
    while (numAnswers <  numBlanks) and ( wrongAnswers <= 4):    
       
          print quote
          user_input = getUserInput( numAnswers + 1 )          # in the "if" condition we are always looking for the first blank
          print "user_input is" + user_input
          evaluationOfInput = evaluateInput(user_input, quote, answers, replaced, numAnswers )
          rightAnswer = evaluationOfInput[0]
          quote = evaluationOfInput[1]
          
      

          if ( rightAnswer ):
                numAnswers += 1   # go on the next answer
                wrongAnswers = 0
                rightAnswer = False
          else:
               print "number of wrong answers" + str(wrongAnswers) 
               wrongAnswers += 1 
    if wrongAnswers >= 5:
      return "You Lose!"
    print quote          # print the completed correct string one last time!
    return "You Win!"

def evaluateInput( user_input, quote, answers, replaced, numAnswers ):  # this function will return a list containing a boolean and a string
                                                                    # the string is the quote, modified or unmodifed

        #answerIndex = numAnswers + 1     # This is the index of 'answers' that we will be evaluating.
        thisAnswer = user_input.lower()  # just as in "fill_in_the_blanks.pyc" we want the answer to be case insensitive
        if thisAnswer == answers[ numAnswers ] :
                # Do a lot of other stuff
                quote = updateQuote ( quote , thisAnswer, numAnswers )
                return [ True, quote ]
        else:
                return [ False, quote ]

def updateQuote ( quote, thisAnswer, numAnswers ):   # Update the 'quote' string by replacing the placeholder with the answer

        replaceList=[]
        placeHolder = "__" + str(numAnswers + 1) + "__"  # create the placeholder we are looking for
        quoteList = quote.split()
        for word in quoteList:

                if ( word == placeHolder ):
                        word = thisAnswer

                replaceList.append(word)

        return " ".join(replaceList)
        
        
        

        
          
def getUserInput(n):    #Get user input for the substitution blank indicated by n
     user_input = raw_input("What should be substituted for __" + str(n) + "__  ")
     return user_input


# Checks if a word in a list is a substring of the word passed in.
def word_in_pos(word, word_list):
    for pos in word_list:
        if pos in word:
            return pos
    return None
        
# Plays a full game of mad_libs. A player is prompted to replace words in ml_string, 
# which appear in parts_of_speech with their own words.  
def play_game(ml_string, parts_of_speech):    
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

placeHolderList = createPlaceHolderList(4)
print placeHolderList
user_input = getUserInput(5)
print user_input
           
print presentText( bluesBrothersQuote, bluesBrothersAnswers )
