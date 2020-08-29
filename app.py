from flask import Flask,render_template,request
import pickle
model=pickle.load(open('level.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/login',methods=["POST"])
def func2():
    SBP=request.form['SBP']
    DBP=request.form['DBP']
    Pulse=request.form['Pulse']
    Temperature=request.form['Temperature']
    data=[[int(SBP),int(DBP),int(Pulse),int(Temperature)]]
    pred=model.predict(data)
    print(pred[0])
    if(pred==[0]):
        sug='you are Fine!'
        return render_template("index.html",y=sug)
    if(pred==[1]):
        sug='Need some Medication!'
        return render_template("index.html",y=sug)
    if(pred==[2]):
        sug='Need to Consult Doctor!'
        return render_template("index.html",y=sug)
        #return render_template("index.html",y=("The level :"+str(pred[0])))
if __name__=='__main__':
   app.run(debug= True)
