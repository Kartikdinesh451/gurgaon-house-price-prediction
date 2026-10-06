# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │   Housing Dataset   │
                    └──────────┬──────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Stratified Train/Test   │
                  │ Split by Income Category│
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   Preprocessing Layer   │
                  │                         │
                  │ Numeric:                │
                  │ Impute → Scale          │
                  │                         │
                  │ Categorical:            │
                  │ One-Hot Encode          │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   Model Comparison      │
                  │                         │
                  │ Linear Regression       │
                  │ Decision Tree           │
                  │ Random Forest           │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   Selected Model        │
                  │ Random Forest Regressor  │
                  └────────────┬────────────┘
                               │
                     ┌─────────┴─────────┐
                     ▼                   ▼
              model.pkl            pipeline.pkl
                     │                   │
                     └─────────┬─────────┘
                               ▼
                     ┌─────────────────┐
                     │ New Input Data  │
                     └────────┬────────┘
                              ▼
                     ┌─────────────────┐
                     │ House Value     │
                     │ Prediction      │
                     └─────────────────┘
```

## Components

- **Data layer:** CSV housing records
- **Preprocessing:** median imputation, standard scaling, one-hot encoding
- **Training:** regression model comparison
- **Persistence:** Joblib model and preprocessing pipeline
- **Inference:** reusable prediction script
- **UI:** Streamlit application
