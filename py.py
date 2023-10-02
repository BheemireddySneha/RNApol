
# filename: Z-Score.py ------- for calculation of Z-Scores for files after anm_rbpA 
import sys
import os
#import pylab 
import numpy 

#File input

def main():
	f =open("5UH5_final_em.sq","r")
	f1 =f.readlines()
	for x in range(len(f1)):
		if x < 277:
			print(f1[x])
			
		else:
			break
		




		
if __name__== "__main__":
	main()
