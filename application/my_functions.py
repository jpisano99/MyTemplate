from application.models import *

def build_sales_list(hierarchy):
    print()
    print("Request:  ",hierarchy)
    print()

    # Build SQL Stmnt from the hierarchy list
    level = 1
    tmp = ""
    sql_where = ""
    sql_columns = ""

    for x in hierarchy:
        tmp = "`Sales_Level_" + str(level) + "`"
        sql_where = sql_where + tmp + "=" + "'" + x + "' AND "
        sql_columns = sql_columns + "," + tmp
        level += 1

    if len(hierarchy) == 0:
        # Adjust SQL stmnt for a starter list
        sql_columns = "`Sales_Level_1`"
        sql_where = ""
    else:
        # Add one add'l column to the request
        sql_columns = sql_columns + "," + "`Sales_Level_" + str(level) + "`"

        # Trim these up
        sql_where = "WHERE " + sql_where.rstrip("AND ")
        sql_columns = sql_columns.lstrip(", ")

    # Build the SQL Statement
    sql = "SELECT DISTINCT " + \
            sql_columns + \
            "FROM sales_levels " + \
            sql_where  + \
            " order by `Sales_Level_1`"
    print()
    print("SQL:  ",sql)
    print()

    # # Run the Query
    query_results = db.engine.execute(sql)

    # Construct the response list
    level_list = []
    for x in query_results:
        build_it = []
        for y in range(level):
            build_it.append(x.values()[y])
        level_list.append(build_it)

    print()
    print("Response:   ",level_list)
    print()

    return (level_list)

if __name__ == "__main__":
    from application.models import *
    from application.my_functions import *
    #jim = ["Americas","AMERICAS_MISC"]
    #jim = []
    #jim = ["Americas"]
    jim = ["Americas", "US COMMERCIAL", "COMMERCIAL EAST AREA","Colonial Select Operation"]
    build_sales_list(jim)
