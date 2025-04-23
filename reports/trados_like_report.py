import pandas as pd
import random

def generate_trados_style_report(output_path):
    segments = ["Repetitions", "100% Matches", "Fuzzy (85-99%)", "New"]
    counts = [random.randint(200, 400) for _ in range(4)]
    total = sum(counts)
    percentages = [round(c / total * 100, 2) for c in counts]

    df = pd.DataFrame({
        "Segment Type": segments,
        "Word Count": counts,
        "Percentage": percentages,
        "Notes": [""] * 4
    })

    df.to_excel(output_path, index=False)
