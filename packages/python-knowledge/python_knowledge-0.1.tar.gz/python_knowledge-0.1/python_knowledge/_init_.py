print('команды: help(1)')
def helpanite(f):
    with open('pyp.txt',encoding='ANSI') as f:
        line = f.readline()
        file = open("copy.txt", "w") 
        
       
        while line:
            line = f.readline()
            file.write(line) 
            #print(line)
            
        file.close() 
        print('В директории, где был создан .py файл, создан .txt док со шпаргалкой по питону')

