from clearml import StorageManager
from clearml import Dataset

manager = StorageManager()

url = 'https://cvat-minio-kqdbp.ep-r.io/yolov6/yolov6_dataset.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=rapyuta%2F20221021%2F%2Fs3%2Faws4_request&X-Amz-Date=20221021T095351Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=9018d388cfe074e0c9a35c94020e0f51119eaed5b869f3a82af4e229f76db387'

# download dataset
dataset_path = manager.get_local_copy(
    remote_url=url
)

dataset_name="yolov6_dataset"
dataset_project="Flappter Dataset"

dataset = Dataset.create(
    dataset_name=dataset_name, 
    dataset_project=dataset_project
)

# 
dataset.add_files(path=dataset_path)

dataset.upload()

dataset.finalize()


dataset_path = Dataset.get(
    dataset_name=dataset_name, 
    dataset_project=dataset_project
).get_local_copy()

print (dataset_path)