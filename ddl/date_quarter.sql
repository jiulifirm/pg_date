CREATE TABLE
	dim.date_quarter (
	    quarter_id CHAR(6) PRIMARY KEY COMMENT '季度id，形如：2024Q1',
		quarter_name VARCHAR(19) UNIQUE COMMENT '季度名称，英文',
		quarter_name_cn VARCHAR(19) UNIQUE COMMENT '季度名称，中文',
        year_id SMALLINT COMMENT '该季度所在的年份id',
		quarter_order TINYINT COMMENT '季度序号',
		first_day_of_the_quarter DATE UNIQUE COMMENT '该季度第一天的日期',
		last_day_of_the_quarter DATE UNIQUE COMMENT '该季度最后一天的日期',
		pre_quarter_id CHAR(6) UNIQUE COMMENT '该季度前一季度的id',
		next_quarter_id CHAR(6) UNIQUE COMMENT '该季度后一季度的id'
	)
WITH
	(orientation = column, COMPRESSION = NO) DISTRIBUTE BY replication;
