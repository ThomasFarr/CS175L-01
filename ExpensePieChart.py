#CS175L
#Thomas Farrell
#ExpensePieChart

import matplotlib.pyplot as plt

def main():
    try:
        file = open('expenses.txt', 'r')
        subjects = []
        amounts = []
        i = 0
        for line in file:
            subject = line.split('\t')[0]
            subjects.append(subject)
            amount = line.split('\t')[1].rstrip('\n')
            if amount.isdigit():
                amounts.append(amount)
            else:
                del subjects[i]
            i+=1
        plt.pie(amounts, labels=subjects)
        plt.title('Monthly Expenses')
        plt.show()
        
    except IOError:
        print ('An error occured trying to read the file.')

if __name__ == '__main__':
    main()
