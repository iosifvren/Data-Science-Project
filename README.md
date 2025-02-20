# Project README

## Overview

This project is designed to manage and analyze recruitment data. It includes various scripts and SQL files to generate, process, and visualize data, as well as to create and manage a database.

## Scripts

### `generate_analytics.py`

This script reads CSV files containing recruitment data, combines them into a single DataFrame, and performs various analyses. It generates an Excel file with the data, summary statistics, and a correlation matrix. Additionally, it creates visualizations such as histograms, pair plots, and box plots, and saves them as images.

### `generate_big_data.py`

This script generates complex dummy data for recruitment analysis. It creates multiple CSV files with random data for various recruitment metrics such as time to hire, time to recruit, candidate experience, and interview scores.

### `import_os.py`

This script sets up the necessary directory structure for the project. It creates folders for storing CSV files, images, SQL datasets, and model results.

### `ML.py`

This script performs machine learning analysis on the recruitment data. It preprocesses the data, trains a `RandomForestRegressor` model, evaluates the model, and saves the results. The results include predictions, mean squared error, and R^2 score, which are saved in a CSV file and an Excel file.

### `readme.py`

This script generates a README file for the project. It reads the contents of the source and SQL directories, and includes the content of each file in the README.

### `Summary.py`

This script generates a summary of the recruitment data. It calculates various metrics such as the count of candidates, average time to hire, and average interview scores, and saves the summary in an Excel file.

### `visuals.py`

This script creates visualizations for the recruitment data. It generates histograms and box plots for various metrics and saves them as images.

### `VB_code.vb`

This script creates pivot tables in an Excel workbook. It reads data from a worksheet, creates a new worksheet for the pivot tables, and sets up the pivot tables to summarize the data.

### `diraarange.ps1`

This PowerShell script organizes the project directory by moving all Excel files to a specific folder.

## SQL Files

### `CREATE DATABASE RecruitmentDB.sql`

This SQL script creates a database named `ProjectDataScience` and defines the schema for the project. It creates tables for candidates, summary metrics, file management, and pivot table data.

### `cross-check.sql`

This SQL script selects all data from the tables in the `ProjectDataScience` database to verify the data.

### `INSER OTHERS.sql`

This SQL script inserts summary metrics and file management data into the `ProjectDataScience` database.

### `INSERT CANDIDATES.sql`

This SQL script inserts candidate data into the `Candidates` table in the `ProjectDataScience` database.
