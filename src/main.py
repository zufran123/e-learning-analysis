import pandas as pd
from connect_db import create_connection
from query_runner import get_course_enrollments
from analysis import plot_course_enrollments
from pdf_report import generate_pdf_report
from tabulate import tabulate

def main():
    # Connect to your database
    conn = create_connection()
    print("✅ Connected to database")

    # Get enrollment data from the database
    enrollments = get_course_enrollments(conn)

    # Print Top 5 Most Enrolled Courses in Terminal
    print("\n📌 Top 5 Most Enrolled Courses:")
    print(tabulate(enrollments.head(5), headers="keys", tablefmt="pretty"))

    # Plot the course enrollments (bar chart or similar)
    plot_course_enrollments(enrollments)

    # Generate a PDF report with the same data
    image_path = plot_course_enrollments(enrollments)  # returns saved image path
    
    generate_pdf_report(enrollments, image_path)


if __name__ == "__main__":
    main()
