

# {
# 	"national":
# 		[
# 			"THW force all news organizations to be non profit(i.e. NHK, BBC, PBS)",
# 			"THR the romanticization of success stories about educational achievement(e.g Biri Gal, Dragon Zakura)",
# 		],
# 	"international":
# 		""
# 		[

# 		],
# }

import json
from collections import OrderedDict
import pprint


json_dict = {}
json_dict["national"] = []
json_dict["international"] = []

input_file_name = "./data/json/data.json"

with open(input_file_name, "r") as f:
	datas = json.loads(f.read())
	for i in range(len(datas["national"])):
		for j in range(len(datas["national"][i]["rounds"])):
			json_dict["national"].append(datas["national"][i]["rounds"][j]["motion"])

	for i in range(len(datas["international"])):
		for j in range(len(datas["international"][i]["rounds"])):
			json_dict["international"].append(datas["international"][i]["rounds"][j]["motion"])


print(len(json_dict["national"]))

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

output_file_name = "./data/motions/data.json"
with open(output_file_name, 'w', encoding='utf-8') as fw:
    fw.write(json.dumps(json_dict, indent=4, cls=MyEncoder))