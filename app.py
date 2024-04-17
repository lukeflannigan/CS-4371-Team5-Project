from flask import Flask, render_template, request, redirect, jsonify
import pandas as pd  # Ensure all your necessary imports are included
import os

# Create the static directory if it doesn't exist
static_dir = os.path.join(os.getcwd(), 'static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app = Flask(__name__)

# Assuming your model loading and prediction code is in fake_news_model.py
from fake_news_model import lr_model, rf_model, gb_model, tfidf_vectorizer, predict

@app.route('/')
def index():
    return render_template('index.html')  # This will show the form to the user

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        article = request.form['article']
        if article:
            predictions = predict(article, lr_model, rf_model, gb_model, tfidf_vectorizer)
            return render_template('results.html', predictions=predictions)
        else:
            return render_template('index.html', error="Please enter an article for prediction.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
