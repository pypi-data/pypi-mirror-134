import os
from glob import glob
from google.cloud import storage


def download(bucket_name, blob_path, down_path, project=''):
    """
    Download file from google storage
    Args:
        bucket_name: name of bucket
        blob_path: path of blob
        down_path: local download path
        project: project name

    Returns:
    """
    storage_client = storage.Client(project=project)
    bucket = storage_client.get_bucket(bucket_name)
    blobs = [x for x in bucket.list_blobs(prefix=blob_path)]
    sep = '/' if down_path[-1] != '/' else ''
    if len(blobs) > 1:
        for blob in blobs:
            os.makedirs(down_path + sep + "/".join(blob.name.split('/')[:-1]), exist_ok=True)
            blob.download_to_filename(down_path + sep + blob.name)
    else:
        blob = bucket.blob(blob_path)
        blob.download_to_filename(down_path + sep + blob.name.split('/')[-1])


def upload(bucket_name, blob_path, local_path, project=''):
    """
    Upload file to google storage
    Args:
        bucket_name: name of bucket
        blob_path: path of blob
        local_path: local file path
        project: project name

    Returns:
    """
    isdir = os.path.isdir(local_path)
    storage_client = storage.Client(project=project)
    bucket = storage_client.get_bucket(bucket_name)
    if isdir:
        for file in sorted(glob(local_path + '/**')):
            upload(bucket_name, blob_path + "/" + os.path.basename(local_path), file, project=project)
    else:
        sep = '/' if blob_path[-1] != '/' else ''
        remote_path = blob_path + sep + local_path.split('/')[-1]
        blob = bucket.blob(remote_path)
        blob.upload_from_filename(local_path)


def list_blobs(bucket_name, blob_path, project=''):
    """
    List blobs of google storage bucket
    Args:
        bucket_name: name of bucket
        blob_path: path of blob
        project: project nome

    Returns:
    """
    storage_client = storage.Client(project=project)
    for blob in storage_client.list_blobs(bucket_name, prefix=blob_path):
        print(blob.name)
