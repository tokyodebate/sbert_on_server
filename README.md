search-similar-motion.onrender.com/ のサイトで使用する文ベクトルと文を生成するためのリポジトリです

git clone https://github.com/tokyodebate/motions

./script.sh を実行して文ベクトルと文を生成する

生成したファイルを
https://github.com/tokyodebate/utds_search_similar_motion.git
に移動する

data/rounds/data.jsonとdata/roundedVectorsInJson/data.jsonを
git@github.com:tokyodebate/utds_search_similar_motion.git
の motions/utds_search_similar_motion/data/ にコピーする

cp ../sbert_on_server/data/roundedVectorsInJson/data.json ./src/data/vectors.json
cp ../sbert_on_server/data/rounds/data.json ./src/data/rounds.json
