import numpy as np
import pandas as pd
import pymannkendall as mk
from typing import Dict

def analyze_trend_from_dataframe(df: pd.DataFrame, date_col: str = 'date', value_col: str = 'value') -> Dict:
    """
    Analyze trend for a time series dataframe using Mann-Kendall and Sen's slope.

    Expects a dataframe with a date column and a numeric value column. Returns a summary dict:
      - trend: 'increasing'|'decreasing'|'no trend'
      - p_value: p-value of the test
      - slope: Sen's slope estimate (if available)
      - n: number of observations
      - summary: textual summary
    """
    if date_col not in df.columns or value_col not in df.columns:
        raise ValueError(f"DataFrame must contain columns {date_col} and {value_col}")

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
            "summary": "Need at least 3 observations to compute a trend."
        }

    # Use pymannkendall's original test (non-seasonal)
    try:
        res = mk.original_test(values, alpha=0.05)
    except Exception:
        # Fallback to simple linear slope if something goes wrong
        slope = float(np.nan)
        trend = "unknown"
        p_value = None
        return {"trend": trend, "p_value": p_value, "slope": slope, "n": int(len(values)), "summary": "Test failed"}

    # Some pymannkendall result objects expose .slope (Sen's slope) on certain methods
    slope = None
    if hasattr(res, 'slope'):
        try:
            slope = float(res.slope)
        except Exception:
            slope = None

    trend = str(res.trend).lower() if res.trend is not None else 'no trend'
    p_value = float(res.p) if hasattr(res, 'p') else None

    summary = f"Mann-Kendall test -> trend={trend}, n={res.n}, p={p_value}, slope={slope}"

    return {
        "trend": trend,
        "p_value": p_value,
        "slope": slope,
        "n": int(res.n),
        "summary": summary
    }


if __name__ == '__main__':
    # quick local test
    import io
    csv = io.StringIO('''date,value
2020-01-01,410
2020-02-01,411
2020-03-01,412
2020-04-01,413
2020-05-01,415
2020-06-01,416
2020-07-01,417
''')
    df = pd.read_csv(csv)
    print(analyze_trend_from_dataframe(df))
