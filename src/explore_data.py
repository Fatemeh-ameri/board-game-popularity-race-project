import pandas as pd
import os
import bar_chart_race as bcr

# Get all dataset files from the raw data folder
files = os.listdir("../data/raw/bgg-ranking-historicals-master")

# Keep only CSV files and sort them chronologically
csv_files = [file for file in files if file.endswith(".csv")]
csv_files = sorted(csv_files)

# Use only a small sample of files for testing
sample_files = csv_files[:5]

all_dataframes = []

# Read and preprocess each CSV file
for csv in sample_files:

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
    df = df[["Name", "Users rated", "Date"]]

    # Store the processed dataframe
    all_dataframes.append(df)

# Combine all daily dataframes into one dataframe
final_df = pd.concat(all_dataframes, ignore_index=True)

# Reshape the dataframe for bar chart race visualization
pivot_df = final_df.pivot_table(
    index="Date",
    columns="Name",
    values="Users rated",
    aggfunc="max"
)

# Number of top games to include in the animation
top_n = 15

# Select the most popular games based on the latest available date
latest_row = pivot_df.iloc[-1]

# Sort games by the number of users rated, from highest to lowest
sorted_games = latest_row.sort_values(ascending=False)

# Get the names of the top games
top_games = sorted_games.head(top_n).index

# Keep only the top games for the animation
top_games_df = pivot_df[top_games]

# Replace missing values with 0 for smoother animation
top_games_df = top_games_df.fillna(0)

'''print(top_games_df.head())
print(top_games_df.shape)'''

# Create a test bar chart race video using the sample data
bcr.bar_chart_race(
    df=top_games_df,
    filename="../outputs/videos/boardgame_race_test.mp4",
    orientation="h",
    sort="desc",
    n_bars=top_n,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=20,
    period_length=800,
    title="Most Rated Board Games on BoardGameGeek Over Time"
)