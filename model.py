import pandas as pd
data=pd.read_excel(r"C:\Users\C J HARINI\Desktop\Choco cost.xlsx")
from sklearn.linear_model import LinearRegression
a=LinearRegression()
data=data.dropna()
x=data.iloc[: , :-1]
y=data.iloc[: , -1]
a.fit(x,y)
print(data.info())
import pickle
pickle.dump(a,open("model1.pkl","wb"))
