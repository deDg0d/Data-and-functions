








def most_seen_cc(sol,risk,profit):
    if iteration>max_it/msc_activation:
        clustered_stocks,bp = risk_cluster(sol,risk,profit) #clustering stocks #sol,risk,profit
        rand,candidate,modified,comp_sharp,set_copy,changed = 1,[],[],[],[],[] 
        clustered_set = [set(clustered_stocks[i][1][0]) for i in range(len(clustered_stocks))] #turn all portfolios into sets
#--------------------------------------------------------(pick from stock's own cluster)----------------------------------------------------------------------------------
        if rand==1: #inner clsuter #counting with 89.0: [89.0] [89.0, 20.0] [89.0, 20.0, 79.0] 20 counts twice due to the fact that it apears 2 times with 89 in two differenet portfolios
            copied = copy.deepcopy(clustered_set)
            for i in range(len(clustered_stocks)): #loop over all clustered stocks
                set_copy.append(copied[i])
                if len(set_copy[i])>=cardinality: #cheking for cardinality problems (K_min)
                    continue #if no problem, pass 
                else:
                    # print('triggered------------------------------------------------------------------')
                    changed.append(i)
                    candidate.clear()
                    need = cardinality-len(set_copy[i]) #need = cardinality-len(set_copy[i]) #determine number of missing stocks
                    comparison_set = clustered_set[bp[clustered_stocks[i][0]]:bp[clustered_stocks[i][0]+1]] #create comparison set within cluster
                    # print(i,'------',comparison_set)
                    for stock in set_copy[i]: #pick the deficited stock
                        for j in range(len(comparison_set)): #compare with comparison set elements
                            if stock in comparison_set[j] and len(comparison_set[j]-set_copy[i])!=0: #check if stock appeared in comparison set j and there is unique candidate to compare
                                # print(f' stock {stock} need {need} stock {set_copy[i]} unique {comparison_set[j]-set_copy[i]} set{comparison_set}') #uncomment for verification
                                for seen in comparison_set[j]-set_copy[i]: #count unique stocks to candidate set 
                                    candidate.append(seen) #add seen stock to candidate universe  
                                    # print(set_copy[i],'C*****',candidate,'***',stock)           
                    count = Counter(candidate)
                    # print('count',count,len(count)) 
                    if len(count)<need: #if algo found less stocks than needed
                        # print('deficit')
                        for key in count.keys(): #filling with found ones
                            set_copy[i].add(key)  
                        for new in (random.sample(set(data_list)-set_copy[i],need-len(count))): #filling rest randomly #rechecked
                            set_copy[i].add(new)
                    if len(count) == need: #if found exactly same amount of stocks than needed
                        for key in count.keys():
                            set_copy[i].add(key)
                    if len(count)>need: #if options were more than need
                        comp_sharp.clear()
                        key = np.array([[key,value] for key,value in count.items()]) #sort candidates based on number of repetition 
                        key = key[key[:,-1].argsort()[::-1]] #sort based on seen times [[23. 3.],[87. 2.],[19. 2.],[88. 2.]]
                        # print(key,'need' , need ,len(key[:need]))
                        if key[need-1][1]!=key[need][1]: #if need-th element was not equal to one element after it
                            for chosen in key[:need]: #add first need-th element to clustered-set
                                set_copy[i].add(chosen[0])
                        else: #if need-th element score was equal to need-th+i 
                            for l in range(need): #add first need-th elements #[[23. 4.],[87. 3.],[19. 3.],[88. 3.]] if need was 2: pick first two
                                comp_sharp.append(key[l])
                            for k in range(need,len(key)): #then first rest which have seen 3. times 
                                if key[k][1]!=key[need-1][1]:
                                    break
                                else: #add them until number of repetition change
                                    comp_sharp.append(key[k])
                            picked = 0
                            for k in range(need):
                                # print('pick',picked,'remain',need-picked,'cardinal PB',set_copy[i]) #uncomment for verification
                                if comp_sharp[k][1]!=comp_sharp[need-1][1]: #pick first elemnts that have higher score 
                                    # print('picked',comp_sharp[k][0]) #uncomment for verification
                                    set_copy[i].add(comp_sharp[k][0])
                                    picked+=1
                                else:
                                    best = better_sharpe(comp_sharp[k:len(comp_sharp)]) #pick stocks with higher return to risk ratio
                                    for sharp in best[:(need-picked)]:
                                        set_copy[i].add(sharp[0])
                                    break       
                    # print(f'cc {set_copy[i]} cluster {comparison_set}') #uncomment for verification
            cardinality_handled = replacement(clustered_stocks,set_copy,changed)
            #   print(len(set(cardinality_handled[i][0])),len(set(sol[i][0])))
            return cardinality_handled