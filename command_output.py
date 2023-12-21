import subprocess

# Command to execute
command = "echo Hello, World!"

# Run the command and capture the output
output = subprocess.check_output(command, shell=True, encoding='utf-8')

# Print the output
print(output)

# Store the output in a variable
output_variable = output.strip()

# Print the stored output
print(output_variable)
