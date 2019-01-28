import os

out = ""

html_files = [
"html/header.html",
"html/projects/svd/svd.html",
"html/projects/gtcadis/gtcadis.html",
"html/projects/turbine/turbine.html",
"html/projects/cuda/cuda.html",
"html/projects/family_tree/family_tree.html",
"html/publications.html",
"html/footer.html"
]

for html_file in html_files:
    with open(html_file, 'r') as f:
        for line in f.readlines():
            out += line

with open("index.html", 'w') as f:
    f.write(out)


