


def assign_weight(number=1,rand_given=0):#weight generator
    if rand_given==0: #randomly pick
        rand = random.choices((1,2), weights=(a,b))[0] 
    else:
        rand = rand_given
    if rand == 1: #random weight
        rand_w = [np.random.random_sample(size=portfolio_size)  for _ in range(number)]
        sum_of_random = [sum(rand_w[i]) for i in range(len(rand_w))] #denominator
        normal_weight = [(lb+(val/sum_of_random[i])*sum_lb) for i in range(number) for val in rand_w[i]] #normalizing the weights
        normal_weight = np.array(normal_weight).reshape(number,portfolio_size) #reshaping
        if up_condition ==True: 
            for i in range(len(normal_weight)):
                up_index = np.where(normal_weight[i]>up)[0]
                if (list(up_index)) == []:
                    continue
                else:
                    while True:
                        up_index = np.where(normal_weight[i]>up)[0]
                        # print(normal_weight[i]) 
                        if (list(up_index)) == [] and sum(normal_weight[i])>0.999 and sum(normal_weight[i])<1.001:
                            break
                        mask = np.ones_like(normal_weight[i], dtype=bool)
                        mask[up_index] = False
                        L = sum(normal_weight[i][mask]) #L for si(F/L)
                        # print(mask)
                        F = 1-((lb*(portfolio_size-len(up_index))) + (up*(len(up_index)))) #F for si(F/L)
                        for j in range(len(normal_weight[i])):
                            if normal_weight[i][j]>=up:
                                normal_weight[i][j] = up
                            else:
                                normal_weight[i][j] = lb + (normal_weight[i][j] * (F/L))
        return normal_weight
    if rand == 2: #equal weight
        weight = [(1/portfolio_size)] * portfolio_size * number
        weight = np.array(weight).reshape(int(len(weight)/portfolio_size),portfolio_size)
        return weight