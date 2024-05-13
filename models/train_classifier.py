"""
ML Pipeline Preparation

This script demonstrates the creation of a machine learning pipeline for classifying messages related to disasters into multiple categories.

The pipeline includes the following steps:
1. Importing libraries and loading data from a database.
2. Defining a tokenization function to process text data.
3. Building a machine learning pipeline using CountVectorizer, TfidfTransformer, and MultiOutputClassifier with RandomForestClassifier.
4. Training the pipeline on the dataset.
5. Testing the model and reporting f1 score, precision, and recall for each output category of the dataset.
6. Improving the model using grid search to find better parameters.

"""

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
import pickle
nltk.download('punkt')
nltk.download('wordnet')

def tokenize(text):
    """
    Tokenization function to process text data.
    
    Args:
    text (str): Input text data.
    
    Returns:
    tokens (list): List of tokenized words.
    """
    
    tokens = word_tokenize(text.lower())
    
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).strip()
        clean_tokens.append(clean_tok)
    
    return clean_tokens

def main():

    engine = create_engine('sqlite:///DisasterResponsePipeline.db')
    df = pd.read_sql_table('DisasterResponseTabel', engine)
    X = df['message']
    
    Y = df.drop(['id', 'message', 'original', 'genre'], axis=1)
       
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),  
        ('tfidf', TfidfTransformer()),  
        ('clf', MultiOutputClassifier(RandomForestClassifier()))  
    ])

    
    parameters = {
        'clf__estimator__n_estimators': [5], 
        'clf__estimator__min_samples_split': [2], 
        'clf__estimator__min_samples_leaf': [1]  
    }

    cv = GridSearchCV(pipeline, param_grid=parameters, cv=2, verbose=3, n_jobs=-1)
    cv.fit(X_train, Y_train)

    Y_pred = cv.predict(X_test)

    for i, col in enumerate(Y_test.columns):
        print(f"Category: {col}\n")
        
        print(classification_report(Y_test[col], Y_pred[:, i]))
        print("="*60)

    with open('model.pkl', 'wb') as f:
        pickle.dump(cv, f)

if __name__ == "__main__":
    main()
