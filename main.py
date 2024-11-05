"""import subprocess
import os

# Define the path to your .tex file
tex_file_path = "resume.tex"
output_directory = os.path.abspath("output")  # Define an output directory

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Define the work experience bullet points
work_experience_points = {
    "Jio Platforms Limited": [
        "Revamped the Jio Cinema platform, increasing user retention by 40\\%.",
        "Engineered test case generation bot using OpenAI GPT models, achieving 90\\% accuracy.",
    ],
    "TCS iON": [
        "Launched a highly responsive hotel reservation system, handling 1,000+ concurrent users.",
        "Integrated front-end with back-end using Spring Boot for smooth data flow."
    ]
}

# Define the projects with titles and bullet points
projects = {
    "Test Gen Bot": [
        "Spearheaded a project to enhance software testing processes, improving efficiency by 60\\%.",
        "Designed and developed a bot using OpenAI GPT's Fine-tuned models."
    ],
    "Chess Bot": [
        "Created a C++ project enabling users to play chess against an AI.",
        "Incorporated advanced chess rules to enhance game complexity."
    ],
    "Cryptocurrency Exchange": [
        "Built an online platform using Reactjs, Solidity, and Pancake Swap API.",
        "Implemented features for depositing funds and trading cryptocurrencies."
    ],
    "Finance-Management": [
        "Integrated OAuth2.0 authentication using the Google Cloud API.",
        "Developed a REST API and implemented MongoDB to streamline data management."
    ]
}

# Read the LaTeX file and store the original content
with open(tex_file_path, 'r', encoding='utf-8') as file:
    original_lines = file.readlines()

# Function to insert bullet points
def insert_bullet_points(lines, placeholder, bullet_points):
    for i, line in enumerate(lines):
        if placeholder in line:
            bullet_point_lines = [f"\\resumeItem{{{bp}}}\n" for bp in bullet_points]
            lines[i:i+1] = bullet_point_lines
            break
    return lines

# Insert work experience bullet points
for company, points in work_experience_points.items():
    lines = insert_bullet_points(original_lines, '% INSERT WORK EXPERIENCE POINTS HERE', points)

# Insert project titles and bullet points
project_lines = []
for title, points in projects.items():
    project_lines.append(f"\\resumeProjectHeading{{\\textbf{{{title}}}}}{{}}\n")
    project_lines.append("\\resumeItemListStart\n")
    project_lines.extend([f"\\resumeItem{{{bp}}}\n" for bp in points])
    project_lines.append("\\resumeItemListEnd\n")

for i, line in enumerate(original_lines):
    if '% INSERT PROJECTS HERE' in line:
        original_lines[i:i+1] = project_lines
        break

# Write the updated content with bullet points to the LaTeX file
with open(tex_file_path, 'w', encoding='utf-8') as file:
    file.writelines(original_lines)

# Define the Docker command to compile the .tex file
docker_command = [
    'docker', 'run', '--rm',
    '-v', f'{os.path.abspath(".")}:/data',  # Mount the current directory to /data in the container
    '-w', '/data',  # Set the working directory inside the container
    'texlive/texlive',
    'pdflatex', '-output-directory', '/data/output', tex_file_path
]

# Run the Docker command
try:
    subprocess.run(docker_command, check=True)
    print("PDF generated successfully.")
    
    # Restore the original LaTeX content
    with open(tex_file_path, 'w', encoding='utf-8') as file:
        file.writelines(original_lines)

except subprocess.CalledProcessError as e:
    print("An error occurred while generating the PDF:", e)
    # If an error occurs, restore the original LaTeX content
    with open(tex_file_path, 'w', encoding='utf-8') as file:
        file.writelines(original_lines)
"""

import subprocess
import os
import shutil

# Define the path to your .tex file
tex_file_path = "resume.tex"
output_directory = os.path.abspath("output")  # Define an output directory

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Define the work experience bullet points
work_experience_points = {
    "Jio Platforms Limited": [
        "Revamped the Jio Cinema platform, increasing user retention by 40\\%.",
        "Engineered test case generation bot using OpenAI GPT models, achieving 90\\% accuracy.",
    ],
    "TCS iON": [
        "Launched a highly responsive hotel reservation system, handling 1,000+ concurrent users.",
        "Integrated front-end with back-end using Spring Boot for smooth data flow."
    ]
}

# Define the projects with titles and bullet points
projects = {
    "Test Gen Bot": [
        "Spearheaded a project to enhance software testing processes, improving efficiency by 60\\%.",
        "Designed and developed a bot using OpenAI GPT's Fine-tuned models."
    ],
    "Chess Bot": [
        "Created a C++ project enabling users to play chess against an AI.",
        "Incorporated advanced chess rules to enhance game complexity."
    ],
    "Cryptocurrency Exchange": [
        "Built an online platform using Reactjs, Solidity, and Pancake Swap API.",
        "Implemented features for depositing funds and trading cryptocurrencies."
    ],
    "Finance-Management": [
        "Integrated OAuth2.0 authentication using the Google Cloud API.",
        "Developed a REST API and implemented MongoDB to streamline data management."
    ]
}

# Read the LaTeX file and store the original content
with open(tex_file_path, 'r', encoding='utf-8') as file:
    original_lines = file.readlines()

# Copy the original content to restore later
backup_lines = original_lines.copy()

# Function to insert bullet points
def insert_bullet_points(lines, placeholder, bullet_points):
    for i, line in enumerate(lines):
        if placeholder in line:
            bullet_point_lines = [f"\\resumeItem{{{bp}}}\n" for bp in bullet_points]
            lines[i:i+1] = bullet_point_lines
            break
    return lines

# Insert work experience bullet points
for company, points in work_experience_points.items():
    original_lines = insert_bullet_points(original_lines, '% INSERT WORK EXPERIENCE POINTS HERE', points)

# Insert project titles and bullet points
project_lines = []
for title, points in projects.items():
    project_lines.append(f"\\resumeProjectHeading{{\\textbf{{{title}}}}}{{}}\n")
    project_lines.append("\\resumeItemListStart\n")
    project_lines.extend([f"\\resumeItem{{{bp}}}\n" for bp in points])
    project_lines.append("\\resumeItemListEnd\n")

for i, line in enumerate(original_lines):
    if '% INSERT PROJECTS HERE' in line:
        original_lines[i:i+1] = project_lines
        break

# Write the updated content with bullet points to the LaTeX file
with open(tex_file_path, 'w', encoding='utf-8') as file:
    file.writelines(original_lines)

# Define the Docker command to compile the .tex file
docker_command = [
    'docker', 'run', '--rm',
    '-v', f'{os.path.abspath(".")}:/data',  # Mount the current directory to /data in the container
    '-w', '/data',  # Set the working directory inside the container
    'texlive/texlive',
    'pdflatex', '-output-directory', '/data/output', tex_file_path
]

# Run the Docker command
try:
    subprocess.run(docker_command, check=True)
    print("PDF generated successfully.")
finally:
    # Restore the original LaTeX content
    with open(tex_file_path, 'w', encoding='utf-8') as file:
        file.writelines(backup_lines)
