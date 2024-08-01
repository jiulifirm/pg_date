# 生成周维度数据
# 作者blaxun
import datetime

from isoweek import Week

file = open(r'../output/week.sql', 'w+', encoding='utf-8')

years = range(1970, 2149)

for year in years:
    for week in Week.weeks_of_year(year):
        week_order = week.week

        # 该周的iso编号，ISO8601:2004，形如：2024W01
        week_id = str(week)

        # 该周在clickhouse中的编号,亦采用iso8601标准，形如：202401
        week_id_iso = str(year) + str(week_order).zfill(2)
        week_name = 'Week ' + str(week_order) + ', ' + str(year)
        week_name_cn = str(year) + '年第' + str(week_order) + '周'

        # 该周第一天（星期一）的日期
        first_day_of_the_week = week.monday()
        last_day_of_pre_week = first_day_of_the_week + datetime.timedelta(days=-1)
        week_year, week_number, day_of_week = last_day_of_pre_week.isocalendar()

        # 该周上一周的id，iso编号
        pre_week_id = str(week_year) + 'W' + str(week_number).zfill(2)

        # 该周最后一天（星期日）的日期
        last_day_of_the_week = week.sunday()
        first_day_of_next_week = last_day_of_the_week + datetime.timedelta(days=1)
        week_year, week_number, day_of_week = first_day_of_next_week.isocalendar()

        # 该周下一周的id，iso编号
        next_week_id = str(week_year) + 'W' + str(week_number).zfill(2)

        # 采用绑定变量方式
        param = {'week_id': week_id, 'week_id_iso': week_id_iso, 'year_id': year, 'week_order': week_order,
                 'week_name': week_name,
                 'week_name_cn': week_name_cn, 'first_day_of_the_week': first_day_of_the_week,
                 'last_day_of_the_week': last_day_of_the_week, 'pre_week_id': pre_week_id, 'next_week_id': next_week_id}

        # 生成clickhouse插入语句
        sql = 'insert into dim.date_week values('
        sql += '\'{week_id}\',\'{week_id_iso}\','
        sql += '\'{week_name}\',\'{week_name_cn}\','
        sql += '\'{year_id}\',{week_order},'
        sql += 'TO_DATE(\'{first_day_of_the_week}\',\'yyyy-mm-dd\'),TO_DATE(\'{last_day_of_the_week}\',\'yyyy-mm-dd\'),'
        sql += '\'{pre_week_id}\',\'{next_week_id}\');\n'

        sql = sql.format(**param)
        file.writelines(sql)
file.close()
print('已生成建表语句:' + 'week.sql')
