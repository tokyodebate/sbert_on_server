import json

with open("./tournamentNames.json") as file:
	tournaments = json.loads(file.read())
	nationals = tournaments["nationals"]
	internationals = tournaments["internationals"]

buffer = ""
for i, file in enumerate(nationals):
	with open(f"./motions/{file}.txt") as f:
		if i > 0:
			buffer += "\n"
		buffer += f.read()
		
with open("./data/tsv/nationals.tsv", "w") as f:
	f.write(buffer)

buffer = ""
for i, file in enumerate(internationals):
	with open(f"./motions/International/{file}.txt") as f:
		if i > 0:
			buffer += "\n"
		buffer += f.read()
with open("./data/tsv/internationals.tsv", "w") as f:
	f.write(buffer)
