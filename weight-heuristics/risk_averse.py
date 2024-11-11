



def risk_parity(portfolio):

    copy_portfo = portfolio.copy()
    volatility = [1/sd[int(portfolio[0][j])] for j in range(portfolio_size)]
    total_volatility = sum(volatility)
    volatility = np.array([lb+(volatility[i]/total_volatility)*sum_lb for i in range(portfolio_size)]).flatten().reshape(1,portfolio_size)
    if up_condition ==True: 
        for i in range(len(volatility)):
            up_index = np.where(volatility[i]>up)[0]
            if (list(up_index)) == []:
                continue
            else:
                while True:
                    up_index = np.where(volatility[i]>up)[0]
                    if (list(up_index)) == [] and sum(volatility[i])>0.999 and sum(volatility[i])<1.001:
                        break
                    mask = np.ones_like(volatility[i], dtype=bool)
                    mask[up_index] = False
                    L = sum(volatility[i][mask]) #L for si(F/L)
                    F = 1-((lb*(portfolio_size-len(up_index))) + (up*(len(up_index)))) #F for si(F/L)
                    for j in range(len(volatility[i])):
                        if volatility[i][j]>=up:
                            volatility[i][j] = up
                        else:
                            volatility[i][j] = lb + (volatility[i][j] * (F/L))
    for j in range(portfolio_size):
        copy_portfo[1][j] = volatility[0][j]
    return copy_portfo