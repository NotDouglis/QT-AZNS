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

def GenerateSituation():
    SituationArray = []
    for x in range(0,6):
        SituationArray.append(random.randint(0,1))
        print(x , " = " , SituationArray[x])     

    return SituationArray

SituationArray = GenerateSituation()


"""
def GenerateOptions(SituationArray):
    UserOptions = []

    if(test == 1):
        UserOptions.append("Look")

    if(test2 == 2):
        UserOptions.append("Go")

    return UserOptions

UserOptions = GenerateOptions(1)
for x in UserOptions:
    print(x)
"""
