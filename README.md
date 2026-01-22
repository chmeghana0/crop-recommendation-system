📌 Crop Recommendation System

This project is a simple machine learning–based web application that suggests the most suitable crop to grow based on soil and weather conditions.
It is built using Python and Flask and is intended as a beginner-friendly ML deployment project.

📌 About the Project

Agriculture depends heavily on factors such as soil nutrients, temperature, rainfall, and humidity.
Choosing the wrong crop can reduce yield.

This project helps by:

Taking soil and environmental inputs

Processing the data using a trained machine learning model

Predicting the best crop for the given conditions

📌 Technologies Used

Python

Flask

NumPy

Pandas

Scikit-learn

HTML & CSS

📌 Input Details

The following values are taken as input from the user:

Nitrogen (N)

Phosphorus (P)

Potassium (K)

Temperature

Humidity

pH value

Rainfall

📌 How the Project Works

The user enters soil and climate values in the web form.

The input data is scaled using MinMaxScaler and StandardScaler.

A trained machine learning model processes the data.

The predicted crop name is displayed on the webpage.

📌 Running the Project in VS Code

Open the project folder in Visual Studio Code.

Open a new terminal inside VS Code.

Make sure Python is installed on the system.

Install the required libraries such as Flask, Pandas, NumPy, and Scikit-learn.

Run the app.py file from the VS Code terminal.

After the server starts, a local address will be shown in the terminal.

Open that address in a web browser to view the application.

📌 Note

This project may require compatible versions of NumPy and Scikit-learn to run locally, as the machine learning model was trained using specific library versions.
