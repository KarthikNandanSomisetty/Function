def swapFileData():
    sample1= input("enter the name of your 1st file: ")
    sample2= input("enter the name of your 2nd file: ")
    data_a="#"
    data_b="#"

    with open(sample1, 'r')as a:
        data_a = a.read()
        
    with open(sample2, 'r')as b:
        data_b = b.read()


    with open(sample1, 'w')as a:
        a.write(data_b)


    with open(sample2, 'w')as b:
        b.write(data_a)

    print("file content changed")

swapFileData()