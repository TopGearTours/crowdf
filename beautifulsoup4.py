import os
import re
from bs4 import BeautifulSoup


def extract_language_sections(file_list):
    result = ""
    for file_name in file_list:
        language = file_name.split(".")[0].upper()
        with open(file_name, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            section_content = soup.get_text("\n", strip=True)
            result += f"=========={language} SECTION==========\n\n"
            result += section_content + "\n\n"

    return result


# List of HTML files to process
html_files = ["en.html", "sk.html", "cz.html", "pl.html", "de.html"]

# Extract language sections
output = extract_language_sections(html_files)

# Write the output to an HTML file
output_file = "output.html"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(output)

print("Output has been written to the file:", output_file)
