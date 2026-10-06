# Project Workflow

1. Load the housing dataset.
2. Create an income-category column for stratified splitting.
3. Split into training and test data.
4. Separate features and target (`median_house_value`).
5. Impute missing numeric values and scale numeric features.
6. One-hot encode the categorical `ocean_proximity` feature.
7. Compare Linear Regression, Decision Tree and Random Forest.
8. Persist the trained Random Forest and preprocessing pipeline with Joblib.
9. Run inference on the held-out input dataset.
10. Save predictions and evaluate them with RMSE, MAE and R².

See `src/model_comparison.py` for the original model-comparison workflow and
`src/original_main.py` for the training/inference script supplied with the project.
