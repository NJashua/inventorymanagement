import numpy as np
import matplotlib.pyplot as plt

# Given data
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
        "Social": 87,
        "Telugu": 20
      }
    }
]

def plot_student_marks(name):
    for student in data:
        if student["name"] == name:
            marks = student["marks"]
            subjects = list(marks.keys())
            height = list(marks.values())
            
            plt.figure(figsize=(10, 8))
            plt.bar(np.arange(5), height, color=['crimson', 'blue', 'yellow', 'purple', 'black'])
            plt.xticks(np.arange(5), subjects, color='orange', rotation=45, fontweight='600', fontsize=10, ha='right')
            plt.title(f'Marks Obtained by {name}')
            plt.xlabel('Subjects')
            plt.ylabel('Marks')
            plt.show()
            break
    else:
        print(f"No data found for '{name}'")

# Example usage

plot_student_marks("Keertan")
