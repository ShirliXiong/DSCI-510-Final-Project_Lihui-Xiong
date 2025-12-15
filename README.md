# DSCI-510-Final-Project_Lihui-Xiong
NYC Property Sale Price Modeling

Course: DSCI 510 – Principles of Programming for Data Science

Author: Lihui Xiong

Date: December 2025

Project Overview:
This project analyzes and models New York City property sale prices using data collected from the NYC Open Data API. The goal is to understand how property size, building type, location (borough), and time-related factors influence sale prices, and to build a predictive linear regression model on log-transformed prices.


How to Run the Project:
1) Get Data by API: this step downloads raw NYC property sale data from the NYC Open Data (Socrata) API
2) Clean Data: converts numeric columns; parses dates removes missing data; consolidates building class categories; creates modeling features
4) Run Analysis: loads the processed dataset and runs the modeling pipeline
5) Produce Visualizations: generates plots used in the report, such as: sale price vs. square feet scatter plot
