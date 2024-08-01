CREATE TABLE
	dim.date_month (
	    month_id CHAR(7) PRIMARY KEY COMMENT '该月所在的月份id，形如：2024-03',
	    month_name VARCHAR(14) UNIQUE COMMENT '月名称，英文',
		month_name_cn VARCHAR(12) UNIQUE COMMENT '月名称，中文',
	    quarter_id CHAR(6) COMMENT '该月所在的季度id，形如：2024Q1',
	    year_id SMALLINT COMMENT '该月所在的年份id',
		month_order TINYINT COMMENT '该月是所在年的第几个月',
		first_day_of_the_month DATE UNIQUE COMMENT '该月第一天的日期',
		last_day_of_the_month DATE UNIQUE COMMENT '该月最后一天的日期',
		pre_month_id CHAR(7) UNIQUE COMMENT '前一个月的id',
		next_month_id CHAR(7) UNIQUE COMMENT '后一个月的id'
	)
WITH
	(orientation = column, COMPRESSION = NO) DISTRIBUTE BY replication;
