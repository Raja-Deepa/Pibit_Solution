import json
from pdfminer.high_level import extract_text

def parse_resume_to_json(resume_text):
    lines = resume_text.split('\n')
    resume_json = {
        "personal_information": {},
        "education": [],
        "work_experience": [],
        "skills": [],
        "projects": [],
        "achievements": [],
        "positions_of_responsibility": [],
        "soft_skills": []
    }

    # Example parsing logic
    section = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if "Name:" in line:
            resume_json["personal_information"]["name"] = line.split("Name:")[1].strip()
        elif "Email:" in line:
            resume_json["personal_information"]["email"] = line.split("Email:")[1].strip()
        elif "Phone:" in line:
            resume_json["personal_information"]["phone"] = line.split("Phone:")[1].strip()
        elif "Education" in line:
            section = "education"
        elif "Experience" in line or "Work Experience" in line:
            section = "work_experience"
        elif "Skills" in line:
            section = "skills"
        elif "Projects" in line:
            section = "projects"
        elif "Achievements" in line:
            section = "achievements"
        elif "Positions of Responsibility" in line:
            section = "positions_of_responsibility"
        elif "Soft Skills" in line:
            section = "soft_skills"
        elif section:
            if section == "skills" or section == "soft_skills":
                resume_json[section].append(line.strip())
            else:
                resume_json[section].append(line.strip())
        else:
            continue

    return resume_json

if __name__ == "__main__":
    resume_path = 'R_Deepa_Resume.pdf'  # Replace with the path to your resume PDF
    resume_text = extract_text(resume_path)
    resume_json = parse_resume_to_json(resume_text)
    
    with open('resume.json', 'w') as json_file:
        json.dump(resume_json, json_file, indent=4)

    print("Resume parsed to JSON and saved as resume.json")
