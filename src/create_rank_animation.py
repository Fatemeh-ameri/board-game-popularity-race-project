import json
import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter


# --- Configuration ---
INPUT_FILE = "../outputs/data/boardgame_rank_timeline_top20.json"
OUTPUT_FILE = "../outputs/videos/rank_based_top20.mp4"

# Animation speed settings
FPS = 30
STEPS_PER_MONTH = 15  # Lower value = shorter video
WIDTH_INCHES, HEIGHT_INCHES = 16, 9
DPI = 100
FONT_FAMILY = "DejaVu Sans"


def create_animation():
    plt.rcParams["font.family"] = FONT_FAMILY

    # 1. Directory management
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"Input file not found at: {INPUT_FILE}")

    # 2. Data loading
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    title = data.get("title", "BoardGameGeek Rankings")
    top_n = data.get("top_n", 10)
    timeline = data["timeline"]

    # 3. Pre-processing: colors and monthly snapshots
    all_games = set()
    snapshots = []

    for entry in timeline:
        ranks = {
            item["game"]: item["rank"]
            for item in entry["rankings"]
        }

        snapshots.append({
            "date": entry["date"],
            "ranks": ranks
        })

        all_games.update(ranks.keys())

    # Assign a unique, consistent color to every game in the dataset
    cmap = plt.colormaps["tab20"].resampled(len(all_games))
    game_colors = {
        game: cmap(i)
        for i, game in enumerate(sorted(all_games))
    }

    # 4. Visualization setup
    fig, ax = plt.subplots(figsize=(WIDTH_INCHES, HEIGHT_INCHES), dpi=DPI)
    total_frames = (len(snapshots) - 1) * STEPS_PER_MONTH

    # Fixed title and dynamic date outside the plotting area
    fig.suptitle(
        title,
        fontsize=26,
        fontweight="bold",
        y=0.93
    )

    date_text = fig.text(
        0.5,
        0.84,
        "",
        ha="center",
        va="center",
        fontsize=30,
        color="#666666",
        fontweight="bold"
    )

    def update(frame):
        ax.clear()

        # Calculate interpolation progress between two consecutive monthly snapshots
        month_idx = frame // STEPS_PER_MONTH
        alpha = (frame % STEPS_PER_MONTH) / (STEPS_PER_MONTH - 1)

        start_snap = snapshots[month_idx]
        end_snap = snapshots[month_idx + 1]

        # Include games currently in the Top N or moving into/out of it
        active_games = set(start_snap["ranks"].keys()) | set(end_snap["ranks"].keys())

        for game in active_games:
            # Use an off-screen visual position for games missing from a month.
            # This is not a real rank; it only lets games smoothly enter or leave the Top N view.
            offscreen_position = top_n + 1

            start_position = start_snap["ranks"].get(game, offscreen_position)
            end_position = end_snap["ranks"].get(game, offscreen_position)

            # Interpolate the visual position between two monthly snapshots
            interpolated_position = (
                start_position + (end_position - start_position) * alpha
            )

            # Vertical mapping: Rank 1 appears at the top, Rank top_n at the bottom
            y_position = (top_n + 1) - interpolated_position

            # Render only games visually inside or near the Top N area
            if interpolated_position <= top_n + 0.5:
                color = game_colors[game]

                # Draw a fixed-width plaque so rank is represented by vertical position,
                # not by bar length.
                ax.barh(
                    y_position,
                    1.0,
                    color=color,
                    edgecolor="white",
                    height=0.7,
                    alpha=0.9,
                    left=0
                )

                # Show rank label only when the game has a valid Top N visual position
                if interpolated_position <= top_n + 0.01:
                    rank_number = int(round(interpolated_position))

                    ax.text(
                        -0.02,
                        y_position,
                        f"Rank {rank_number}",
                        va="center",
                        ha="right",
                        color="#333333",
                        fontweight="bold",
                        fontsize=16
                    )

                # Display full board game name
                ax.text(
                    0.02,
                    y_position,
                    game,
                    va="center",
                    ha="left",
                    color="white",
                    fontweight="bold",
                    fontsize=13
                )

        # Current date display using the real snapshot date from the JSON
        current_date = start_snap["date"] if alpha < 0.5 else end_snap["date"]
        date_text.set_text(current_date)

        # Formatting
        ax.set_xlim(-0.35, 1.35)
        ax.set_ylim(0.5, top_n + 1)
        ax.axis("off")

        plt.subplots_adjust(
            left=0.1,
            right=0.9,
            top=0.80,
            bottom=0.1
        )

    # 5. Export video
    print(f"Starting export to {OUTPUT_FILE}...")

    animation = FuncAnimation(
        fig,
        update,
        frames=total_frames,
        interval=1000 / FPS
    )

    writer = FFMpegWriter(fps=FPS, bitrate=4000)
    animation.save(OUTPUT_FILE, writer=writer)

    plt.close()
    print("Animation complete.")


if __name__ == "__main__":
    create_animation()