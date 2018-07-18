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

SituationArray = GenerateSituation()

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

UserOptions = GenerateOptions(SituationArray)

for x in UserOptions:
    print(x)

