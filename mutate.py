#how to mutate strings in a list
fileNames= ["1.Raw Data.txt","1.Reports.txt","1.Presentations.txt"]
for filename in fileNames:
    filename = filename.replace(".", "-",1)
    print(filename)