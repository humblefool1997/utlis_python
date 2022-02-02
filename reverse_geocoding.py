import what3words
import pandas as pd 

geocoder = what3words.Geocoder("5R3TRHSD")
df = pd.read_csv('dataset.csv')
X = df['X']
Y = df['Y']
x = list(X)
y = list(Y)

Address = []
for i in range(len(x)):
  
  res = geocoder.convert_to_3wa(what3words.Coordinates(x[i],y[i]))
  Address.append(res['nearestPlace'])
print(Address)
