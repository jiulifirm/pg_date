# 生成月维度数据
# 作者blaxun

import calendar
import datetime
import math

file = open(r'../output/month.sql', 'w+', encoding='utf-8')

years = range(1970, 2149)
months = range(1, 13)

for year in years:
    for month in months:
        # 当月第一天
        first_day_of_the_month = datetime.date(year, month, 1)

        last_day_of_pre_month = first_day_of_the_month + datetime.timedelta(days=-1)

        # 当月总天数
        days = calendar.monthrange(year, month)[1]

        # 当月最后一天
        last_day_of_the_month = datetime.date(year, month, days)

        first_day_of_next_month = last_day_of_the_month + datetime.timedelta(days=1)

        # 月id
        month_id = first_day_of_the_month.strftime('%Y-%m')

        # 月名称
        month_name = first_day_of_the_month.strftime('%B %Y')

        # 月名称_中文
        month_name_cn = str(year) + '年' + str(month) + '月'

        quarter = math.ceil(month / 3)

        quarter_id = str(year) + 'Q' + str(quarter)

        pre_month_id = last_day_of_pre_month.strftime('%Y-%m')

        next_month_id = first_day_of_next_month.strftime('%Y-%m')

        # 采用绑定变量方式
        param = {'month_id': month_id, 'quarter_id': quarter_id, 'year_id': year, 'month_order': month,
                 'month_name': month_name, 'month_name_cn': month_name_cn,
                 'first_day_of_the_month': first_day_of_the_month, 'last_day_of_the_month': last_day_of_the_month,
                 'pre_month_id': pre_month_id, 'next_month_id': next_month_id}

        sql = 'INSERT INTO dim.date_month values('
        sql += '\'{month_id}\','
        sql += '\'{month_name}\',\'{month_name_cn}\','
        sql += '\'{quarter_id}\',{year_id},{month_order},'
        sql += 'TO_DATE(\'{first_day_of_the_month}\',\'yyyy-mm-dd\'),'
        sql += 'TO_DATE(\'{last_day_of_the_month}\',\'yyyy-mm-dd\'),'
        sql += '\'{pre_month_id}\',\'{next_month_id}\');\n'

        sql = sql.format(**param)
        file.writelines(sql)
file.close()
print('已生成建表语句:' + 'month.sql')
