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

    # Go fetch the records from the db
    # Records are returned formatted as per the __repr__ in the model

    coverages = Coverage.newest_name(12)
    # coverages = Coverage.newest()

    for jim in coverages:
        print(jim)

    return render_template('list.html', coverages=coverages)

@application.route('/detail/<int:page_num>')
def detail(page_num):
    details = Coverage.query.paginate(per_page=12,page=page_num,error_out=True)
    return render_template('detail.html',details=details,my_name='any')


# @application.route('/team', methods=['GET', 'POST'])
# def team():
#     req_page = 1
#     if request.method == 'POST':
#         print('Got a POST: ', request.get_data())
#     elif request.method == 'GET':
#         print('Got a GET: ', request.get_data())
#         query_page = request.args.get('page_request')
#         if query_page =='None':
#             req_page = 1
#         elif query_page == '10more':
#             req_page = 3
#         elif query_page == '10less':
#             req_page = 2
#
#     # Go fetch the records from the db
#     # Records are returned formatted as per the __repr__ in the model
#
#     # Default is 20 results per page
#     my_pages = Coverage.query.paginate(per_page=10)
#     print("next page..",my_pages.next_num)
#     print ("pages  ",my_pages.pages)
#     print (db.session.query(Coverage).count())
#
#     coverages = Coverage.get_page(req_page)
#     # coverages = Coverage.newest()
#
#     return render_template('detail.html', coverages=coverages, my_name='any')


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






