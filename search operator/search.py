


def search(original,candidate,improvement,fit_original,dominator):
    better = []
    fit_candidate = fitness([candidate])
    # print(fit_candidate) 
    for i in range(repeat): #simple normalization
        weight = [original[1][j] + random.uniform(0,c)*(candidate[1][j]-original[1][j]) for j in range(portfolio_size)]
        weight = [weight[j] if weight[j]>=0 else random.uniform(candidate[1][j],original[1][j]) for j in range(portfolio_size)] #handling negative constraint
        summation = sum(weight) #normalization section
        normal_weight = np.array([lb+(weight[j]/summation)*sum_lb   for j in range(portfolio_size)])#normalization section
        if up_condition ==True: 
            # for i in range(len(normal_weight)):
                up_index = np.where(normal_weight>up)[0]
                if (list(up_index)) == []:
                    pass
                else:
                    while True:
                        up_index = np.where(normal_weight>up)[0]
                        if (list(up_index)) == [] and sum(normal_weight)>0.999 and sum(normal_weight)<1.001:
                            break
                        mask = np.ones_like(normal_weight, dtype=bool)
                        mask[up_index] = False
                        L = sum(normal_weight[mask]) #L for si(F/L)
                        F = 1-((lb*(portfolio_size-len(up_index))) + (up*(len(up_index)))) #F for si(F/L)
                        for j in range(len(normal_weight)):
                            if normal_weight[j]>=up:
                                normal_weight[j] = up
                            else:
                                normal_weight[j] = lb + (normal_weight[j] * (F/L))
        portfolio = np.array(list(original[0])+list(normal_weight)).reshape(2,portfolio_size)
        fit_portfolio = fitness([portfolio])
        if dominator==False:
            if fit_portfolio[0][0]>fit_original[0][0] and fit_portfolio[1][0]<fit_original[1][0]:

                return portfolio
                break
            temp_score =  landa*((fit_portfolio[0][0]/fit_original[0][0])-1) + (1-landa)*(1-(fit_portfolio[1][0]/fit_original[1][0]))    #claculating improvement 
            if temp_score>0:
                better.append([temp_score,portfolio]) #save that answer to better
        if dominator==True:
            if fit_portfolio[0][0]>fit_candidate[0][0] and fit_portfolio[1][0]<fit_candidate[1][0]:
                return portfolio
                break
            else:
                continue
    
    
    
    if better == []: #neither satisfied nor better
        return candidate
    else: #not satisfied but better activated
        return sorted(better, key=lambda x: x[0])[-1][1] #pick the best improvement