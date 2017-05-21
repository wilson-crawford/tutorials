from sys import argv

script, filename = argv

txt = open(filename)

print "Here's you file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
# modifiers.  the + modifier 'w+', 'r+', and 'a+'
# this will open the file both read and write mode,
# depending on the character use position.
