// import React, { useState } from 'react';
// import './App.css';
const fs = require("fs");
const cosSimilarity = require("cos-similarity")
// import cosSimilarity from "cos-similarity";
// import cosSimilarity from "cos-similarity";
// import datastructure from "./data/datastructure.json"
// import motions from "./data/motions.json"
// import top20 from "./data/top20.json"
// import allVectors from "./data/allVectors.json"

let input_file_name = "data/datastructure/allVectors.json";

let allVectors;
try {
	allVectors = JSON.parse(fs.readFileSync(input_file_name, 'utf-8'));
} catch (err) {
	console.log(err);
}

require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');

const use = require('@tensorflow-models/universal-sentence-encoder');

// interface AppProps {}
// function App({}: AppProps) {

	// const [text, setText] = useState("hello world");
	// const [ranks, setRanks] = useState("ranks come here");
	// const [topk, setTopk] = useState("topk comes here");
	let text = "regulation for abortion"

	function text2embed() {
		use.load().then(model => {
		// Embed an array of sentences.
			const sentences = [
				text
			];
			// console.log(text);
			model.embed(sentences).then(async embeddings => {
			embeddings.print(true /* verbose */);
			let vec = await embeddings.array();
			// vec, allVectors　との間でranking
			let similarities = {}
			let similarity = -1;
			// console.log(allVectors[0]);
			// console.log(allVectors.length);
			let length = allVectors.length;

			for (let i = 0; i<length; i++){
				// console.log(vec)
				// console.log(allVectors[i]);
				let vecs = allVectors[i];
				similarity = cosSimilarity(vec[0], vecs);
				// similarity = cosSimilarity([1, 2, 3], [2, 3, 4]);
///////////////////////
				console.log(similarity);
				similarities[i] = similarity;
			}

			let arr = similarities;
			var keys=[];
			for(let key in arr) keys.push(key);
			function compare(a,b){
				return arr[b]-arr[a];
			}
			let result = [];
			keys.sort(compare);
			for(let i=0; i<10; i++){
				result.push(keys[i]);
			}
			console.log(result);
			});
		});
	}

	function get_topk() {

	}

	function handleClick() {
		text2embed();
	}

	handleClick();