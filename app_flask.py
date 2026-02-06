from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load model and preprocessor
def load_assets():
    try:
        with open('xgboost_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('preprocessor.pkl', 'rb') as f:
            preprocessor = pickle.load(f)
        return model, preprocessor
    except Exception as e:
        print(f"Error loading assets: {str(e)}")
        return None, None

model, preprocessor = load_assets()

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for single prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Prepare input data
        input_data = pd.DataFrame({
            'age': [float(data['age'])],
            'gender': [data['gender']],
            'course': [data['course']],
            'study_hours': [float(data['study_hours'])],
            'class_attendance': [float(data['class_attendance'])],
            'internet_access': [data['internet_access']],
            'sleep_hours': [float(data['sleep_hours'])],
            'sleep_quality': [data['sleep_quality']],
            'study_method': [data['study_method']],
            'facility_rating': [data['facility_rating']],
            'exam_difficulty': [data['exam_difficulty']]
        })
        
        # Transform and predict
        input_processed = preprocessor.transform(input_data)
        prediction = float(model.predict(input_processed)[0])
        
        # Determine grade
        if prediction >= 80:
            grade = 'A'
        elif prediction >= 60:
            grade = 'B'
        elif prediction >= 40:
            grade = 'C'
        else:
            grade = 'D'
        
        # Determine status
        if prediction >= 80:
            status = 'Excellent'
        elif prediction >= 60:
            status = 'Good'
        elif prediction >= 40:
            status = 'Average'
        else:
            status = 'Needs Improvement'
        
        return jsonify({
            'success': True,
            'score': round(prediction, 2),
            'grade': grade,
            'status': status
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

# Route for batch prediction
@app.route('/batch-predict', methods=['POST'])
def batch_predict():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'success': False, 'error': 'Please upload a CSV file'}), 400
        
        # Read CSV
        df = pd.read_csv(file)
        
        # Required columns
        required_cols = ['age', 'gender', 'course', 'study_hours', 'class_attendance', 
                        'internet_access', 'sleep_hours', 'sleep_quality', 'study_method', 
                        'facility_rating', 'exam_difficulty']
        
        missing = [c for c in required_cols if c not in df.columns]
        if missing:
            return jsonify({'success': False, 'error': f'Missing columns: {", ".join(missing)}'}), 400
        
        # Prepare data
        X = df[required_cols].copy()
        X_processed = preprocessor.transform(X)
        predictions = model.predict(X_processed)
        
        # Add predictions to dataframe
        results = df.copy()
        results['predicted_score'] = predictions
        results['grade'] = results['predicted_score'].apply(
            lambda x: 'A' if x >= 80 else 'B' if x >= 60 else 'C' if x >= 40 else 'D'
        )
        
        # Generate statistics
        stats = {
            'avg_score': round(float(predictions.mean()), 2),
            'max_score': round(float(predictions.max()), 2),
            'min_score': round(float(predictions.min()), 2),
            'std_dev': round(float(predictions.std()), 2),
            'total_records': len(predictions)
        }
        
        # Convert results to HTML table
        results_html = results.to_html(classes='table table-striped table-hover', index=False)
        
        # Generate CSV download
        csv_data = results.to_csv(index=False)
        
        return jsonify({
            'success': True,
            'stats': stats,
            'html_table': results_html,
            'csv_data': csv_data
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    if model is None or preprocessor is None:
        print("Error: Could not load model or preprocessor!")
    else:
        print("✅ Model and preprocessor loaded successfully!")
        print("🚀 Starting Flask app at http://localhost:5000")
        app.run(debug=True, host='localhost', port=5000)
