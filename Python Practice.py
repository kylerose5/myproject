# Let's use tuples to store information about a file: its name, its type and its size in bytes. 
# This code returns the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
#__________________________________________________________________________________________________________________________

# function that creates a new list containg 1 string/person including their name and email address.
# formated like this------ Terrance Ford <terrance@example.com>
def full_emails(people): # this funciton will recieve a list of people. people is list of tuples(email add, full name)
    result = []
    for email, name in people: # unpacking values as we iterate in variables called email and name
        result.append("{} <{}>".format(name,email)) 
    return result
print(full_emails([("alex@example.com", "Alex Diego"),("shay@example.com", "Shay Brandt")]))
#_______________________________________________________________________________________________________________________

# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [file.replace('.hpp', '.h') for file in filenames]
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
#________________________________________________________________________________________________________________________________________

# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2,
def group_list(group, users):
  members = ', '.join(users)
  return '{}:{}'.format(group, ' ' + members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"