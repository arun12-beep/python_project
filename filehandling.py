with open("test.txt","w") as f:
    print("enter the contets to the file. type bye to stop")
    while True:
        content=input(">>")
        if "bye" in content.lower():
            break
        f.write(content+"\n")
print("writing to file is completed..")
print("contents in file is:")
try:
    with open("test.txt","r") as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print("file does't exist")