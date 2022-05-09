const fs = require("fs");

let input_file_name = "data/datastructure/rounded.json"
let datas;

// try {
datas = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));
// } catch (err) {
// 	console.log(err);
// }


let output_file_name = "data/datastructure/round.json"

let output = JSON.stringify(datas);
fs.writeFileSync(output_file_name, output);