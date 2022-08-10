import os

# I can never remember this, but use it all the time.

currentdir = os.getcwd()
contents_of_current_dir = os.listdir(currentdir)

print(currentdir)
for i in contents_of_current_dir:
    # do some stuff to the items in the dir
    print(i)
