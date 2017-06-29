# Madlibs:
# 1. Create a few variables that get certain bits of info from the user
# 2. Print out a string with a short story, using the info gathered
# %s (string) %d (digit)
name = raw_input("What is your name? >>")
age = raw_input("How old are you? >>")
home = raw_input("Where do you live? >>")
feeling = raw_input("How are you feeling? >>")
story = "Here is a %s story. A long long time ago lived a dog called %s. %s was its home. A human called Tom lived together with %s until it died at the age of %s." % (feeling,name,home,name,age)

print story
