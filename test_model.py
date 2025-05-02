import pickle

# Step 1: Try to load the model
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Failed to load model:", e)
    exit()

# Step 2: Try to make a sample prediction
try:
    # Replace these values with typical input shape your model expects
    sample_input = [[25, 1, 0, 45000, 1, 2, 4, 5, 560001]]  # Example input
    prediction = model.predict(sample_input)
    print("✅ Prediction successful:", prediction)
except Exception as e:
    print("❌ Failed to predict:", e)

import pickle

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# View model type
print("Model type:", type(model))

# View model structure (example: if it's a DecisionTreeClassifier)
print(model)

# View model parameters
print("Parameters:", model.get_params())
