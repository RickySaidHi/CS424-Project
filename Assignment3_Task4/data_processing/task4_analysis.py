# Task 4: Quantitative analysis

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["axes.titleweight"] = "bold"

# Load the 15 participant files
tables = []
for number in range(1, 16):
    answers = pd.read_csv(f"../eval-results/participant_{number}.csv")
    answers["participant"] = number
    tables.append(answers)
df = pd.concat(tables, ignore_index=True)

# Score each answer
correct_answers = {"1A": "First Floor Circle Lounge", "1B": "West Terrace", "2A": "West Terrace", "2B": "Inner Circle"}

# Average chair occupancy (%) on days without rain for the two locations
# Task 1 questions ask about midday and Task 2 questions ask about the morning.
real_values = {
    "1A": {"First Floor Circle Lounge": 33.63, "Commuter Center": 83.70},
    "1B": {"West Terrace": 35.16, "East Terrace": 58.72},
    "2A": {"West Terrace": 5.68, "Pier Room": 28.92},
    "2B": {"Inner Circle": 8.96, "Pier Room": 28.92},
}

correct = []
guess_error = []
for question, location, guess in zip(df["question_id"], df["response"], df["numeric_response"]):
    correct.append(location == correct_answers[question])
    guess_error.append(abs(guess - real_values[question][location]))
df["correct"] = correct
df["guess_error"] = guess_error

# Summary table
groups = df.groupby("condition")
summary = pd.DataFrame({
    "Correct (out of 30)": groups["correct"].sum(),
    "Correct (%)": groups["correct"].mean() * 100,
    "Guess error, median": groups["guess_error"].median(),
    "Guess error, average": groups["guess_error"].mean(),
    "Time, median (s)": groups["completion_seconds"].median(),
    "Time, fastest (s)": groups["completion_seconds"].min(),
    "Time, slowest (s)": groups["completion_seconds"].max(),
})
print("summary:\n", summary.round(1).T, "\n")

# Each participant's average guess error and difficulty rating with each chart
errors = df.pivot_table(index="participant", columns="condition", values="guess_error")
ratings = df.pivot_table(index="participant", columns="condition", values="visualization_difficulty")
print("Guessed closer with interactive:", (errors["Interactive"] < errors["Static"]).sum(), "of 15")
print("Rated static harder to use:", (ratings["Static"] > ratings["Interactive"]).sum(), "of 15\n")

# Each person's average time on their first two questions vs their last two
df["half"] = "first two"
df.loc[df["part_number"] > 2, "half"] = "last two"
halves = df.pivot_table(index="participant", columns="half", values="completion_seconds")
halves["change"] = halves["last two"] - halves["first two"]
print("First two vs. Last two questions:\n", halves.round(1))
print("Faster in their last two questions:", (halves["change"] < 0).sum(), "of 15\n")

# Split people by the chart they started with, then average the two groups
times = df.pivot_table(index="participant", columns="condition", values="completion_seconds")
times["difference"] = times["Interactive"] - times["Static"]
times["started_with"] = df[df["part_number"] == 1].set_index("participant")["condition"]
group_average = times.groupby("started_with")["difference"].mean()
print("Interactive minus static in seconds\n", group_average.round(1).to_string())
print("Average of the two groups:", round(group_average.mean(), 1), "seconds\n")

# Task Accuracy per Trial
colors = {"Static": "#d4453e", "Interactive": "#23BB60"}
markers = {"Static": "o", "Interactive": "s"}
shift = {"Static": -0.2, "Interactive": 0.2}
questions = ["1A", "1B", "2A", "2B"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# the share of answers with the correct location
for i, q in enumerate(questions + ["All"]):
    for condition in ["Static", "Interactive"]:
        rows = df[df["condition"] == condition]
        if q != "All":
            rows = rows[rows["question_id"] == q]
        percent = rows["correct"].mean() * 100
        x = i + shift[condition]
        ax1.bar(x, percent, width=0.38, color=colors[condition])
        ax1.text(x, percent + 2, f"{rows['correct'].sum()}/{len(rows)}", ha="center")
ax1.set_xticks(range(5), questions + ["All"])
ax1.grid(axis="y", alpha=0.3)
ax1.set(title="Correct location chosen", xlabel="Question", ylabel="Share of trials correct (%)", ylim=(0, 110))

# Draws every answer as a dot with a blue median triangle
def dots_by_question(ax, column, write_median=False):
    for i, q in enumerate(questions):
        for condition in ["Static", "Interactive"]:
            values = df[(df["question_id"] == q) & (df["condition"] == condition)][column]
            x = i + shift[condition]
            spread = [x - 0.05 + 0.015 * k for k in range(len(values))]
            ax.scatter(spread, values, color=colors[condition], marker=markers[condition])
            ax.scatter(x + 0.14, values.median(), color="#062a57", marker="^", s=90)
            if write_median:
                ax.text(x, -10, f"{values.median():.1f} s", ha="center", va="top", fontsize=9)
    ax.set_xticks(range(4), questions)
    ax.grid(axis="y", alpha=0.3)
    # empty points, only used for the legend
    ax.scatter([], [], color=colors["Static"], marker="o", label="Static")
    ax.scatter([], [], color=colors["Interactive"], marker="s", label="Interactive")
    ax.scatter([], [], color="#062a57", marker="^", label="Median")

dots_by_question(ax2, "guess_error")
ax2.set(title="Chair occupancy guess error", xlabel="Question", ylabel="How far off the guess was (%)", ylim=(0, 62))

fig.suptitle("Task Accuracy per Trial", fontsize=14, fontweight="bold")
fig.legend(*ax2.get_legend_handles_labels(), loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.94))
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig("../visualizations/Assignment3/eval_accuracy.png", dpi=160)

# Completion Time per Trial
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

# The time for every answer and the median
dots_by_question(ax1, "completion_seconds", write_median=True)
ax1.tick_params(axis="x", pad=20)
ax1.set(title="Time per trial", xlabel="Question (median time below)",
        ylabel="Completion time (seconds)", ylim=(0, 340))

order = halves.sort_values("change")
for row, person in enumerate(order.index):
    start = order.loc[person, "first two"]
    end = order.loc[person, "last two"]
    first_chart = times.loc[person, "started_with"]
    second_chart = "Interactive" if first_chart == "Static" else "Static"
    ax2.annotate("", xy=(end, row), xytext=(start, row),
                 arrowprops=dict(arrowstyle="->", color="gray", shrinkA=6, shrinkB=6))
    ax2.scatter(start, row, color=colors[first_chart], marker=markers[first_chart], zorder=3)
    ax2.scatter(end, row, color=colors[second_chart], marker=markers[second_chart], zorder=3)
    ax2.text(max(start, end) + 6, row, f"{order.loc[person, 'change']:+.0f} s", va="center")
ax2.set_yticks(range(15), [f"P{person}" for person in order.index])
ax2.invert_yaxis()
ax2.grid(axis="x", alpha=0.3)
ax2.set(title="Each person's time: first 2 questions vs last 2", xlim=(0, 250),
        xlabel="Average seconds per question (arrow: first 2 questions to last 2)")

fig.suptitle("Completion Time per Trial", fontsize=14, fontweight="bold")
fig.legend(*ax1.get_legend_handles_labels(), loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.94))
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig("../visualizations/Assignment3/eval_time.png", dpi=160)