import numpy as np
import matplotlib.pyplot as plt

provincess = np.arange(1,8)

meanturn = np.zeros(provincess.size)

for h,provinceN in enumerate(provincess):
    if provinceN != 5:
        continue
    N = 10000
    
    points = np.zeros(N)
    turns = np.zeros(N)
    for i in range(N):
        deck = np.array(['e']*3+['c']*7)
        np.random.shuffle(deck)
        prog = 0
        oldprog = 0
        turn = 0
        provinces = provinceN
        smithies = 1
        while provinces > 0:
            turn += 1

            # draw

            draws = 5
            prog = oldprog + draws
            if prog > len(deck):
                prog = draws
                np.random.shuffle(deck[:oldprog])
                tmp = deck[:oldprog].copy()
                deck[:len(deck)-oldprog] = deck[oldprog:]
                deck[len(deck)-oldprog:] = tmp
                oldprog = 0
        
            hand = deck[oldprog:prog]

            # actions
            if 'smithy' in hand:
                draws += 3
                prog = oldprog + draws
                if prog > len(deck):
                    prog = draws
                    np.random.shuffle(deck[:oldprog])
                    tmp = deck[:oldprog].copy()
                    deck[:len(deck)-oldprog] = deck[oldprog:]
                    deck[len(deck)-oldprog:] = tmp
                    oldprog = 0
                hand = deck[oldprog:prog]
        
            money = np.sum(hand == 'c') + np.sum(hand == 's')*2 + np.sum(hand == 'g')*3
        
            # buys
            buys = 1
            
            if money >= 4 and buys > 0 and smithies > 0:
                deck = np.hstack(('smithy', deck))
                prog += 1
                buys -= 1
                smithies -= 1
            

            if money >= 8 and buys > 0:
                deck = np.hstack(('p', deck))
                prog += 1
                buys -= 1
                provinces -= 1
            
            if money >= 6 and buys > 0:
                deck = np.hstack(('g', deck))
                prog += 1
                buys -= 1
        
            if money >= 3 and buys > 0:
                deck = np.hstack(('s', deck))
                prog += 1
                buys -= 1
            
            oldprog = prog
    
        points[i] = np.sum(deck == 'e') + np.    sum(deck == 'd')*3 + np.sum(deck == 'p') * 6
        turns[i] = turn
    meanturn[h] = np.mean(turns)
    plt.hist(turns)
    plt.show()
        
'''
plt.figure()
plt.plot(provincess, meanturn, 'k')
plt.grid('on')
plt.show()
'''