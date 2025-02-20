import pandas as pd
import os

base_dir = r"C:\Users\a880862\OneDrive - ATOS\Desktop\new proj"

csv_files = [os.path.join(base_dir, 'csvs', f) for f in os.listdir(os.path.join(base_dir, 'csvs')) if f.endswith('.csv')]
df_all = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

summary_baseline = {
    'Metric': [
        'Count of Candidates', 
        'Average Time to Hire', 
        'Min Time to Hire', 
        'Max Time to Hire', 
        'Average Time to Recruit', 
        'Min Time to Recruit', 
        'Max Time to Recruit', 
        'Missing Start Date Ratio', 
        'Average Active Demands', 
        'Average Candidate Experience', 
        'Average Interview Scores'
    ],
    'Value': [
        df_all['Candidate_ID'].count(),
        df_all['Time_to_Hire'].mean(),
        df_all['Time_to_Hire'].min(),
        df_all['Time_to_Hire'].max(),
        df_all['Time_to_Recruit'].mean(),
        df_all['Time_to_Recruit'].min(),
        df_all['Time_to_Recruit'].max(),
        df_all['Missing_Start_Date'].mean(),
        df_all['Active_Demands'].mean(),
        df_all['Candidate_Experience'].mean(),
        df_all['Interview_Scores'].mean()
    ]
}

summary_df = pd.DataFrame(summary_baseline)

summary_xlsx_path = os.path.join(base_dir, 'Summary.xlsx')
summary_df.to_excel(summary_xlsx_path, sheet_name='Baseline', index=False)

print(f'Summary baseline saved to {summary_xlsx_path}')