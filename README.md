# Disaster_Response_Pipeline

**Introduction**<br>
- This project demonstrates the creation of a machine learning pipeline to classify messages related to disasters into multiple categories. The pipeline includes data processing, model training, and web application development.
<br>
<br>
<br>
Files <br>  <br>
- ETL Pipeline Preparation: Python script for Extract, Transform, Load (ETL) pipeline preparation : process_data.py <br>
- ML Pipeline Preparation: Python script for Machine Learning (ML) pipeline preparation : train_classifier.py <br>
- Flask Web App: Python script for Flask web application developmen : run.py <br>
- Data Files: <br>
     -  disaster_messages.csv: CSV file containing messages data. <br>
     -  disaster_categories.csv: CSV file containing categories data. <br>
<br>
<br>
<br>
Instructions <br> <br>
- ETL Pipeline Preparation: <br>
    - Run the process_data.py script to preprocess the messages and categories data, and store the cleaned data in an SQLite database. <br>
- ML Pipeline Preparation: <br>
    - Run the train_classifier.py script to build and train a machine learning model using the cleaned data. <br>
    - The trained model will be saved as a pickle file. <br>
- Flask Web App: <br>
    - Run the run.py script to start the Flask web application. <br>
    - Access the web application in your browser. <br>
    - Enter a message in the provided text box, and the model will classify it into relevant categories. <br>
<br>
<br>
<br>
Dependencies <br> <br>
- Python 3.x <br>
- Libraries: pandas, sqlalchemy, scikit-learn, nltk, flask, plotly <br>
<br>
<br>
<br>
Credits <br> <br>
- This project is part of the Udacity Data Scientist Nanodegree Program.
![image](https://github.com/Noorh1997/Disaster_Response_Pipeline/assets/162990234/09f572a5-eabc-4f44-9e4c-6aaeb99f911b)
