#CS175L
#Thomas Farrell
#Avg & Grade

y = 1
scores = []
letter_grade = []
def determine_grade(test_score):
    if test_score > 89:
        a = ("    A")
        letter_grade.append(a)
    elif test_score > 79 and test_score < 89:
        b = ("    B")
        letter_grade.append(b)
    elif test_score > 69 and test_score < 79:
        c = ("    C")
        letter_grade.append(c)
    elif test_score > 59 and test_score < 69:
        d = ("    D")
        letter_grade.append(d)
    else:
        f = ("    F")
        letter_grade.append(f)
    

def calc_average():
    y = 1
    scores = []
    total = 0
    print ("")
    for y in range(1,6):
        question = "Enter Score " + str(y) + ":   "
        test_score = int(input(question))
        scores.append(test_score)
        determine_grade(test_score)
        total += test_score
        y += 1
    print (" ")
    print ("Score   Numeric Grade   Letter Grade")
    print ("---------------------------------------")
    print ("Score 1:   " + str(float(scores[0])) + letter_grade[0])
    print ("Score 2:   " + str(float(scores[1])) + letter_grade[1])
    print ("Score 3:   " + str(float(scores[2])) + letter_grade[2])
    print ("Score 4:   " + str(float(scores[3])) + letter_grade[3])
    print ("Score 5:   " + str(float(scores[4])) + letter_grade[4])
    avg = total / 5
    print ("Average score: ", avg, end="")
    avg = test_score
    determine_grade(test_score)
    print (letter_grade[5])
    print("")
    repeat()

def repeat():
    again = input("Enter 'yes' if you would like to do another calculation: ")
    if again == 'yes' or again =='Yes':
        letter_grade.clear()
        calc_average()
    elif again == 'no' or again == 'No':
        print ("Have a Good Day!")
    else:
        print("Not right input. Must be 'yes' or 'no'.")
        repeat()
                  
calc_average()


