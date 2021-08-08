# Need to insert this code to the console
def voting_check(name):
    if voted.get(name):
        print("You've voted already!")
    else:
        voted[name] = True
        print('You can vote')


voted = {}
voting_check('Andrew')
