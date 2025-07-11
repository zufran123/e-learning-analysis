import matplotlib.pyplot as plt
import os

def plot_course_enrollments(df):
    """
    Plots horizontal bar chart of course enrollments.
    Expects DataFrame with columns 'Course_Title' and 'Enrollments'
    """
    plt.figure(figsize=(10, 5))
    plt.barh(df['Course_Title'], df['Enrollments'], color='skyblue')
    plt.xlabel("Number of Enrollments")
    plt.ylabel("Course Title")
    plt.title("Enrollments per Course")
    plt.tight_layout()

    # Define path before saving and returning
    plot_path = os.path.join("visualizations", "course_enrollments.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"📊 Plot saved to: {plot_path}")

    return plot_path
