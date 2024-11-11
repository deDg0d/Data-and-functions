



def score_mcdm(sol,sol_list):
    # print('ini',sol,sol_list,len(sol)) #uncomment for verificatrion
    while len(sol)!=cardinality:
        elm_score = []
        candidate_clusters = list({best_cluster_corr[clustered[int(elm)]][i]   for elm in sol  for i in range(cluster_checker)}) #adding candidate clusteres
        portfolio_groups = [clustered[int(elm)] for elm in sol_list] #grouping portfolios stock groups
        for elm in candidate_clusters:
            score = 0
            for group in portfolio_groups:
                score+=score_clusters[elm][group]
            elm_score.append(score)
        candidates = cluster_matrix[candidate_clusters[np.argsort(elm_score)[::-1][0]]]
        # print(candidate_clusters[np.argsort(elm_score)[::-1][0]])
        candidates = list(set(candidates) - sol) #deleting picked stocks
        corr_score = [0] * len(candidates)
        for stock in sol:
            for i in range(len(candidates)):
                corr_score[i]+=corr[int(stock)][candidates[i]]
        # print(corr_score)
#                          ------------------------------------------SAW section------------------------------------
        sharpe_container = [sharpe_ratio[stock] for stock in candidates] #gather sharpe ratio input for mcdm
        max_sharpe = max(sharpe_container)
        min_corr_score = min(corr_score)
        sharpe_container = [sharpe/max_sharpe  for sharpe in sharpe_container] #normalize => the sharpe ratios | profit type
        normal_corr_score = [min_corr_score/score for score in corr_score] #normalize => the correlation score | cost type
        corr_weight = 1-sharpe_weight
        sharpe_container = [sharpe*sharpe_weight for sharpe in sharpe_container]
        normal_corr_score = [corr*corr_weight for corr in normal_corr_score]
        saw_score = [sharpe_container[i]+normal_corr_score[i] for i in range(len(candidates))] #calculating overal score
        sol.add(candidates[saw_score.index(max(saw_score))]) #add best candidates
        for i in range(len(sol_list)):
            if list(sol_list).count(sol_list[i])>1:
                sol_list[i] = candidates[saw_score.index(max(saw_score))]
                break
        # print('finale--------',sol,sol_list,len(sol)) #uncomment for verificatrion
    return sol