
def swapFileData():
    a=open("file1.txt","r")
    data_a=a.read()

    b=open("file2.txt","r")
    data_b=b.read()

    a=open("file1.txt","w")
    a.write(data_b)

    b=open("file2.txt","w")
    b.write(data_a)
swapFileData()
