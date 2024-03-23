#Reading Files

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#Writing to Files

with open("my_file.txt", mode="w") as file:
    file.write("New text.")

#append
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
    
#Opening a File that doesn't exit in write mode will create it from scratch

with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.")
