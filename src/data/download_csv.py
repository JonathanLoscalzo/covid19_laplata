import requests

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR_SLdkuSRDoWej3f80xvmU2KhbPXM2uJe2s0pvg7DisWCaX9nQORsWZ976fcYB2N3gQrMan_hnN7xE/pub?output=csv"
output = "data/raw/data.csv"

resp = requests.get(url)

with open(output, "w") as file:
    file.write(resp.text)