from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Encoding dictionaries (must match training)
gender_map = {'Male': 1, 'Female': 0}
marital_map = {'Single': 1, 'Married': 2, 'Prefer Not to say': 0}
occupation_map = {'Student': 1, 'Employee': 2, 'Self Employeed': 3, 'House wife': 4}
education_map = {'Graduate': 1, 'Post Graduate': 2, 'Ph.D': 3, 'School': 4, 'Uneducated': 5}
feedback_map = {'Positive': 1, 'Negative': 0}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form.get('age', 0))
        gender = gender_map.get(request.form.get('gender'), 0)
        marital_status = marital_map.get(request.form.get('marital_status'), 0)
        monthly_income = int(request.form.get('monthly_income', 0))
        occupation = occupation_map.get(request.form.get('occupation'), 2)
        education = education_map.get(request.form.get('education'), 0)
        
        family_size = int(request.form.get('family_size', 0))
        review = int(request.form.get('review', 0))
        pincode = int(request.form.get('pincode', 0))

        input_data = [[age, gender, marital_status, monthly_income, occupation, education, family_size, pincode, review]]

        prediction = model.predict(input_data)[0]
        output = "User Will Order Food Online Again" if prediction == 1 else "User Will Not Order Food Again Online"
        prediction_type = "positive" if prediction == 1 else "negative"

        print("INPUT DATA:", input_data)
        print("PREDICTION:", prediction)
        print("Prediction Type:", prediction_type)
        print("prediction_text:", output)

    except Exception as e:
        output = f"Error: {e}"
        prediction_type = None

    return render_template('index.html', prediction_text=output, prediction_type=prediction_type)


if __name__ == "__main__":
    app.run(debug=True)
