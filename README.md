# Machine Learning-Powered Insider Threat Detection System for Organizational Security and Risk Management
Machine learning-powered system for detecting anomalous insider activities and identifying potential organizational security threats using user behavior analysis.
## Project Overview

This project presents a machine learning-powered insider threat detection system designed to identify potentially malicious or anomalous user behavior within an organization. The system analyzes user activity and behavioral characteristics to distinguish between normal and potentially threatening activities.

The proposed system applies machine learning techniques to security-related behavioral data and evaluates multiple models for insider threat detection. It also provides a web-based interface for analyzing user inputs and generating threat predictions.

The system aims to improve organizational security by supporting early detection of suspicious behavior, reducing dependency on traditional rule-based detection methods, and helping security teams prioritize potential threats.
## Objectives

- Detect potentially malicious or anomalous insider behavior using machine learning techniques.
- Analyze user activity and behavioral patterns to identify suspicious activities.
- Compare multiple machine learning models for insider threat detection.
- Reduce false positives and improve the prioritization of potential security threats.
- Provide a web-based interface for user input and threat prediction.
- Support organizations in improving security monitoring and risk management.
## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Deep Learning:** TensorFlow / Keras
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Web Framework:** Flask
- **Frontend:** HTML, CSS
- **Development Environment:** Jupyter Notebook / Anaconda
- **Model Serialization:** Pickle
- **Dataset:** CSV-based user behavioral and security-related data
## Machine Learning Models

The system evaluates multiple machine learning and deep learning models to analyze user behavior and identify potential insider threats.

- **Random Forest:** Used for classification of normal and potentially threatening user behavior.
- **Decision Tree:** Used to generate interpretable classification decisions based on user activity features.
- **XGBoost:** Used as a gradient boosting model for threat classification.
- **Convolutional Neural Network (CNN):** Used as a deep learning approach for threat classification.

The trained models are saved and integrated into the application to support threat prediction.
## Dataset

The project uses a CSV-based dataset containing user behavioral and security-related attributes for insider threat detection.

The dataset is used for:

- Data preprocessing and cleaning
- Exploratory data analysis
- Feature analysis and visualization
- Training machine learning and deep learning models
- Evaluating model performance
- Predicting potential insider threat behavior

The dataset used in the project is provided as `psychometric.csv`.

## System Workflow

The system follows the following workflow:

1. **User Data Collection** – Collect relevant user behavioral and security-related attributes.
2. **Data Preprocessing** – Clean the dataset, handle required transformations, and prepare the input features.
3. **Feature Scaling** – Scale the input features using the trained scaler.
4. **Model Prediction** – Pass the processed data through the trained machine learning/deep learning models.
5. **Threat Classification** – Classify the user's behavior based on the model prediction.
6. **Result Generation** – Display the predicted threat status through the web-based application.
7. **Security Analysis** – Use the prediction to support identification and prioritization of potentially suspicious behavior.
## Results

The developed system analyzes user behavioral and security-related data and generates predictions to identify potentially suspicious insider activities.

The project includes multiple visualizations to support data analysis and understand behavioral patterns, including:

- **Heatmap** – Shows relationships and correlations between dataset features.
- **Pairplot** – Provides visual analysis of relationships between important features.
- **Boxplot** – Helps identify feature distributions and potential outliers.
- **Violin Plot** – Shows the distribution and variation of behavioral features.
- **Threat Count Visualization** – Represents the distribution of detected threat and non-threat cases.

The trained machine learning models are integrated into the Flask-based application to provide threat predictions through a web interface.
