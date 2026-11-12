"""Conservative, schema-agnostic cleaning for the CMS hospital CSV."""
import argparse
import json
from pathlib import Path
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw/Hospital_General_Information_2.csv")
    parser.add_argument("--output", default="data/processed/hospital_general_information_clean.csv")
    args = parser.parse_args()
    src, dest = Path(args.input), Path(args.output)
    if not src.exists() or src.stat().st_size == 0:
        raise SystemExit(f"Missing or empty input CSV: {src}")
    df = pd.read_csv(src, dtype="string", low_memory=False)
    original_rows = len(df)
    original_cols = list(df.columns)
    # Preserve source column labels; trim surrounding whitespace in text values.
    for col in df.columns:
        df[col] = df[col].str.strip()
        df[col] = df[col].replace("", pd.NA)
    df = df.dropna(how="all")
    rows_after_blank_removal = len(df)
    df = df.drop_duplicates()
    duplicate_rows_removed = rows_after_blank_removal - len(df)
    dest.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(dest, index=False)
    audit = {
        "input": str(src), "output": str(dest),
        "input_rows": original_rows, "rows_after_blank_removal": rows_after_blank_removal,
        "duplicate_rows_removed": duplicate_rows_removed, "output_rows": len(df),
        "columns": original_cols,
        "cleaning_actions": ["trim surrounding whitespace", "convert empty strings to null",
                             "remove fully blank rows", "remove exact duplicate rows"]
    }
    audit_path = dest.parent / "cleaning_audit.json"
    audit_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")
    print(json.dumps(audit, indent=2))

if __name__ == "__main__":
    main()
