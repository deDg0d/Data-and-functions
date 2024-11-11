


def assign_sharpe_weight(portfolio):#weight generator #
    ratio = np.array([sharpe[int(portfolio[i][0][j])] if sharpe[int(portfolio[i][0][j])]>=0 else 1/(sharpe[int(portfolio[i][0][j])]*-10000)  for i in range(len(portfolio))
    for j in range(portfolio_size)]).reshape(len(portfolio),portfolio_size)
    sum_w = [sum(ratio[i]) for i in range(len(ratio))]
    stocks = [portfolio[i][0] for i in range(len(portfolio))] #lb+(val/sum_of_random[i])*sum_lb
    w = np.array([min(lb+(ratio[i][j]/sum_w[i])*sum_lb,up) for i in range(len(portfolio)) for j in range(portfolio_size)]).reshape(len(portfolio),portfolio_size)
    if up_condition ==True: 
            for i in range(len(w)):
                up_index = np.where(w[i]>up)[0]
                if (list(up_index)) == []:
                    continue
                else:
                    while True:
                        up_index = np.where(w[i]>up)[0]
                        if (list(up_index)) == [] and sum(w[i])>0.999 and sum(w[i])<1.001:
                            break
                        mask = np.ones_like(w[i], dtype=bool)
                        mask[up_index] = False
                        L = sum(w[i][mask]) #L for si(F/L)
                        F = 1-((lb*(portfolio_size-len(up_index))) + (up*(len(up_index)))) #F for si(F/L)
                        for j in range(len(w[i])):
                            if w[i][j]>=up:
                                w[i][j] = up
                            else:
                                w[i][j] = lb + (w[i][j] * (F/L))
    final_w = np.array([[stocks[i],w[i]] for i in range(len(portfolio))])
    return final_w
