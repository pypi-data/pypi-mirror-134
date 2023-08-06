import os
import re

import boto3
from botocore.exceptions import ClientError

from metastore.utils import create_logger

logger = create_logger('objects')


def normalize(file_path):
    p = re.sub(r'/\./?', '/', file_path)
    p = re.sub(r'/+', '/', p)
    p = re.sub(r'^/+', '', p)

    return p


class Storage(object):

    def __init__(self):
        self.client = boto3.client('s3')
        # TODO hardcode it! It is PoC!!!
        self.bucket = 'infuseai.metastore'

    def exists(self, key):
        try:
            self.client.head_object(Bucket=self.bucket, Key=key)
            return True
        except ClientError as e:
            if 'Not Found' in str(e):
                return False
            raise e

    def download(self, src: str, dest: str):
        if src == ".":
            src = ""

        key = normalize(f'{src}')
        # single file download
        if self.exists(src):
            self._single_file_download(key, dest)
            return

        # download directory
        os.makedirs(dest, exist_ok=True)
        prefix_len = len(key)
        response = self.client.list_objects_v2(Bucket=self.bucket, Prefix=key)
        for c in response['Contents']:
            save_path = os.path.join(dest, c['Key'][prefix_len:])
            self._single_file_download(c['Key'], save_path)

    def _single_file_download(self, key: str, dest: str):
        if not os.path.exists(os.path.dirname(dest)):
            os.makedirs(os.path.dirname(dest), exist_ok=True)

        with open(dest, "wb") as fh:
            try:
                response = self.client.get_object(Bucket=self.bucket, Key=key)
                fh.write(response['Body'].read())
            except BaseException:
                raise

    def get_content(self, key: str):
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=key)
            return response['Body'].read().decode('utf-8')
        except BaseException:
            raise

    def upload_content(self, content: str, dest):
        self.client.put_object(Bucket=self.bucket, Key=normalize(dest), Body=content.encode('utf-8'))

    def upload(self, src: str, dest: str):
        has_trailing_slash = src.endswith('/')
        src = os.path.abspath(os.path.expandvars(os.path.expanduser(src)))

        # single file upload
        if os.path.isfile(src):
            self._single_file_upload(src, dest)
            return

        # upload directory
        if os.path.isdir(src):
            self._directory_files_upload(src, dest, has_trailing_slash)
            return

        raise ValueError(f'Cannot upload {src}: it is not a file or directory')

    def _directory_files_upload(self, src: str, dest: str, has_trailing_slash: bool):
        if dest == '.':
            dest = ''

        # without trailing slash -> add directory to the prefix
        base_prefix_path = None
        if has_trailing_slash:
            base_prefix_path = f'{dest}'
        else:
            base_prefix_path = f'{dest}/{os.path.basename(src)}'

        base_prefix_path = normalize(base_prefix_path)
        logger.info(f'set up directory upload base prefix to {base_prefix_path}')
        start_dir_len = None
        for root, dirs, files in os.walk(src):
            if start_dir_len is None:
                start_dir_len = len(root)

            for filename in files:
                key = normalize(f'{base_prefix_path}{root[start_dir_len:]}/{filename}')
                from_file = os.path.join(root, filename)
                logger.info(f'copy file: {os.path.join(root, filename)} => {key}')
                with open(from_file, "rb") as fh:
                    self.client.put_object(Bucket=self.bucket, Key=key, Body=fh)

    def _single_file_upload(self, src, dest):
        if dest == '.':
            dest = os.path.basename(src)
        key = f'{dest}'
        key = normalize(key)

        logger.info(f'single file upload to {key}')
        with open(src, "rb") as fh:
            self.client.put_object(Bucket=self.bucket, Key=key, Body=fh)
