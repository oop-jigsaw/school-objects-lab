import pandas as pd
from school import School

def query_api():
    url = "https://raw.githubusercontent.com/jigsawlabs-student/decision-trees-intro/master/3-practical-ds-4/nyc_hs_sat.csv"
    df = pd.read_csv(url)
    return df.to_dict('records')


def build_instances(school_dicts):
    selected_attrs = ['dbn', 'name', 'boro', 'writing_score', 'math_avg', 
        'reading_avg', 'total_students', 'attendance_rate']
    schools = []
    for school_dict in school_dicts:
        selected_attr_dict = {k:v for k, v in school_dict.items() if k in selected_attrs}
        school = School(**selected_attr_dict)
        schools.append(school)
    return schools


def largest_total_score_school(schools):
    return max(schools, key=lambda school: school.total_score())

def average_total_score_of(schools):
    return round(sum([school.total_score() for school in schools])/len(schools), 0)

def largest_average_student_attendance(schools):
    return max(schools, key=lambda school: school.avg_student_attendance())
