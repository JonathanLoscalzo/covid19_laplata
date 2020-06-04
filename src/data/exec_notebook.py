import papermill as pm

def execute():
   pm.execute_notebook(
      './notebooks/00-viz_casos.ipynb',
      './notebooks/00-viz_casos-output.ipynb',
      parameters=dict(datafile='./data/raw/data.csv')
   )

if __name__ == "__main__":
   execute()