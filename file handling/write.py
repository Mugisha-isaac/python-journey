f = open("demofile.txt", "a")
f.write("New content added to the file")
f.close()

# reading file after appending new data
f = open("demofile.txt", "r")
print(f.read())
f.close()
