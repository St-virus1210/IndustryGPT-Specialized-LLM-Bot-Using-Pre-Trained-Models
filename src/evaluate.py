import json, csv
from pathlib import Path

DATA = Path("data/eduassist_dataset.jsonl")

def load():
    with DATA.open(encoding="utf-8") as f:
        return [json.loads(x) for x in f]

if __name__ == "__main__":
    rows = load()
    print("Dataset records:", len(rows))
    cats = {}
    for r in rows:
        cats[r["category"]] = cats.get(r["category"], 0) + 1
    print("Category distribution:")
    for k, v in sorted(cats.items()):
        print(f"  {k}: {v}")
    print("\nEvaluation reminder: create a held-out test set and score actual model outputs for relevance, correctness, and scope handling.")
