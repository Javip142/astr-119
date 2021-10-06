#python exceptions let you deal with
#unexpected results

try:
	print(a)	#this will throw an exception since a is not defined 
except:
	print("a is not defined!")

	#there are specifice errors to help with cases
try:
	print(a)	#this will throw an exception since a is not defined
except NameError: 
	print("a is still not defined!")
except:
	print("Somethin else went wrong")

#this will break our program
#what type of program would this be useful for
#since a is not defined
print(a)
