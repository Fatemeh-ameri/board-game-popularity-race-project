# Board Game Popularity Race

A Python data visualization project that shows how board game popularity changes over time using historical BoardGameGeek ranking data.

The project creates an animated bar chart race based on the number of BoardGameGeek users who rated each game.

---

## Overview

This project processes historical BoardGameGeek ranking snapshots and converts them into a monthly time-series visualization.

The current version includes a working end-to-end pipeline that:

- reads historical BGG CSV files
- selects the latest available snapshot from each month
- tracks games using stable game IDs
- reshapes the data into a time-series format
- dynamically selects games that enter the top N over time
- exports an MP4 bar chart race animation

This is an educational and portfolio project focused on data cleaning, time-series preparation, pandas reshaping, and animated data visualization.

---

## Features

- Monthly sampling from historical CSV snapshots
- Stable game tracking using BoardGameGeek game IDs
- Dynamic top-N game selection across the full timeline
- Missing value handling for animation
- MP4 export using `bar_chart_race` and FFmpeg

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

Dataset repository: [bgg-ranking-historicals](https://gitlab.com/recommend.games/bgg-ranking-historicals)

The raw dataset is not included in this repository because it is large. It should be downloaded separately and placed inside:

    data/raw/

Expected local structure:

    data/
    └── raw/
        └── bgg-ranking-historicals-master/
            ├── 2016-10-12T00-30-40.csv
            ├── 2016-10-14T00-31-11.csv
            └── ...

---

## Project Structure

    board-game-popularity-race-project/

    ├── data/
    │   └── raw/                 # Raw dataset files (ignored by Git)

    ├── outputs/
    │   └── videos/              # Generated animations (ignored by Git)

    ├── src/
    │   └── explore_data.py      # Data processing and animation pipeline

    ├── requirements.txt
    ├── .gitignore
    └── README.md

---

## Installation

Clone the repository:

    git clone <your-repo-url>
    cd board-game-popularity-race-project

Create and activate a virtual environment:

### macOS / Linux

    python3 -m venv venv
    source venv/bin/activate

### Windows

    python -m venv venv
    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

---

## FFmpeg Requirement

This project uses FFmpeg to export MP4 animations.

### macOS with Homebrew

    brew install ffmpeg

Verify the installation:

    ffmpeg -version

---

## How to Run

From the project root, run:

    cd src
    python explore_data.py

The generated video will be saved inside:

    outputs/videos/

---

## Current Workflow

The current pipeline performs the following steps:

1. Load and sort historical CSV filenames
2. Select the latest available snapshot from each month
3. Load and preprocess selected files
4. Use game IDs to track games consistently over time
5. Build a pivot table with dates as rows and game IDs as columns
6. Select games that appear in the top N during the timeline
7. Replace missing values with 0 for animation
8. Rename game IDs to game names for display
9. Render the animated bar chart race video

---

## Notes on Interpretation

The current visualization uses `Users rated` as the popularity metric.

This means the animation shows how many BoardGameGeek users rated each game over time. It does not directly show the highest-rated or best-ranked games.

Games with many ratings may appear more prominently than highly ranked games with fewer total ratings.

---

## Future Improvements

Possible future improvements include:

- adding an intro/title card
- improving visual styling and colors
- adding annotations for major game releases
- experimenting with other metrics such as rank or Bayes average
- building a fastest-rising board games analysis
- adding command-line options for metric, top N, and output filename

---

## License

This project is intended for educational and portfolio purposes.