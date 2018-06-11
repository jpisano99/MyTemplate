from application.models import *


def build_sales_dict(sales_level_1):
    # Find all Sales Levels
    sql = "SELECT DISTINCT "+ \
            "`Sales_Level_1`,`Sales_Level_2`,`Sales_Level_3`,`Sales_Level_4`,`Sales_Level_5` " + \
            "FROM sales_levels " + \
            "WHERE `Sales_Level_1` = " + "'" + sales_level_1 + "' " \
            "order by `Sales_Level_1`"
    all_sales_levels = db.engine.execute(sql)

    sales_level_dict= {}
    current_key = ""
    current_list = []

    # Prime the key
    current_key = all_sales_levels.first()[0]

    # Rerun the Query
    all_sales_levels = db.engine.execute(sql)
    cntr = 0

    for x in all_sales_levels:
        cntr = cntr + 1
        if current_key != x.values()[0]:
            #create new dict entry
            sales_level_dict[current_key] = current_list
            # reset key and list
            current_list=[]
            current_key = x.values()[0]
        else:
            current_list.append((x.values()[1], x.values()[2], x.values()[3], x.values()[4]))

    # Add the last dict entry
    sales_level_dict[current_key] = current_list

    #DEBUG Code
    for key,values in sales_level_dict.items():
        print (key)
        for value in values:
            # if key == 'Americas':
            print(key,value[0],value[1],value[2],value[3])
            #print('# ',cntr,' ',key," : ",value)

    return (sales_level_dict)

