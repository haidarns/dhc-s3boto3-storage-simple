import logging

from django.conf import settings
from django.core.files.base import ContentFile

from health_check.storage.backends import StorageHealthCheck
from health_check.exceptions import ServiceUnavailable


class S3Boto3StorageSimpleHealthCheck(StorageHealthCheck):
    """
    Tests the status of a `S3BotoStorage` file storage backend.

    S3BotoStorage is included in the `django-storages` package
    and recommended by for example Amazon and Heroku for Django
    static and media file storage on cloud platforms.

    ``django-storages`` can be found at https://git.io/v1lGx
    ``S3Boto3Storage`` can be found at
        https://github.com/jschneier/django-storages/blob/master/storages/backends/s3boto3.py
    """

    logger = logging.getLogger(__name__)
    storage = 'storages.backends.s3boto3.S3Boto3Storage'

    def get_file_name(self):
        return 'health_check_storage_test/test.txt'

    def check_status(self):
        try:
            # import boto3
            # s3 = boto3.client('s3')
            # s3.head_bucket(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
            # print('testing')

            storage = self.get_storage()
            filename = self.get_file_name()

            if not storage.exists(filename):
                print('File not exist, upload check file')
                storage.save(
                    filename, ContentFile(content=self.get_file_content())
                )
            return True
        except Exception as e:
            print(e)
            raise ServiceUnavailable('Unable access bucket') from e
