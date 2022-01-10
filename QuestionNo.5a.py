#To write a python program to print a specified list after removing 4th element
#The list in our case is colours = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colours = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Element_to_be_removed = input(" The element to be removed is: ") #In order to remove an element, which in our case is Black.
colours.remove(Element_to_be_removed)
print(colours)


