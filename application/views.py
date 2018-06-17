from flask import render_template, flash, redirect, url_for, request, session,jsonify
import json
from application import application, app
from application.models import *
from application.my_functions import *


@application.route('/get_levels' ,methods=['POST'])
def get_levels():
    hierarchy = json.loads((request.data).decode("utf-8"))
    levelArray = build_sales_list(hierarchy)
    return jsonify({'levels': levelArray})

@application.route('/')
def index():
    return render_template('select_test.html')

@application.route('/process',methods=['GET','POST'])
def process():
    email = request.form['email']
    name = request.form['name']
    print("email: ", request.form['email'],"name: ",request.form['name'])
    print ()
    print ("Request form: ",request.form.to_dict())
    # jim = build_sales_dict('Americas')

    if name == 'Americas':
        jim = build_sales_dict('Americas')
        newName = "Got Americas"
        print (newName)

    if name and email:
        newName = name[::-1]

        return jsonify({'name': newName})

    else:
        print ("i ain't got it")

    return jsonify({'error': 'Missing data!'})


@application.route('/saveit/<int:id>',methods=['GET', 'POST'])
def saveit(id):
    if request.method == 'POST':
        record = Coverage.query.filter(Coverage.id == id)
        action = request.form['btnClick']
        print("Action taken :", action, record[0].id, record[0].pss_name)
        if action == 'edit':
            record[0].pss_name = request.form['pss_name']
            record[0].tsa_name = request.form['tsa_name']
            record[0].sales_level_1 = request.form['sales_level_1']
            record[0].sales_level_2 = request.form['sales_level_2']
            record[0].sales_level_3 = request.form['sales_level_3']
            record[0].sales_level_4 = request.form['sales_level_4']
            record[0].sales_level_5 = request.form['sales_level_5']
            record[0].fiscal_year = request.form['fiscal_year']
            db.session.commit()
        elif action == 'delete':
            names = Coverage.query.filter(Coverage.id == id).delete()
            db.session.commit()
        elif action == 'mail':
            pass

    return render_template('index.html')


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
    record = Coverage.query.filter(Coverage.id == id)
    if action == 'delete':
        action = ['delete','Delete this ?']
    elif action == 'mail':
        action =  ['mail','Mail This ?']
    elif action == 'edit':
        action = ['edit','Save Changes ?']

    print("Action request :",action,record[0].id,record[0].pss_name)

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
        sales_levels = build_sales_dict("Americas")
        print('Got a GET: ', request.get_data())
        details = db.session.query(Coverage.sales_level_4.distinct())
    return render_template('input.html',details=details,sales_levels=sales_levels)


@application.route('/testing')
def testing():
    details = db.session.query(Coverage.sales_level_4.distinct())
    for detail in details:
        print(detail)
    return render_template('testing.html',details=details)


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@application.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500