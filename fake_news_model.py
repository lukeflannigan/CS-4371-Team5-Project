#!/usr/bin/env python
# coding: utf-8

# Import libraries
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, confusion_matrix, roc_auc_score
import xgboost as xgb

# Read the datasets
true_df = pd.read_csv('data/True.csv')
fake_df = pd.read_csv('data/Fake.csv')

# Add a 'label' column to indicate real (1) or fake (0) news
true_df['label'] = 1
fake_df['label'] = 0

# Combine the datasets
combined_df = pd.concat([true_df, fake_df], ignore_index=True)
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Remove duplicates from the dataset
combined_df.drop_duplicates(inplace=True)

# Currently dropping the title, subject, and date columns from the DataFrame - only focusing on the text for model
combined_df.drop(['title', 'subject', 'date'], axis=1, inplace=True)

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>|https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'\bReuters\b', '', text)
    words = text.split()
    stopwords_set = set('your stopwords list here')
    filtered_words = [word for word in words if word not in stopwords_set]
    return ' '.join(filtered_words)

# Apply the preprocessing function to each article text in the DataFrame
combined_df['text'] = combined_df['text'].apply(preprocess_text)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(combined_df['text'], combined_df['label'], test_size=0.2, random_state=42)

# Vectorization
tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Model Training
lr_model = LogisticRegression()
rf_model = RandomForestClassifier()
gb_model = xgb.XGBClassifier()
lr_model.fit(X_train_tfidf, y_train)
rf_model.fit(X_train_tfidf, y_train)
gb_model.fit(X_train_tfidf, y_train)

def create_comparison_graph(models, prob_real, prob_fake, file_path):
    bar_width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))
    index = np.arange(len(models))
    
    bar1 = ax.bar(index, prob_real, bar_width, label='Real', color='blue')
    bar2 = ax.bar(index + bar_width, prob_fake, bar_width, label='Fake', color='red')
    
    # Labels and Titles
    ax.set_title('Probability of Authenticity')
    ax.set_xlabel('Model')
    ax.set_ylabel('Probability (%)')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(models)
    ax.legend()
    
    plt.savefig(file_path)
    plt.close()

# Prediction Function
def predict(article, lr_model, rf_model, gb_model, tfidf_vectorizer):
    preprocessed_article = preprocess_text(article)
    vect_article = tfidf_vectorizer.transform([preprocessed_article])
    
    # Predictions and probabilities
    lr_pred_prob = lr_model.predict_proba(vect_article)[0]
    rf_pred_prob = rf_model.predict_proba(vect_article)[0]
    gb_pred_prob = gb_model.predict_proba(vect_article)[0]
    
    # Arrays for plotting
    models = ["Logistic Regression", "Random Forest", "XGBoost"]
    prob_real = [lr_pred_prob[1]*100, rf_pred_prob[1]*100, gb_pred_prob[1]*100]
    prob_fake = [lr_pred_prob[0]*100, rf_pred_prob[0]*100, gb_pred_prob[0]*100]
    
    # Save the graph
    create_comparison_graph(models, prob_real, prob_fake, 'static/prediction_graph.png')
    
    # Prepare return data
    predictions = {
        'Logistic Regression': {'result': "Real" if lr_pred_prob[1] > 0.5 else "Fake", 'probability': f"{lr_pred_prob[1]*100:.2f}%"},
        'Random Forest': {'result': "Real" if rf_pred_prob[1] > 0.5 else "Fake", 'probability': f"{rf_pred_prob[1]*100:.2f}%"},
        'XGBoost': {'result': "Real" if gb_pred_prob[1] > 0.5 else "Fake", 'probability': f"{gb_pred_prob[1]*100:.2f}%"}
    }
    
    return predictions


