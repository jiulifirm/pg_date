# 生成日维度数据
# 作者blaxun

import calendar
import datetime
import math

file = open(r'../output/day.sql', 'w+', encoding='utf-8')

d = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '日'}

years = range(1970, 2149)
months = range(1, 13)

for year in years:
    for month in months:
        # 当月总天数
        days = calendar.monthrange(year, month)[1]
        for day_of_month in range(1, days + 1):
            # 标准日期
            day_date = datetime.date(year, month, day_of_month)

            # 日id
            day_id = day_date.strftime('%Y-%m-%d')

            pre_day = day_date + datetime.timedelta(days=-1)
            # 前一日id
            pre_day_id = pre_day.strftime('%Y-%m-%d')

            next_day = day_date + datetime.timedelta(days=1)
            # 后一日id
            next_day_id = next_day.strftime('%Y-%m-%d')

            month_id = day_date.strftime('%Y-%m')

            # 月份英文名
            month_name = day_date.strftime('%B')

            day_name = month_name + ' ' + str(day_of_month) + ', ' + str(year)

            day_name_cn = str(year) + '年' + str(month) + '月' + str(day_of_month) + '日'

            # 星期几
            week_day = day_date.strftime('%A')

            # 星期编号所在年，年中第几周，星期几
            week_year, week_number, day_of_week = day_date.isocalendar()

            # iso星期id
            week_id = str(week_year) + 'W' + str(week_number).zfill(2)

            # clickhouse星期id
            week_id_ch = str(week_year) + str(week_number).zfill(2)

            # 中文星期几
            week_day_cn = '星期' + d.get(day_of_week)

            # 季度序号
            quarter = math.ceil(month / 3)

            # 季度ID
            quarter_id = str(year) + 'Q' + str(quarter)

            # 上季度所在年
            lq_year = year

            # 上季最后一个月
            lql_month = (quarter - 1) * 3

            if lql_month == 0:
                lql_month = 12
                lq_year = year - 1

            # 上季最后一个月总天数
            lqlm_days = calendar.monthrange(lq_year, lql_month)[1]

            # 上季最后一个天
            lql_date = datetime.date(lq_year, lql_month, lqlm_days)

            # 季度第几天
            day_of_quarter = (day_date - lql_date).days

            # 年中第几天
            day_of_year = day_date.strftime('%j')

            # 采用绑定变量方式
            param = {'day_id': day_id,
                     'day_date': day_date,
                     'week_id': week_id,
                     'week_id_ch': week_id_ch,
                     'month_id': month_id,
                     'quarter_id': quarter_id,
                     'year_id': year,
                     'day_name': day_name,
                     'day_name_cn': day_name_cn,
                     'week_day': week_day,
                     'week_day_cn': week_day_cn,
                     'day_of_week': day_of_week,
                     'day_of_month': day_of_month,
                     'day_of_quarter': day_of_quarter,
                     'day_of_year': day_of_year,
                     'pre_day_id': pre_day_id,
                     'next_day_id': next_day_id
                     }

            sql = 'INSERT INTO dim.date_day values('
            sql += '\'{day_id}\','
            sql += 'TO_DATE(\'{day_date}\',\'yyyy-mm-dd\'),'
            sql += '\'{day_name}\',\'{day_name_cn}\','
            sql += '\'{week_day}\',\'{week_day_cn}\','
            sql += '\'{week_id}\',{week_id_ch},\'{month_id}\',\'{quarter_id}\',{year_id},'
            sql += '{day_of_week},{day_of_month},{day_of_quarter},{day_of_year},'
            sql += '\'{pre_day_id}\',\'{next_day_id}\');\n'

            sql = sql.format(**param)
            file.writelines(sql)
file.close()
print('已生成建表语句:' + 'day.sql')
