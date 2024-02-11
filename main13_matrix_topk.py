import json
from re import M

import numpy as np
from numpy import dot
from numpy.linalg import norm

input_file_name = "data/vectors/data.json"


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

json_topk = []

with open(input_file_name) as f:
    json_dict = json.loads(f.read())

    m = np.matrix(json_dict)
    print(m)
    print(m*m.T)
    mm = -m*m.T
    print(mm)
    print(mm.argsort())
    mm_argsort = mm.argsort()
    output = mm_argsort[:, 0: 20]
    print(output)

    output_file_name = "data/datastructure/top20.json"
    with open(output_file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(output, cls=MyEncoder))
        # f.write(str(output))
        # for line in output["national"]:
        #     np.savetxt(f, line, fmt="%d")


    # def topk(List1, vectors, sentences, K=10):
    # 	results = []
    # 	for _ in range(len(vectors)):
    # 		List2 = vectors[_]
    # 		result = dot(List1, List2) / (norm(List1) * norm(List2))
    # 		results.append(result)
    # 	K = 10
    # 	# ソートはされていない上位k件のインデックス
    # 	my_array = np.array(results)
    # 	unsorted_max_indices = np.argpartition(-my_array, K)[:K]
    # 	# 上位k件の値
    # 	y = my_array[unsorted_max_indices]
    # 	# 大きい順にソートし、インデックスを取得
    # 	indices = np.argsort(-y)
    # 	# 類似度上位k件のインデックス
    # 	max_k_indices = unsorted_max_indices[indices]
    # 	max_k_sentences = []
    # 	for i in max_k_indices:
    # 		max_k_sentences.append(sentences[i])
    # 	return max_k_indices, max_k_sentences

    # json_dict["national_topk_id"] = []
    # indices, sentences = topk(json_dict["national_vectors"][0], json_dict["national_vectors"], json_dict["national"])
    # json_dict["national_topk_id"].append(indices)
    # # print(indices)
    # # print(json_dict)

    # json_dict["national_topk_id"] = []
    # length = len(json_dict["national"])
    # national_vectors = json_dict["national_vectors"]
    # national = json_dict["national"]
    # for i in range(length):
    # 	indices, sentences = topk(json_dict["national_vectors"][i], national_vectors, national)
    # 	json_dict["national_topk_id"].append(indices)
    # 	if i % 1 == 0:
    # 		print(f"national {i}/{length}")

    # json_dict["international_topk_id"] = []
    # length = len(json_dict["international"])
    # international_vectors, international = json_dict["international_vectors"], json_dict["international"]
    # for i in range(length):
    # 	indices, sentences = topk(json_dict["international_vectors"][i], international_vectors, international)
    # 	json_dict["international_topk_id"].append(indices)
    # 	if i % 1 == 0:
    # 		print(f"international {i}/{length}")

    # output_file_name = "data/datastructure/motions_vectors_topk.json"
    # with open(output_file_name, "w", encoding="utf-8") as f:
    # 	f.write(json.dumps(json_dict, indent=4, cls=MyEncoder))






    # length = len(json_dict["national"])
    # national_vectors = json_dict["national_vectors"]
    # national = json_dict["national"]
    # for i in range(length):
    # 	indices, sentences = topk(national_vectors[i], national_vectors, national)
    # 	json_topk["national"].append(indices)
    # 	if i % 1 == 0:
    # 		print(f"national {i}/{length}")


    # length = len(json_dict["international"])
    # international_vectors, international = json_dict["international_vectors"], json_dict["international"]
    # for i in range(length):
    # 	indices, sentences = topk(international_vectors[i], international_vectors, international)
    # 	json_topk["international"].append(indices)
    # 	if i % 1 == 0:
    # 		print(f"international {i}/{length}")

    # output_file_name = "data/datastructure/topk.json"
    # with open(output_file_name, "w", encoding="utf-8") as f:
    # 	f.write(json.dumps(json_topk, indent=4, cls=MyEncoder))







    # json_dict["0"]["top_k_indices"], json_dict["0"]["top_k_sentences"] = topk(json_dict["0"]["vector"])

# for _ in json_dict:
# 	json_dict[_]["top_k_indices"], json_dict[_]["top_k_sentences"] = topk(
# 		json_dict["0"]["vector"]
# 	)








# file = "internationals.json"
# func(f"./data/json/{file}", f"./data/json/topk/{file}")
