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
        return Coverage.query.all()

    def newest_name(num):
        return Coverage.query.order_by((Coverage.pss_name)).limit(num)

    def __repr__(self):
       return "<name {}: '{} , {}'>".format(self.id, self.pss_name,self.tsa_name)