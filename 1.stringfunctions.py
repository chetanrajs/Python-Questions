#len() function
str="Python is very very easy"
print("length of string is:",len(str))

#count() function
str="Python is very very easy"
print(str.count("y"))
print(str.count("easy"))

#index() function
str="Python is very very easy"
print(str.index("is"))
print(str.index("a"))

#upper() function
str="Python is very very easy"
print(str.upper())

#lower() function
str="Python is very very easy"
print(str.lower())

#Capitalize() function
str="Python is very very easy"
print(str.capitalize())

#startswith() function
str="Python is very very easy"
print(str.startswith("very"))
print(str.startswith("Python"))
print(str.startswith("is"))

#endswith() function
str="Python is very very easy"
print(str.endswith("easy"))
print(str.endswith("very"))

#split() function
str="Python is very very easy"
print(str.split())

#join() function
str="Python is very very easy"
temp1="!"
temp2="-"
print(temp1.join(str))
print(temp2.join(str))

#find() method
str="Python is very very easy"
print(str.find("is"))
print(str.find("n"))
print(str.find("x"))

#strip() function
str="Python is very very easy"
print(str.strip())

#lstrip() function
str="Python is very very easy"
print(str.lstrip())

#rstrip() function
str="Python is very very easy"
print(str.rstrip())

#replace() function
str="Python is very very easy"
print(str.replace("easy","good"))
