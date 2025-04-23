import pandas as pd

def generate_main_report(data_list, output_path):
    df = pd.DataFrame(data_list)
    df.to_excel(output_path, index=False)

