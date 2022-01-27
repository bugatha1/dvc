create env

```bash
conda create -n wineq python=3.8 -y

source activate base
```

activate env

```bash
conda activate wineq
```

create a requirements file

```bash
touch requirements.txt
```

install the req file

```bash
pip install -r requirements.txt
```

download data from kaggle

git init

dvc init

dvc add data_given/winequality.csv

git add . && git commit -m "first commit"

```bash
git remote add origin https://github.com/c17hawke/simple-dvc-demo.git
git branch -M main
git push origin main
```

tox command - 
```bash
tox
```

for rebuilding -
```bash
tox -r
```

pytest command -
```bash
pytest -v
```

setup command - 
```bash
pip install -e .
```

build your own package commands - 
```bash
python setup.py sdist bdist wheel
```







