from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import os

# Base directory for reliable relative path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

template_dir = os.path.join(BASE_DIR, "templates")
if not os.path.exists(template_dir):
    for candidate in [
        os.path.join(os.getcwd(), "crop_project", "templates"),
        os.path.join(os.getcwd(), "templates"),
        os.path.join(os.path.dirname(BASE_DIR), "crop_project", "templates"),
        os.path.join(os.path.dirname(BASE_DIR), "templates")
    ]:
        if os.path.exists(candidate):
            template_dir = candidate
            break

static_dir = os.path.join(BASE_DIR, "static")
if not os.path.exists(static_dir):
    candidate_static = os.path.join(os.path.dirname(BASE_DIR), "static")
    if os.path.exists(candidate_static):
        static_dir = candidate_static
    else:
        static_dir = None

app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir
)

# Robust model path resolution
possible_model_paths = [
    os.path.join(BASE_DIR, "yield_model.pkl"),
    os.path.join(os.getcwd(), "crop_project", "yield_model.pkl"),
    os.path.join(os.getcwd(), "yield_model.pkl"),
    os.path.join(os.path.dirname(BASE_DIR), "crop_project", "yield_model.pkl"),
    os.path.join(os.path.dirname(BASE_DIR), "yield_model.pkl")
]

MODEL_PATH = None
for path in possible_model_paths:
    if os.path.exists(path):
        MODEL_PATH = path
        break

model = None
if MODEL_PATH:
    try:
        model = joblib.load(MODEL_PATH)
        print(f"Model loaded successfully from: {MODEL_PATH}")
    except Exception as e:
        print(f"Error loading model from {MODEL_PATH}: {e}")
        model = None
else:
    print("Warning: yield_model.pkl not found in expected locations.")


# Home Page
@app.route('/')
def home():
    return render_template("index.html")


# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        error_msg = "Model is not loaded. Please verify 'yield_model.pkl' exists."
        if request.is_json:
            return jsonify({"status": "error", "message": error_msg}), 500
        return f"Error: {error_msg}", 500

    try:
        # Extract inputs from either JSON or Form Data
        if request.is_json:
            data = request.get_json() or {}
            region = data.get('Region')
            soil_type = data.get('Soil_Type')
            crop = data.get('Crop')
            weather = data.get('Weather_Condition')
            rainfall = float(data.get('Rainfall_mm', 0))
            temperature = float(data.get('Temperature_Celsius', 0))
            fertilizer_raw = data.get('Fertilizer_Used')
            irrigation_raw = data.get('Irrigation_Used')
            days = int(data.get('Days_to_Harvest', 0))
        else:
            region = request.form.get('Region')
            soil_type = request.form.get('Soil_Type')
            crop = request.form.get('Crop')
            weather = request.form.get('Weather_Condition')
            rainfall = float(request.form.get('Rainfall_mm', 0))
            temperature = float(request.form.get('Temperature_Celsius', 0))
            fertilizer_raw = request.form.get('Fertilizer_Used')
            irrigation_raw = request.form.get('Irrigation_Used')
            days = int(request.form.get('Days_to_Harvest', 0))

        # Safely parse boolean values
        fertilizer = True if str(fertilizer_raw).lower() in ['1', 'true', 'yes', 'y'] else False
        irrigation = True if str(irrigation_raw).lower() in ['1', 'true', 'yes', 'y'] else False

        # Validate required string inputs
        if not region or not soil_type or not crop or not weather:
            raise ValueError("All categorical fields (Region, Soil Type, Crop, Weather Condition) are required.")

        # Create input dataframe for model prediction
        sample = pd.DataFrame({
            'Region': [region],
            'Soil_Type': [soil_type],
            'Crop': [crop],
            'Weather_Condition': [weather],
            'Rainfall_mm': [rainfall],
            'Temperature_Celsius': [temperature],
            'Fertilizer_Used': [fertilizer],
            'Irrigation_Used': [irrigation],
            'Days_to_Harvest': [days]
        })

        # Run model inference
        prediction = model.predict(sample)
        output = round(float(prediction[0]), 2)

        # Return JSON if requested or form submission
        if request.is_json or request.headers.get('Accept') == 'application/json':
            return jsonify({
                "status": "success",
                "predicted_yield": output,
                "unit": "tons/hectare"
            })

        return f"Predicted Crop Yield: {output} tons/hectare"

    except Exception as e:
        if request.is_json:
            return jsonify({"status": "error", "message": str(e)}), 400
        return f"Error: {str(e)}", 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)