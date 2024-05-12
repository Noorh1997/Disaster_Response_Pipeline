# Disaster_Response_Pipeline

**Introduction**
This project demonstrates the creation of a machine learning pipeline to classify messages related to disasters into multiple categories. The pipeline includes data processing, model training, and web application development.

**Files**
ETL Pipeline Preparation: Python script for Extract, Transform, Load (ETL) pipeline preparation.
process_data.py
ML Pipeline Preparation: Python script for Machine Learning (ML) pipeline preparation.
train_classifier.py
Flask Web App: Python script for Flask web application development.
run.py
Data Files:
disaster_messages.csv: CSV file containing messages data.
disaster_categories.csv: CSV file containing categories data.
**Instructions**
ETL Pipeline Preparation:
Run the process_data.py script to preprocess the messages and categories data, and store the cleaned data in an SQLite database.
ML Pipeline Preparation:
Run the train_classifier.py script to build and train a machine learning model using the cleaned data.
The trained model will be saved as a pickle file.
Flask Web App:
Run the run.py script to start the Flask web application.
Access the web application in your browser at http://localhost:3000/ to interact with the trained model.
Enter a message in the provided text box, and the model will classify it into relevant categories.
**Dependencies**
Python 3.x
Libraries: pandas, sqlalchemy, scikit-learn, nltk, flask, plotly
**Credits**
This project is part of the Udacity Data Scientist Nanodegree Program.
![image](https://github.com/Noorh1997/Disaster_Response_Pipeline/assets/162990234/09f572a5-eabc-4f44-9e4c-6aaeb99f911b)
