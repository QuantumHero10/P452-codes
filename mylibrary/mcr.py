# Monte Carlo integration function
import numpy as np

def main(f,a,b,rng):

    # Generate random samples within the integration range a to b
    x_values = np.array(rng)
    
    x_values = x_values*(b-a) + a  # To convert random numbers from 0 to 1 range to the required range a to b

    # Evaluate the function at each sample point
    y_values = [f(x) for x in x_values]
    
    # Estimate the integral using Monte Carlo integration
    integral_approximation = (sum(y_values[:])/len(y_values)) * (b-a)
    
    return integral_approximation
