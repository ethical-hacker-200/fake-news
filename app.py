from flask import Flask, render_template, request, jsonify  
from model import predict_news  

app = Flask(__name__)  

@app.route("/")  
def home():  
    return render_template("index.html")  

@app.route("/predict", methods=["POST"])  
def predict():  
    news_text = request.form["news_text"]  
    result = predict_news(news_text)  
    return jsonify({"prediction": "Fake News" if result == "LABEL_1" else "Real News"})  

if __name__ == "__main__":  
    app.run(debug=True)
