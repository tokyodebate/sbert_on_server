#!/bin/zsh

cd /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/motions
git pull
cd ..


python3 /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/main1_create_tsv.py
python3 /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/main11_create_datastructure_json.py
python3 /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/main11_create_datastructure_simple.py
python3 /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/main11_create_motions_json.py
node /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/main12_create_vectors.js
python3 /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/main13_matrix_topk.py

python3 /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/legacy_code.py

mv /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/data/datastructure/allVectors.json /Users/koki/Desktop/utcode/tensorflowjs_project/tensorflowjs_sp/src/data/
mv /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/data/datastructure/datastructure_simple.json /Users/koki/Desktop/utcode/tensorflowjs_project/tensorflowjs_sp/src/data/

mv /Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/data/datastructure/copy.json /Users/koki/Desktop/utcode/tensorflowjs_project/tensorflowjs_sp/src/data/
