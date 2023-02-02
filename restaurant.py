#CS175L
#Thomas Farrell
#Restaurant

vegetarian = False
vegan = False
gluten_free = False

vegetarian = input('Is anyone in your party a vegetarian? ')
if vegetarian == 'yes':
    vegetarian = True
else:
    vegetarian = False



vegan = input('Is anyone in your party a vegan? ')
if vegan == 'yes':
    vegan = True
else:
    vegan = False


gluten_free = input('Is anyone in your party gluten-free? ')
if gluten_free == 'yes':
    gluten_free = True
else:
    gluten_free = False
    
print("Here are your restuarant choices.")

if vegetarian == False and vegan == False and gluten_free == False:
    print(" Joe's Gourmet Burgers")
elif vegan == False and gluten_free == False:
    print(" Mama's Fine Italian")
elif vegan == False:
    print(" Main Street Pizza Company")


print(" Corner Cafe")
print(" The Chef's Kitchen")
