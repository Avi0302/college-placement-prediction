# College Placement Prediction

This project predicts student placement outcomes using machine learning. It provides a web interface for users to input student details and receive placement predictions.

## Project Structure

```
app.py                        # Main Flask application
college model.ipynb           # Jupyter notebook for model development
college_student_placement_dataset.csv  # Dataset used for training
placement_model.pkl           # Trained ML model
requirements.txt              # Python dependencies
static/image/placement.jpeg   # Image used in the web app
templates/form.html           # Input form template
templates/result.html         # Result display template
```

## Features
- Predicts placement status based on student data
- User-friendly web interface
- Machine learning model built and trained in Jupyter Notebook

## Setup Instructions
1. Clone the repository:
   ```powershell
   git clone <repo-url>
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```powershell
   python app.py
   ```
4. Open your browser and go to `http://localhost:5000`

## Usage
- Fill in the student details in the form
- Submit to get placement prediction

## License
This project is licensed under the MIT License.

## Author
- [Your Name]
