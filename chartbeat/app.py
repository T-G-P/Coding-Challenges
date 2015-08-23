from flask import Flask, request, abort, Response
from models import Host, ApiKey, db
#from extensions import db
from utils import chartbeat_request, process_data
import datetime
import os
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(app)

@app.route('/api/v1.0/increasingconcurrents', methods=['GET'])
def get_increasing_concurrents():
    result = []
    api_key = request.args.get('apikey')
    host_name = request.args.get('host')

    if not api_key or not host_name:
        abort(401)

    res = chartbeat_request(api_key, host_name)
    if res.status_code != 200:
        #bad request
        abort(400)


    Host.query.first()
    api_key_obj = ApiKey.query.filter_by(api_key=api_key).first()
    if not api_key_obj:
        api_key_obj = ApiKey(api_key=api_key)
        db.session.add(api_key_obj)
        db.session.commit()

    host_obj = Host.query.filter_by(host_name=host_name).first()
    if not host_obj:
        #make new host store in db and return nothing
        #create relationship for this api key and host
        host_obj = Host(host_name=host_name, top_pages=res.json())
        #do async
        if host_obj not in api_key_obj.hosts:
            api_key_obj.add_host(host_obj)

        db.session.add(host_obj)
        db.session.commit()
        return jsonify(result)

    if host_obj:
        if host_obj not in api_key_obj.hosts:
            #do async
            api_key_obj.add_host(host_obj)
        #need to compare against current chartbeat data
        #need to also return new page visitor count
        local_data = process_data(host_obj.top_pages)
        current_data = process_data(res.json())
        for page in current_data:
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
            #sort result by increasing visitors
            result = sorted(
                result,
                key=lambda result: result['change'],
                reverse=True
            )

        #do async
        host_obj.top_pages = res.json()
        host_obj.updated_at = datetime.datetime.utcnow()
        db.session.commit()

        return Response(json.dumps(result),  mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
