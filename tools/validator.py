# -*- coding: utf-8 -*- 
from flask import flash

def validate_form(form):
	
    err = 0

    if form['name'] == '':
            flash(u'Необходимо заполнить ФИО')
            err = 1
    if form['phone'] == '':
            flash(u'Необходимо заполнить телефон')
            err = 1
    if form['email'] == '':
            flash(u'Необходимо заполнить email')
            err = 1
    if form['address'] == '':
            flash(u'Необходимо заполнить адрес')
            err = 1

    if err == 1:
    	return False
    else:
    	return True