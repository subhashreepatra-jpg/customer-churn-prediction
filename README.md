# Customer Churn Prediction Using Machine Learning

## Project Overview

This project focuses on predicting customer churn in the banking sector using machine learning techniques. The project analyzes customer demographic, financial, and account-related information to identify patterns associated with customer churn.

## Objectives

- Analyze customer churn patterns.
- Identify important factors associated with churn.
- Perform exploratory data analysis.
- Develop a machine learning model for churn prediction.
- Compare Random Forest and Logistic Regression.
- Evaluate model performance using accuracy, confusion matrix, classification report, and AUC.
- Identify important features influencing churn prediction.

## Dataset

The dataset contains banking customer information including:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Status
- Active Membership
- Estimated Salary
- Customer Churn Status

The target variable is `Exited`.

## Machine Learning Models

### Random Forest Classifier

Accuracy: 86.35%

AUC: 0.85

### Logistic Regression

Accuracy: 80.45%

AUC: 0.77

## Key Findings

- Overall churn rate: 20.37%
- Female churn rate: 25.07%
- Male churn rate: 16.40%
- Germany had the highest churn rate: 32.44%
- Age group 51–60 had the highest churn rate: 56.21%
- Age group 18–30 had the lowest churn rate: 7.50%
- Age was the most important feature in the Random Forest model.

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Machine Learning
- Data Visualization

## Project Files

- Customer Churn Project.ipynb — Machine learning analysis and implementation.
- Customer Churn Report.pdf — Complete project report.
- Customer Churn Report.docx — Editable project report.

## Conclusion

The Random Forest model performed better than Logistic Regression and achieved 86.35% accuracy with an AUC of 0.85. The project demonstrates how machine learning can be used to analyze customer churn and support customer-retention strategies.
