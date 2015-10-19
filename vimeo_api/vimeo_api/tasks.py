from .extensions import celery
from .config import DefaultConfig
import shutil


@celery.task
def delete_file(filehash):
    delete_path = '%s/%s' % (DefaultConfig.UPLOAD_FOLDER,
                             filehash)
    shutil.rmtree(delete_path)
