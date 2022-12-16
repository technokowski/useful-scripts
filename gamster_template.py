import pandas as pd
import os, csv
from datetime import date

today = date.today()
print(today)

# Script to create an upload-friendly user template to Asset Tiger.
# It first queries gam, the google admin third-party tool, 
# and opens the results of that query with csv reader.
# Then it creates a properly formatted csv with the correct column
# headers for Asset Tiger, and populates that csv with csv reader object.
# Last step is to convert the results to an excel spreadsheet using Pandas.

# configurable gam parameters
org = "Students"
userpath = "~/bin/gam/gam "
orgp = f"orgUnitPath='/{org}'"
x_file = "1_raw_gam_query.csv"

grades = {"/Students/School1/01": "01", "/Students/School2/kg": "KG", "/Students/School3/12": "12" 
            }

departments = {"/Students/School1/01": "SchoolName1", "/Students/School2/kg": "SchoolName2", "/Students/School3/12": "SchoolName3"
            }

# gam command generates a csv with: email, first name, last name, and the ou of each student.
# Appropriate formatting for Asset Tiger needs a column with combined first and last, 
# and column with academy, which is extracted from the ou column based on conditions.
gam_execute = f"{userpath} print users firstname lastname ou query {orgp}>{x_file}"
# runs that actual gam command with the above variables as a parameter. 
os.system(gam_execute)

# empty list object which is populated as-is by the contents of the gam results csv from above
data: list
with open(x_file, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# A new csv file is created and populated with the contents of the data list.
# Appropriate column headers are created
with open('2_correct_gam_result.csv', 'w', newline='') as nf:
    writer = csv.writer(nf)
    writer.writerow(
        ['Name', 'Email', 'Employee ID', 
                'Title', 'Phone', 'Site', 'Location', 'Department', 'Notes', 'Person Type']
    )
    # Loops through the data list and places the correct data in the correct columns.
    # The main conditional formatting logic is below. Academy, Full Name.
    # The rest of columns are either left blank or filled with default date.
    for row in data[1:]:
        # try and except block will filter out any dictionary entries not listed in grades and departments
        # If an OU needs to be added, it will have to be added accordingly to the grades and departments dicts
        try:
            user_department = departments[row[3]]
            user_grade = grades[row[3]]
            # Full Name is created by combining first and last.
            fname = row[1] + " " + row[2]
        except:
            continue

        writer.writerow([fname,row[0],None,None,None,"Grade Level",user_grade,user_department,None,"Student"])

# Convert to excel spreadsheet
df = pd.read_csv('2_correct_gam_result.csv')
print(df)

df.to_excel(f'AssTiger_upload_{today}.xlsx', index=False)