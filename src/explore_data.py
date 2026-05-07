import pandas as pd
import os
import bar_chart_race as bcr

# Get all dataset files from the raw data folder
files = os.listdir("../data/raw/bgg-ranking-historicals-master")

# Keep only CSV files and sort them chronologically
csv_files = [file for file in files if file.endswith(".csv")]
csv_files = sorted(csv_files)

# Keep only the latest snapshot from each month
monthly_files = {}

for csv in csv_files:
    month = csv[:7]
    monthly_files[month] = csv

# Convert monthly snapshots into a list
selected_files = list(monthly_files.values())

all_dataframes = []

# Read and preprocess each CSV file
for csv in selected_files:

    file_path = os.path.join(
        "../data/raw/bgg-ranking-historicals-master",
        csv
    )

    df = pd.read_csv(file_path)

    # Extract the date from the filename
    date = csv.split("T")[0]

    # Add the date as a new column
    df["Date"] = date

    # Keep only the columns needed for the visualization
    df = df[["ID", "Name", "Users rated", "Date"]]

    # Store the processed dataframe
    all_dataframes.append(df)

# Combine all daily dataframes into one dataframe
final_df = pd.concat(all_dataframes, ignore_index=True)

# Create a mapping from game ID to game name for display
id_to_name = final_df.drop_duplicates("ID").set_index("ID")["Name"]

# Reshape the dataframe for bar chart race visualization
pivot_df = final_df.pivot_table(
    index="Date",
    columns="ID",
    values="Users rated",
    aggfunc="max"
)

# Number of top games to include in the animation
top_n = 20

# Select games that appear in the top N at any point in time
top_games_over_time = set()

for date, row in pivot_df.iterrows():
    top_games_for_date = row.sort_values(ascending=False).head(top_n).index
    top_games_over_time.update(top_games_for_date)

# Keep only games that were in the top N at least once
top_games_df = pivot_df[sorted(top_games_over_time)]

# Replace missing values with 0 for smoother animation
top_games_df = top_games_df.fillna(0)

# Rename game ID columns to game names for display
top_games_df = top_games_df.rename(columns=id_to_name)

# Remove the column index name for cleaner output
top_games_df.columns.name = None

# Create a monthly bar chart race video
bcr.bar_chart_race(
    df=top_games_df,
    filename="../outputs/videos/boardgame_race_monthly_dynamic_top20.mp4",
    orientation="h",
    sort="desc",
    n_bars=top_n,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=8,
    period_length=300,
    title="Most Rated Board Games on BoardGameGeek (2016 - 2026)"
)