import pandas as pd

def get_course_enrollments(conn):
    """
    Returns a DataFrame with course titles and their total enrollments from the database.
    """
    query = """
        SELECT c.title AS Course_Title, COUNT(*) AS Enrollments
        FROM user_course_activity uca
        JOIN courses c ON uca.course_id = c.course_id
        GROUP BY c.title
        ORDER BY Enrollments DESC;
    """
    return pd.read_sql_query(query, conn)
