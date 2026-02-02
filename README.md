Crop Recommendation System
-----
Project Overview
----
The Crop Recommendation System is a machine learning based web application that recommends the most suitable crop to grow based on soil nutrients and weather conditions.
It helps improve crop selection and agricultural productivity by analyzing environmental factors.

This project is built using Python and Flask and is intended as a beginner friendly machine learning deployment project.

About the Project
--------
Agriculture depends heavily on factors such as soil nutrients, temperature, rainfall, and humidity.
Choosing the wrong crop for a given environment can lead to reduced yield.

This project helps by taking soil and environmental inputs from the user, processing the data using a trained machine learning model, and predicting the best crop for the given conditions.

Technologies Used
-----
Python,
Flask,
NumPy,
Pandas
Scikit learn,
HTML and CSS

Input Details
-----
The following values are taken as input from the user.

Nitrogen (N),
Phosphorus (P),
Potassium (K),
Temperature,
Humidity,
pH value,
Rainfall

How the Project Works
-----
1.The user enters soil nutrient and climate values through the web form.

2.The input data is preprocessed using MinMaxScaler and StandardScaler.

3.The trained machine learning model processes the data.

4.The predicted crop name is displayed on the webpage.

5.Running the Project in Visual Studio Code

6.Open the project folder in Visual Studio Code.

7.Open a new terminal inside Visual Studio Code.

8.Make sure Python is installed on the system.

9.Install the required libraries using the command shown below.

10.pip install flask numpy pandas scikit-learn

11.Run the application using the following command.

python app.py
---
After the server starts, a local URL will appear in the terminal.

Open the URL in a web browser to view the application.

Output
--
After submitting the input values, the system displays the name of the most suitable crop for the given soil and weather conditions on the result page.
The output is shown clearly on the web interface, allowing the user to understand the recommended crop easily.

Note
---
This project may require compatible versions of NumPy and Scikit learn, as the machine learning model was trained using specific library versions.

## Key Learnings
This project helped me understand:
- Data preprocessing and feature scaling
- Training and using machine learning models
- Integrating ML models with Flask
- Building and deploying a simple web application

