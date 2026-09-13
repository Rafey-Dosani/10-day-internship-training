# Day 3 – Facility Dataset Analysis

## Overview

This project performs data cleaning, analysis, and visualization on a facility dataset containing information such as cleanliness, odor, waste levels, water availability, footfall, complaints, and inspection dates.

## Project Structure

```text
day-03/
│
├── data-cleaning/
│   ├── facility_data.csv
│   └── data_cleaning.py
│
├── analysis/
│   ├── facility_analysis.py
│   └── visualizations.py
│
├── visualizations/
│   ├── avg_cleanliness_by_location.png
│   ├── complaints_by_location.png
│   ├── cleanliness_histogram.png
│   ├── footfall_vs_complaints.png
│   └── correlation_heatmap.png
│
└── README.md
```

## Tasks Performed

* Identified missing values
* Checked duplicate records
* Validated numerical and categorical data
* Handled invalid dates
* Detected outliers using the IQR method
* Calculated key statistics
* Performed location-wise analysis
* Generated insights and visualizations

## Key Statistics

The analysis includes:

* Mean
* Median
* Minimum
* Maximum
* Standard Deviation
* Correlation analysis

## Visualizations

* Bar Chart: Average Cleanliness by Location
* Bar Chart: Total Complaints by Location
* Histogram: Cleanliness Score Distribution
* Scatter Plot: Footfall vs Complaints
* Correlation Heatmap

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## How to Run

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

Run the data cleaning script:

```bash
cd data-cleaning
python data_cleaning.py
```

Run the analysis and visualization scripts:

```bash
cd ../analysis
python facility_analysis.py
python visualizations.py
```

## Author

**Mohammad Rafey Dosani**

10-Day Intern Technical Training & Domain Assessment Program
