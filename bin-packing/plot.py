import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'Algorithms':['FirstFit', 'BestFit', 'NextFit', 'WorstFit'], 'Fitness':[0.8429, 0.8739, 0.6123, 0.7432]})

ax = df.plot.bar(x='Algorithms', y='Fitness')

plt.show()