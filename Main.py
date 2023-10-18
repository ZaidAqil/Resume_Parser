import re
import openpyxl
import spacy
from spacy.matcher import Matcher

loader =r"C:\Users\zaida\Documents\GitHub\Quantum\Resume_parsing\Resume Sample\txt"

with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume Screening/degree.txt", 'r') as f:
    jobskill = f.read()


def find_degree (jobskill):
    # Compile a regular expression pattern to match the jobskill
    pattern = re.compile('|'.join(re.escape(x) for x in jobskill.split('\n')),re.IGNORECASE)

    # Open and read the text file to search
    with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume3.txt", 'r') as f:
        text = f.read()

    # Find all matches of the jobskill names in the text file
    matches = pattern.findall(text)

    # Print the matches
    def myFunc(x):
      if x == "":
        return False
      else:
        return True

    degree_filtered = filter(myFunc, matches)
    degree_non_repeated = list(set(degree_filtered))
    return degree_non_repeated
    # for x in degree_non_repeated:
    #     print(x)
    # return

degree = find_degree(jobskill)
string_degree = str(degree)




import spacy

nlp = spacy.load("en_core_web_sm")

def find_address():
    with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume3.txt",) as f:
        resume_text = f.read()
        text = resume_text

    doc = nlp(text)

    addresses = []

    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:
            addresses.append(ent.text)

    # print(addresses[0:2])
    return (addresses[0:2])


address=find_address()
string_address = str(address)



def work_experience():
    with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume3.txt", 'r') as f:
        resume_text = f.read()

    # Define a regular expression pattern to match the start of the work experience section
    work_exp_start_pattern = r'EXPERIENCE|WORK EXPERIENCE|Working Experience|Work Experience|WORKINGEXPERIENCE|WORKING EXPERIENCE'

    # Define a regular expression pattern to match the end of the work experience section
    work_exp_end_pattern = r'LANGUAGE PROFICIENCY|VOLUNTEER EXPERIENCES|EXTRA-CURRICULAR ACTIVITIES|ACHIEVEMENTS & EXTRA CURRICULAR ACTIVITIES|Education|CERTIFICATION|SKILSS LANGUAGE'

    # Search for the start and end patterns in the resume text
    work_exp_start_match = re.search(work_exp_start_pattern, resume_text)
    work_exp_end_match = re.search(work_exp_end_pattern, resume_text)

    if work_exp_start_match and work_exp_end_match:
        # Extract the text between the start and end patterns
        work_exp_text = resume_text[work_exp_start_match.end():work_exp_end_match.start()]

        # Print the extracted text
        return (work_exp_text)
    else:
        return ('Work experience section not found.')




work_exp=work_experience()
string_work = str(work_exp)

with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume Screening/software_skills_zaid.txt", 'r') as f:
    softskill = f.read()
def software_skills(softskill):


    # Compile a regular expression pattern to match the softskill
    pattern = re.compile('|'.join(re.escape(x) for x in softskill.split('\n')), re.IGNORECASE)

    # Open and read the text file to search
    with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume 17.txt", 'r') as f:
        text = f.read()

    # Find all matches of the jobskill names in the text file
    matches = pattern.findall(text)

    # Print the matches
    def myFunc(x):
        if x == "":
            return False
        else:
            return True

    skills_filtered = filter(myFunc, matches)
    skills_non_repeated = list(set(skills_filtered))
    return skills_non_repeated

skills = software_skills(softskill)
string_software = str(skills)



with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume Screening/univesity.txt", 'r') as f:
    universities = f.read()

def university(universities):
# Compile a regular expression pattern to match the university names
    pattern = re.compile('|'.join(re.escape(x) for x in universities.split('\n')),re.IGNORECASE)

    # Open and read the text file to search
    with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume3.txt", 'r') as f:
        text = f.read()

    # Find all matches of the university names in the text file
    matches = pattern.findall(text,re.IGNORECASE)

    def myFunc(x):
      if x == "":
        return False
      else:
        return True


    universities_filtered = filter(myFunc, matches)
    universities_non_repeated = list(set(universities_filtered))
    return universities_non_repeated



uni = university(universities)
string_uni = str(uni)

with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume Screening/college.txt", 'r') as f:
    college_data = f.read()

def college(college_data):
    # Compile a regular expression pattern to match the collage_data
    pattern = re.compile('|'.join(re.escape(x) for x in college_data.split('\n')), re.IGNORECASE)

    # Open and read the text file to search
    with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume 13.txt", 'r') as f:
        text = f.read()

    # Find all matches of the jobskill names in the text file
    matches = pattern.findall(text)

    # Print the matches
    def myFunc(x):
        if x == "":
            return False
        else:
            return True

    college_filtered = filter(myFunc, matches)
    college_non_repeated = list(set(college_filtered))
    return college_non_repeated


college_went = college(college_data)
string_college = str(college_went)


def find_email():
    with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume3.txt",) as f:
        resume_text = f.read()

    email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', resume_text)
    personal_email=email[0]
    return personal_email

first_email= find_email()
string_email = str(first_email)


def extract_mobile_number():
    with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume3.txt",) as f:
        resume_text = f.read()
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), resume_text)
    if phone:
         number = ''.join(filter(lambda x: x.isdigit() or x == '+', phone[0]))
         if len(number) > 10:
           return '+' + number
         else:
             return number

with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume3.txt", ) as f:
    resume_text = f.read()

def get_phone(resume_text):
    phone_number2 = []
    # with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume3.txt", ) as f:
    #     resume_text = f.read()
    for item in resume_text:
        phone_number2.append(extract_mobile_number())
        matches = phone_number2

        def myFunc(x):
            if x == "":
                return False
            else:
                return True

    phone_numbers_filtered = filter(myFunc, matches)
    phone_numbers_non_repeated = list(set(phone_numbers_filtered))
    return phone_numbers_non_repeated



first_phone= get_phone(resume_text)
string_phone = str(first_phone)

with open("C:/Users/zaida/Documents/GitHub/Quantum/Resume_parsing/Resume Sample/txt/Resume 9.txt", ) as f:
    extract_name = f.read()
    text = extract_name


def extract_names(extract_name):
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)

    # Define the pattern for name extraction
    pattern = [
        {'POS': 'PROPN'},
        {'POS': 'PROPN', 'OP': '?'},
        {'POS': 'PROPN'}
    ]

    matcher.add('NAME', [pattern])

    doc = nlp(resume_text)
    matches = matcher(doc)

    names = []
    for match_id, start, end in matches:
        names.append(doc[start:end].text)

    return names[0:1]


if __name__ == '__main__':

    names = extract_names(extract_name)

    if names:
        # print("Extracted names:")
        for name in names:
            print (str(name))
    else:
        print("No names found in the resume.")

data = [
    ["Name","Email","Phone Number","Degree", "Address","College","University","Skills","Work Experience"],
    [name,string_email,string_phone,string_degree,string_address,string_college,string_uni,string_software,string_work]]
print(data)

workbook = openpyxl.Workbook()
sheet = workbook.active

for row_idx, row_data in enumerate(data, 1):
    for col_idx, cell_value in enumerate(row_data, 1):
        sheet.cell(row=row_idx, column=col_idx).value = cell_value

workbook.save("output.xlsx")
