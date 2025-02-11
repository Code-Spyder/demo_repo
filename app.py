from flask import Flask, render_template, request
import pickle

app=Flask(__name__)

@app.route("/")
def fun1():
    return render_template("info.html")

@app.route("/predict", methods = ["post"])
def fun2():
    nm = request.form['name']
    exp = float(request.form['exp'])
    mymodel = pickle.load(open('model1.pkl', "rb"))
    sal = round(mymodel.predict([[exp]])[0],2)

    #return "<h1> hi {} <br/> your predicted salary is {} </h1>".format(nm,sal)
    return f"<h1> hi {nm} <br/> your predicted salary is {sal} </h1>"
    #return render_template("second.html", name = nm, salary = sal)

if __name__ == "__main__" :
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8888)
      