# 生成年维度数据
# 作者blaxun
import calendar
import datetime

file = open(r'../output/year.sql', 'w+', encoding='utf-8')

for year in range(1970, 2149):

    year_id = year

    # 获取当年第一天
    first_day_of_the_year = datetime.date(year, 1, 1)

    # 获取当年最后一天
    last_day_of_the_year = datetime.date(year, 12, 31)

    # 获取当年2月总天数
    feb_days = calendar.monthrange(year, 2)[1]

    # 判断是否闰年
    is_leap_year = 0
    if feb_days == 29:
        is_leap_year = 1

    pre_year_id = year_id - 1

    next_year_id = year_id + 1

    # 采用绑定变量方式
    param = {'year_id': year_id, 'first_day_of_the_year': first_day_of_the_year,
             'last_day_of_the_year': last_day_of_the_year,
             'is_leap_year': is_leap_year, 'pre_year_id': pre_year_id, 'next_year_id': next_year_id}

    sql = 'insert into dim.date_year values({year_id},'
    sql += '\'{year_id}年\','
    sql += 'TO_DATE(\'{first_day_of_the_year}\',\'yyyy-mm-dd\'),'
    sql += 'TO_DATE(\'{last_day_of_the_year}\',\'yyyy-mm-dd\'),'
    sql += '{is_leap_year},{pre_year_id},{next_year_id});\n'

    sql = sql.format(**param)
    file.writelines(sql)
file.close()
print('已生成建表语句:' + 'year.sql')
