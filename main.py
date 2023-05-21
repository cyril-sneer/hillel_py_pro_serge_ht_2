#! .venv/bin/python3


import funcs  # importing a module containing our functions
import flask


app = flask.Flask(__name__)


@app.route('/')  # root
def index():
    return flask.render_template('index.html',
                                 title='The Flask!!!')


@app.route('/requirements/')  # Project requirements
def requirements():
    return flask.render_template('requirements.html',
                                 title='Project requirements',
                                 req_list=funcs.get_text_file(txt_file_name='requirements.txt'))


@app.route('/generate-users/', methods=['GET', 'POST'])  # Fake users list
def generate_users():
    quantity = flask.request.args.get('count', 100)  # get the "count" query-parameter from URL-string
    return flask.render_template('generate_users.html',
                                 title='Users list',
                                 users_list=funcs.get_fake_users(quantity=int(quantity)))


@app.route('/mean/')  # Average height and weight
def show_averages():
    aver_height, aver_weight = funcs.calc_average_height_and_weight('hw.csv')
    return flask.render_template('aver_height_and_weight.html',
                                 title='Average height and weight',
                                 aver_height=aver_height,
                                 aver_weight=aver_weight)


@app.route('/space/')  # Astronauts quantity & names
def show_astro_quantity():
    astro_qty, astro_names = funcs.get_astros(json_link='http://api.open-notify.org/astros.json')
    return flask.render_template('show_astro.html',
                                 title='Astronauts info',
                                 astro_qty=astro_qty,
                                 astro_names=astro_names)


if __name__ == '__main__':
    app.run(debug=False)
