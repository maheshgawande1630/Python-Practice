#WAF to find in which line of the file does the word "learning" occur first.print -1 if word not found

def print_line():
    word="learning"
    data = True
    line_no = 1

    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1
          

                
            
print_line()