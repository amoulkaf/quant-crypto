import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def nice_angle( a, b, c):
    #expect a, b ,c to be price at 3 consecutive times
    a = np.array([0, a])
    b = np.array([1, b])
    c = np.array([2, c])
    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    print(a)
    print(np.degrees(angle))
    return True


class RsiDivergence:

    @staticmethod
    def nice_peak(df):
        #tries to select only peaks that have a minimum of variation compared to they right and left points
        #calculates the sum of the rise before the peak(%) , and the drop after it , and returns true if it is higher than a minimum
        # a naive way to write it is 2 * df.data - df.data.shift(1) - df.data.shift(-1)) / df.data.mean() > 0.02
        print("shit is ")
        print((2 * df.data - df.data.shift(1) - df.data.shift(-1)) / df.data.mean())
        print("real")
        return True

    def peaks(self, data):
        # Generate a noisy AR(1) sample
        np.random.seed(0)

        rs = data
        xs = []
        for r in rs:
            xs.append(float(r))

        df = pd.DataFrame(xs, columns=['data'])

        # Find local peaks
        # df['min'] = df.data[(df.data.shift(1) > df.data) & (df.data.shift(-1) > df.data)]
        df['max'] = df.data[(df.data.shift(1) < df.data) & (df.data.shift(-1) < df.data) & self.nice_peak(df)]

        # Plot results
        # plt.scatter(df.index, df['min'], c='r')
        plt.scatter(df.index, df['max'], c='g')
        df.data.plot()
        plt.show()