from flask import Blueprint, request, make_response
import mimetypes


api = Blueprint('api', __name__, url_prefix='vimeo/api/v1.0')


@api.route('/upload', methods=['PUT'])
def upload_file():
    # if setting a password, need to store this in database
    # also need downloaded key
    # will have hash like this:
    # {filename: {password: ..., downloaded: false}}

# request_data = g.request_data
# auth_user = g.auth_user
# errors = []
# file_dict = request_data

# try:
#     file_key = list(file_dict.keys())[0]
# except IndexError as e:
#     errors.append(repr(e))
#     response = {"payload": {}, "errors": errors}
#     return jsonify(response), 400

# file = file_dict[file_key]
# if file and allowed_file(file.filename):
#     file.filename = "%s.%s" % (
#         str(auth_user.id), file.filename.rsplit(".", 1)[1])
#     file_name = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
# else:
#     abort(400)

# url = request.base_url.rsplit(request.url_root)[1]
# photo_url = "%s/%s" % (url, file_name)
# auth_user.photo_url = photo_url
# db.session.commit()

# response = {
#     "payload": {
#         "user_id": auth_user.id,
#         "url": "/user/details/%d" % auth_user.id,
#         "photo_url": auth_user.photo_url,
#         "name": auth_user.name,
#         "email": auth_user.email,
#         "phone": auth_user.phone,
#         "contacts": auth_user.get_contacts(),
#         "blocked_contacts": auth_user.get_blocked_contacts(),
#         "skills": auth_user.get_skills(),
#         "phone_status": auth_user.phone_status,
#         "type": auth_user.type
#     },
#     "errors": errors
# }
# return jsonify(response), 200


@api.route('/file/<filename>', methods=['GET'])
def download_file(filename):

    mimetype = mimetypes.guess_type(filename)[0]

    redirect_path = "/vimeo/api/v1.0/files/"+filename

    response = make_response("")
    response.headers["X-Accel-Redirect"] = redirect_path
    response.headers["Content-Type"] = mimetype
    return response
