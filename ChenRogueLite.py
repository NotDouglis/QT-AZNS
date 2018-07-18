import random

#SituationArray will have 1 or 0 depending on the circumstances
"""
Array Position Values
0 = Dark
1 = Door North
2 = Door South
3 = Door East
4 = Door West
5 = Enemy
"""

#Generate Situation
def GenerateSituation():
    SituationArray = []
    for x in range(0,6):
        SituationArray.append(random.randint(0,1))
        print(x , " = " , SituationArray[x])     
    return SituationArray

#Generate Options based on the situation
def GenerateOptions(SituationArray):
    UserOptions = []

    if(SituationArray[0] == 1):
        UserOptions.append("Light")

    if(SituationArray[1] == 1):
        UserOptions.append("Go North")

    if(SituationArray[2] == 1):
        UserOptions.append("Go South")

    if(SituationArray[3] == 1):
        UserOptions.append("Go East")

    if(SituationArray[4] == 1):
        UserOptions.append("Go West")

    if(SituationArray[5] == 1):
        UserOptions.append("Attack")
    return UserOptions

def GenerateDescription(SituationArray):
    #Beginning
    DescriptionString = "You are in a "

    #Dark or Lit
    if(SituationArray[0] == 1):
        DescriptionString += "Dark Room."
    else:
        DescriptionString += "Room."

    DescriptionString += " You can go "
    
    #Directions
    if(SituationArray[1] == 1):
        DescriptionString += "North"
    else:
        DescriptionString += ""

    if(SituationArray[2] == 1):
        if(SituationArray[1] == 1):
            DescriptionString += ", "
        DescriptionString += "South"
    else:
        DescriptionString += ""

    if(SituationArray[3] == 1):
        if(SituationArray[1] == 1 or SituationArray[2] == 1):
            DescriptionString += ", "
        DescriptionString += "East"
    else:
        DescriptionString += ""

    if(SituationArray[4] == 1):
        if(SituationArray[1] == 1 or SituationArray[2] == 1 or SituationArray[3] or 1 ):
            DescriptionString += ", "
        DescriptionString += "West"
    else:
        DescriptionString += ""
    return DescriptionString

def SituationSetup():
    #Setup
    SituationArray = GenerateSituation()
    UserOptions = GenerateOptions(SituationArray)
    Description = GenerateDescription(SituationArray)
    #Print
    print("")
    print(Description,"\n")
    print("Potential Options:")
    Count = 1
    for x in UserOptions:
        print(Count,":",x)
        Count+=1
    return SituationArray

#Setup Situation and Options
CurrentSituation = SituationSetup()
Situations = []
Situations.append(CurrentSituation)

