# Contributors:
# Jerry Ge
# Daiming Yang
# University of Southern California

import os
import filecmp

SSTF_Input_Files = []
total_tests = 0
passed_tests = 0

def Parse_Input_Files(path):
	for entry in os.listdir(path):
		if os.path.isfile(os.path.join(path, entry)):
			#print(type(entry))
			global total_tests
			total_tests += 1
			SSTF_Input_Files.append(str(entry))

os.system("clear")
Checker_Path = "CSCI350_HW2_Q1_Checker"
print("=========================================")
print("*****Welcome to CSCI350 HW2 Checker******")
print("=========================================")

os.chdir("../")
os.system("make clean")
os.system("make")
print("-----Compiled Successfully---------------")
# os.chdir(Checker_Path)
# os.system("pwd")

Parse_Input_Files(Checker_Path + "/Input")

# Run the program and generate outputs
for i in range(len(SSTF_Input_Files)):
	input_file_path = Checker_Path + "/Input" + "/" + SSTF_Input_Files[i]
	out_name = SSTF_Input_Files[i][:-3]
	out_name += ".out"
	output_file_path = Checker_Path + "/Output" + "/" + out_name
	os.system("./sim < " + input_file_path + " > " + output_file_path)

	# Compare the Outputs
	expected_file_path = Checker_Path + "/Output" + "/E_" + out_name

	with open(output_file_path) as f1:
		with open(expected_file_path) as f2:
			if f1.read() != f2.read():
				print("Input File Name: " + SSTF_Input_Files[i] + "\n")
				print("Expected: ")
				os.system("cat " + expected_file_path)

				print("Your Output: " )
				os.system("cat " + output_file_path)
			else:
				global passed_tests
				passed_tests += 1
				print("Input File Name: " + SSTF_Input_Files[i] + "\n")
				print("Test Passed!")

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if total_tests == passed_tests:
	print("=========================================================")
	print("======================ALL PASSED!========================")
	print("=========================================================")
else:
	print("Failed: " + str(total_tests - passed_tests) + "/" + str(total_tests))