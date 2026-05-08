# Board Game Popularity Race

A Python data visualization project that explores how board game popularity and rankings change over time using historical BoardGameGeek ranking data.

The project currently includes two visualizations:

- an animated bar chart race based on the number of users who rated each game
- a rank-based animation showing how top-ranked board games move over time

---

## Overview

This project processes historical BoardGameGeek ranking snapshots and converts them into monthly time-series visualizations.

The pipeline uses stable BoardGameGeek game IDs to track games over time, then converts the data into formats suitable for animation.

This is an educational and portfolio project focused on:

- data cleaning
- time-series preparation
- pandas reshaping
- handling missing values
- animated data visualization

---

## Features

- Monthly sampling from historical CSV snapshots
- Stable game tracking using BoardGameGeek game IDs
- Dynamic top-N game selection across the full timeline
- Animated race based on `Users rated`
- Rank timeline JSON export
- Rank-based animation using actual rank positions
- MP4 export with FFmpeg

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
    │   └── raw/                         # Raw dataset files ignored by Git

    ├── outputs/
    │   ├── data/                        # Processed JSON files
    │   └── videos/                      # Generated videos ignored by Git

    ├── src/
    │   ├── create_users_rated_race.py   # Creates the users-rated bar chart race
    │   ├── create_rank_timeline_json.py # Exports cleaned rank timeline JSON
    │   └── create_rank_animation.py     # Creates rank-based animation from JSON

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

Run scripts from the `src` directory.

### 1. Create the users-rated race

    cd src
    python create_users_rated_race.py

This creates an MP4 animation based on the number of users who rated each game.

### 2. Create the rank timeline JSON

    python create_rank_timeline_json.py

This creates:

    outputs/data/boardgame_rank_timeline_top10.json

### 3. Create the rank-based animation

    python create_rank_animation.py

This creates an MP4 animation based on actual BoardGameGeek rank positions.

Generated videos are saved inside:

    outputs/videos/

---

## Notes on Interpretation

The users-rated animation shows how many BoardGameGeek users rated each game over time. It reflects popularity by number of ratings, not necessarily game quality or rank.

The rank-based animation uses BoardGameGeek ranks. Lower rank numbers are better, and Rank 1 appears at the top.

A game appears in the rank animation when it enters the selected Top N timeline. Missing games are not assigned fake ranks in the exported JSON.

---

## License

This project is intended for educational and portfolio purposes.
