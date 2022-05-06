import json
import re
import copy

from regex import E
#  naitonals.tsv をそのまま表せるjson
index = -1
id = -1
i = -1
json_dict = {}
def tsv2json(input_file, type="national"):
	global json_dict
	json_dict[type] = {}
	global index, id, i
	index, id, i = -1, -1, -1
	title = ""
	flag = True
	with open(input_file, "r") as f:
		for x in f.readlines():
			t_count = x.count("\t")
			if t_count == 1:
				flag = True
				i = -1
				index += 1
				json_dict[type][str(index)] = {}
				title = x.strip()
				json_dict[type][(str(index))]["title"] = title
			elif t_count == 2:
				if flag:
					json_dict[type][(str(index))]["motions"] = {}
					flag = False
				i += 1
				id += 1
				print(i)
				print(id)
				# json_dict[type][(str(index))]["motions"] = {}

				json_dict[type][(str(index))]["motions"][i] = {}
				# d["id"] = id
				# d["info"] = {}
				# d["info"]["title"] = title
				# d["info"]["round"] = x.strip()
				json_dict[type][(str(index))]["motions"][i]["id"] = id
				json_dict[type][(str(index))]["motions"][i]["info"] = {}
				json_dict[type][(str(index))]["motions"][i]["info"]["title"] = title
				json_dict[type][(str(index))]["motions"][i]["info"]["round"] = x.strip()
			elif t_count == 3:
				# d["info"]["motion"] = x.strip()
				json_dict[type][(str(index))]["motions"][i]["info"]["motion"] = x.strip()
			elif t_count == 4:
				# d["info"]["slide"] = x.strip()
				json_dict[type][(str(index))]["motions"][i]["info"]["slide"] = x.strip()

import numpy

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
tsv2json("./data/tsv/nationals.tsv", "international")



output_file_name = "./data/datastructure/datastructure.json"
with open(output_file_name, 'w', encoding='utf-8') as fw:
	fw.write(json.dumps(json_dict, indent=4, cls=MyEncoder))


