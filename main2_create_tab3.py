import json
import re


# motions = {}
# index = -1
def tsv2json(input_file, output_file, with_slide=False):
    motions = {}
    index = -1
    # global index
    with open(input_file, "r") as f:
        # a = file.readlines()
        # d = {}
        # key = -1
        # value = ""
        flag = True
        for x in f.readlines():
            t_count = x.count("\t")
            if t_count == 3:
                index += 1
                motions[index] = x.strip()
                flag = True
            elif t_count == 4:
                if not with_slide:
                    if flag:
                        flag = False
                    motions[index] += x.strip()
                else:
                    if flag:
                        motions[index] += " \n\t\t[slide begins] "
                        flag = False
                    motions[index] += x.strip()

    with open(output_file, "w", encoding="utf-8") as fw:
        fw.write(json.dumps(motions, indent=4))


# Driver Code
input_filename = "./data/tsv/nationals.tsv"
output_filename = "./data/tab3/nationals.json"
tsv2json(input_filename, output_filename, False)

input_filename = "./data/tsv/internationals.tsv"
output_filename = "./data/tab3/internationals.json"
tsv2json(input_filename, output_filename, False)

input_filename = "./data/tsv/nationals.tsv"
output_filename = "./data/tab3/with_slide/nationals.json"
tsv2json(input_filename, output_filename, True)

input_filename = "./data/tsv/internationals.tsv"
output_filename = "./data/tab3/with_slide/internationals.json"
tsv2json(input_filename, output_filename, True)
