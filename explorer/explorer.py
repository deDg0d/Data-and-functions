import numpy as np
import random

def explorer(sol,stock_rand):
    number = round(int(len(sol)*no))
    optimized = []
    # stock_rand = random.sample(range(0,len(sol)),number) #pick random stock
    equal_weight = assign_weight(1,2) #equal weight (1) #code 2 is for equal weighting
    for i in stock_rand:
        r_to_R = assign_sharpe_weight([sol[i]])[0] #return to risk (2)
        r_to_var = assign_sharpe_variance([sol[i]])[0] #return to variance (3)
        r_p = risk_parity(sol[i]) #risk_parity(4) 
        random_weight = assign_weight() #random weights(5)
        stock_adjuster = [stock for stock in sol[i][0]] #adding and reshaping
        equal_sol = np.array([stock_adjuster + list(equal_weight[0])]).reshape(2,portfolio_size) #adding and reshaping
        random_sol = np.array([stock_adjuster + list(random_weight[0])]).reshape(2,portfolio_size) #adding and reshaping
        fit_ori,fit_r_R,fit_r_var,fit_r_p,fit_rand,fit_equal = fitness([sol[i]]),fitness([r_to_R]),fitness([r_to_var]),fitness([r_p]),fitness([random_sol]),fitness([equal_sol]),
        index_mapper_to_candidates = [r_to_R,r_to_var,r_p,random_sol,equal_sol] #to 
        best_method,best_score,dominator_points,dominator = domination_check(fit_ori,fit_r_R,fit_r_var,fit_r_p,fit_rand,fit_equal) #[r_R,r_var,r_p,rand,equal]
        if best_method == 10: #before:best_score<0
            continue
        if len(dominator_points)!=0:
            for i in range(len(dominator_points)):
                optimized.append(search(sol[i],index_mapper_to_candidates[dominator_points[i][0]],dominator_points[i][1],fit_ori,dominator))
        else:
            optimized.append(search(sol[i],index_mapper_to_candidates[best_method],best_score,fit_ori,dominator))
    return(optimized)