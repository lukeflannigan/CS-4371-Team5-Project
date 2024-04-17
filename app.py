from flask import Flask, render_template, request, redirect, jsonify
import os
from fake_news_model import predict

# Create the static directory
static_dir = os.path.join(os.getcwd(), 'static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        article = request.form['article']
        if article:
            predictions = predict(article)
            return render_template('results.html', predictions=predictions)
        else:
            return render_template('index.html', error="Please enter an article for prediction.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)