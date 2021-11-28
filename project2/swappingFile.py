def swappingFile ():
    file1=input("ORIGINAL FILE")
    file2=input("SWAPPING FILE1")
    file3=input("SWAPPING FILE2")
    file4=input("SWAPPING FILE3")
##reading the files    
    with open(file1,'r') as a:
        data_a=a.read()
    with open(file2,'r') as b:
        data_b=b.read()
    with open(file3,'r') as c:
        data_c=c.read()
    with open(file4,'r') as d:
        data_d=d.read()
##writing the files
    with open(file1,'w+') as a:
        a.write(data_d)
    with open(file2,'w+') as b:
        b.write(data_c) 
    with open(file3,'w+') as c:
        c.write(data_b)  
    with open(file4,'w+') as d:
        d.write(data_a) 
##calling the function
swappingFile()                