from flask import Blueprint, request, abort, Response
from .models import Host, ApiKey
from ..utils import chartbeat_request, convert_data
from ..extensions import db
import datetime
import json


api = Blueprint('api', __name__, url_prefix='/api/v1.0')


@api.route('/increasingconcurrents', methods=['GET'])
def get_increasing_concurrents():
    result = []
    api_key = request.args.get('apikey')
    host_name = request.args.get('host')

    if not api_key or not host_name:
        abort(401)

    res = chartbeat_request(api_key, host_name)
    if res.status_code != 200:
        # bad request
        abort(400)

    api_key_obj = ApiKey.query.filter_by(api_key=api_key).first()
    if not api_key_obj:
        api_key_obj = ApiKey(api_key=api_key)
        db.session.add(api_key_obj)
        db.session.commit()

    host_obj = Host.query.filter_by(host_name=host_name).first()
    if not host_obj:
        # make new host store in db and return nothing
        # create relationship for this api key and host
        host_obj = Host(host_name=host_name, top_pages=res.json())
        if host_obj not in api_key_obj.hosts:
            api_key_obj.add_host(host_obj)

        db.session.add(host_obj)
        db.session.commit()

        return Response(json.dumps(result),  mimetype='application/json')

    if host_obj:
        # if the request is cached, there is a responsed associated
        # to it in the postgres db
        if res.from_cache:
            return Response(
                json.dumps(host_obj.increasing_visitors),
                mimetype='application/json'
            )

        if host_obj not in api_key_obj.hosts:
            api_key_obj.add_host(host_obj)
        # need to compare against current chartbeat data
        # need to process the data to make it more usable and
        # get faster lookup time for visitor counts
        local_data = convert_data(host_obj.top_pages)
        current_data = convert_data(res.json())

        for page in current_data:
            # If a new page is encountered, ignore it since there is no
            # history for it locally yet
            try:
                change = current_data[page][0]-local_data[page][0]
            except KeyError:
                continue
            if change > 0:
                result.append(
                    {
                        'i': current_data[page][1],
                        'change': change
                    }
                )

        if result:
            # sort result by increasing visitors using the change value
            result = sorted(
                result,
                key=lambda result: result['change'],
                reverse=True
            )

        host_obj.increasing_visitors = result
        host_obj.top_pages = res.json()
        host_obj.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    return Response(json.dumps(result),  mimetype='application/json')
