from flask import Blueprint, request, make_response, abort, jsonify
from flask import current_app as app
from ..extensions import db
from .models import File
import mimetypes
import os


api = Blueprint('api', __name__, url_prefix='vimeo/api/v1.0')


@api.route('/upload', methods=['PUT'])
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
    File.add_file(filename, password)

    new_file_obj.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    response = {"status": "File Uploaded Successfully"}

    return jsonify(response), 201


@api.route('/file/<filehash>', methods=['GET'])
def download_file(filehash):
    file_obj = File.query.filter_by(filehash=filehash).first()
    password = request.args.get('password')

    if not file_obj:
        abort(404)

    if file_obj.gone:
        abort(410)

    if file_obj.password and not password:
        abort(401)

    if password and not File.validate_password(password):
        abort(401)

    file_obj.gone = True
    db.session.commit()

    filename = file_obj.filename
    mimetype = mimetypes.guess_type(filename)[0]

    redirect_path = "/vimeo/api/v1.0/files/"+filename

    response = make_response("")
    response.headers["X-Accel-Redirect"] = redirect_path
    response.headers["Content-Type"] = mimetype
    return response
