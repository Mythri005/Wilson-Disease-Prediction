from flask import Flask, render_template, request
import numpy as np
from joblib import load
from PyPDF2 import PdfReader

app = Flask(__name__)

# Load the trained model
model = load("wilson_model_weights_new.joblib")

# Define the feature names (used in the model)
feature_names = [
    "Age", "Copper in Urine", "Copper in Blood Serum", "Ceruloplasmin Level", 
    "ATB7B Gene Mutation", "Kayser-Fleischer Rings", "Neurological Symptoms Score", 
    "AST", "Cognitive Function Score", "ALT"
]

# Function to extract feature values from the PDF
def extract_values_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Extract numerical values
    lines = text.split("\n")
    values = []
    for feature in feature_names:
        for line in lines:
            if feature in line:
                value = line.split()[-1]  # Assuming the value is at the end of the line
                try:
                    values.append(float(value))
                except ValueError:
                    print(f"Could not parse value for {feature}: {value}")
                    return None
    return np.array(values).reshape(1, -1)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle the uploaded file
        pdf_file = request.files["pdf_file"]
        if pdf_file:
            input_data = extract_values_from_pdf(pdf_file)
            if input_data is not None:
                # Make prediction
                prediction = model.predict(input_data)
                if prediction[0] == 1:
                    return templates("positive.html")  # Redirect to positive result page
                else:
                    return templates("negative.html")  # Redirect to negative result page
            else:
                return "Error: Could not extract feature values from the PDF."
        else:
            return "Error: No file uploaded."
    return render_template("index.html")  # Render the upload page initially

if __name__ == "_main_":
    app.run(debug=True)