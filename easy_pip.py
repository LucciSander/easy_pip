import os


def pip_export():
	name = input("filename: ")
	if not ".txt" in name:
		name += ".txt"
	os.system("py -m pip list > {}".format(name))

def pip_import():
	file_path = input("path to import-file: ")
	if "\"" in file_path:
		file_path = file_path.replace("\"", "")

	elif  "\'" in file_path:
		file_path = file_path.replace("\'", "")

	if "\\" in file_path:
		file_path = file_path.replace("\\", "/")

	with open(file_path, "r") as f:
		libs = f.readlines()[2::]

	for lib in libs:
		lib_name = ""
		for char in lib:
			if char == " ":
				break
			lib_name += char
		os.system("pip install {}".format(lib_name))




action = input("[1] to export pip-list\n[2] to import pip-list\n")


if action == "1":
	pip_export()
elif action == "2":
	pip_import()

