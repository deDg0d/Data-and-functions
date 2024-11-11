



def create_portfo(number=1,size=portfolio_size):
    weight = assign_weight(number)
    if size == portfolio_size:
        stock = [random.sample(range(1,data_num+1), size) for _ in range(number)] #generating stocks
    else:
        stock = []
        for _ in range(number):
            # print('sdd',sorted_sharpe[min(data_num-1,round(random.expovariate(exp_miu_lambda*1)*data_num))][0])
            
            assets = random.choices(range(1,data_num+1),k=random.choice(range(cardinality,portfolio_size+1)))
            assets.extend(random.choices(assets,k = portfolio_size - len(assets)))
            stock.append(assets)
        # stock = np.array(stock)
            
    portfolio = [(stock[i],weight[i]) for i in range(number)] #adding weights to stocks
    portfolio = np.array(portfolio).reshape(number*2 , portfolio_size).reshape(number , 2 , portfolio_size) # 2d array
    return portfolio