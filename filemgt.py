def read_and_modify_file():
    # Get filename from user
    filename = input("Enter the filename to read: ")
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = "modified_" + filename
        
        # Write modified content to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Success! Modified file saved as '{output_filename}'")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{filename}'. It might be a binary file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()