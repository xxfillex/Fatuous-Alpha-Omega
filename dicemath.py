def intinput(T):
    while True:
        I=input(T)                          #asks for a number according to the text given in the parameter
        if I.isdigit() == True: 
            I=int(I)
            if I > 1000:
                print("Please choose a number below 1000")
                continue                    #redoes the process as a number above 1000 was given
        else:
            print("please choose a valid integer")
            continue                        #redoes the process as anything else than an integer was given
        return I    
def getavg(X, Y): #returns average values, and makes a list of each probability of rolling something
    T=0
    for N in range(1, X+1): #for each value N you can roll on the dice
        P=( 
            pow( (X+1)-N, (Y+1) )
            - pow( (X-N), (Y+1) ) 
            )/pow( X, (Y+1) ) #formula for the probability of rolling N with Y disadvantage dices for 1dX 
        L.append(P) #append the probability to roll N
        T += N*P    #add how much N contribues to the total average to T to get the average for disadvantage
    A=X/2+0.5       #average of rolling 1dX
    D=A-T           #average difference advantage/disadvantage gives compared to normal average    
    return [D, A]

def getvalues(X, Y): #makes a list of the values that should be printed
    for I in range(0, X): 
        F.append("N = "+str(I+1))                       #the value N
        F.append("{:.3f}%".format(L[I]*100))            #the probability to roll N with disadvantage
        F.append("{:.3f}%".format(sum(L[I:])*100))      #sums every probability above N, giving you the probability of rolling above something with disadvantage
        F.append("{:.3f}%".format(L[X-I-1]*100))        #the last element of the list is the probability of rolling N with advantage
        F.append("{:.3f}%".format(sum(L[:X-I])*100))    #sums every probability below the reverse of N, which therefore calculates advantage instead
    for I in range(0, X*5):
        F[I]+=" "*(20-len(F[I]))                        #makes each element in the list have the length 20

def printres(X, Y, R): #prints everything in a neat manner
    print("                    Disadv P(N):        Disadv P(>=N):      Adv P(N):           Adv P(>=N):")
    for N in range(0, X*5, 5):
        print(str(F[N])+str(F[N+1])+str(F[N+2])+str(F[N+3])+str(F[N+4]))  #prints 5 elements at a time on the same line
    print("The average result with",Y,"disadvantage dice: {:.3f}".format(R[1]-R[0])) #prints average disadvantage for 1dX with Y disadvantage dices
    print("The average result with",Y,"advantage dice:    {:.3f}".format(R[1]+R[0])) #prints average advantage for 1dX with Y advantage dices    
    print("The regular average is:                      {:.3f}".format(R[1])) #prints the regular average
    print("The average increase or decrease is:         {:.3f}".format(R[0])) #prints the average change


def keeplooping():
    C=input("repeat (y/n)? ") #repeats the process only if a variation of yes is inputted
    if C == "y" or C == "yes" or C == "Y" or C == "Yes":
        #sets the loop to repeat and clears the lists so that they can be used again
        L.clear()
        F.clear()    
        return True
    return False

L=[]
F=[]
C=True

while C == True:
    X=intinput("Input the size of the dice: 1d")
    Y=intinput("The number of disadvantage/advantage dices: ")
    R=getavg(X, Y)          #calculates the average results for disadvantage
    getvalues(X, Y)         #makes a list of the values to be printed
    printres(X, Y, R)       #prints said values
    C=keeplooping()         #checks if the user wants to restart the process