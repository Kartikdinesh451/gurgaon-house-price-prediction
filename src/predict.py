from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODEL = joblib.load(ROOT / "models" / "model.pkl")
PIPELINE = joblib.load(ROOT / "models" / "pipeline.pkl")

def predict(input_csv: str, output_csv: str) -> None:
    data = pd.read_csv(input_csv)
    features = data.drop(columns=["median_house_value"], errors="ignore")
    transformed = PIPELINE.transform(features)
    data["predicted_median_house_value"] = MODEL.predict(transformed)
    data.to_csv(output_csv, index=False)

if __name__ == "__main__":
    predict(
        str(ROOT / "data" / "test_input.csv"),
        str(ROOT / "outputs" / "predictions_from_script.csv"),
    )
