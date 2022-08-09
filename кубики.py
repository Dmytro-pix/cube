import random
a = 0 # number of player points
b = 0 # number of bot points

def kubik(t):
    if t == 1:
        print("****************")
        print("*              *")
        print("*              *")
        print("*              *")
        print("*      *       *")
        print("*              *")
        print("*              *")
        print("*              *")
        print("****************")
    elif t == 2:
        print("****************")
        print("*              *")
        print("*       *      *")
        print("*              *")
        print("*      *       *")
        print("*              *")
        print("*              *")
        print("*              *")
        print("****************")
    elif t == 3:
        print("****************")
        print("*              *")
        print("*      *       *")
        print("*              *")
        print("*      *       *")
        print("*              *")
        print("*      *       *")
        print("*              *")
        print("****************")
    elif t == 4:     
        print("****************")
        print("*              *")
        print("*              *")
        print("*              *")
        print("*      *       *")
        print("*              *")
        print("*              *")
        print("*              *")
        print("****************")
    elif t == 5:
        print("****************")
        print("*              *")
        print("*  *       *   *")
        print("*              *")
        print("*      *       *")
        print("*              *")
        print("*  *        *  *")
        print("*              *")
        print("****************")
    elif t == 6:
        print("****************")
        print("*              *")
        print("*   *      *   *")
        print("*              *")
        print("*   *      *   *")
        print("*              *")
        print("*   *      *   *")
        print("*              *")
        print("****************")

for i in range(5):
    print("Round №",i+1)
    player = random.randint(1,6)
    bot = random.randint(1,6)
    print("The player has dropped",player,"point")
    kubik(player)
    print("The bot dropped",bot,"point")
    kubik(bot)
    a = a + player
    b = b + bot
    v = input("Press Enter to continue")
if a > b:
    print("Player victory!",a,":",b)
elif a < b:
    print("Bot win!",b,":",a)
else:
    print("Fighting draw!",a,":",b)
