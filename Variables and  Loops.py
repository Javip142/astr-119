import numpy as np #we use numpy for lots of things

def main():
	i=0            # intergers can be declared with a number
	n=10           #here is another interger
	x=119.0        #floating ppoint nums are declared with a ". "

	# we can use numpy to declare arrays quickly
	# arrays are collection of numbers were each number is indexed by 
	# another number

	y = np.zeros(n,dytpe=float)  #delcares 10 zeros as floats using np

	#we can use for lopps to iterate with a variable
	for i in range(n): # i in range[0.n-1]
		y[i]  = 2.0 * float(i) +1. #set y=2i+1 as floats

	# we can alsoo simpy iterate throgh a variable
	for y_element in y:
		print(y_element)

#execute the main function
if __name__ == "__main__":
	main()