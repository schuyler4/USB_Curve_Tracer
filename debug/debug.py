import pandas as pd
import matplotlib.pyplot as plt

the_data = pd.read_csv('./term_trace.csv')
array = the_data.to_numpy()

print(array[:,0])

plt.plot(array[:,1], array[:,0])
plt.show()

def delta(series):
    deltas = []
    for i, _ in enumerate(series):
        if(i != len(series) - 1):  
            deltas.append(series[i+1] - series[i])
    return deltas

print(delta(array[:,1]))
