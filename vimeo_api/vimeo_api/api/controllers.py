from flask import Blueprint, request, make_response, abort, jsonify
from flask import current_app as app
from ..extensions import db
from ..tasks import delete_file
from .models import File
import mimetypes
import os


api = Blueprint('api', __name__, url_prefix='/vimeo/api/v1.0')


@api.route('/file', methods=['PUT'])
def upload_file():
    if not request.files:
        abort(400)

    password = request.form.get('password')

    try:
        file_key = list(request.files.keys())[0]
        new_file_obj = request.files[file_key]
    except IndexError:
        abort(400)

    filename = new_file_obj.filename
    new_file_record = File.add_file(filename, password)

    new_path = '%s/%s' % (app.config['UPLOAD_FOLDER'],
                          new_file_record.filehash)
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    new_file_obj.save(os.path.join(new_path, filename))

    response = {
        "status": "File Uploaded Successfully",
        "url": "%s%s/file/%s" % (request.url_root,
                                 api.url_prefix.lstrip('/'),
                                 new_file_record.filehash)
    }
    return jsonify(response), 201


@api.route('/file/<filehash>', methods=['GET'])
def download_file(filehash):
    file_obj = File.query.filter_by(filehash=filehash).first()
    password = request.args.get('password')

    if not file_obj:
        abort(404)

    elif file_obj.status == 'Gone':
        abort(410)

    elif file_obj.password and not password:
        abort(401)

    elif password and not file_obj.validate_password(password):
        abort(401)

    file_obj.status = 'Gone'
    db.session.commit()

    filename = file_obj.filename
    filehash = file_obj.filehash
    mimetype = mimetypes.guess_type(filename)[0]

    redirect_path = "/vimeo/api/v1.0/files/%s/%s" % (filehash, filename)

    response = make_response("")
    response.headers["X-Accel-Redirect"] = redirect_path
    response.headers["Content-Type"] = mimetype

    delete_file.apply_async(args=[filehash], countdown=30)

    return response
