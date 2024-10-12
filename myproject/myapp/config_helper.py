# this is needed so I can avoid duplicating this code in forms.yp and views.py
import yaml

def load_config():
    with open('myapp/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config