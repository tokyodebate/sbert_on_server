//expressモジュールの読み込み
const express = require('express')
//expressのインスタンス化
const app = express()
const fs = require("fs");


input_file_name = "data/vectors/nationals.json";

try {
    data = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));
    console.log(Object.keys(data).length);
} catch (err) {
    console.log(err);
}

const length = Object.keys(data).length;
const len = 100;

console.log(data["0"]["sentence"]);

// console.log(data["0"])


//8080番ポートでサーバーを待ちの状態にする。
//またサーバーが起動したことがわかるようにログを出力する


// //GETリクエストの設定
// //'/get'でアクセスされた時に、JSONとログを出力するようにする
// app.get('/', (req, res)=> {
//     res.json({ "pet": "dog"});
//     console.log('GETリクエストを受け取りました')
//     res.end();
// })

// app.listen(8080, () => {
//   console.log("サーバー起動中");
// });

