CREATE TABLE
	dim.date_year (
		year_id SMALLINT PRIMARY KEY COMMENT '年份id',
		year_name_cn VARCHAR(7) UNIQUE COMMENT '年份名称，中文',
		first_day_of_the_year DATE UNIQUE COMMENT '该年第一天的日期',
		last_day_of_the_year DATE UNIQUE COMMENT '该年最后一天的日期',
		is_leap_year TINYINT COMMENT '是否闰年',
		pre_year_id SMALLINT UNIQUE COMMENT '该年前一年的id',
		next_year_id SMALLINT UNIQUE COMMENT '该年后一年的id'
	)
WITH
	(orientation = column, COMPRESSION = NO) DISTRIBUTE BY replication;
