#!/bin/zsh

# git clone git@github.com:tokyodebate/motions.git
# mkdir ./data/json && mkdir ./data/motions && mkdir ./data/rounds && mkdir ./data/tsv && mkdir ./data/vectors && mkdir ./data/roundedVectorsInJson

python3 ./motion2tsv.py
python3 ./tsv2json.py
python3 ./createRoundsFromTsv.py
python3 ./motions.py
node ./createVectors.js
python3 ./createRoundedVectors.py
node ./createRoundedVectorsInJson.js


# data/rounds/data.json を rounds.json
# data/roundedVectorsInJson/data.json を vectors.json 
# git@github.com:tokyodebate/utds_search_similar_motion.git
# の motions/utds_search_similar_motion/data/ にコピーする
# cp ../sbert_on_server/data/roundedVectorsInJson/data.json ./src/data/vectors.json
# cp ../sbert_on_server/data/rounds/data.json ./src/data/rounds.json