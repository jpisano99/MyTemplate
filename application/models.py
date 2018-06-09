from application import db

class Coverage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pss_name = db.Column(db.String(30))
    tsa_name = db.Column(db.String(30))
    sales_level_1 = db.Column(db.String(30))
    sales_level_2 = db.Column(db.String(30))
    sales_level_3 = db.Column(db.String(30))
    sales_level_4 = db.Column(db.String(30))
    sales_level_5 = db.Column(db.String(30))
    fiscal_year = db.Column(db.String(30))

    @staticmethod
    def newest():
        return Coverage.query.order_by(Coverage.pss_name).all()

    def get_page(page_num):
        num_of_pages = Coverage.query.paginate(per_page=10)
        return Coverage.query.order_by(Coverage.id).offset(page_num*10)

    def newest_name(num):
        return Coverage.query.order_by(Coverage.pss_name).limit(num)

    # def get_pss(find_pss):
    #     print("looking for" ,find_pss)
    #     return Coverage.query.filter(Coverage.id==2)

    def __repr__(self):
       return "<name {}: '{} , {}'>".format(self.id, self.pss_name,self.tsa_name)

class Managers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(45))
    first_name = db.Column(db.String(45))
    segment = db.Column(db.String(45))

    @staticmethod
    def newest():
        return Managers.query.order_by(Managers.last_name).all()

    def __repr__(self):
       return "<name {}: '{} , {}'>".format(self.id, self.last_name,self.first_name,self.segment)

class sales_levels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Sales_Level_1 = db.Column(db.String(30))
    Sales_Level_2 = db.Column(db.String(30))
    Sales_Level_3 = db.Column(db.String(30))
    Sales_Level_4 = db.Column(db.String(30))
    Sales_Level_5 = db.Column(db.String(30))

    # @staticmethod
    # def newest():
    #     return Managers.query.order_by(Managers.last_name).all()

    # def __repr__(self):
    #    return "<name {}: '{} , {}'>".format(sel