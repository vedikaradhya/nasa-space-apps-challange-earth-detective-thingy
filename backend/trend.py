import io
import os
from typing import Dict, Any

import pandas as pd
import pymannkendall as mk


def analyze_trend_from_dataframe(df: pd.DataFrame, date_col: str = "date", value_col: str = "value") -> Dict[str, Any]:
    if date_col not in df.columns or value_col not in df.columns:
        raise ValueError(f"DataFrame must contain {date_col} and {value_col}")

    series = df[[date_col, value_col]].dropna().copy()
    series[date_col] = pd.to_datetime(series[date_col])
    series = series.sort_values(date_col)
    values = series[value_col].astype(float).to_numpy()

    if len(values) < 3:
        return {
            "trend": "insufficient_data",
            "p_value": None,
            "slope": None,
            "n": int(len(values)),
            "summary": "Need at least 3 observations to compute a trend.",
        }

    try:
        res = mk.original_test(values, alpha=0.05)
        slope = getattr(res, "slope", None)
        p_value = getattr(res, "p", None)
        trend = str(res.trend).lower() if getattr(res, "trend", None) is not None else "no trend"
        summary = f"Trend={trend}; n={res.n}; p={p_value}; slope={slope}"
        return {
            "trend": trend,
            "p_value": float(p_value) if p_value is not None else None,
            "slope": float(slope) if slope is not None else None,
            "n": int(res.n),
            "summary": summary,
        }
    except Exception:
        # fallback on a coarse linear approximation
        diffs = pd.Series(values).diff().dropna()
        slope_est = float(diffs.mean()) if len(diffs) else 0.0
        trend = "increasing" if slope_est > 0 else "decreasing" if slope_est < 0 else "stable"
        return {
            "trend": trend,
            "p_value": 0.05,
            "slope": slope_est,
            "n": int(len(values)),
            "summary": "Fallback coarse-trend estimation used.",
        }


def load_sample_csv() -> pd.DataFrame:
    sample_path = os.path.join(os.path.dirname(__file__), "sample_data", "co2_sample.csv")
    return pd.read_csv(sample_path)


def csv_to_time_series(data: str) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(data))
