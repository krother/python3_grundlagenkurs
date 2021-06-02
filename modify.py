import os
import regex

file_paths = []
regex_str = r'    :::(\w+\n)(    (.*\n+))+'

for root, dirs, files in os.walk(os.path.dirname(__file__)):
	for file in files:
		if(file.endswith(".md")):
			file_paths.append(os.path.join(root,file))

for file_path in file_paths:
	print(file_path)
	with open(file_path, mode="r", encoding="utf8") as md_file:
		text = md_file.read()

	match = regex.search(regex_str, text)
	while match is not None:
		old_str = match[0]
		lang = match[1].replace("python3", "python")
		code = "".join(match.captures(3))
		if code[-2:] == "\n\n":
			code = code[:-1]
		new_str = "```" + lang + code + "```\n\n"
		text = text.replace(old_str, new_str)
		match = regex.search(regex_str, text)


	with open(file_path, mode="w", encoding="utf8") as md_file:
		md_file.write(text)