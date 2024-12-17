import os

text = input()

def write_and_read(text):
    file_path = os.path.join(os.getcwd(), 'output.txt')
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        result = file.read()
    
    return result

print(write_and_read(text))
