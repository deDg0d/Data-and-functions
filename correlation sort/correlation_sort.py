




def simple_correlation_sort(sol):
    rand = 1
    changed,comp_sharp = [],[]
    clustered_set = [set(sol[i][0]) for i in range(len(sol))]
    for i in range(len(sol)):

        if rand==1:
            if len(clustered_set[i])>=cardinality:
                continue
            else:
                #while:
                condition = False
                # order_counter = []
                # order_counter.clear()
                need = cardinality - len(clustered_set[i])
                changed.append(i)
                # order = random.sample(clustered_set[i],len(clustered_set[i]))
                sharpe_values = [[elm,sharpe[int(elm)][0]] for elm in clustered_set[i]]  #determine sharpe values
                sharpe_values = sorted(sharpe_values,key=lambda x: x[1])[::-1] 
                # list_clustered_set = [elm for elm in clustered_set[i]]
                order = [elm[0] for elm in sharpe_values] #determine order
                # print('solution',sharpe_values,'order',order) 
                # print('initial',order)
                for j in range(len(order)): #loop through elements of portfolio
                    if condition==True:
                        break
                    for stock in (scs[int(order[j])]): #loop through lowest correlation stocks with order[j] elmenets
                        # print('in loop',order)
                        eligible = 0 #stocks which has lower correlation than corr_threshold with all other stocks
                        if len(clustered_set[i])==cardinality:
                            condition = True
                            break
                        # print('low break',set(order)-set((order[j],9999)))
                        for comp in list(set(order)-set((order[j],9999))): #compare stock element with all other order elements
                            # print('stock',stock[0],'comp',comp,'order',order[j],order,'corr',corr[int(stock[0])][int(comp)]) #uncomment for verification
                            if corr[int(stock[0])][int(comp)]<=corr_threshold: #check if stock have low corr with all other elements
                                eligible+=1
                        # print(eligible,j,len(order)-1,(1-(j/(len(order)-1))))
                        if eligible==len(order)-1:
                            clustered_set[i].add(stock[0])
                            order.append(stock[0])
                            # print(stock,'------------------',len(clustered_set[i]),need,eligible) #uncomment for verification
                        if eligible>=int((1-(j/(len(order)-1)))*(len(order)-1)):
                            clustered_set[i].add(stock[0])
                            order.append(stock[0])
    cardinality_handled = replacement_for_scs(sol,clustered_set,changed)                    
    # [print('finale',len(set(cardinality_handled[i][0]))) for i in range(len(cardinality_handled))] #uncomment for verificatoin
    return cardinality_handled