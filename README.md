# Mendeley LaTeX bibliography fixer

Developed on Python version 3.9.6

Install requirements with
```bash
pip install -r requirements.txt
```

Script `main.py` takes a single argument:
- the absolute path to the `.bib` file to be fixed

The script will save a fixed version of the specified file in the same directory,
with the suffix `_fixed` appended to the file name.

All words that ought to have their formatting kept should be listed line-by-line
in `dictionary.txt`.

The process of 'fixing' a file simply involves surrounding all occurrences in
paper titles of any word listed in `dictionary.txt` with curly brackets `{` `}`,
so that when loaded into LaTeX, the formatting of those words is left alone.

### Example

`bibliography.bib`:
```bibtex
@article{citation_key,
   abstract = {...abstract...},
   author = {author 1, author 2},
   month = {x},
   title = {Paper title with 3D acronyms appearing in a CT scanner ASAP},
   url = {http://ur.l},
   year = {xxxx},
}
```

When formatted in LaTeX, the title would likely be rendered as 'Paper title with
3d acronyms appearing in a ct scanner asap'.

With `dictionary.txt` containing the following lines:
```
3D
CT
ASAP
```

Running `python main.py /path/to/bibliography.bib` will produce the file
`/path/to/bibliography_fixed.bib`, containing:
```bibtex
@article{citation_key,
   abstract = {...abstract...},
   author = {author 1, author 2},
   month = {x},
   title = {Paper title with {3D} acronyms appearing in a {CT} scanner {ASAP}},
   url = {http://ur.l},
   year = {xxxx},
}
```
 Which LaTeX will render as 'Paper title with 3D acronyms appearing in a CT
 scanner ASAP'