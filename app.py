from flask import Flask, request, render_template

import pickle
import numpy as np

app = Flask(__name__)

# Load mode1
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
   try:
    features = [float(x) for x in request.form.values()]
except:
    return render_template("index.html", prediction_text="Invalid Input")
    final_features = np.array([features])
    
    prediction = model.predict(final_features)

    result = "Low Risk" if prediction[0] == 0 else "High Risk"

    return render_template("index.html", prediction_text=result)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
