Create python environment called projectenv

python -m venv name

activate ---

name\Scripts\activate

Created requirements.txt file and install libraries
pip install -r requirements.txt

Created README.md file for recording the projects steps
```bash
ni readme.md
```

Create template file to define structue of project such as folders and files required
```bash
ni template.py
```

```bash
download data from below link
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5
```

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given\winequality.csv
```

```bash
git add .
```

```bash
git commit -m "First Commit"
```

```bash 
oneliner command
git add . ; git commit -m "Updated Readme"
```

```bash
tox command -
tox
```

for rebuilding -
```bash
tox -r 
```

pytest command
```bash
pytest -v
```

setup commands -
```bash
pip install -e . 
```


build your own package commands-
```bash
python setup.py sdist bdist_wheel
```