# Board Game Popularity Race

A Python data visualization project that shows how board game popularity changes over time using historical BoardGameGeek ranking data.

The project builds an animated bar chart race based on the number of users who rated each game on BoardGameGeek.

---

## Project Overview

This project processes historical BoardGameGeek ranking snapshots and turns them into a time-based animated visualization.

The current version creates a monthly bar chart race showing the most-rated board games over time.

This is an educational and portfolio project focused on:

- data cleaning
- time-series preparation
- reshaping data with pandas
- handling missing values
- building animated visualizations
- writing a reusable data processing pipeline

---

## Features

- Load historical BoardGameGeek CSV snapshots
- Select the latest available snapshot from each month
- Extract dates from filenames
- Combine multiple historical snapshots into one dataset
- Use stable game IDs for tracking games over time
- Reshape the data into a wide time-series format
- Select games that enter the top N at any point in the timeline
- Rename game IDs back to game names for display
- Handle missing values for animation
- Generate an animated bar chart race video

---

## Current Status

The current version includes a working end-to-end pipeline that can:

- read historical BGG ranking files
- sample the data monthly
- preprocess and combine the data
- build a pivot table for visualization
- dynamically select top games over time
- export an MP4 bar chart race animation

The code has been refactored into reusable functions to make the pipeline easier to read and maintain.

---

## Technologies Used

- Python
- pandas
- Matplotlib
- bar_chart_race
- FFmpeg

---

## Dataset

This project uses historical BoardGameGeek ranking snapshots from the `bgg-ranking-historicals` dataset.

The raw dataset is not included in this repository because it is large. It should be downloaded separately and placed inside:

```text
data/raw/
```

Expected local structure:

```text
data/
└── raw/
    └── bgg-ranking-historicals-master/
        ├── 2016-10-12T00-30-40.csv
        ├── 2016-10-14T00-31-11.csv
        └── ...
```

---

## Project Structure

```text
board-game-popularity-race-project/

├── data/
│   └── raw/                 # Raw dataset files (ignored by Git)

├── outputs/
│   └── videos/              # Generated animations (ignored by Git)

├── src/
│   └── explore_data.py      # Current data processing and animation pipeline

├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd board-game-popularity-race-project
```

Create and activate a virtual environment:

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## FFmpeg Requirement

This project uses FFmpeg to export MP4 animations.

### macOS with Homebrew

```bash
brew install ffmpeg
```

Verify the installation:

```bash
ffmpeg -version
```

---

## How to Run

From the project root, run:

```bash
cd src
python explore_data.py
```

The generated video will be saved inside:

```text
outputs/videos/
```

---

## Current Workflow

The current pipeline performs the following steps:

1. Load all CSV filenames from the dataset folder
2. Keep only CSV files and sort them chronologically
3. Select the latest available snapshot from each month
4. Load and preprocess selected files
5. Keep the columns needed for visualization
6. Use game IDs to track games consistently over time
7. Build a pivot table with dates as rows and game IDs as columns
8. Select games that appear in the top N during the timeline
9. Replace missing values with 0 for animation
10. Rename game IDs to game names for display
11. Render the animated bar chart race video

---

## Notes on Interpretation

The current visualization uses `Users rated` as the popularity metric.

This means the animation shows how many BoardGameGeek users rated each game over time. It does not directly show the highest-rated or best-ranked games.

Games with many ratings may appear more prominently than highly ranked games with fewer total ratings.

---

## Future Improvements

Possible future improvements include:

- adding an intro/title card to the final video
- improving visual styling and colors
- adding annotations for major game releases
- experimenting with other metrics such as rank or Bayes average
- building a “fastest-rising board games” analysis
- separating the current script into multiple modules
- adding command-line options for metric, top N, and output filename

---

## License

This project is intended for educational and portfolio purposes.