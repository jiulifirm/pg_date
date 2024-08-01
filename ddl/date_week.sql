CREATE TABLE dim.date_week
(
    week_id CHAR(7) PRIMARY KEY COMMENT '周缩写,形如：2024W10',
    week_id_iso CHAR(6) UNIQUE COMMENT '周id，iso8601,形如：202410',
	week_name VARCHAR(13) UNIQUE COMMENT '周名称，英文',
    week_name_cn VARCHAR(15) UNIQUE COMMENT '周名称，中文',
    year_id SMALLINT COMMENT '该周所在年的id',
    week_order TINYINT COMMENT '该周是所在年的第几周',
    first_day_of_the_week Date UNIQUE COMMENT '该周第一天的日期',
    last_day_of_the_week Date UNIQUE COMMENT '该周最后一天的日期',
    pre_week_id CHAR(7) UNIQUE COMMENT '前一周的id',
    next_week_id CHAR(7) UNIQUE COMMENT '后一周的id'
)
WITH
	(orientation = column, COMPRESSION = NO) DISTRIBUTE BY replication;
