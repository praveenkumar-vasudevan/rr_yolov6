from clearml import StorageManager
from clearml import Dataset
import tempfile
from pathlib import Path
import os
import zipfile
import uuid
import sys
import argparse

# args
#  input: cvat ids
#  options: resizing, augmenting, ...
#  output: s3_endpoint, bucket_name, blob_name

def get_args_parser(add_help=True):
    parser = argparse.ArgumentParser(description='CVAT To s3 bucket', add_help=add_help)
    parser.add_argument('--cvats', default=[], type=str, nargs='+', required=True, help='cvat ids')
    parser.add_argument('--img', default=640, type=int, help='image size (pixels)')
    parser.add_argument('--endpoint', default='', type=str, help='s3 endpoint')
    parser.add_argument('--bucket', default='', type=str, help='name of the bucket')
    parser.add_argument('--blob', default='', type=str, help='blob name')
    return parser

# flow
## parse args
## download to a temp folder from cvats
## resize the images and accordingly the image labels
## merge the cvats and labels
## archive the dataset
## save the archive to the s3 bucket

if __name__ == '__main__':
    args = get_args_parser().parse_args()

    # create a temp directory
    # extract the dataset
    tempdir = tempfile.gettempdir()
    tf = uuid.uuid4().hex
    p = Path(tempdir) / tf
    print(p)
    os.makedirs(str(p))

    # download the cvats to the temp directory

    #

    pass