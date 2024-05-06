import matplotlib
matplotlib.use('TkAgg')

from flask import Flask, request, render_template, g
import json

import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# JSON data of students
data = [
    {
        "name": "Kaustubh",
        "marks": {
            "English": 85,
            "Maths": 90,
            "Science": 88,
            "Social": 78
        }
    },
    {
        "name": "Nithin",
        "marks": {
            "English": 75,
            "Maths": 82,
            "Science": 80,
            "Social": 85
        }
    },
    {
        "name": "Jayanth",
        "marks": {
            "English": 92,
            "Maths": 88,
            "Science": 78,
            "Social": 90
        }
    },
    {
        "name": "Keertan",
        "marks": {
            "English": 80,
            "Maths": 85,
            "Science": 92,
            "Social": 87
        }
    }
]

def get_details(name):
    for student in data:
        if student["name"] == name:
            marks = student["marks"]
            subjects = list(marks.keys())
            height = list(marks.values())

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(np.arange(len(subjects)), height, color=['lightgray', 'yellow', 'lavender', 'slateblue'])
            ax.set_xticks(np.arange(len(subjects)))
            ax.set_xticklabels(subjects, color='black', rotation=20, fontweight='600', fontsize=10, ha='right')
            ax.set_title(f"Marks Obtained by {name}")
            ax.set_xlabel("Subjects")
            ax.set_ylabel("Marks")
            
            # Save plot to BytesIO buffer
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.getvalue()).decode()

            plt.close(fig)
            return f'<img src="data:image/png;base64,{img_base64}">'
    else:
        print(f"No data found for {name}")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/plot", methods=["POST"])
def plot():
    student_name = request.form.get("studentName")
    graph_html = get_details(student_name)
    return render_template("index.html", graph=graph_html)

if __name__ == "__main__":
    app.run(debug=True)
