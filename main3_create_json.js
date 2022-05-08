const fs = require("fs");

require('@tensorflow/tfjs');
// require('@tensorflow/tfjs-node')
const use = require('@tensorflow-models/universal-sentence-encoder');

function f(output_file_name, sentences, length, with_slide_sentences) {
	let buffer = {}
	use.load().then(model => {
		model.embed(sentences).then(async embeddings => {
			// embeddings.print(true);
			const vec = await embeddings.array();
			// const length = Object.keys(data).length
			for (let i=0; i<length; i++) {buffer[String(i)] = {"vector": vec[i], "sentence": with_slide_sentences[i]}}
			// console.log(buffer);
			console.log(buffer["0"]);
			let output = JSON.stringify(buffer);
			fs.writeFileSync(output_file_name, output);
		});
	});
}

function read(input_file_name, output_file_name, with_slide_file_name) {
	let data;
	try {
		data = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));
	} catch (err) {
		console.log(err);
	}

	let with_slide_data;
	try {
		with_slide_data = JSON.parse(fs.readFileSync(with_slide_file_name, 'utf-8'));
	} catch (err) {
		console.log(err);
	}


	let length = Object.keys(data).length;
	// console.log(length)
	const sentences = [];
	for (let i=0; i<length; i++) {
		sentences.push(data[String(i)]);
	}
	console.log(sentences)
	const with_slide_sentences = [];
		for (let i=0; i<length; i++) {
		with_slide_sentences.push(with_slide_data[String(i)]);
	}
	// console.log(sentences);
	f(output_file_name, sentences, length, with_slide_sentences);
}

read('./data/tab3/nationals.json', './data/json/nationals.json', './data/tab3/with_slide/nationals.json');

read('./data/tab3/internationals.json', './data/json/internationals.json', 'data/tab3/with_slide/internationals.json');

