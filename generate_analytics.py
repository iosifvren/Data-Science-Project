import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlsxwriter

base_dir = r"C:\Users\a880862\OneDrive - ATOS\Desktop\new proj"

csv_files = [os.path.join(base_dir, 'csvs', f'complex_dummy_data_{i}.csv') for i in range(1, 4)]
df_all = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

print(df_all.head())

print(df_all.isnull().sum())

print(df_all.describe())

numeric_df = df_all.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()
print(correlation_matrix)

excel_path = os.path.join(base_dir, 'masterfile.xlsx')
writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')

df_all.to_excel(writer, sheet_name='Data', index=False)

df_all.describe().to_excel(writer, sheet_name='Summary')

correlation_matrix.to_excel(writer, sheet_name='Correlation')

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig(os.path.join(base_dir, 'pngs', 'correlation_matrix.png'))
plt.close()

worksheet = writer.sheets['Correlation']
worksheet.insert_image('K1', os.path.join(base_dir, 'pngs', 'correlation_matrix.png'))


for column in numeric_df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(numeric_df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.savefig(os.path.join(base_dir, 'pngs', f'distribution_{column}.png'))
    plt.close()
    worksheet = writer.sheets['Data']
    worksheet.insert_image(f'K{len(numeric_df.columns) + 2}', os.path.join(base_dir, 'pngs', f'distribution_{column}.png'))

sns.pairplot(numeric_df)
plt.savefig(os.path.join(base_dir, 'pngs', 'pairplot.png'))
plt.close()
worksheet = writer.sheets['Data']
worksheet.insert_image(f'K{len(numeric_df.columns) + 20}', os.path.join(base_dir, 'pngs', 'pairplot.png'))

plt.figure(figsize=(12, 8))
sns.boxplot(data=numeric_df)
plt.xticks(rotation=90)
plt.title('Boxplot of Numerical Columns')
plt.savefig(os.path.join(base_dir, 'pngs', 'boxplot.png'))
plt.close()
worksheet = writer.sheets['Data']
worksheet.insert_image(f'K{len(numeric_df.columns) + 40}', os.path.join(base_dir, 'pngs', 'boxplot.png'))

writer.close()
