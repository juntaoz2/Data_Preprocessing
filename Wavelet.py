import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import func
from func import wt

data = pd.read_csv("/Users/juntao/Desktop/Apple.csv")

data['Date'] = pd.to_datetime(data.Date)
data = data.sort_values('Date')
time = data['Date']
data = data.set_index('Date')
data = data.loc['2005-01-03':'2014-01-03', :]
d = data['PX_CLOSE'].tolist()

#start plotting
plt.plot(d, 'b')
plt.title('Historical Apple Stock Price')
plt.xlabel('time')
plt.ylabel('stock price')
plt.show()


coe = wt(d, plot = True)
