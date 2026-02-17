files = [
    "report.pdf",
    "data.csv",
    "image.png",
    "notes.txt",
    "summary.pdf",
    "photo.png",
    "README"
]
grouped_files = {}
for file in files:
    if "." in file:
        name, ext = file.rsplit(".", 1)
        ext = ext.lower()
    else:
        ext = "no_extension"
    grouped_files.setdefault(ext, []).append(file)
print(grouped_files)