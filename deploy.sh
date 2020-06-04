python src/data/download_csv.py
python src/data/exec_notebook.py
jupyter nbconvert notebooks/00-viz_casos-output.ipynb --to html --no-input --output ../index.html
rm notebooks/00-viz_casos-output.ipynb