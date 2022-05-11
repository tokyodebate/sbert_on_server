import json

import matplotlib.pyplot as plt
import numpy as np

input_file_name = "/Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/data/datastructure/allVectors.json"

x = []
with open(input_file_name) as f:
    json_dict = json.loads(f.read())
    for i in range(len(json_dict)):
        for j in range(len(json_dict[0])):
            x.append(json_dict[i][j])
x = np.array(x)

print(f"shape: {len(json_dict), len(json_dict[0])}")
print(f"max: {max(x)}")
print(f"min: {min(x)}")
print(f"mean: {sum(x)/len(x)}")
# 内積を保持するためにはv→v/σの変形はok. (v-μ)/σだとシフトする. normalize=max(max(numbers), -min(numbers)).    v / normalize * 127
print(np.sort(x)[300:400])

# normalize = max(max(x), -min(x))
# x = x / normalize * 127
# a = np.array(x, dtype="i8")

# print(f"normalized max: {max(x)}")
# print(f"normalized min: {min(x)}")
# print(f"normalized mean: {sum(x)/len(x)}")

# print(f"normalized max: {max(a)}")
# print(f"normalized min: {min(a)}")
# print(f"normalized mean: {sum(a)/len(a)}")
# print(a)

# import math

# import numpy
# class MyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, numpy.integer):
#             return int(obj)
#         elif isinstance(obj, numpy.floating):
#             return float(obj)
#         elif isinstance(obj, numpy.ndarray):
#             return obj.tolist()
#         else:
#             return super(MyEncoder, self).default(obj)

# output_file_name = "./data/datastructure/int8"
# with open(output_file_name, 'w', encoding='utf-8') as fw:
#     fw.write(json.dumps(a, indent=4, cls=MyEncoder))
# # with open("./data/datastructure/int", "w") as f:
# # 	f.write(w)


