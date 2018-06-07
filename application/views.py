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


@application.route('/list')
def list():
    # Simple List
    # Go fetch the records from the db
    # Records are returned formatted as per the __repr__ in the model
    coverages = Coverage.newest_name(12)
    return render_template('list.html', coverages=coverages)


@application.route('/detail/<int:page_num>')
def detail(page_num):
    # Display db rows with options for delete/edit/email
    # Sourced from YouTube pagination example
    # https://www.youtube.com/watch?v=hkL9pgCJPNk
    details = Coverage.query.paginate(per_page=6,page=page_num,error_out=True)
    return render_template('detail.html',details=details,my_name='any')


@application.route('/modify/<string:action>/<int:id>', methods=['GET', 'POST'])
def modify(action,id):
    print ('action:',action)
    print ('record',id)

    record = Coverage.query.filter(Coverage.id == id)
    if action == 'delete':
        action = "Delete This ?"
    elif action == 'mail':
        action = "Mail This ?"
    elif action == 'edit':
        action = "Edit This ?"

    print("Deleting :",record[0].id,record[0].pss_name)

    if request.method == 'POST':
        print('Got a POST: ', request.get_data())
        for form_item in request.form.items():
            print(form_item)
    return render_template('modify.html', record=record,action=action)


@application.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())
        for form_item in request.form.items():
            print(form_item)

        # Create a SQLAlchmey object to hand to the db
        name = Coverage(pss_name=request.form['pss_name'],
                        tsa_name=request.form['tsa_name'],
                        sales_level_1=request.form['sales_level_1'],
                        sales_level_2=request.form['sales_level_2'],
                        sales_level_3=request.form['sales_level_3'],
                        sales_level_4=request.form['sales_level_4'],
                        sales_level_5=request.form['sales_level_5'],
                        fiscal_year=request.form['fiscal_year'])
        print (type(name))
        db.session.add(name)
        db.session.commit()
        return redirect('/')
    elif request.method == 'GET':
        print('Got a GET: ', request.get_data())
    return render_template('input.html')


@application.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())
    elif request.method == 'GET':
        print('Got a GET: ', request.get_data())

    # Go fetch the records from the db
    # Records are returned formatted as per the __repr__ in the model

    # Fetch the record(s) you want to delete
    #name = Coverage.get_pss("Cathy")

    names = Coverage.query.filter(Coverage.pss_name == "Susanne East-Brooke").delete()
    # print(type(names))
    # for name in names:
    #     print (name)
    #
    # db.session.delete(names)
    db.session.commit()
    print("deleted")

    return render_template('index.html')


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@application.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500






