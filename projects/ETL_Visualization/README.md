# Video Game Sales Data Analysis

This project utilizes a comprehensive dataset of video game sales to perform exploratory analysis, focusing on global sales trends, platform popularity, and regional market share.

## 💾 Dataset Overview

The primary dataset, `games.csv`, contains sales data for over 16,500 video games across various platforms, regions, genres, and publishers. This data is valuable for identifying market trends, predicting future game sales, and conducting comparative analysis of gaming platforms.

| Feature | Description |
| :--- | :--- |
| `Rank` | Ranking of overall sales |
| `Name` | The game's name |
| `Platform` | Platform of the game's release (e.g., PC, PS4, Wii) |
| `Year` | Year of the game's release |
| `Genre` | Genre of the game |
| `Publisher` | Publisher of the game |
| `NA_Sales` | Sales in North America (in millions) |
| `EU_Sales` | Sales in Europe (in millions) |
| `JP_Sales` | Sales in Japan (in millions) |
| `Other_Sales` | Sales in the rest of the world (in millions) |
| `Global_Sales` | Total worldwide sales (in millions) |

## 🔗 Data Source

The dataset used is the Video Game Sales dataset, originally sourced from Kaggle:
* **Kaggle Dataset:** [Video Game Sales](https://www.kaggle.com/datasets/anandshaw2001/video-game-sales)
* **License:** CC0: Public Domain

## 📁 Project Files

| File Name | Type | Description |
| :--- | :--- | :--- |
| `games.csv` | CSV | The raw dataset containing historical video game sales figures across regions and platforms. |
| `playstation_games.ipynb` | Jupyter Notebook | The primary analysis script, which performs data cleaning, feature engineering, and exploratory data analysis (EDA) on the sales data. |

## 🛠️ Analysis and Methodology (`playstation_games.ipynb`)

The Jupyter Notebook, titled `playstation_games.ipynb`, executes the following key steps for data analysis:

### 1. Data Preparation
* Loads the `games.csv` file using pandas.
* **Data Cleaning:** Checks for and drops rows with missing values, primarily in the `Year` and `Publisher` columns.
* Converts the `Year` column to an integer data type.

### 2. Feature Engineering
* New columns are created to represent the proportional sales share for each region relative to global sales:
    * `NA_Regional_Share`
    * `EU_Regional_Share`
    * `JP_Regional_Share`
    * `Other_Regional_Share`

### 3. Key Findings
* The analysis aggregates the total `Global_Sales` by `Platform` to determine overall console performance.
* **Platform Sales:** The analysis indicates that the **PS2** is the platform with the highest lifetime global sales in the dataset.
* **Visualization:** A pie chart titled 'Platform Popularity: Global Sales Share' is generated to show the breakdown of global sales across all platforms.