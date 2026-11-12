"""Profile the downloaded CMS Hospital General Information CSV."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
import pandas as pd

ID_HINTS = ("provider id", "facility id", "ccn", "cms certification")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw/Hospital_General_Information_2.csv")
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()
    source, out_dir = Path(args.input), Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    if not source.exists():
        print(f"Input file not found: {source}", file=sys.stderr); return 1
    if source.stat().st_size == 0:
        print(f"Input file is empty (0 bytes): {source}", file=sys.stderr); return 2

    # Read as strings initially; this protects provider IDs and leading zeroes.
    df = pd.read_csv(source, dtype="string", low_memory=False)
    df.columns = [re.sub(r"\\s+", " ", str(c)).strip() for c in df.columns]
    id_columns = [c for c in df.columns if any(h in c.lower() for h in ID_HINTS)]
    missing = df.isna().sum().rename("missing_count").to_frame()
    missing["missing_pct"] = (missing["missing_count"] / max(len(df), 1) * 100).round(2)
    missing = missing.sort_values(["missing_pct", "missing_count"], ascending=False)
    report = {
        "source_file": str(source), "file_size_bytes": source.stat().st_size,
        "rows": int(len(df)), "columns": int(len(df.columns)),
        "duplicate_full_rows": int(df.duplicated().sum()),
        "likely_identifier_columns": id_columns, "column_names": list(df.columns),
        "dtypes": {c: str(t) for c, t in df.dtypes.items()},
        "missingness": missing.reset_index(names="column").to_dict(orient="records")
    }
    (out_dir / "data_profile.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    missing.reset_index(names="column").to_csv(out_dir / "missingness_report.csv", index=False)
    print(f"Rows: {len(df):,} | Columns: {len(df.columns):,}")
    print(f"Duplicate full rows: {report['duplicate_full_rows']:,}")
    print(f"Likely ID columns: {id_columns or 'None detected'}")
    print(f"Reports saved in {out_dir}")
    print("Actual columns:")
    for col in df.columns: print(f" - {col}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
