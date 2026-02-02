Crop Recommendation System
Project Overview

The Crop Recommendation System is a machine learning based web application that recommends the most suitable crop to grow based on soil nutrients and weather conditions.
It helps improve crop selection and agricultural productivity by analyzing environmental factors.

This project is built using Python and Flask and is intended as a beginner friendly machine learning deployment project.

About the Project

Agriculture depends heavily on factors such as soil nutrients, temperature, rainfall, and humidity.
Choosing the wrong crop for a given environment can lead to reduced yield.

This project helps by taking soil and environmental inputs from the user, processing the data using a trained machine learning model, and predicting the best crop for the given conditions.

Technologies Used

Python
Flask
NumPy
Pandas
Scikit learn
HTML and CSS

Input Details

The following values are taken as input from the user.

Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
pH value
Rainfall

How the Project Works

The user enters soil nutrient and climate values through the web form.

The input data is preprocessed using MinMaxScaler and StandardScaler.

The trained machine learning model processes the data.

The predicted crop name is displayed on the webpage.

Running the Project in Visual Studio Code

Open the project folder in Visual Studio Code.

Open a new terminal inside Visual Studio Code.

Make sure Python is installed on the system.

Install the required libraries using the command shown below.

pip install flask numpy pandas scikit-learn

Run the application using the following command.

python app.py

After the server starts, a local URL will appear in the terminal.

Open the URL in a web browser to view the application.

Note

This project may require compatible versions of NumPy and Scikit learn, as the machine learning model was trained using specific library versions.
