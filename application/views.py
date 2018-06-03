from flask import render_template, flash, redirect, url_for, request, session
from application import application,app
from application.models import *


@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())
    elif request.method == 'GET':
        print('Got a GET: ', request.get_data())

    coverages = Coverage.newest_name(12)
    return render_template('index.html', coverages=coverages)


@application.route('/list', methods=['GET', 'POST'])
def list():
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())
    elif request.method == 'GET':
        print('Got a GET: ', request.get_data())

    coverages = Coverage.newest_name(12)
    return render_template('list.html', coverages=coverages)


@application.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())
    elif request.method == 'GET':
        print('Got a GET: ', request.get_data())

    return render_template('input.html')


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@application.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500






