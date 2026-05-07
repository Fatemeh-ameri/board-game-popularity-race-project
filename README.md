# Board Game Popularity Race

A data visualization project that explores how the popularity of board games changes over time using historical BoardGameGeek ranking data.

The main goal of this project is to build animated bar chart race visualizations that show how the most-rated board games evolve across different time periods.

---

## Project Preview

This project generates animated visualizations similar to:

- Top board games by number of users rated
- Popularity changes over time
- Historical ranking evolution on BoardGameGeek

The current version is an early prototype focused on building the data pipeline and animation workflow.

---

## Features

- Load historical BoardGameGeek CSV snapshots
- Extract timestamps from filenames
- Build a time-series dataset
- Reshape data for visualization
- Select top games dynamically
- Handle missing values
- Generate animated bar chart race videos

---

## Current Progress

The current prototype can:

- Read multiple historical BGG CSV files
- Combine daily snapshots into a single dataset
- Transform the data into a wide time-series format
- Select the top games based on user ratings
- Generate a first working animated bar chart race video

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- bar_chart_race
- FFmpeg

---

## Dataset

This project uses historical BoardGameGeek ranking snapshots from the:

`bgg-ranking-historicals`

dataset.

The raw dataset is not included in this repository because of its large size.

---

## Project Structure

```text
board-game-popularity-race-project/

├── data/
│   └── raw/                 # Raw dataset files (ignored by Git)

├── outputs/
│   └── videos/              # Generated animations (ignored by Git)

├── src/
│   └── explore_data.py      # Current prototype pipeline

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

### macOS (Homebrew)

```bash
brew install ffmpeg
```

You can verify the installation with:

```bash
ffmpeg -version
```

---

## How to Run

Run the prototype script:

```bash
cd src
python explore_data.py
```

The generated animation will be saved inside:

```text
outputs/videos/
```

---

## Current Workflow

The current pipeline performs the following steps:

1. Load historical CSV snapshots
2. Extract dates from filenames
3. Preprocess and combine the datasets
4. Reshape the data using pivot tables
5. Select the top games by user ratings
6. Handle missing values
7. Generate an animated bar chart race

---

## Future Improvements

Planned improvements include:

- Running the pipeline on the full historical dataset
- Performance optimization
- Better animation styling and themes
- Higher resolution exports
- Dynamic labels and transitions
- Additional visual analytics projects
- Ranking trend analysis
- Fastest-rising games analysis
- Long-term popularity tracking

---

## Notes

The current version uses a small sample of CSV files for testing and development purposes.

The project is still under active development.

---

## License

This project is intended for educational and portfolio purposes.