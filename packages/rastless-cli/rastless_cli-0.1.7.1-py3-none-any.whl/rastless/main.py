from rastless.aws.db import Database
from rastless.aws.s3 import S3Bucket
from rastless import settings


class RastlessCfg:
    def __init__(self, debug=False):
        self.db_table_name = settings.RASTLESS_TABLE_NAME
        self.db = Database(self.db_table_name)
        self.s3_bucket_name = settings.RASTLESS_BUCKET_NAME
        self.s3_bucket = S3Bucket(self.s3_bucket_name)
        self.debug = debug
