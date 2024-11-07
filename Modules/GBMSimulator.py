import numpy as np

class GBMSimulator:

    def __init__(self):
        pass
        '''
        Initialises Instance of GBMSimulator class
        '''

    def simulate(self, mu,n,T, M, y0, sigma):
        """
        A function to simulate geometric Brownian motion for given  

        Args:
            mu (int): drift coefficient
            n (int): number of steps
            T (int): time in years
            M (int): number of sims
            y0 (int): initial value
            sigma (int): volatility

        Returns:
            array: M different paths simulated by geometric brownian motion, each path taking n timesteps

        Example:
            >>> simulator = GBMSimulator(mu=0.1, n=1000, T=1, M=10, y0=100, sigma=0.2)
            >>> paths = simulator.simulate()
            >>> paths.shape
            (1001, 10)

        """    
        # calculate each time step
        dt = T/n        

        # simulate using numpy array
        st = np.exp(    
            (mu - sigma**2 / 2) * dt
                                    + sigma*np.random.normal(0, np.sqrt(dt), size=(M,n)).T
                                )

        # include array of 1's
        st = np.vstack([np.ones(M), st])

        st = y0 * st.cumprod(axis=0)

        return st

