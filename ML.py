from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os
import pandas as pd
from openpyxl import Workbook

base_dir = r"C:\Users\a880862\OneDrive - ATOS\Desktop\new proj"

def load_data(base_dir):
    df_all = pd.concat([pd.read_csv(os.path.join(base_dir, 'csvs', f'complex_dummy_data_{i}.csv')) for i in range(1, 4)], ignore_index=True)
    return df_all

def preprocess_data(df):
    X = df[['Time_to_Recruit', 'Missing_Start_Date', 'Active_Demands', 'Candidate_Experience', 'Interview_Scores']]
    y = df['Time_to_Hire']
    return X, y

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return y_pred, mse, r2

def save_results(y_test, y_pred, mse, r2, base_dir):
    model_results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    model_results.to_csv(os.path.join(base_dir, 'model_results', 'model_predictions.csv'), index=False)
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Machine Learning"
    ws.append(["Metric", "Value"])
    ws.append(["Mean Squared Error", mse])
    ws.append(["R^2 Score", r2])
    
    wb.save(os.path.join(base_dir, 'ML.xlsx'))

def main():
    df_all = load_data(base_dir)
    X, y = preprocess_data(df_all)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    y_pred, mse, r2 = evaluate_model(model, X_test, y_test)
    save_results(y_test, y_pred, mse, r2, base_dir)
    print(f'Mean Squared Error: {mse}')
    print(f'R^2 Score: {r2}')

if __name__ == "__main__":
    main()