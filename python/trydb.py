# Example: read_file.py

# Define the file path
file_path = r'C:\Users\Lenovo\Desktop\house_prices.csv'  # Replace with your file path

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the entire file contents
    file_contents = file.read()
    
# Print or process the file contents
print("File Contents:")
print(file_contents)
