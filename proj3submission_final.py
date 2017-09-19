# Blues Brothers level
# full quote  = " What kind of music do you usually have here? We have both kinds; country and western! "
bluesBrothersQuote = "What kind of __1__ do you usually have here? We have __2__ kinds; __3__ and __4__ !"
bluesBrothersAnswers = [ "music", "both", "country", "western" ]


# Animal House Level
# full quote  " What are the grade point averages of the Deltas ? \
#        Kruger  1.2 \
#        Dorfman 0.2 \
#        Hoover  1.6 \
#        Blutarsky  0.0"

animalHouseQuote = "What are the grade point averages of the Delta's Kruger  __1__ Dorfman __2__  Hoover  __3__ Blutarsky __4__"

animalHouseAnswers = [ "1.2","0.2","1.6","0.0" ]

# Godfather level
# Full Quote  Times have changed. It's not like the Old Days, when we can do anything we want.
# A refusal is not the act of a friend. If Don Corleone had all the judges and the politicians in New York,
# then he must share them, or let us others use them. He must let us draw the water from the well.
# Certainly he can present a bill for such services; after all... we are not Communists .

godfatherQuote = "Emilio Barzini's speech:\n \
 Times have changed. It's not like the Old Days, when we can do anything we want.\n \
 A __1__ is not the act of a friend. If Don __2__ had all the __3__ and the \n \
 __4__ in New York, then he must __5__ them, or let us others use them. \n \
 He must let us draw the __6__ from the well. Certainly he can present a __7__ \n \
 for such services; after all... we are not __8__ ."

godfatherAnswers =["refusal", "corleone", "judges", "politicians","share", "water", "bill", "communists"]



def presentText( quote , answers): #  Present the original text or replaced text
                                      
    numAnswers = 0     
    
    wrongAnswers = 0
    
                                        
                                      # of the answer list
    while (numAnswers <  len(answers)) and ( wrongAnswers <= 4):    
       
          print quote
          user_input = getUserInput( numAnswers + 1 )          # in the "if" condition we are always looking for the first blank
          
          evaluationOfInput = evaluateInput(user_input, quote, answers, numAnswers )
                        # evaluationOfInput will be a list that will contain as its first element a boolean that
                        #will tell us of the user input is correct or incorrect. The second
                        # element will be the modified or unmodifed string
          rightAnswer = evaluationOfInput[0]
          quote = evaluationOfInput[1]
          
      

          if ( rightAnswer ):
                numAnswers += 1   # go on the next answer
                wrongAnswers = 0
                
          else:
               
               wrongAnswers += 1 
    if wrongAnswers >= 5:
      return "You Lose!"
    print quote          # print the completed correct string one last time!
    return "You Win!"

def evaluateInput( user_input, quote, answers, numAnswers ):  # this function will return a list containing a boolean and a string
                                                                    # the string is the quote, modified or unmodifed

        
        thisAnswer = user_input.lower()  # just as in "fill_in_the_blanks.pyc" we want the answer to be case insensitive
        if thisAnswer == answers[ numAnswers ] :
                
                quote = updateQuote ( quote , thisAnswer, numAnswers )
                return [ True, quote ]
        else:
                return [ False, quote ]

def updateQuote ( quote, thisAnswer, numAnswers ):   # Update the 'quote' string by replacing the placeholder with the answer

        replaceList=[]
        placeHolder = "__" + str(numAnswers + 1) + "__"  # create the placeholder we are looking for
        quoteList = quote.split()
       
        for word in quoteList:

                if ( word in placeHolder ):
                        word = word.replace(placeHolder, thisAnswer)

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
        


def playGame( level ): # initialize the game

        if level == "easy":
                print presentText( bluesBrothersQuote, bluesBrothersAnswers )
        elif level == "medium":
                print presentText(animalHouseQuote, animalHouseAnswers )
        elif level == "hard":
                print presentText(godfatherQuote, godfatherAnswers )
        else:
                # we should never get here
                print "input was invalid"

        return
                
        

def getInitialInput(): #  get and validate the user's requested level of play
        levels = [ "easy", "medium", "hard" ]
        while True:
                user_input = raw_input("Select a level:  ")
                if user_input.lower() in levels:
                        return user_input.lower()

                else:
                        print "Invalid input!"

                        
                
print "Welcome to the Movie Quiz. Please select a level by typing easy, medium or hard"
print "easy:  The Blues Brothers"
print "medium: Animal House"
print "hard: The Godfather"
print " "

level = getInitialInput()

playGame( level )

