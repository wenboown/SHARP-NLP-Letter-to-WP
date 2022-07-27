# SHARP paper's supplement


This is written with Sphinx. 
To view the generated docs: 
https://wenboown.github.io/SHARP-NLP-Letter-to-WP/

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
