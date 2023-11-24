# Project README

## Project Overview

This project consists of two main components: a Jupyter notebook (`Project.ipynb`) and a Flask web application (`website.py`). The primary goal is to read data from a CSV file named `SalaryPrediction.csv`, store it in an SQLite database named `salary`, and create a website to showcase the dataset.

## Project Structure

### 1. Project.ipynb

- **Responsibility**: Reading data from the CSV file and storing it in an SQLite database.
- **Steps**:
  - Utilizes the pandas library to read data from `SalaryPrediction.csv`.
  - Connects to an SQLite database named `salary`.
  - Creates a table named `salaries` and inserts the data into it.

### 2. website.py

- **Responsibility**: Creating a Flask web application with three routes: Homepage, Dataset Page, and About Page.
- **Routes**:
  - **Homepage**: Default landing page with links to navigate to the Dataset and About pages.
  - **Dataset Page**: Displays data from dthe SQLite database, allowing users to adjust the number of visible records.
  - **About Page**: Provides information about the dataset's source and schema.

### 3. templates

- **Folder**: Contains HTML pages to be served by the Flask application.

## Methodology

1. **Data Extraction and Storage**:
   - Data is extracted from the CSV file (`SalaryPrediction.csv`) using the pandas library.
   - The data is then stored in an SQLite database (`salary`) using the sqlite3 library.

2. **Web Application**:
   - A Flask web application is created to showcase the dataset.
   - Three routes are defined: Homepage, Dataset Page, and About Page.

3. **Dataset Page Functionality**:
   - The Dataset Page reads data from the SQLite database using the sqlite3 library.
   - The number of visible records on the dataset page can be adjusted dynamically.

## How to Run the Project

1. Run the Jupyter notebook `Project.ipynb` to extract and store the data in the SQLite database.
2. Execute the Flask web application by running the `website.py` file.
3. Access the website through the provided routes: Homepage, Dataset Page, and About Page.

Feel free to explore the code in both files (`Project.ipynb` and `website.py`) for more details on the implementation.

## Dependencies

- Mentioned in requiremnts.txt
