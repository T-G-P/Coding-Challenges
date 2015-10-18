from flask import current_app as app
from vimeo_api.app import create_celery
import shutil

celery = create_celery(app)


@celery.task
def delete_file(filehash):
    delete_path = '%s/%s' % (app.config['UPLOAD_FOLDER'],
                             filehash)
    shutil.rmtree(delete_path)
