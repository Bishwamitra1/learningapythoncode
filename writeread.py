file = open('input.txt','w') # open the file
file.write('first text,dhdhfdhfk,sddsdsdd\n') # write to the file


file =open('input.txt', 'a') # open the file to append mode
file.write('Adding text,sdfsdsd,sdfsdfsd\n')

file =open('input.txt', 'r') # open the file in read mode 
content = file.read() # read the content of the file

file.close()

print(content)