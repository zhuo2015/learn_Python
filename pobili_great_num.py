import random
#import matplotlib.pyplot as plt

times = 1
rounds = 0
probli_head = []
while times !=0:
    times=int(input('times you want drop(enter 0 to quit):'))
    if times == 0:
        break
    else:
        rounds=int(input('rounds you want drop:'))
        times_pro = rounds
        probli = 0
        while times_pro != 0:
            times_pro -= 1
            head_coin = 0
            word_coin = 0
            for i in range(times):
                rand_num=random.randint(0,1)
                #print(rand_num)
                if rand_num == 0:
                    head_coin +=1
                else:
                    word_coin +=1
            probli2 = float('%.2f' % (head_coin/(head_coin+word_coin)))
            #print('prob: %.2f' % probli2)
            probli += probli2
            probli_head.append(probli)
        #print('prob: %.2f' %(probli))
            
            
        #print('head_coin:', head_coin)
        #print('word_coin:', word_coin)
        print('Probility: %.2f%%' % (probli/rounds*100))

    
        
