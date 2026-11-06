"""
Functions for combining students and companies for the speed dates
"""
import re
import pandas as pd
import numpy as np
import os

def new_student(name_st:str, year_st:int, subject_st:str) -> pd.Series:
    """
    This function creates a new student

    args:
        name: student name
        year: study year student

    Returns:
        pd.Series() with information about the student
    """

    student = pd.Series({"name_st" : name_st,
                         "year_st" : year_st,
                         "subject_st" : subject_st})
    return student

def new_company(name_cp:str, time_cp:list, subject_cp) -> pd.Series:
    """
    This function creates a new company

    args:
        name_cp: company name
        time_cp: list of existing of twoo bools, first bool for if the company attending the first halve and the second for attending the second halve.
        subject_cp: What subject is the company interested in DS, EN or OR

    Returns:
        pd.Series() with information about the company
    """

    company = pd.Series({"name_cp" : name_cp,
                         "first_hlv" : time_cp[0],
                         "second_hlv" : time_cp[1],
                         "subject_cp" : subject_cp})
    return company


def make_student_df(file : str) -> pd.DataFrame:
    """
    Makes a usable pd.DataFrame from the imported excel file

    args:
        file: The filename of the excel file

    Returns:
        pd.DataFrame with name, year, english, subject
    """
    df = pd.read_excel(file)
    df = df[["Your full name:", "Your class code:", "Your specialization:"]]
    df.columns=["name", "class", "subject"]

    df_st = pd.DataFrame(columns=["name", "year", "english", "subject"])

    for i in df.iterrows():
        ind = i[0]
        row = i[1]

        name = row["name"].lower()
        if "am" in row["class"].lower():
            english = True
        else:
            english = False
        year = re.sub('\D', '', row["class"])

        df_st.loc[ind] = [name, year, english, row["subject"]]

    return df_st

def make_company_df(file : str) -> pd.DataFrame:
    """
    Makes a usable pd.DataFrame from the imported excel file

    args:
        file: The filename of the excel file

    Returns:
        pd.DataFrame with name, year, english, subject
    """
    df = pd.read_excel(file)
    df = df.iloc[:, [6, 9, 12]]
    df.columns = range(3)

    df_cp = pd.DataFrame(columns=["name", "english", "ds", "or", "en", "first", "second"])

    for i in df.iterrows():
        ind = i[0]
        row = i[1]
        
        if row[0] == row[0]:
            name = row[0].lower()
            if row[1] == "Yes":
                english = True
            else:
                english = False

            if "Data Science" in row[2]:
                ds = True
            else:
                ds = False

            if "Operations Research" in row[2]:
                or_ = True
            else:
                or_ = False

            if "Engineering" in row[2]:
                en = True
            else:
                en = False

            df_cp.loc[ind] = [name, english, ds, or_, en, np.nan, np.nan]

    return df_cp
        
def update_excel():
    """
    updates the existing excel file that exists for the students and companys

    Returns:
        A updated excel file
    """

    if os.path.isfile("C:/Users/jobwi/OneDrive - Office 365 Fontys/Documenten/school/Netwerkdag/website_TW_Netwerkdag_2026/student_company_list.xlsx"):
        df_st = pd.read_excel("student_company_list.xlsx", sheet_name="students")
        df_cp = pd.read_excel("student_company_list.xlsx", sheet_name="companies")

        df_new_st = make_student_df("Networking Day - Student Sign-up 2026.xlsx")
        df_new_cp = make_company_df("Networking Day 2026 Applied Mathematics - Company Registration.xlsx")

        for i in df_new_st.iterrows():
            ind = i[0]
            row = i[1]
            if row["name"] not in df_st["name"]:
                df_st.loc[len(df_st.index)] = row

        for i in df_new_cp.iterrows():
            ind = i[0]
            row = i[1]
            if row["name"] not in df_cp["name"]:
                df_cp.loc[len(df_cp.index)] = row
    
    else:
        df_st = make_student_df("Networking Day - Student Sign-up 2026.xlsx")
        df_cp = make_company_df("Networking Day 2026 Applied Mathematics - Company Registration.xlsx")

    with pd.ExcelWriter("student_company_list.xlsx", engine='openpyxl') as writer:
        df_st.to_excel(writer, sheet_name="students", index=False)
        df_cp.to_excel(writer, sheet_name="companies", index=False)
