from flask import Flask, request, render_template
import pandas as pd
from src.components.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Extract input from form
        input_data = {
            'fixed acidity': [float(request.form.get('fixed_acidity', 0))],
            'volatile acidity': [float(request.form.get('volatile_acidity', 0))],
            'citric acid': [float(request.form.get('citric_acid', 0))],
            'residual sugar': [float(request.form.get('residual_sugar', 0))],
            'chlorides': [float(request.form.get('chlorides', 0))],
            'free sulfur dioxide': [float(request.form.get('free_sulfur_dioxide', 0))],
            'total sulfur dioxide': [float(request.form.get('total_sulfur_dioxide', 0))],
            'density': [float(request.form.get('density', 0))],
            'pH': [float(request.form.get('pH', 0))],
            'sulphates': [float(request.form.get('sulphates', 0))],
            'alcohol': [float(request.form.get('alcohol', 0))]
        }

        # ✅ Create DataFrame from input
        df = pd.DataFrame(input_data)

        # ✅ Initialize and use pipeline
        pipeline = PredictionPipeline()
        prediction = pipeline.predict(df)

        # ✅ Display formatted prediction
        result = f"🍷 Predicted Wine Quality Score: <strong>{prediction[0]:.2f}</strong>"
        return render_template("index.html", prediction_text=result)

    except Exception as e:
        error_msg = f"❌ Error occurred: {str(e)}"
        return render_template("index.html", prediction_text=error_msg)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
