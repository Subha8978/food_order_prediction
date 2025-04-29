from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Encoding dictionaries (must match what was used during model training)
gender_map = {'Male': 0, 'Female': 1}
marital_map = {'Single': 0, 'Married': 1}
occupation_map = {'Student': 0, 'Professional': 1, 'Other': 2}
education_map = {'Undergraduate': 0, 'Graduate': 1, 'Postgraduate': 2}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        gender = gender_map.get(request.form['gender'], 0)
        marital_status = marital_map.get(request.form['marital_status'], 0)
        income = float(request.form['income'])
        occupation = occupation_map.get(request.form['occupation'], 2)
        education = education_map.get(request.form['education'], 0)
        family_size = int(request.form['family_size'])
        review = int(request.form['review'])
        pincode = int(request.form['pincode'])

        input_data = [[age, gender, marital_status, income, occupation, education, family_size, review, pincode]]
        prediction = model.predict(input_data)[0]

        output = "User Will Order Food Online" if prediction == 1 else "User Will Not Order Food Online"
    except Exception as e:
        output = f"Error: {e}"

    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
