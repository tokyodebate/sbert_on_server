const fs = require("fs");

require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node')
const use = require('@tensorflow-models/universal-sentence-encoder');

function f(output_file_name, sentences, length, with_slide_sentences) {
	let buffer = {}
	use.load().then(model => {
		model.embed(sentences).then(async embeddings => {
			// embeddings.print(true);
			const vec = await embeddings.array();
			return vec
			// const length = Object.keys(data).length
			// for (let i=0; i<length; i++) {buffer[String(i)] = {"vector": vec[i], "sentence": with_slide_sentences[i]}}
			// // console.log(buffer);
			// console.log(buffer["0"]);
			// let output = JSON.stringify(buffer);
			// fs.writeFileSync(output_file_name, output);
		});
	});
}

function read(input_file_name, output_file_name) {
	let data;
	try {
		data = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));
	} catch (err) {
		console.log(err);
	}

	// let length = Object.keys(data["national"]).length;
	const sentences = [];
	for (let i=0; i<Object.keys(data["national"]).length; i++) {
		for (let j=0; j<Object.keys(data["national"][String(i)]["motions"]).length; j++){
			sentences.push(data["national"][String(i)]["motions"][String(j)]["info"]["motion"]);
		}
	}
	// console.log(sentences);
	let vec = f(sentences);
	console.log(vec);
}

// input_file_name = "./data/datastructure/datastructure.json"
read("./data/datastructure/datastructure.json", "./data/datastructure/vectors/datastructure.json");


