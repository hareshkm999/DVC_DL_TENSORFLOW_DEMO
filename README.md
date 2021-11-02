# DVC DL DEMO

download data --> [source](https://drive.google.com/drive/u/0/folders/1tz4IOoJKdi999IRdqJY04VOifyllRzj1)

## commands

### create new env
```bash
conda create --prefix python=3.7 -y

```

### activate new env
```bash
source activate ./env
```

### init DVC git
```bash
git init
dvc init
```
### create empty files and direcories
```bash
touch dvc.yaml setup.py params.yaml setup.py README.md .gitignore

mkdir -p config src/utils
touch config/config.yaml config/secrets.yaml src/__init__.py src/utils/__init__.py src/stage_01_load_save.py

```
### freezing requirements
```bash

pip freeze > requirements.txt

```


