##Given string
A="Why fit in, When you are Born to Stand Out"
#q1 find length of string #use len(string-var)
print(f'Length of a String: {len(A)}')
#q2 to check how many times an alphabet is occuring
print(f'To check how many time w is occuring:{A.count("W")}')
#q3 lower-case and upper-case
print(A.lower())#converts string to lower-case
print(A.upper())#converts string to upper-case
#q4 To convert following string to title
print(A.title()) #ist letter of each word as upper-case
#q5 To find index of a part of string
print(A.find("Why fit in")) #returns index of where founded in string