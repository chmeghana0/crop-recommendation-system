from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))
mx = pickle.load(open('minmaxscaler.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values
        N = request.form.get('Nitrogen')
        P = request.form.get('Phosphorus')  # FIXED SPELLING
        K = request.form.get('Potassium')
        temperature = request.form.get('Temperature')
        humidity = request.form.get('Humidity')
        ph = request.form.get('pH')
        rainfall = request.form.get('Rainfall')

        # Debugging: Print received inputs
        print("Received Inputs: ", N, P, K, temperature, humidity, ph, rainfall)

        # Validate inputs
        if None in [N, P, K, temperature, humidity, ph, rainfall]:
            return "Error: Missing input values. Please fill all fields in the form."

        # Convert to float
        N, P, K = float(N), float(P), float(K)
        temperature, humidity, ph, rainfall = float(temperature), float(humidity), float(ph), float(rainfall)

        # Prepare input for model
        single_pred = [[N, P, K, temperature, humidity, ph, rainfall]]

        # Apply transformations
        mx_features = mx.transform(single_pred)
        sc_mx_features = sc.transform(mx_features)

        # Make prediction
        prediction = model.predict(sc_mx_features)

        # Debugging: Print model prediction
        print("Model Prediction: ", prediction[0])

        return render_template("index.html", result=prediction[0])

    except Exception as e:
        print("Error: ", str(e))
        return "An error occurred. Check the console for details."

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
