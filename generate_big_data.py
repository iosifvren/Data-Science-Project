import os
import pandas as pd
import numpy as np

base_dir = r"C:\Users\a880862\OneDrive - ATOS\Desktop\new proj"

def generate_complex_dummy_data(num_rows):
    np.random.seed(42)
    
    data = {
        'Candidate_ID': np.arange(1, num_rows + 1),
        'Time_to_Hire': np.random.randint(5, 30, size=num_rows),
        'Time_to_Recruit': np.random.randint(10, 60, size=num_rows),
        'Missing_Start_Date': np.random.choice([0, 1], size=num_rows),
        'Active_Demands': np.random.randint(1, 10, size=num_rows),
        'Candidate_Experience': np.random.randint(1, 15, size=num_rows),  
        'Recruiter_ID': np.random.choice(np.arange(1, 50), size=num_rows),  
        'Job_Level': np.random.choice(['Junior', 'Mid', 'Senior'], size=num_rows),
        'Interview_Scores': np.random.randint(1, 501, size=num_rows)  
    }
    
    return pd.DataFrame(data)

for i in range(1, 4):
    df = generate_complex_dummy_data(50)
    df.to_csv(os.path.join(base_dir, 'csvs', f'complex_dummy_data_{i}.csv'), index=False)