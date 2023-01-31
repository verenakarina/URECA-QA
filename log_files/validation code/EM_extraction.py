import re
import os

#input base EM
base_EM = float(58.00)

#input target log file
input_folder = "/Users/verenakarina/Desktop/URECA/log_files/results/single_reader" #change to target folder file path
folder_list = os.listdir(input_folder)

for folder in sorted(folder_list, reverse=True):
    if folder != ".DS_Store":
        print(folder)
        file_list = f"{input_folder}/{folder}"
        log_list = os.listdir(file_list)

        for log in log_list:
            if log != ".hydra":
                input_log = f"{file_list}/{log}"

                #read log file line by line, convert to list of strings
                with open(input_log) as f:
                    f = f.readlines()

                EM_line = "EM"
                for line in f:
                    if EM_line in line:
                        EM_string = line


                #Regular Expression to parse EM score
                EM_score = re.search(r'EM\s([0-9]+\.[0-9]+)', EM_string)
                EM = EM_score.group()
                #convert string to integer
                final_EM = float(EM[-5:])
                if final_EM < base_EM:
                    print(final_EM, "lower than base")
                elif final_EM == base_EM:
                    print(final_EM, "same as base")
                else:
                    print(final_EM, "higher than base")
