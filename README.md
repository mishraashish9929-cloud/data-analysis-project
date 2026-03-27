🎬 Netflix Content Analytics Dashboard
An end-to-end data analytics project that explores Netflix's global content library using Python for data cleaning and Power BI for interactive visualization.

📊 Live Dashboard
🔗 https://mishraashish9929-cloud.github.io/data-analysis-project/

🛠️ Tools & Technologies
ToolPurposePython (Pandas)Data cleaning & preprocessingPower BIDashboard & visualizationsGitHub PagesDashboard hosting

 Data Cleaning (Python)
The raw Netflix dataset was cleaned using Pandas:

Removed duplicate records
Handled missing values in director, cast, and country columns
Standardized date formats in date_added
Parsed and normalized the listed_in (genres) column
Exported cleaned data as cleaned_netflix_data.csv


📈 Dashboard Highlights

8,807 titles analyzed across Movies and TV Shows
Content trends from 2010 to 2021
Top producing countries — US leads with 2,818 titles
Genre breakdown — International Movies & Dramas dominate
Rating distribution — TV-MA is the most common rating


📁 Project Structure
netflix-dashboard/
│

├── cleaned_netflix_data.csv    # dataset
├── data.py                     # Python data cleaning notebook
├── index.html                  # Interactive dashboard
└── README.md                   # Project documentation

📂 Dataset

Source: Kaggle Netflix Movies and TV Shows
Records: 8,807 titles
Features: Title, Type, Director, Cast, Country, Release Year, Rating, Genre

 Author
Ashish Mishra
