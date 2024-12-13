###1
def proportion_of_education(data):
    total_children = len(data)
    
    if total_children == 0:
        return {
            "less_than_high_school": 0,
            "high_school": 0,
            "more_than_high_school": 0,
            "college_degree": 0
        }
        
    count_less_than_high_school = 0
    count_high_school = 0
    count_more_than_high_school = 0
    count_college_degree = 0

    for entry in data:
        education_level = entry.get('mother_education', 0)
        
        if education_level < 12:
            count_less_than_high_school += 1
        elif education_level == 12:
            count_high_school += 1
        elif education_level > 12 and education_level < 16:
            count_more_than_high_school += 1
        elif education_level >= 16:
            count_college_degree += 1

    return {
        "less_than_high_school": count_less_than_high_school / total_children,
        "high_school": count_high_school / total_children,
        "more_than_high_school": count_more_than_high_school / total_children,
        "college_degree": count_college_degree / total_children
    }


###2




















###3 

import pandas as pd
