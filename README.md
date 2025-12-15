# DSCI-510-Final-Project_Lihui-Xiong
NYC Property Sale Price Modeling
Course: DSCI 510 – Principles of Programming for Data Science
Author: Lihui Xiong
Date: December 2025

Project Overview:
This project analyzes and models New York City property sale prices using data collected from the NYC Open Data API. The goal is to understand how property size, building type, location (borough), and time-related factors influence sale prices, and to build a predictive linear regression model on log-transformed prices.
The project demonstrates the full data science pipeline required in DSCI 510: API-based data collection, data cleaning, feature engineering, statistical analysis, and visualization using Python.

How to Run the Project:
1) Get Data (API Collection)
python src/get_data.py
2) Clean Data (Preprocessing)
saves the cleaned dataset into data/processed/
python src/clean_data.py
3) Run Analysis (Modeling)
loads the processed dataset and runs the modeling pipeline:
python src/run_analysis.py
4) Produce Visualizations
generates plots used in the report (saved into results/ or displayed depending on implementation), such as:
sale price vs. square feet scatter plot
python src/visualize_results.py
