# -*- coding: utf-8 -*- 
import flask, flask.views, os
from tools.validator import validate_form
from tools.mailer import send_email
from tools.js import json_loader
from tools.crypto import rand_string, caesar

app = flask.Flask(__name__)
app.config.from_object('config')



class View(flask.views.MethodView):
    def get(self, command=None):
        return flask.render_template('index.html') 
    
#app.add_url_rule('/', view_func=View.as_view('main'))


@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
@app.route('/post/<fhash>', methods=['POST'])
def home(fhash = ''):
	if flask.request.method == 'POST':
		'''
		from datetime import datetime
		if ( flask.session.get('last_post') ): 
			
			diff = datetime.utcnow() - flask.session.get('last_post')

			return diff
			'''
		if fhash == '' or flask.session.get('fhash') != fhash:
			return flask.redirect(flask.url_for('post'))

		if validate_form(flask.request.form):
			send_email('Новый заказ',
						None,
						app.config['ADMINS'],
						flask.request.form)

			flask.session.pop('fhash', None)
			#flask.session['last_post'] = datetime.utcnow()

			return flask.redirect(flask.url_for('post'))
			#return flask.render_template('order_finished.html')

	fhash = rand_string()
	flask.session['fhash'] = caesar(fhash, app.config['CAESAR_CHIPER_CODE'])
	return flask.render_template('index.html',
								form=flask.request.form,
								esigs=json_loader(os.path.join(app.root_path, app.config['ESIGS_JSON'])),
								fhash = fhash
								)

# Anti bots mock
@app.route('/post', methods=['GET', 'POST'])
def	post(): 
	return flask.render_template('order_finished.html')

@app.route('/gallery.html')
def gallery():
	return flask.render_template('gallery.html',
								esigs=json_loader(os.path.join(app.root_path, app.config['ESIGS_JSON']))
								)

@app.route('/<fileName>.html')
def page(fileName):
	try: 
		return flask.render_template('%s.html' % fileName) 
	except:
		return page_not_found(404)

@app.route('/pprint')
def pprint():
	import pprint
	return flask.session.get('fhash')
	return pprint.pformat(flask.session)

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('errors/not_found.html'), 404





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
