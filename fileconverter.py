input_file_path = "normal.txt"
output_file_path = "symbreg.csv"

# Read the content of the input file
with open(input_file_path, "r") as input_file:
    content = input_file.read()

# Replace tabs with pipe characters
modified_content = content.replace("\t", "|")

# Write the modified content to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(modified_content)

print(f"Tabs replaced and saved to {output_file_path}")