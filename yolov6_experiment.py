from clearml import Dataset, Task, Logger
import tempfile
from pathlib import Path
import os
import zipfile
import uuid
import sys

sys.path.insert(0, './tools')

from train import main, get_args_parser

if __name__ == '__main__':
    task = Task.init(project_name='Evaluation', task_name='Yolov6 Training',  output_uri="http://172.29.138.42:8081")

    
    args = get_args_parser().parse_args()
    # download dataset
    dataset_name="yolov6_dataset"
    dataset_project="Flappter Dataset"

    dataset_path = Dataset.get(
        dataset_name=dataset_name, 
        dataset_project=dataset_project
    ).get_local_copy()

    print (dataset_path)
    Logger.current_logger().report_text(dataset_path)
    
    # extract the dataset
    tempdir = tempfile.gettempdir()
    tf = uuid.uuid4().hex

    p = Path(tempdir) / tf

    print(p)

    os.makedirs(str(p))

    src_path = Path(dataset_path) / os.listdir(dataset_path)[0]

    print(src_path)

    with zipfile.ZipFile(src_path,"r") as zip_ref:
        zip_ref.extractall(str(p))

    # validate the files exist
    yaml = Path(p) / 'dataset.yaml'

    print (f'yaml file exists: {yaml.exists()}')
    Logger.current_logger().report_text(f'yaml file exists: {yaml.exists()}')

    if (yaml.exists()):
        # creating a variable and storing the text
        # that we want to search
        search_text = "$DATA_ROOT"

        # creating a variable and storing the text
        # that we want to add
        replace_text = str(p)

        # Opening our text file in read only
        # mode using the open() function
        with open(str(yaml), 'r') as file:
            data = file.read()
            print (data)
            data = data.replace(search_text, replace_text)
            print(data)

        # Opening our text file in write only
        # mode to write the replaced content
        with open(str(yaml), 'w') as file:

            # Writing the replaced data in our
            # text file
            file.write(data)
    
    args.data_path = str(yaml)

    main(args=args)


# clearml-task --project Evaluation --name "Yolov6 training" --repo "git@github.com:praveenkumar-vasudevan/rr_yolov6.git" --branch "main" --script "yolov6_experiment.py" --requirement "requirements.txt" --queue default --output-uri "http://172.29.138.42:8081" --args batch=32 conf=configs/yolov6n.py data=data/coco.yaml device=0 img_size=416 check_images=1 check_labels=1 write_trainbatch_tb=1