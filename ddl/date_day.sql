CREATE TABLE
	dim.date_day (
		day_id CHAR(10) PRIMARY KEY COMMENT '该天的id，形如：2024-03-08',
		day_date Date UNIQUE COMMENT '该天的标准日期类型',
		day_name VARCHAR(18) UNIQUE COMMENT '该天的英文名称',
		day_name_cn VARCHAR(17) UNIQUE COMMENT '该天的中文名称',
		week_day VARCHAR(9) COMMENT '该天是星期几，英文表达',
		week_day_cn VARCHAR(9) COMMENT '该天是星期几，中文表达',
		week_id CHAR(7) COMMENT '该天所在的周id，iso8601,形如：2024W10',
		week_id_iso INTEGER COMMENT '该天所在的周id，兼容clickhouse表示法,形如：202410',
		month_id CHAR(7) COMMENT '该天所在的月份id，形如：2024-03',
		quarter_id CHAR(6) COMMENT '该天所在的季度id，形如：2024Q1',
		year_id SMALLINT COMMENT '该天所在的年份id',
		day_of_week TINYINT COMMENT '该天是一个星期当中的第几天',
		day_of_month TINYINT COMMENT '该天是一个月当中的第几天',
		day_of_quarter TINYINT COMMENT '该天是一个季度当中的第几天',
		day_of_year SMALLINT COMMENT '该天是一年当中的第几天',
		pre_day_id CHAR(10) UNIQUE COMMENT '该天的前一天',
		next_day_id CHAR(10) UNIQUE COMMENT '该天的后一天'
	)
WITH
	(orientation = column, COMPRESSION = NO) DISTRIBUTE BY replication;
