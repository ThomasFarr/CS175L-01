#CS175L
#Thomas Farrell
#Average From Input File

def main():
    infile = open('numbers.txt', 'r')
    x = 0
    total = 0
    for line in infile:
        x += 1
        print("I read in",str(x),"number(s) Current number is:      ", float(line), end="")
        print (" Total is:    ", end="  ")
        total += float(line)
        print (total)
    avg = total / x
    print("Average: ", avg)

if __name__ == '__main__':
    main()
