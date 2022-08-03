# SHARP paper's supplement


This is written with Sphinx. 
To view the generated docs: 
https://wenboown.github.io/SHARP-NLP-Letter-to-WP/

Install `pandoc`:
```shell
 brew install pandoc
```

Use `pandoc` to convert docx file to rst file:
```shell
pandoc input.docx -f docx -t rst -o output.rst
```

Then review the output format and make changes accordingly.

To update the content in Github page:
```bash
make github
```

To update the html files in build directory for local development preview:
```bash
make clean && make html
```

### Note for serving on github page:
Need to add `.nojekyll` file under `docs` for the css, etc. to load correctly.

Ref: 
https://www.sphinx-doc.org/en/master/usage/quickstart.html
