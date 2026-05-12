try:
    with open("input.txt", "x") as f:
        f.write("Hello, World!")
except FileExistsError:
    print("File already exists")
else:
    print("File created successfully")
