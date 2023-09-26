def create_text_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    filename = "output.txt"  # Change this to your desired file name
    content = "This is the content of the text file."  # Change this to your desired content
    
    create_text_file(filename, content)
