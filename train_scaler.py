import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Example dataset (Replace with actual training data)
X_train = np.random.rand(100, 7)  # 100 samples, 7 features

# Train the StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)  # Fit it to training data

# Save the scaler as standscaler.pkl
with open("standscaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Scaler saved as 'standscaler.pkl'")
