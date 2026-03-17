# Netflix Dataset Analysis

## Overview

This project performs Exploratory Data Analysis (EDA) on a dataset of movies and TV shows available on Netflix. The goal is to analyze trends in content types, genres, ratings, release years, and country distribution to gain insights into streaming media content.

## Dataset

The dataset contains information about movies and TV shows available on Netflix.

**Dataset file:** `netflix_titles.csv`

### Dataset Features

* show_id – Unique ID for each title
* type – Movie or TV Show
* title – Name of the content
* director – Director of the content
* cast – Actors/Actresses
* country – Country where it was produced
* date_added – Date added to Netflix
* release_year – Year of release
* rating – Age rating of the content
* duration – Duration of movie or number of seasons
* listed_in – Genre or category
* description – Short description of the content

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## Project Workflow

1. Import necessary libraries
2. Load and explore the dataset
3. Data cleaning and handling missing values
4. Perform exploratory data analysis
5. Create visualizations to understand trends

## Key Analysis

* Distribution of Movies vs TV Shows
* Content added to Netflix over the years
* Top countries producing Netflix content
* Most common ratings
* Most popular genres

## Example Insights

* Movies are more common than TV Shows on Netflix.
* Content production increased significantly after 2015.
* The United States and India contribute a large portion of Netflix content.
* Drama and Comedy are among the most common genres.

## Project Structure

```
Netflix-Dataset-Analysis
│
├── netflix_titles.csv
├── netflix_analysis.py
├── README.md
└── visualization_images
```

## How to Run the Project

1. Download the dataset.
2. Install required libraries.

```
pip install pandas matplotlib seaborn
```

3. Run the Python script.

```
python netflix_analysis.py
```

## Future Improvements

* Build a recommendation system
* Add interactive dashboards
* Perform advanced statistical analysis

## Author

Project created for learning data analysis using Python.
