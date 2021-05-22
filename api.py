from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def queryresult(title):

    query = "SELECT * FROM higherlowerdata WHERE"
    to_filter = []

    if title:
        query += ' title=? AND'
        to_filter.append(title)
    if not title:
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return results


@app.errorhandler(404)
def page_not_found(e):

    return "<h1>404 Page not found</h1>"


@app.route("/", methods=['GET', 'POST'])
def main():

    return "<h1>Welcome to 'The Higher Lower Game API'</h1><h3>Made with <3 by Soham Sahare</h3>"


@app.route('/api/v1/resources/data/all', methods=['GET'])
def api_all():

    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    data = cur.execute('SELECT * FROM higherlowerdata;').fetchall()

    return jsonify(data)


@app.route('/api/v1/resources/data/title/<title>', methods=['GET'])
def api_filter_title(title):

    title = title.lower()
    results = queryresult(title)

    return jsonify(results)


@app.route('/api/v1/resources/data/searchvolume/<title>', methods=['GET'])
def api_filter_search(title):

    title = title.lower()
    results = queryresult(title)

    return jsonify(results[0]["searches"])


@app.route('/api/v1/resources/data/higherlower/<title_left>/<title_right>', methods=['GET'])
def api_filter_higherlower(title_left, title_right):

    title = title_left.lower()
    results1 = queryresult(title)

    title = title_right.lower()
    results2 = queryresult(title)

    search1 = results1[0]["searches"]
    search2 = results2[0]["searches"]

    if search1 < search2 or search1 == search2:
        answer = "Higher"
    else:
        answer = "Lower"

    return answer


if __name__ == "__main__":

    app.run(debug=True)
