from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
      data = request.form["upiid"]
      return render_template("index.html", upi=data)
    else:
      return render_template("upi.html")

@app.route("/<upi>")
def next(upi):
  return render_template("index.html", upi=upi)

if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000,use_reloader=True,threaded=True)