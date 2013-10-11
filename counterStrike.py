import sys
import glob
import os

def main():
	filenames = glob.glob("*.txt")
	filenames_len = len(filenames)
	if (filenames_len == 0):
		print "No students upload their numbers.";
		exit(0)
	else:
		names = [None]*(filenames_len)
		self_number = [None]*(filenames_len)
		other_number1 = [None]*(filenames_len)
		other_number2 = [None]*(filenames_len)
		other_number3 = [None]*(filenames_len)
		
		for i in range (0, filenames_len):
			f = open(filenames[i], "r");
			names[i] = f.readline().rstrip()
			self_number[i] = f.readline().rstrip()
			other_number1[i] = f.readline().rstrip()
			other_number2[i] = f.readline().rstrip()
			other_number3[i] = f.readline().rstrip()
			f.close()

		print "*Follow this:     Name  \tSelf_number\tReview_#1\tReview_#2\tReview_#3"
		print"--------------------------------------------------------------------------------------------"
		
		for i in range (0, filenames_len):
			result = ""
			result += names[i]
			result += "\t\t"
			result += self_number[i]
			result += "\t\t"
			for j in range (0, filenames_len):
				if (other_number1[i] == self_number[j]):
					result += names[j]+"("+other_number1[i]+")"
					result += "\t\t"
					break
			if (other_number1[i] != self_number[j]):
				result += other_number1[i]
				result += "\t\t"
			for m in range (0, filenames_len):
				if (other_number2[i] == self_number[m]):
					result += names[m]+"("+other_number2[i]+")"
					result += "\t\t"
					break
			if (other_number2[i] != self_number[m]):
				result += other_number2[i]
				result += "\t\t"
			for n in range (0, filenames_len):
				if (other_number3[i] == self_number[n]):
					result += names[n]+"("+other_number3[i]+")"
					result += "\t\t"
					break
			if (other_number3[i] != self_number[n]):
				result += other_number3[i]
				result += "\t\t"
			print result
			print"----------------------------------------------------------------------------------------------------------------------------"




			
if __name__ == "__main__":
	main()
