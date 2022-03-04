## Assignment - MLflow
### Docker Docs - Orientation and setup:
https://docs.docker.com/get-started/

### Steps


#### 1
Install Jupiter Notebook
https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/install.html
or
https://jupyter.readthedocs.io/en/latest/install.html

#### 2
Install mlflow
```
pip3 install mlflow
```
or
```
python3 -m pip install mlflow
```
or
```
python3 -m pip install mlflow[extras]
```
or
```
conda install -c conda-forge mlflow
```

#### 3
Run tutorial
https://www.mlflow.org/docs/latest/tutorials-and-examples/tutorial.html


#### 4
Create report with Assignment description into docx and send by e-mail for checking.


### Links
MLflow Documentation | https://www.mlflow.org/docs/latest/index.html

MLflow tutorial | https://www.mlflow.org/docs/latest/tutorials-and-examples/tutorial.html

Coursera Machine Learning Design (Week 3) | https://www.coursera.org/learn/machine-learning-design/home/week/3


* Use "--no-conda" if you have problems with conda installation
```
mlflow run --no-conda sklearn_elasticnet_wine -P alpha=0.42
```