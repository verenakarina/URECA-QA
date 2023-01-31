import re
import os

#input target log file
input_folder = "/Users/verenakarina/Desktop/URECA/log_files/results/single_retrieval" #change to target folder file path
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

                #parameter from BioLinkBERT
                parameter = ["encoder_model_type: hf_bert",
                            "pretrained_model_cfg: michiyasunaga/BioLinkBERT-base",
                            "pretrained_file: null",
                            "projection_dim: 0",
                            "sequence_length: 300",
                            "dropout: 0.1",
                            "fix_ctx_encoder: false",
                            "pretrained: true"]

                #CHECK PARAMETER
                #check whether the parameters in target log file match those in BioLinkBERT's
                match_phrase = 0
                for line in f:
                    for phrase in parameter:
                        if phrase in line:
                            match_phrase += 1
                            break
                if len(parameter) == match_phrase:
                    print("Parameters: matched!")
                else:
                    print("Parameters: NOT matched!")


                #CHECK INPUT AND OUTPUT FILE

                csv_line = "Reading saved model from"
                for line in f:
                    if csv_line in line:
                        #regular expression to parse input csv
                        csv_name = re.search('en-\w+-en', line)
                        input_csv_name = csv_name.group()

                        #extract input and output file from target log file
                        input_output = ["Reading saved model from", "out_file: /"]

                        #check match
                        match_file = []
                        for line in f:
                            for phrase in input_output:
                                if phrase in line:
                                    match_file.append(line)
                                    break

                        check = 0
                        regexp = re.compile(rf'{input_csv_name}')
                        for file in match_file:
                            if regexp.search(file):
                                check += 1

                        if check == 2:
                            print("Input and output file: matched!")
                        else:
                            print("Input and output file: NOT matched!")

