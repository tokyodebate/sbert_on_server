# {
# 	"national": [
# 		{
# 			"titleId": 0,
# 			"title": "Aoyama Women's Cup (2021)",
# 			"rounds":
# 				[
# 					{
# 						"id": 0,
# 						"roundId": 0,
# 						"title": "Aoyama Women's Cup (2021)",
# 						"round": "R1",
# 						"motion": "THW force all news organizations to be non profit(i.e. NHK, BBC, PBS)"
# 						"slide": ""
# 					},
# 				]
# 		},
# 	],
# 	"international": [
# 		{

# 		}
# 	],
# }



import copy
import json
import re

import numpy

json_dict = {}
json_dict["national"] = []
json_dict["international"] = []

titleId, id, roundId = 0, 0, 0
len_f = 0
data = {}
# result = {}
# result["national"] = []
# result["international"] = []
results = {}
results["data"] = []
def tsv2json(input_file, type="national"):
    global json_dict
    global titleId, id, roundId, len_f, data
    with open(input_file, "r") as f:
        i = 0
        lst = f.readlines()
        len_f = 0
        for _ in lst:
            len_f += 1

        while (i < len_f):
            print(i)
            # for i, x in enumerate(f.readlines()):
            t_count = lst[i].count("\t")
            if t_count == 0:
                i += 1
            elif t_count == 1:
                if data:
                    json_dict[type].append(data)
                roundId = 0
                data = {}
                title = lst[i].strip()
                data["titleId"] = titleId
                data["title"] = lst[i].strip()
                data["rounds"] = []
                titleId += 1
                i += 1
            elif t_count == 2:
                # data_inner = {}
                # data_inner["id"] = id
                # id += 1
                # data_inner["roundId"] = roundId
                # roundId += 1
                # data_inner["title"] = title
                round = lst[i].strip()
                i += 1
            elif t_count == 3:
                data_inner = {}
                data_inner["id"] = id
                id += 1
                data_inner["roundId"] = roundId
                roundId += 1
                data_inner["round"] = round
                data_inner["title"] = title
                data_inner["motion"] = lst[i].strip()
                data_inner["slide"] = ""
                data_inner["type"] = type
                # data_inner["vector"] = []
                # data_inner["topk"] = []
                i += 1
                # while (i < len_f and lst[i].count('\t') == 3):
                #     data_innder["motion"]
                while (i < len_f and lst[i].count('\t') == 4):
                    data_inner["slide"] += lst[i].strip()
                    i += 1
                data["rounds"].append(data_inner)
                results["data"].append(data_inner)
                # json_dict[type][titleId - 1]["rounds"][roundId - 1]["slide"] = ""
            # elif t_count == 4:
            # 	print(titleId, id, title)

            # 	json_dict[type][titleId - 2]["rounds"][roundId - 2]["slide"] += lst[i].strip()
            # 	# json_dict[type][titleId - 1]["rounds"][roundId - 1]["slide"] += "\n"
            # 	# json_dict[type][titleId]["rounds"][roundId]["slide"] += "\n"


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


tsv2json("./data/tsv/nationals.tsv", "national")
tsv2json("./data/tsv/internationals.tsv", "international")

output_file_name = "./data/datastructure/datastructure_simple.json"

with open(output_file_name, 'w', encoding='utf-8') as fw:
    fw.write(json.dumps(results, indent=4, cls=MyEncoder))
