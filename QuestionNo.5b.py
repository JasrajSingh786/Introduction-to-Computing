#To replace two elements in a list and replace that with a single element.
colours = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colours[3:5] = ['Purple'] #Because the index of Black is 3 and [3:5] is interpreted as replace from Index 3 to Index 4 by 'Purple'. 
print(colours)