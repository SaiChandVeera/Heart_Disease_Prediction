from flask import Flask, render_template, request, redirect, url_for, flash, session
import pickle
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_this_in_production'

# Load the saved model
model_path = 'models/heart_prediction_model.pkl'
try:
    with open(model_path, 'rb') as f:
        model_data = pickle.load(f)
        knn_model = model_data['model']
        print("Model loaded successfully!")
except FileNotFoundError:
    print("Model file not found. Using dummy prediction for now.")
    knn_model = None
except Exception as e:
    print(f"Error loading model: {e}")
    knn_model = None

# -------------------------
# Home Page with Login Form
# -------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        # Simple login check (no database)
        if email == "user@gmail.com" and password == "password":
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('predict'))
        else:
            flash('Invalid credentials. Please use email: user@gmail.com and password: password', 'danger')
            return redirect(url_for('home'))
    
    # If user is already logged in, redirect to predict page
    if session.get('logged_in'):
        return redirect(url_for('predict'))
    
    return render_template('login.html')

# -------------------------
# Heart Disease Prediction
# -------------------------
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Check if user is logged in
    if not session.get('logged_in'):
        flash('Please login to access the prediction tool.', 'warning')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        try:
            # Collecting all 13 features with validation
            required_fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                             'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
            
            features = []
            for field in required_fields:
                value = request.form.get(field)
                if value is None or value == '':
                    flash(f'Please fill in the {field} field.', 'danger')
                    return redirect(url_for('predict'))
                features.append(float(value))
            
            # Ensure input dimensions match model expectations
            input_data = np.array([features])
            
            # Make prediction
            if knn_model:
                try:
                    prediction = knn_model.predict(input_data)[0]
                    print(f"Model prediction: {prediction}")
                except Exception as e:
                    print(f"Model prediction error: {e}")
                    # Fallback to dummy prediction
                    prediction = 1 if (features[0] > 50 and features[3] > 140) or features[4] > 240 else 0
            else:
                # Dummy prediction logic if model not available
                # Based on age > 50, high blood pressure > 140, or high cholesterol > 240
                prediction = 1 if (features[0] > 50 and features[3] > 140) or features[4] > 240 else 0
            
            result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
            
            return render_template('result.html', result=result)
            
        except ValueError as e:
            flash('Please enter valid numeric values for all fields.', 'danger')
            return redirect(url_for('predict'))
        except Exception as e:
            flash(f'Error processing prediction: {str(e)}', 'danger')
            return redirect(url_for('predict'))
    
    return render_template('index.html')

# -------------------------
# Logout Route
# -------------------------
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('home'))

# -------------------------
# Error Handlers
# -------------------------
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# -------------------------
# Run the Flask Application
# -------------------------
if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5050)