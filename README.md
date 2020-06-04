# Info Covid19 La Plata
Se están acumulando la información que da la Municipalidad de La Plata en su instagram, en este repositorio.


## Ejecutar código automáticamente

- Obteniendo info de un excel que se va actualizando.
- Estamos ejecutando la notebook con papermill.
- Exportando a HTML con nbconvert.
- Se puede ver el html en [covid19_laplata/](https://jonathanloscalzo.github.io/covid19_laplata/)
```bash
python3 ./deploy.py
jupyter nbconvert ./notebooks/00-viz_casos-output.ipynb --to html --no-input --output ../index.html
rm ./notebooks/00-viz_casos-output.ipynb
```

## TODOs
- [ ] Automatizar el proceso bash para ejecutar con github actions o similar.

