import config
from db import run_sql
select_code_sql = "select status,status_id from status;"
result=run_sql(select_code_sql)
print result[0][0]
