from os import listdir
import os
import time
from git.repo import Repo

html_file_path = 'index.html'


musics = listdir("music")
full_musics = []
for name in musics:
	full_musics.append("music/" + name)

print(full_musics)
full_musics.sort(key=os.path.getmtime)


musics = []
for song in full_musics:
	musics.insert(0,song[6:])


print(f'this is all the sorted music:')

for song in musics:
	print(song)

print("\n\n")

new_line_content = f"    const dasuifhlsiuefhasuilefyasefhaseufashe = {musics};"

print(f'generated new line content:\n\n{new_line_content}\n')

print(f'locating line in {html_file_path}\n')

with open(html_file_path, 'r') as file:
	lines = file.readlines()
	y = 0
	for x in lines:
		y+=1
		if "dasuifhlsiuefhasuilefyasefhaseufashe" in x:
			break
	print(f"found at line {y}\n")

line_number_to_change = y-1

print(f"modifying line\n")

if 0 <= line_number_to_change < len(lines):
	lines[line_number_to_change] = new_line_content + '\n'
	with open(html_file_path, 'w') as file:
		file.writelines(lines)
	print(f"Line {line_number_to_change + 1} has been successfully changed.")
else:
	print(f"Line number {line_number_to_change + 1} is out of range.")

print("adding, commiting and pushing to github")

repo = Repo('D:/Projects/fire website/sohan-n.github.io')

repo.index.add('*')
repo.index.commit('commit from updater')

origin = repo.remotes[0]
origin.push()

print('all done')