
import json


def func(input_file_name, output_file_name):
    with open(input_file_name) as f:
        json_string = f.read()
        json_dict = json.loads(json_string)

    print(json_dict["0"])
    print(len(json_dict))
    print(json_dict["0"]["sentence"])
    print(json_dict["0"]["vector"])

    import numpy as np
    from numpy import dot
    from numpy.linalg import norm

    def topk(List1, K=10):
        results = []
        for _ in json_dict:
            List2 = json_dict[_]["vector"]
            result = dot(List1, List2) / (norm(List1) * norm(List2))
            results.append(result)
        K = 10
        # ソートはされていない上位k件のインデックス
        my_array = np.array(results)
        unsorted_max_indices = np.argpartition(-my_array, K)[:K]
        # 上位k件の値
        y = my_array[unsorted_max_indices]
        # 大きい順にソートし、インデックスを取得
        indices = np.argsort(-y)
        # 類似度上位k件のインデックス
        max_k_indices = unsorted_max_indices[indices]
        max_k_sentences = []
        for i in max_k_indices:
            max_k_sentences.append(json_dict[str(i)]["sentence"])
        return max_k_indices, max_k_sentences

    print(topk(json_dict["1"]["vector"]))

    # json_dict["0"]["top_k_indices"], json_dict["0"]["top_k_sentences"] = topk(json_dict["0"]["vector"])

    for _ in json_dict:
        json_dict[_]["top_k_indices"], json_dict[_]["top_k_sentences"] = topk(
            json_dict["0"]["vector"]
        )

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

    with open(output_file_name, "w", encoding="utf-8") as output_file_name:
        output_file_name.write(json.dumps(json_dict, indent=4, cls=MyEncoder))



func("./data/datastructure/datastructure.json", "./data/datastructure/topk/datastructure.json")

# file = "internationals.json"
# func(f"./data/json/{file}", f"./data/json/topk/{file}")
