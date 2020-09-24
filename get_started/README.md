[Src: from DVC Get Started](https://dvc.org/doc/start/data-pipelines)

Download the files using wget or curl, unzip 
```
curl -o code.zip https://s3-us-east-2.amazonaws.com/dvc-public/code/get-started/code.zip
mkdir get_started 
unzip code.zip -d get_started
```

This will generate a dvc.yaml file in the same dir that the command is run
```
cd get_started
dvc run -n prepare \
          -p prepare.seed,prepare.split \
          -d src/prepare.py -d ../data/data.xml \
          -o ./data/prepared \ 
          python src/prepare.py ../data/data.xml
```

Track changes with git 
```
git add dvc.lock dvc.yaml data/.gitignore
```

Push this to remote storage
``` 
dvc push 
```
