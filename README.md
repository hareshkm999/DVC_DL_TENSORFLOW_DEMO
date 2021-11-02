# DVC DL DEMO

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
touch config/config.yaml config/secrets.yaml
```


