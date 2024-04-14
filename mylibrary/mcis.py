import numpy as np
import mylibrary.lcg as lcg # Importing LCG pRNG used in Q1
# Monte Carlo integration with importance sampling
def main(f,p,p_inv,N):
    # Generate samples from p
    samples = np.array(lcg.main(572,16381,N))
    X = [p_inv(x) for x in samples]
    
    # Evaluate integral estimate
    f_x = [f(x) for x in X]
    p_x = [p(x) for x in X]
    f_p_x = [x/y for x,y in zip(f_x,p_x)]
    return sum(f_p_x[:])/len(f_p_x)
