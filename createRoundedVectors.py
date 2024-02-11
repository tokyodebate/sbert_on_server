import json

from collections import OrderedDict
import pprint


input_file_name = "./data/vectors/data.json"

import numpy as np

with open(input_file_name) as f:
	datas = np.array(json.loads(f.read()))*10000

json_dict = []
for i in range(datas.shape[0]):
	lst = []
	for j in range(datas.shape[1]):
		lst.append(int(datas[i][j]))
	json_dict.append(lst)


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

output_file_name = "./data/roundedVectors/data.json"
with open(output_file_name, 'w', encoding='utf-8') as fw:
	fw.write(json.dumps(json_dict, indent=4, cls=MyEncoder))