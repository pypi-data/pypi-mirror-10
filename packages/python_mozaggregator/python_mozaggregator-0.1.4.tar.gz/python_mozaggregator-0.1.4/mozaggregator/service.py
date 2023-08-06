import argparse
import ujson as json

from flask import Flask, request, abort
from db import create_connection, histogram_revision_map
from moztelemetry.histogram import Histogram
from aggregator import scalar_histogram_labels

app = Flask(__name__)


def execute_query(query, params=tuple()):
    db = create_connection(host_override=host)
    cursor = db.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()


@app.route('/aggregates_by/<prefix>/channels/')
def get_channels(prefix):
    try:
        channels = execute_query("select * from list_channels(%s)", (prefix, ))
        if not channels:
            abort(404)

        return json.dumps([channel[0] for channel in channels])
    except:
        abort(404)


@app.route('/aggregates_by/<prefix>/channels/<channel>/dates/')
def get_dates(prefix, channel):
    try:
        result = execute_query("select * from list_buildids(%s, %s)", (prefix, channel))
        if not result:
            abort(404)

        pretty_result = map(lambda r: {"version": r[0], "date": r[1]}, result)
        return json.dumps(pretty_result)
    except:
        abort(404)


@app.route('/aggregates_by/<prefix>/channels/<channel>/dates/<version>_<date>', methods=["GET"])
def get_date(prefix, channel, version, date):
    try:
        dimensions = json.dumps({k: v for k, v in request.args.iteritems()})
        result = execute_query("select * from get_metric(%s, %s, %s, %s, %s)", (prefix, channel, version, date, dimensions))

        if not result:  # Metric not found
            abort(404)

        pretty_result = []
        for row in result:
            label = row[0]
            histogram = row[1][:-1]
            count = row[1][-1]

            # Retrieve labels for histogram
            revision = histogram_revision_map.get(channel, "nightly")  # Use nightly revision if the channel is unknown
            try:
                labels = Histogram(request.args["metric"], histogram, revision=revision).get_value().keys().tolist()
            except Exception as e:
                # Count histogram or simple measurement
                # TODO: deal properly with those
                labels = scalar_histogram_labels

            pretty_result.append({"label": label, "histogram": dict(zip(labels, histogram)), "count": count})

        return json.dumps(pretty_result)

    except:
        abort(404)


if __name__ == "__main__":
    global host

    parser = argparse.ArgumentParser(description="Aggregation REST service", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-d", "--debug", help="Debug mode", dest="debug", action="store_true")
    parser.add_argument("-o", "--host", help="DB hostname", default=None)

    parser.set_defaults(debug=False)
    args = parser.parse_args()
    host = args.host

    app.run("0.0.0.0", debug=args.debug)
