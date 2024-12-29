import os
import glob
import re
#pathNamespaces
final_list = []
for name in glob.glob("./**/*.md", recursive=True):
    if "README" in name:
        fix_name = name.replace("\\","/")[1:-10]
        if fix_name:
            final_list.append(fix_name)

with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

with open('index.html','w',encoding='utf-8') as f:
    str_2add = "pathNamespaces: "+str(final_list)+","
    new_content = re.sub("pathNamespaces: \[.*\],", str_2add, content, count=1)
    f.write(new_content)

print(str_2add)
os.system('pause')