import hash_function
import sys

# test = hash_function.hash("hello world")

# print(test)

arr_of_lines = []

file_to_hash = open("file_to_hash.txt", "r")
for line in file_to_hash.readlines(): #file.readlines(), splits the file into a list, where each element is a seperate line
  arr_of_lines.append(line)
#  print(len(arr_of_lines))
# print ("Name of the file: ", file_to_hash.name)
# line = file_to_hash.readline()
# print ("Read Line: %s" % (line))
# Close opened file


file_to_hash.close()