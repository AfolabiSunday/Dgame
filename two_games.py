#All input are in lowercase, if there is any more ways to enhance this pls feel free to share via dm, thanks for playing




def game():

    secretword = 'folabi'
    solo = 'sololearn'
    lang = 'python'
    prog = 'online'
    i = 0
    answer = ''
    print('welcome stranger, Trust you are good')
    name = input('what will you like me to call you?  ')
    print()
    print(name + ' lets get it going')
    question1 = input('i am a man with 5 legs two head and one big hand, WHAT AM I?   ')
    print()
    if question1 == secretword:
        print('coreect!')
        i = i+ 1
    else:
        print('Sorry, you got it Wrong')
        i = i+ 0
    print()
    question2 = input('What is the name of where this script is publised ? ')
    if question2 == solo:
        print('Correct! ')
        i= i+ 1
    else:
        print('Sorry, Your Answer is Wrong')
        i= i+ 0
    print()
    question3 = input('Which programming language is the best for Blockchain? ')
    if question3 == lang:
        print('Correct ')
        i+= 1
    else:
        print('Sorry, Your Answer is Wrong')
        i+= 1
    print()
    question4= input ('Which is the best way to learn programming ? , Online or Offline ')
    if question4 == prog:
        print('Correct Again!')
        i+= 1
    else:
        print('Sorry, Your Answer is Wrong')
        i+= 0
    print('You scored ' + str(i) + ' that nice!')
    print()
    print('thanks for coming')
    print()


def game2():

    i = 0
    print('welcome stranger, Trust you are good')
    name = input('what will you like me to Call you? ')
    print()
    '''print('welcome stranger, this is a CA test to know what you know')'''
    name = input('Who is the presnt president of Nigeria? (a) Yaradua (b)Goodluck (c)Buari  ' )
    if name == 'c':
        i = i+1
    else:
        i = i+0
    print()
    name2 = input('when is the next election? (a)2019 (b) 2018 (c) 2017  '  )
    if name2 == 'a':
        i = i+1
    else:
        i = i+0
    print()
    name3 = input('where is the capital of nigeria? (a) kokodome (b)abuja (c) Ibadan   ')
    if name3 == 'b':
        i = i+1
    else:
        i = i+0
    print()
    print('weldone your scores is ' + str(i))


question = 'game'
question2 = 'question'

namer = input('welcome new users, what will you like me to call you ? ')
print()
'''print('welcome ' + namer + ' !')'''
query = input('which of the game will you like to play ? ' + 'pls choose between QUESTIONS and GAME ')
print()
if query == question2:
    game2()
if query == question:
    print(game())
else:
    print('sorry you entered and inValid command')
print()
print('Thanks for Trying this game and questions out, ')
print('if there is anyway you think i need to improve, pls let me know thanks')
