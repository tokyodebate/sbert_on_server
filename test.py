import json

input_file_name = "data/datastructure/motions_vectors_topk.json"

with open(input_file_name) as f:
	json_dict = json.loads(f.read())

	print(json_dict.keys())
	print(len(json_dict["national_topk_id"]))
	print(json_dict["national_topk_id"])
	print(len(json_dict["national"]))
