# Forest Fire Weather Index Prediction

## Overview
The Forest Fire Weather Index (FWI) Prediction project is a machine learning-based web application that predicts the Fire Weather Index using meteorological and environmental data. The goal is to provide a tool that helps assess fire risk levels based on key weather parameters.

## Problem Statement
Forest fires are catastrophic events that can cause massive destruction. Predicting the Fire Weather Index (FWI) is crucial for early prevention and mitigation strategies. This project aims to develop an ML-based web application that accurately predicts FWI using supervised learning models.

## Goals
- Develop an interactive web application for FWI prediction.
- Implement a machine learning model for accurate predictions.
- Perform exploratory data analysis (EDA) to identify key influencing factors.
- Optimize feature selection for improved model performance.
- Deploy the model in a user-friendly Flask-based web interface.

## Tech Stack

### Frontend
- HTML, CSS, JavaScript - For building the UI.
- Bootstrap - For styling and responsiveness.

### Backend
- Flask - Python-based web framework for handling user interactions.
- scikit-learn - Machine learning library for model training.
- numPy, pandas - Data manipulation and analysis.
- pickle - For model serialization and loading.

### Machine Learning
- Supervised Learning - Regression model for numerical prediction.
- Ridge Regression - Used for prediction to prevent overfitting.
- StandardScaler - Used for data normalization.

## Data Collection & Processing
The dataset used for training the model consists of meteorological and environmental features:
- Temperature (°C)
- Relative Humidity (%)
- Wind Speed (km/h)
- Rainfall (mm)
- Fine Fuel Moisture Code (FFMC)
- Duff Moisture Code (DMC)
- Initial Spread Index (ISI)
- Classes (Fire/No Fire classification)
- Region (Encoded numeric values)

### Exploratory Data Analysis (EDA)
- Identified missing values and outliers.
- Analyzed the correlation between features and the FWI.
- Visualized data distributions and trends using histograms, scatter plots, and heatmaps.

### Feature Engineering & Selection
- Standardized numerical features using StandardScaler.
- Performed feature selection to remove redundant attributes.
- Converted categorical variables into numeric representations.

## Model Training & Evaluation
- Used Ridge Regression for modeling FWI prediction.
- Split data into training and testing sets.
- Evaluated model performance using Mean Squared Error (MSE) and R-squared values.
- Optimized hyperparameters for better accuracy.

## Web Application
The Flask-based web app provides an interactive UI for users to input weather parameters and get predictions.

### Home Page ('index.html')
- Displays project title and description.
- Provides a button to navigate to the prediction page.
- Contains background images related to forest fires.

### Prediction Page ('home.html')
- Accepts user inputs for meteorological parameters.
- Displays the predicted Fire Weather Index.
- Shows error messages in case of incorrect inputs.

### Backend Logic ('application.py')
- Loads pre-trained Ridge Regression model (ridge.pkl).
- Loads StandardScaler (scaler.pkl) for data preprocessing.
- Handles form inputs and prediction requests.
- Renders results on the home.html page.

## Running the Application
### Step 1: Install Dependencies
```
pip install flask numpy pandas scikit-learn
```

### Step 2: Run the Flask App
```
python application.py
```

### Step 3: Open in Browser
Visit: 'http://127.0.0.1:5000/'

## Future Enhancements
- Implement deep learning models for better accuracy.
- Integrate real-time weather data from APIs.
- Improve UI/UX with enhanced visualizations.
- Deploy the app to a cloud platform (AWS, Heroku, etc.)

