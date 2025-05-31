import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Example dataset (Replace this with your actual dataset)
X_train = np.random.rand(100, 7)  # 100 samples, 7 features

# Train the MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train)  # Fit it to training data

# Save the scaler as minmaxscaler.pkl
with open("minmaxscaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("MinMaxScaler saved as 'minmaxscaler.pkl'")
