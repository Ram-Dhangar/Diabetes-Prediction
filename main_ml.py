from flask import Flask,render_template,request
app =Flask(__name__)
import pickle
import numpy

file=open('diabetes.plk','rb')
#open a file where you stores the pickle data

model=pickle.load(file)
#file close
file.close()
@app.route('/',methods=["GET","POST"])
def form():
    if request.method=="POST":
        myDict = request.form
        print(myDict)
        Gender =int(myDict["Gender"])
        age =int(myDict["age"])
        if Gender==0:
            Pregnence =0
            print(Pregnence)

        else:
            Pregnence =int(myDict["Pregnence"])

        g =int(myDict["g"])
        bp =int(myDict["bp"])
        insulin =int(myDict["insulin"])
        bmi =int(myDict["bmi"])

        if Gender==0:
            li=[[Gender,g,bp,insulin,bmi,age]]

        else:
            li=[[Pregnence,g,bp,insulin,bmi,age]]

        dia_prob =model.predict_proba(li)[0][1]*10000
        print(dia_prob)
       
        

        return render_template("show2.html", dia=dia_prob)

    return render_template("index2.html")   

# @app.route('/home')  
# def home():

#     return render_template("index2.html")   

#render_template("show2.html")
if __name__ == "__main__":
    app.run(debug=True)
     