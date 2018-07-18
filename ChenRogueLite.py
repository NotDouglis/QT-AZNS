def GenerateOptions(test,test2):
    UserOptions = []

    if(test == 1):
        UserOptions.append("Look")

    if(test2 == 2):
        UserOptions.append("Go")

    return UserOptions

UserOptions = GenerateOptions(1,2)
for x in UserOptions:
    print(x)
