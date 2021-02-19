#Michael King
#Use Find/Replace

ui = input("Enter a phrase")
newText = ui.replace("a", "4")
newText = ui.replace("b", "8")
newText = ui.replace("e", "3")
newText = ui.replace("l", "1")
newText = ui.replace("o", "0")
newText = ui.replace("s", "5")
newText = ui.replace("t", "7")

print(newText)
# Does not print out the replaced text, only the original text

#HOWEVER THIS WORKS ... why do I have to use the same variable name?

my_text = input("Enter some text: ")

my_text = my_text.replace("a", "4")
my_text = my_text.replace("b", "8")
my_text = my_text.replace("e", "3")
my_text = my_text.replace("l", "1")
my_text = my_text.replace("o", "0")
my_text = my_text.replace("s", "5")
my_text = my_text.replace("t", "7")

print(my_text)
