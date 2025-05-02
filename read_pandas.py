from pathlib import Path
import pandas as pd


def load_parque():
    p = Path("./data/")
    files = list(f for f in p.iterdir() if f.name.endswith('.parquet')) 
    return (pd.read_parquet(f) for f in files)


def write_img(series: pd.Series):
    path = Path('assets/images/')
    path.mkdir(parents=True, exist_ok=True)

    for _nr , row in series.iterrows():
        img_dict, classes = row

        img_name = img_dict['path']
        img_bytes =img_dict['bytes']


        with open(path / img_name, 'wb') as img_file:
            img_file.write(img_bytes)
        
        print(_nr, path / img_name, classes)

