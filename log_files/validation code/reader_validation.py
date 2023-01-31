import re
import os

#input target log file
input_folder = "/Users/verenakarina/Desktop/URECA/log_files/results/single_reader"
folder_list = os.listdir(input_folder)

for folder in sorted(folder_list, reverse=True):
    print(folder)
    file_list = f"{input_folder}/{folder}"
    log_list = os.listdir(file_list)

    for log in log_list:
        if log != ".hydra":
            input_log = f"{file_list}/{log}"

            #read log file line by line, convert to list of strings
            with open(input_log) as f:
                f = f.readlines()

            #parameter from BioASQ
            parameter = ["encoder_model_type: hf_bert",
                        "pretrained_model_cfg: gdario/biobert_bioasq",
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
