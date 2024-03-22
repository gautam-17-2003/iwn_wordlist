import csv
def main():
    input_file = 'verb.txt'
    with open(input_file, 'r',encoding="utf-8") as file:
                # Read the content of the file
                content = file.read()
                
    modified_content = content.replace(':', ',')

    with open('verb.txt', 'w',encoding="utf-8") as file:
                # Write the modified content back to the file
                file.write(modified_content)

    print("Commas replaced successfully.")
    
if __name__ == "__main__":
    main()