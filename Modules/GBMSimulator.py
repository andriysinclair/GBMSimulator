import numpy as np

class GBMSimulator:

    def __init__(self, mu,n,T, M, y0, sigma):

        '''
        Initialise parameters for the GBM simulator

        Args:
        mu (int): drift coefficient
        n (int): number of steps
        T (int): time in years
        M (int): number of sims
        y0 (int): initial value
        sigma (int): volatility
        '''
        self.mu = mu
        self.n = n
        self.T=T
        self.M = M
        self.y0 = y0
        self.sigma = sigma

    def simulate(self):
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
        dt = self.T/self.n        

        # simulate using numpy array
        st = np.exp(    
            (self.mu - self.sigma**2 / 2) * dt
                                    + self.sigma*np.random.normal(0, np.sqrt(dt), size=(self.M,self.n)).T
                                )

        # include array of 1's
        st = np.vstack([np.ones(self.M), st])

        st = self.y0 * st.cumprod(axis=0)

        return st

