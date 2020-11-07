from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
      return render_template("upi.html")
    else:
      data = request.form["upiid"]
      return redirect(f"/{data}")

@app.route("/<upi>")
def next(upi):
  return render_template("index.html", upi=upi)

if __name__=="__main__":
    #app.debug = True
    app.run(host="0.0.0.0",port=5000,use_reloader=True,threaded=True)
