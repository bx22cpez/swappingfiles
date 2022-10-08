def swapFileData():
    file1=input("input first file name-")
    file2=input("input second file name-")
    with open(file1,"r")as a:
        dataa=a.read()
        print (dataa)
    with open(file2,"r")as b:
        datab=b.read()

    with open(file1,"w")as a:
        a.write(datab)

    with open(file2, "w")as b:
        b.write(dataa)



swapFileData()

