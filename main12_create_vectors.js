const fs = require("fs");

require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');

const use = require('@tensorflow-models/universal-sentence-encoder');
// const { model } = require("@tensorflow/tfjs");

input_file_name = "data/datastructure/motions.json";

let datas;
try {
	datas = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));
} catch (err) {
	console.log(err);
}

// Hi there 👋. Looks like you are running TensorFlow.js in Node.js. To speed things up dramatically, install our node backend, which binds to TensorFlow C++, by running npm i @tensorflow/tfjs-node, or npm i @tensorflow/tfjs-node-gpu if you have CUDA. Then call require('@tensorflow/tfjs-node'); (-gpu suffix for CUDA) at the start of your program. Visit https://github.com/tensorflow/tfjs-node for more details.

// function read(input_file_name, output_file_name) {
// 	let datas;
// 	try {
// 		datas = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));
// 	} catch (err) {
// 		console.log(err);
// 	}

// 	let vec;
// 	let sentences = datas["national"][0]
// 	use.load().then(model => {
// 		model.embed(sentences).then(async embeddings => {
// 			vec = await embeddings.array();
// 			datas
// 		});
// 	});


let sentences;
let vectors = {}
vectors["national"] = []
vectors["international"] = []
// use.load()
// .then(model => {
// 	model.embed(sentences)
// 	.then(async embeddings => {
// 		let vec = await embeddings.array();
// 		console.log(vec)
// 		datas["national_vectors"] = []
// 		for (let i=0; i<Object.keys(sentences).length; i++){
// 			datas["national_vectors"].append(vec[i])
// 		}
// 		console.log(datas);
// 	});
// });
let allVectors = []
use.load()
.then(model => {
	sentences = datas["national"]
	console.log(sentences);
	model.embed(sentences)
	.then(async embeddings => {
		let vec = await embeddings.array();
		console.log(vec);
		datas["national_vectors"] = [];
		for (let i=0; i<Object.keys(sentences).length; i++){
			datas["national_vectors"].push(vec[i]);
			vectors["national"].push(vec[i]);
			allVectors.push(vec[i]);
		}
		console.log(datas[["national_vectors"]]);
		use.load()
		.then(model => {
			sentences = datas["international"]
			console.log(sentences);
			model.embed(sentences)
			.then(async embeddings => {
				let vec = await embeddings.array();
				console.log(vec);
				datas["international_vectors"] = [];
				for (let i=0; i<Object.keys(sentences).length; i++){
					datas["international_vectors"].push(vec[i]);
					vectors["international"].push(vec[i]);
					allVectors.push(vec[i]);
				}
				// console.log(datas["international_vectors"]);
				// output_file_name = "data/datastructure/motions_vectors.json"
				// let output = JSON.stringify(datas);
				// fs.writeFileSync(output_file_name, output);
				output_file_name = "data/datastructure/allVectors.json"

				let output = JSON.stringify(allVectors);
				fs.writeFileSync(output_file_name, output);

			});
		});
	});
});



