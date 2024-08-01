# 生成季度维度数据
# 作者blaxun
import calendar
import datetime
import math

e = {1: 'First', 2: 'Second', 3: 'Third', 4: 'Fourth'}
d = {1: '一', 2: '二', 3: '三', 4: '四'}
file = open(r'../output/quarter.sql', 'w+', encoding='utf-8')

for year in range(1970, 2149):
    for q in d.keys():
        quarter_id = str(year) + 'Q' + str(q)
        quarter_name = e.get(q) + ' quarter ' + str(year)
        quarter_name_cn = str(year) + '年第' + d.get(q) + '季度'

        # 当季第一个月
        first_month = (q - 1) * 3 + 1

        # 获取当季第一个月的第一天
        first_day_of_the_quarter = datetime.date(year, first_month, 1)
        last_day_of_pre_quarter = first_day_of_the_quarter + datetime.timedelta(days=-1)
        # 上季度序号
        pre_quarter_no = math.ceil(last_day_of_pre_quarter.month / 3)
        # 上季度ID
        pre_quarter_id = str(last_day_of_pre_quarter.year) + 'Q' + str(pre_quarter_no)

        # 获取当季第三个月的第一天
        last_month_first_day = datetime.date(year, first_month, 1)

        # 获取当月的总天数
        monthRange = calendar.monthrange(year, first_month + 2)[1]

        last_day_of_the_quarter = datetime.date(year, first_month + 2, monthRange)
        first_day_of_next_quarter = last_day_of_the_quarter + datetime.timedelta(days=1)
        # 下季度序号
        next_quarter_no = math.ceil(first_day_of_next_quarter.month / 3)
        # 下季度ID
        next_quarter_id = str(first_day_of_next_quarter.year) + 'Q' + str(next_quarter_no)

        # 采用绑定变量方式
        param = {'quarter_id': quarter_id, 'quarter_order': q, 'quarter_name': quarter_name,
                 'quarter_name_cn': quarter_name_cn, 'year_id': year,
                 'first_day_of_the_quarter': first_day_of_the_quarter,
                 'last_day_of_the_quarter': last_day_of_the_quarter, 'pre_quarter_id': pre_quarter_id,
                 'next_quarter_id': next_quarter_id}

        sql = 'INSERT INTO dim.date_quarter values'
        sql += '(\'{quarter_id}\','
        sql += '\'{quarter_name}\',\'{quarter_name_cn}\','
        sql += '{year_id},{quarter_order},'
        sql += 'TO_DATE(\'{first_day_of_the_quarter}\',\'yyyy-mm-dd\'),'
        sql += 'TO_DATE(\'{last_day_of_the_quarter}\',\'yyyy-mm-dd\'),'
        sql += '\'{pre_quarter_id}\',\'{next_quarter_id}\');\n'

        sql = sql.format(**param)
        file.writelines(sql)

file.close()
print('已生成建表语句:' + 'quarter.sql')
