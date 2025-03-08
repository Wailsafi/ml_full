# House Price Prediction - Machine Learning Model

## Overview
This project is a **Flask-based web application** that utilizes a **machine learning model** to predict house prices based on input features. The model is trained and deployed using `pickle` for serialization, allowing real-time predictions via a web interface and an API endpoint.

## Features
- **Flask Web Interface:** A simple UI for users to input house-related parameters.
- **REST API Endpoint:** JSON-based API for programmatic predictions.
- **Machine Learning Model:** Pre-trained regression model for price estimation.
- **Scalability:** Uses a `scaler.pkl` file to preprocess input features consistently.

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed along with the following dependencies:

```bash
pip install flask numpy pandas scikit-learn pickle5
```

### Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Wailsafi/ml_full.git
   cd ml_full
   ```
2. Ensure the required model files (`regmodel.pkl` and `scalar.pkl`) are present.
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## API Usage
### Predict via API
Send a **POST** request to `http://127.0.0.1:5000/predict_api` with JSON data



## Project Structure
```
ml_full/
│-- app.py              # Flask application
│-- regmodel.pkl        # Serialized ML model
│-- scalar.pkl          # Scaler for preprocessing
│-- templates/
│   └── home.html       # HTML for web UI
```


