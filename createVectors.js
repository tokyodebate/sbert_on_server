const fs = require("fs");

require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');

const use = require('@tensorflow-models/universal-sentence-encoder');

input_file_name = "data/motions/data.json";

let datas;
try {
	datas = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));
} catch (err) {
	console.log(err);
}


let sentences;
let vectors = {}
vectors["national"] = []
vectors["international"] = []

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
				output_file_name = "data/vectors/data.json"

				let output = JSON.stringify(allVectors);
				fs.writeFileSync(output_file_name, output);

			});
		});
	});
});



