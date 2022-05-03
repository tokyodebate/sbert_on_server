
import json
import re

def tsv2json(input_file,output_file):
	file = open(input_file, 'r')
	a = file.readlines()
	d = {}
	key = -1
	value = ""
	for x in a:
		# print(x)
		t_count = x.count("\t")
		if t_count == 0:
			pass
		elif t_count == 1:
			# print("t_count==1")
			if value:
				d[key] = value
			key += 1
			value = x[1:]
		else:
			value += x[1:]
	print(key)
	
	with open(output_file, 'w', encoding='utf-8') as output_file:
		output_file.write(json.dumps(d, indent=4))

# Driver Code
input_filename = 'nationalText.txt'
output_filename = 'nationalText.json'
tsv2json(input_filename, output_filename)

input_filename = 'internationalText.txt'
output_filename = 'internationalText.json'
tsv2json(input_filename, output_filename)

# print("\tAsian Debate Institute Summer 2017\n\t\tR1A\n\t\t\tTHW cut funding to secondary school for low graduate rates\n\t\tR1B\n\t\t\tTHBT school systems should build curricula in a way that emphasis national pride.\n\t\tR2A\n\t\t\tTH regrets the rise of the political discussion in social media. (facebook, twitter)\n\t\tR2B\n\t\t\tTHBT movement should prioritize using social media over socializing physical movement\n\t\tR3A\n\t\t\tTH, as a minority group, supports widespread positive but inaccurate depiction of culture in a mainstream media.\n\t\t\t\tMinority groups are often known for a certain positive but exaggerated stereotypes\n\t\t\t\t- e.g. Chinese people have a culture of studying really hard and are good at math\n\t\t\t\t- e.g. African-American are better at sport because black kids\n\t\t\t\thave a culture of playing a lot of basketball.\n\t\tR3B\n\t\t\tTHB in the censorship of art.\n\t\tR4A\n\t\t\tTHW torture terrorist for information.\n\t\tR4B\n\t\t\tTH supports political movements using violent action when peaceful protest has failed.\n\t\tOF\n\t\t\tTHW allow children to sue parents for past negligence in raising the children.\n\t\tQF\n\t\t\tTHBT national war memorials should commemorate on the casualties of all side of the conflict\n\t\tSF\n\t\t\tTHW create public housing for poor people in wealthy neighborhood.\n\t\tGF\n\t\t\tTHW plug into the pleasure machine\n\t\t\t\tIn a context of this motion, a pleasure machine is a perfect simulation of real life where you can decide everything about your life (i.e. income intelligence appearance etc). Entering this machine is permanent. You will retain memories of your previous life. You can extend your natural life span.\n")