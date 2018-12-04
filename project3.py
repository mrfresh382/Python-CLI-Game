import random

answerPlace=["___1___", "___2___", "___3___", "___4___"]
## several functions refer to this variable

def setupGame():
    ## This initializes the game variables
    ## e1q1 is Easy mode, Question 1, e1a1 is Easy mode Answers for question 1, etc...
    e1q1='''The first president of the US was ___1___ . The current President is Donald ___2___ . That last president before President ___2___ was ___3___ . ___3___ served in office for ___4___ years. The least popular president was arguably ___5___ , who said "I'm not a crook!!" (Last names only)'''
    e1a1=['Washington','Trump','Obama','8', 'Nixon']
    e1q2='''___1___ is a computer language which is possibly named after the British comedy show ___2___ ___1___ .  ___3___ is used to design the markup of a webpage . ___4___ is used to define the style aspects of a webpage. '''
    e1a2=['Python', 'Monty', 'HTML' , 'CSS' ]
    e1q3='''If you want to watch a sappy romantic show, then you should watch the ___1___ channel. If you want to watch a grindhouse, action flic, then you should watch ___2___ . ___3___ shows movies, some tv shows, and boxing. If you like home improvement and remodeling, then ___4___ is for you.'''
    e1a3=['Lifetime', 'El Rey', 'HBO', 'HGTV']
    e1q4='''Pizza sauce is made from ___1___ sauce. There is also ___2___ oil in pizza sauce. ___3___ is a popular pizza store and is also a type of tabletop game. The best pizza comes from ___4___ ovens. I love pizza!!!'''
    e1a4=['tomato', 'olive', 'Dominos', 'brick']

    gameDatabase={"Easy"  : [ [e1q1, e1a1], [e1q2, e1a2] , [e1q3,e1a3], [e1q4, e1a4] ] , "Medium": [ ['1+2 = ___1___   2 + 21 = ___2___   4+6= ___3___   3+9 = ___4___',['3','23', '10', '12']], ['3-1 = ___1___    4-2 = ___2___  321 - 21 = ___3___   196-28 = ___4___',['2','2','300', '168']] , ['3 x 2=  ___1___    5 x 2 = ___2___     32 x 6 = ___3___     17 x 5 = ___4___ ',['6', '10', '192', '85']], ['4 % 2 = ___1___     5 % 2= ___2___     51 % 17 = ___3___    123 % 7 = ___4___', ['0','1','0','4'] ] ],"Hard"  : [ ['___1___ is a text editor and rymes with "Lyme". ___2___ is another text editor and is bigger than an electron and proton. ___3___ is a type of Interactive Development Environment or ___4___ for short.',['Sublime', 'Atom', 'Eclipse', 'IDE']], ['___1___ code is code that is already complied and cannot be opened by a text editor. ___2___ code can be run by the windows command line or by using the ___2___ ___3___ . Testing individual lines of code or experimenting new ___4___ can be easily done with the ___3___ .',['Byte', 'Python', 'interpreter', 'functions']] , ['If you are really into computers, you can buy a Raspberry ___1___ , which is costs less than $ ___2___ and runs a version of ___3___ operating system. You can also play ___4___ on the Raspberry ___1___ . ',['Pi','40', 'Linux', 'games']], ["___1___ engine optimization is a modern way to advertise your business. If your business doesn't show up if you do a ___2___ search, then you should invest in ___1___ engine optimization. ___3___ is a company that can assist small businesses with e-Commerce, but there are many free-lance ___4___ that can help with ___5___ marketing. ",['Search','Google','HubSpot', 'programmers', 'digital']] ] }
    numTriesRemaining=5 ##sets number of lives in the game
    ## A dictionary with the game questions and answers and the lives remaining are provided to the main() function
    return gameDatabase , numTriesRemaining


def selDiff():
    ##Asks the player for what the level of difficulty they want to play
    ##Like the example, there is Easy/Medium/Hard. It will accept the first letter
    ## or an uppercase or lowercase spelled difficulty ie ( e, h, hard, Hard, med)
    easyList=['Easy', 'easy', 'e', 'E']
    medList=['Medium', 'medium', 'm', 'Med', 'med']
    hardList=['hard', 'Hard', 'h', 'H']
    
    difficultyOut=""
    while ( not(difficultyOut) ):
        difficultyIn=raw_input("Select difficulty ( Easy|Medium|Hard) ...")
        if difficultyIn in easyList:
            difficultyOut="Easy"
        elif difficultyIn in medList:
            difficultyOut="Medium"
        elif difficultyIn in hardList:
            difficultyOut= "Hard"
        else:
            print "You did not select a correct level, please try again"
    return difficultyOut



