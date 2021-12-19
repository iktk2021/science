from flask import  Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def index():
    image=request.args.get("images/cover.jpg")
    return render_template("basic.html",image=image)
@app.route("/solids")
def solids():  
    return render_template("solids.html")
@app.route("/liquids")
def liquids():
    return render_template("liquids.html")
@app.route("/gases")
def gases():
    return render_template("gases.html")
@app.route("/phases_of_changes")
def phases():
    return render_template("phasesofchanges.html")
@app.route("/phases_of_changes/melting")
def melting():
    return render_template("melting.html")
@app.route("/phases_of_changes/freezing")
def freezing():
    return render_template("freezing.html")
@app.route("/phases_of_changes/evaporating")
def evaporating():
    return render_template("evaporating.html")
@app.route("/phases_of_changes/boiling")
def boiling():
    return render_template("boiling.html")
@app.route("/phases_of_changes/condensation")
def condensation():
    return render_template("condensation.html")
@app.route("/phases_of_changes/sublimation")
def sublimation():
    return render_template("sublimation.html")
@app.route("/phases_of_changes/desposition")
def desposition():
    return render_template("desposition.html")
@app.route("/credit")
def credit():
    return render_template("credits.html")
if __name__=="__main__":
    app.run()                                               