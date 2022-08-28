import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Housing.csv')
# print(data)

X=data[['Location','Avg_price']]
# print(X)

Y=data[['Price']]
# print(Y)

X.shape
Y.shape

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25)
X_train.shape,Y_train.shape,X_test.shape,Y_test.shape


from sklearn.preprocessing import MinMaxScaler
SS= MinMaxScaler()
SS.fit(X_train)
X_train_scaled= SS.transform(X_train)
X_test_scaled= SS.transform(X_test)
X_train_scaled
X_test_scaled


from sklearn.tree import DecisionTreeClassifier
model_DT=DecisionTreeClassifier()
model_DT.fit(X_train_scaled,Y_train)
Y_predict =model_DT.predict(X_test_scaled)
plt.scatter(X_test[Y_test==0]['Location'],X_test[Y_test==0]['Avg_price'],c='red',alpha=0.7)


