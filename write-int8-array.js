const fs = require("fs");

d = fs.readFileSync("/Users/koki/Desktop/utcode/tensorflowjs_project/sbert_generate_server/data/datastructure/int8")
const data = new Int8Array(d);
fs.writeFileSync("./data.bin", data);

const data2 = new Int8Array(fs.readFileSync("./data.bin"));
console.log(data2);