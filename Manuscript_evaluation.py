
import tkinter as tk
from tkinter import ttk
def calculate_score():
    total_score = sum([int(description.split(":")[0]) for description in [var.get() for var in criteria_vars]])
    result_label.config(text=f"Total Score: {total_score} / 10")
    
    if total_score > 7:
        recommendation_label.config(text="Recommendation: Strongly consider for publication.")
    elif 5 <= total_score <= 7:
        recommendation_label.config(text="Recommendation: Can consider for publication.")
    else:
        recommendation_label.config(text="Recommendation: Reject.")

app = tk.Tk()
app.title("ManuScore: Manuscript Evaluation Tool")

# Create a frame for the dropdown menus and labels
frame = ttk.Frame(app)
frame.pack(padx=10, pady=10)

criteria = [
    "Originality",
    "Significance",
    "Methodological Rigor",
    "Clarity and Quality of Writing",
    "Ethical Considerations"
]

descriptions = [
    [
        "0: No new insights, repetitive or derivative work.",
        "1: Some new insights but largely builds upon existing work.",
        "2: Completely original research or a novel perspective on an existing topic."
    ],
    [
        "0: Lacks significance, doesn't address a meaningful question or gap.",
        "1: Addresses a known issue but may not have a major impact.",
        "2: Addresses a critical gap or question in the field, likely to have a significant impact."
    ],
    [
        "0: Flawed or inappropriate methodology, lacks clarity.",
        "1: Adequate methodology but may have minor issues or lacks thoroughness.",
        "2: Robust and appropriate methodology, well-executed and clearly described."
    ],
    [
        "0: Poorly organized, unclear, major grammatical/stylistic errors.",
        "1: Generally clear but may have some organizational or grammatical issues.",
        "2: Well-organized, clear, and free of grammatical or stylistic errors."
    ],
    [
        "0: Major ethical concerns, lack of permissions or informed consent, evidence of plagiarism.",
        "1: Meets basic ethical standards but may lack thorough documentation or have minor issues.",
        "2: Fully ethical, proper citations, permissions, and informed consents in place."
    ]
]

criteria_vars = [tk.StringVar(value=descriptions[i][0]) for i in range(len(criteria))]

for i, criterion in enumerate(criteria):
    label = ttk.Label(frame, text=criterion)
    label.grid(row=i, column=0, sticky=tk.W, pady=5)
    
    combo = ttk.Combobox(frame, textvariable=criteria_vars[i], values=descriptions[i], width=100)
    combo.grid(row=i, column=1)
    combo.set(descriptions[i][0])

calculate_button = ttk.Button(app, text="Calculate Score", command=calculate_score)
calculate_button.pack(pady=20)

result_label = ttk.Label(app, text="Total Score: 0 / 10")
result_label.pack(pady=10)

recommendation_label = ttk.Label(app, text="Recommendation: ")
recommendation_label.pack(pady=10)


app.mainloop()