def gameOver( numRemaining ):
    ## takes input for number of tries remaining and will terminate the game if all 5 are used
    if numRemaining>0:
        print "You have" , numRemaining , "tries to go."   
        return numRemaining
    else:
        print "You have used all your tries, better luck next time!"
        exitTheGame=raw_input( "Press enter to close game")
        exit(0)

def playGame( checkTriesLeft, questionDBLoc, nextBlank):
    ## This is a recursive function that take user input, decreases triesRemaining, an keeps playing
    ## nextBlank keeps track of which answer the player is on in each sentance
    livesLeft= checkTriesLeft  ##localizing this variable, had issues with another function, so a extra line of code was needed
    showInstructions()
    addMissingWord(questionDBLoc, answerPlace, nextBlank) ## This prints the sentence and includes any correct answers that are filled in
    ##print questionDBLoc[1][nextBlank] ##CHEAT MODE
    userAnswer=raw_input("Blank {0} _".format( nextBlank+1)) ## aligns with the actual displayed number
    if userAnswer == questionDBLoc[1][nextBlank]:
        print 'That is correct!!!!'
        nextBlank+=1
    else:
        print 'That is NOT correct'
        livesLeft-=1
    if nextBlank==len(questionDBLoc[1]):
        return (livesLeft)
        ## This returns the number of lives remaining
    livesLeftRecursive=playGame( gameOver(livesLeft) , questionDBLoc, nextBlank) # livesLeftRecursive is an arbitrary variable that carries the livesLeft amount back to the first playGame() instance
    return livesLeftRecursive
    ## This adjusts the numTriesRemaining in main() for each question, the original value is passed to the first playGame() call in main()

def showInstructions():
    ## Prints the instructions for the user each time they attempt to fill in the blank
    print ""
    print "Type in your answer and then press enter to submit"

def randomizeQuestions(questionDicLoc, selectedDifficulty):
    ## randomizes the questions for the game upfront
    randomGameDatabase=questionDicLoc[selectedDifficulty]
    random.shuffle(randomGameDatabase)
    return randomGameDatabase

def askKeepPlaying( difficulty):
    ## Asks the user if they want to go to the next level
    keepGoing = ""
    while not(keepGoing):
        keepGoing=raw_input("Continue to next difficulty mode ? y/n  ")
        if keepGoing in ['n', 'no', 'No']:
            exit(0)
        if keepGoing in ['y', 'yes', 'Yes', 'ye']:
            if difficulty == "Easy":
                return "Medium"
            elif difficulty=="Medium":
                return "Hard"
        print "Please enter (y/n)"
        keepGoing=""
        
def addMissingWord(gameDB, answerPlaces, nextBlank):    
    ## Used Chapter 3 code to insert the correct answer, and prints out the sentence as the player answers correctly
    
    out_string = []
    in_string = gameDB[0].split()

     ## used to update the previous answers in the sentence
    
    '''if nextBlank==0: OLD CODE
        print gameDB[0]
        # got rid of this to remove a phantom '[]', couldn't figure it out
    else:'''

    for word in in_string:
        if nextBlank>=1 and word in answerPlaces[0:nextBlank]:
            ### This assumes that the first blank has already been answered correctly 
            previousAnsBlank=answerPlaces[0:nextBlank].index(word)
            word = word.replace(  answerPlaces[previousAnsBlank],gameDB[1][previousAnsBlank])
            out_string.append(word)
            ### Some old code here
            '''if answerPlaces[nextBlank-1]==word:
                word = word.replace(  answerPlaces[nextBlank-1],gameDB[1][nextBlank-1])
                out_string.append(word)
                elif nextBlank>=2 and word in answerPlaces[0:nextBlank-1]:'''
        else:
            out_string.append(word)
    out_string = " ".join(out_string)
    print out_string



def main():
    ## I created a main function to store the initalization of the core game flow, I found this in numerous Python educational texts
    gameDatabase, gameLives=setupGame() 
    difficulty=selDiff()
    newGameDB = randomizeQuestions(gameDatabase, difficulty)
    for level in newGameDB:
            ##level[1] is the answer bank
            ##level[0] is the sentence
            ##print level[1]
            ##print level[0]   
        gameLives= playGame(gameLives,level,0) # the 0 establishes a index at 0 to keep track of where the player is
        print "You won this level!"
    while( difficulty!="Hard"):  #This asks if the player wants to play a harder mode
        difficulty= askKeepPlaying(difficulty)
        newGameDB = randomizeQuestions(gameDatabase, difficulty)
        for level in newGameDB:
            gameLives= playGame(gameLives,level,0)
            print "You won this level!"
    print "You win the game!!!!!!"

if __name__ == "__main__":
    main()