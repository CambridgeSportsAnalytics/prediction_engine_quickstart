# Standard library imports
import random # For generating random numbers

# Third-party library imports
import numpy as np # For numerical computations and array operations


def get_multi_theta_dataset(num_tasks:int=1, 
                            num_variables:int=10, 
                            num_observations:int=5_000, 
                            _seed:int=random.getrandbits(32),
                            _precision:str="float32"):
    """Generate random sample data for a matrix of independent 
    variables, X, dependent variable, y, and a set of 
    circumstances, Theta.
    
    Parameters
    ----------
    num_tasks : int, optional (default = 1)
        Number of tasks, Q.
    num_variables : int, optional (default = 10)
        Number of independent variables, K.
    num_observations : int, optional (default = 5_000)
        Number of observations in each task, N. 
    seed : int, optional (default = random.getrandbits(32))
        Specify random number generator seed. Recommend using a constant
        for repeatable results, such as 42. 
        Otherwise use random.getrandbits(32).
    _precision: str, optional (default = "float32")
        Specify the precision type for running the analysis, float32
        or float64.

    Returns
    -------
    ndarray [N-by-1]
        Vector of dependent variable (y)
    ndarray [N-by-K]
        Matrix of independent variables (X).
    ndarray [Q-by-K]
        Matrix of circumstances (Theta)
    """    

    # Set the random seed for reproducibility
    np.random.seed(_seed)
    
    # Generate random X matrix with Q rows and k columns
    X = np.random.rand(num_observations, num_variables).astype(_precision)
    
    # Generate random Y values of shape (N, 1)
    y = np.random.rand(num_observations, 1).astype(_precision)
    
    # Generate theta as a random row vector of shape (1, K)
    theta = np.random.rand(num_tasks, num_variables).astype(_precision)
    
    # Print shapes for verification
    _display_dimensions(y, X, theta)
    
    return y, X, theta


def get_multi_y_dataset(num_tasks:int=1, 
                        num_variables:int=7, 
                        num_observations:int=5_000, 
                        _seed:int=random.getrandbits(32),
                        _precision:str="float32"):
    """Generate random sample data for a matrix of independent 
    variables, X, dependent variable, y, and a set of 
    circumstances, Theta.
    
    Parameters
    ----------
    num_tasks : int, optional (default = 1)
        Number of tasks, Q.
    num_variables : int, optional (default = 7)
        Number of independent variables, K.
    num_observations : int, optional (default = 5_000)
        Number of observations in each task, N. 
    seed : int, optional (default = random.getrandbits(32))
        Specify random number generator seed. Recommend using a constant
        for repeatable results, such as 42. 
        Otherwise use random.getrandbits(32).
    _precision: str, optional (default = "float32")
        Specify the precision type for running the analysis, float32
        or float64.

    Returns
    -------
    ndarray [N-by-Q]
        Matrix of dependent variable (Y)
    ndarray [N-by-K]
        Matrix of independent variables (X).
    ndarray [1-by-K]
        Row vector of circumstances (theta)
    """    

    # Set the random seed for reproducibility
    np.random.seed(_seed)
    
    # Generate random X matrix with Q rows and k columns
    X = np.random.rand(num_observations, num_variables).astype(_precision)
    
    # Generate random Y values of shape (N, 1)
    y = np.random.rand(num_observations, num_tasks).astype(_precision)
    
    # Generate theta as a random row vector of shape (1, K)
    theta = np.random.rand(1, num_variables).astype(_precision)
    
    # Print shapes for verification
    _display_dimensions(y, X, theta)
    
    return y, X, theta


def _display_dimensions(y:np.ndarray, X:np.ndarray, theta:np.ndarray):
    """Prints the dimensions of y, X, and theta matrices to terminal
    for verification.

    Parameters
    ----------
    y : ndarray
        Vector or matrix of dependent variable(s).
    X : ndarray
        Vector or matrix of independent variable(s).
    theta : ndarray
        Vector or matrix of circumstance(s).
    """    
    
    print(f"\nY dimensions:     {y.shape},\
            \nX dimensions:     {X.shape},\
            \nTheta dimensions: {theta.shape}\n\n")