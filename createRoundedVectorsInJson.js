const fs = require("fs");

let input_file_name = "data/roundedVectors/data.json"
let datas;

datas = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));


let output_file_name = "data/roundedVectorsInJson/data.json"

let output = JSON.stringify(datas);
fs.writeFileSync(output_file_name, output);