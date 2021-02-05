import hash_function
import sys

# test = hash_function.hash("hello world")

# print(test)

arr_of_lines = []

file_to_hash = open("file_to_hash.txt", "r")
for line in file_to_hash.readlines(): #file.readlines(), splits the file into a list, where each element is a seperate line
   temp_arr = line.split('=')
   temp_str = temp_arr[0] + " = " + hash_function.hash(temp_arr[1]).decode("utf-8") 
   print(temp_str)
   arr_of_lines.append(temp_str)
#  print(len(arr_of_lines))
# print ("Name of the file: ", file_to_hash.name)
# line = file_to_hash.readline()
# print ("Read Line: %s" % (line))
# Close opened file

file_to_hash.close()

with open("result.txt", 'w') as writer:
    for line in arr_of_lines:
        writer.write(line + "\n")

writer.close
