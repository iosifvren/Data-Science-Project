import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

base_dir = r"C:\Users\a880862\OneDrive - ATOS\Desktop\new proj"

df_all = pd.concat([pd.read_csv(os.path.join(base_dir, 'csvs', f'complex_dummy_data_{i}.csv')) for i in range(1, 4)], ignore_index=True)

plt.figure(figsize=(10, 6))
sns.histplot(df_all['Time_to_Hire'], bins=15, kde=True)
plt.title('Distribution of Time to Hire')
plt.xlabel('Time to Hire (Days)')
plt.ylabel('Frequency')
plt.savefig(os.path.join(base_dir, 'pngs', 'time_to_hire_distribution.png'))
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_all, x='Candidate_Experience', y='Time_to_Hire')
plt.title('Time to Hire vs. Candidate Experience')
plt.xlabel('Candidate Experience (Years)')
plt.ylabel('Time to Hire (Days)')
plt.savefig(os.path.join(base_dir, 'pngs', 'time_to_hire_vs_experience.png'))
plt.close()