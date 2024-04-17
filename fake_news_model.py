import joblib
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Load the trained models
lr_model = joblib.load('pretrained_models/lr_model.pkl')
rf_model = joblib.load('pretrained_models/rf_model.pkl')
gb_model = joblib.load('pretrained_models/gb_model.pkl')

# Load the vectorizer
tfidf_vectorizer = joblib.load('pretrained_models/tfidf_vectorizer.pkl')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>|https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\bReuters\b', '', text)
    words = text.split()
    stopwords_set = set('need to place stop words here')
    filtered_words = [word for word in words if word not in stopwords_set]
    return ' '.join(filtered_words)

def create_comparison_graph(models, prob_real, prob_fake, file_path):
    plt.style.use('seaborn-whitegrid')

    bar_width = 0.35  # Width of the bars
    index = np.arange(len(models))  # The position of bars on the x-axis

    fig, ax = plt.subplots(figsize=(10, 6))

    # Creating bars for "Real" and "Fake"
    bar1 = ax.bar(index, prob_real, bar_width, label='Real', color='blue', alpha=0.8)  # Blue for "Real"
    bar2 = ax.bar(index + bar_width, prob_fake, bar_width, label='Fake', color='red', alpha=0.8)  # Red for "Fake"

    ax.set_title('Probability of Authenticity', fontsize=16, fontweight='bold', color='black', pad=20)
    ax.set_xlabel('Model', fontsize=14, color='black')
    ax.set_ylabel('Probability (%)', fontsize=14, color='black')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(models, fontsize=12, fontweight='bold', color='black')

    ax.legend(frameon=False, fontsize=12, loc='upper left')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#dbdbdb')

    ax.grid(True, which='major', axis='y', linestyle='--', linewidth=0.5, color='grey', alpha=0.5)
    ax.set_axisbelow(True)

    ax.set_facecolor('white')
    fig.set_facecolor('white')

    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()

def predict(article):
    preprocessed_article = preprocess_text(article)
    vect_article = tfidf_vectorizer.transform([preprocessed_article])
    
    lr_pred_prob = lr_model.predict_proba(vect_article)[0]
    rf_pred_prob = rf_model.predict_proba(vect_article)[0]
    gb_pred_prob = gb_model.predict_proba(vect_article)[0]
    
    models = ["Logistic Regression", "Random Forest", "XGBoost"]
    prob_fake = [lr_pred_prob[1], rf_pred_prob[1], gb_pred_prob[1]]
    prob_real = [lr_pred_prob[0], rf_pred_prob[0], gb_pred_prob[0]]
    
    create_comparison_graph(models, prob_real, prob_fake, 'static/prediction_graph.png')
    
    predictions = {
        'Logistic Regression': {'result': "Fake" if lr_pred_prob[1] > 0.5 else "Real", 'probability': lr_pred_prob[1], 'class': 1 if lr_pred_prob[1] > 0.5 else 0},
        'Random Forest': {'result': "Fake" if rf_pred_prob[1] > 0.5 else "Real", 'probability': rf_pred_prob[1], 'class': 1 if rf_pred_prob[1] > 0.5 else 0},
        'XGBoost': {'result': "Fake" if gb_pred_prob[1] > 0.5 else "Real", 'probability': gb_pred_prob[1], 'class': 1 if gb_pred_prob[1] > 0.5 else 0}
    }
    
    return predictions