import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle



if __name__ == "__main__":

    df=pd.read_excel("covid.xlsx")
    #reading excel file.
    #print(df.head())
    x=df[["Age","CO-Patient","Diabetes","Feaver"]]
    #above are input items for machine lreaning
    y=df[["Vaccine"]]
    #dependent variable 

    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    len(x_train)
    #dividng data into training and testing split

    reg=linear_model.LogisticRegression()
    #creating instance of Regression
    m=reg.fit(df[["Age","CO-Patient","Diabetes","Feaver"]],df.Vaccine)
    #fitting the best line stored whole model into m variable

    #open a file where you want to store data
    file=open('model.plk','wb')

    #dump information to that file
    pickle.dump(m,file)
    file.close()
    # code for inference
    input=[45,1,0,1]
    VaccProb=m.predict_proba([input])[0][1]
    print(VaccProb)