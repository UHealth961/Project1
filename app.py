from flask import Flask, render_template, request
import mysql
import model2 as m

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    disease=[]
    if request.method=="POST":
        symptoms_list=request.form.getlist('my_checkbox')
        symptoms=",".join([i for i in symptoms_list])
        disease=m.predictDisease(symptoms)
    return render_template("symptoms.html", my_disease=disease)

@app.route("/uhealth.html")
def uhealth():
    return render_template("uhealth.html")
    

@app.route("/diseasepredictor.html")
def diseasepredictor():
    return render_template("symptoms.html")

@app.route("/contact-us2.html")
def contactus2():
    return render_template("contact-us2.html")

@app.route("/contact-us.html")
def contactus():
    return render_template("contact-us.html")

@app.route("/homepage.html")
def homepage():
    return render_template("homepage.html")

@app.route("/calculators.html")
def calculators():
    return render_template("calculators.html")

@app.route("/bmicalculator.html")
def bmicalculator():
    return render_template("bmicalculator.html")

@app.route("/bmrcalculator.html")
def bmrcalculator():
    return render_template("bmrcalculator.html")

@app.route("/bodyfatcalculator.html")
def bodyfatcalculator():
    return render_template("bodyfatcalculator.html")

@app.route("/emergency.html")
def emergency():
    return render_template("emergency.html")

@app.route("/findadoctor.html")
def findadoctor():
    return render_template("findadoctor.html")

@app.route("/specialists.html")
def specialists():
    return render_template("specialists.html")

@app.route("/get-started.html")
def getstarted():
    return render_template("get-started.html")

@app.route("/sign-up.html")
def signup():
    return render_template("sign-up.html")

@app.route("/myprofile.html")
def myprofile():
    return render_template("myprofile.html")

@app.route("/services.html")
def services():
    return render_template("services.html")

if __name__ == "__main__":
    app.run(debug=True)

