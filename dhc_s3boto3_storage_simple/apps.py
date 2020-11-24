from django.apps import AppConfig

from health_check.plugins import plugin_dir


class HealthCheckConfig(AppConfig):
    name = 'dhc_s3boto3_storage_simple'

    def ready(self):
        from .backends import S3Boto3StorageSimpleHealthCheck
        plugin_dir.register(S3Boto3StorageSimpleHealthCheck)
