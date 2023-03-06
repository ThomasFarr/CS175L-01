#CS175L
#Thomas Farrell
#Average From Input File

def main():
    x = 1
    total = 0
    try:
        infile = open('numbers.txt', 'r')
        for line in infile:
            try:
                print("I read in",str(x),"number(s) Current number is:      ", float(line), end="")
                print (" Total is:    ", end="  ")
                total += float(line)
                print (total)
                x += 1
    
            except ValueError:
                print('Non-numeric data found in the file.')
            
        avg = total / (x - 1)
        print("Average: ", avg)

    except IOError:
        print('An error occured trying to read the file.')   
    
if __name__ == '__main__':
    main()
