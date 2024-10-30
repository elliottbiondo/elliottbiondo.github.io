# script for concatenating HTML files


def all_lines(html_file):

    with open(html_file, 'r') as f:
        return f.readlines()

out = all_lines("html/header.html")

## Projects section {
##projects = ["fges", "svd", "gtcadis", "turbine", "cuda", "family_tree"]
#projects = ["layered", "fges", "svd", "gtcadis"]
#out += all_lines("html/projects_header.html")
#for proj in projects:
#    out += all_lines("html/projects/{0}/cover.html".format(proj))
#for proj in projects:
#    out += all_lines("html/projects/{0}/{0}.html".format(proj))
#out += all_lines("html/projects_footer.html")
## } Projects section

out += all_lines("html/publications.html")
out += all_lines("html/footer.html")


with open("index.html", 'w') as f:
    f.write("".join(out))


