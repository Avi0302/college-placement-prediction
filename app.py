from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("placement_model.pkl")

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        iq = float(request.form['iq'])
        prev_sem = float(request.form['prev_sem'])
        cgpa = float(request.form['cgpa'])
        academic = request.form['academic']
        internship = request.form['internship']
        extra_curr = float(request.form['extra_curr'])
        comm_skills = float(request.form['comm_skills'])
        projects = int(request.form['projects'])

        # Encode categorical values
        academic_map = {"Poor": 0, "Average": 1, "Good": 2, "Excellent": 3}
        internship_map = {"No": 0, "Yes": 1}

        input_data = np.array([[iq, prev_sem, cgpa,
                                academic_map[academic],
                                internship_map[internship],
                                extra_curr, comm_skills, projects]])

        prediction = model.predict(input_data)[0]

        result = "✅ You are likely to get placed!" if prediction == 1 else "❌ You may not get placed."
        
        return render_template('result.html', result=result)

# 🔹 Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
