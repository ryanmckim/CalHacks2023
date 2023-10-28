import re

# Define the file path
file_path = "requirements.txt"

# Define a regular expression pattern to remove the extra information
pattern = r'@\s.*'

# Read the contents of the file
with open(file_path, 'r+') as file:
    file_content = file.read()
    # Move the cursor to the beginning of the file
    file.seek(0)
    # Remove the extra information using re.sub
    cleaned_content = re.sub(pattern, '', file_content)
    # Write the modified content back to the file
    file.write(cleaned_content)
    # If the new content is shorter than the previous content, truncate the file to the new size
    file.truncate()

