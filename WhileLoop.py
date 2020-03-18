import  datetime;
a=0
file = open("c:\\shayan\InsideShayan\\log.txt", "a")
file1 = open("c:\\shayan\InsideShayan\\log1.txt", "a")
file2 = open("c:\\shayan\InsideShayan\\log2.txt", "a")

while a<=1000:
    text= str(a)+" = "+str(datetime.datetime.now())
    print(text)
    file.write(text)
    file1.write(text)
    file2.write(text)
    from time import sleep
    sleep((0.0))
    a=a+1

file.close()
