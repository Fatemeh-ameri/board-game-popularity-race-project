import pandas as pd
import os
import bar_chart_race as bcr


# Project configuration
DATA_FOLDER = "../data/raw/bgg-ranking-historicals-master"
OUTPUT_FILE = "../outputs/videos/boardgame_race_monthly_dynamic_top20_fast.mp4"


TOP_N = 20


def get_csv_files(data_folder):
    """Get all CSV files from the dataset folder and sort them chronologically."""
    files = os.listdir(data_folder)
    csv_files = [file for file in files if file.endswith(".csv")]
    csv_files = sorted(csv_files)
    return csv_files


def select_monthly_snapshots(csv_files):
    """Select the latest available snapshot for each month."""
    monthly_files = {}

    for csv in csv_files:
        month = csv[:7]
        monthly_files[month] = csv

    selected_files = list(monthly_files.values())

    return selected_files


def load_and_preprocess_files(selected_files, data_folder):
    """Load selected CSV files, add dates, and keep columns needed for visualization."""
    all_dataframes = []

    for csv in selected_files:
        file_path = os.path.join(data_folder, csv)

        df = pd.read_csv(file_path)

        date = csv.split("T")[0]
        df["Date"] = date

        df = df[["ID", "Name", "Users rated", "Date"]]

        all_dataframes.append(df)

    final_df = pd.concat(all_dataframes, ignore_index=True)

    return final_df


def create_pivot_table(final_df):
    """Create a pivot table for the bar chart race visualization."""
    
    id_to_name = final_df.drop_duplicates("ID").set_index("ID")["Name"]

    # Use game IDs as columns because IDs are more stable than game names
    pivot_df = final_df.pivot_table(
        index="Date",
        columns="ID",
        values="Users rated",
        aggfunc="max"
    )

    return pivot_df, id_to_name


def prepare_animation_data(pivot_df, id_to_name, top_n):
    """Prepare the final dataframe used for the bar chart race animation."""

    # Include any game that enters the top N during the timeline
    top_games_over_time = set()

    for date, row in pivot_df.iterrows():
        top_games_for_date = row.sort_values(
            ascending=False
        ).head(top_n).index

        top_games_over_time.update(top_games_for_date)

    top_games_df = pivot_df[sorted(top_games_over_time)]

    # Missing values mean the game was not present in that snapshot
    top_games_df = top_games_df.fillna(0)

    # Use names only for display after selecting games by stable IDs
    top_games_df = top_games_df.rename(columns=id_to_name)

    top_games_df.columns.name = None

    return top_games_df


# Run the full data processing and animation pipeline
def main():
    csv_files = get_csv_files(DATA_FOLDER)
    selected_files = select_monthly_snapshots(csv_files)
    final_df = load_and_preprocess_files(selected_files, DATA_FOLDER)
    pivot_df, id_to_name = create_pivot_table(final_df)

    top_games_df = prepare_animation_data(
        pivot_df,
        id_to_name,
        TOP_N
    )

    # Render the final monthly bar chart race video
    bcr.bar_chart_race(
        df=top_games_df,
        filename=OUTPUT_FILE,
        orientation="h",
        sort="desc",
        n_bars=TOP_N,
        fixed_order=False,
        fixed_max=True,
        steps_per_period=10,
        period_length=400,
        figsize=(10, 6),
        dpi=144,
        bar_label_size=7,
        tick_label_size=7,
        title_size=14,
        title="Most Rated Board Games on BoardGameGeek (2016 - 2026)"
    )


if __name__ == "__main__":
    main()    