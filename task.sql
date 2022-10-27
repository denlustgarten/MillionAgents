-- выбрать всех пользователей (user_id), которые впервые создали отчет в 2021-м году, 
-- и подсчитать сумму вознаграждений (reward) за 2022-й год в одном запросе.

DROP TABLE IF EXISTS reports_t;
CREATE TABLE reports_t
(
    id int PRIMARY KEY,
    user_id int,
    reward int,
    created_at timestamp without time zone
)

insert into reports_t values (17,100,12,'2022-06-04 18:24:54');
insert into reports_t values (1,17,12,'2009-06-04 18:24:54');
insert into reports_t values (2,11,12,'2009-06-04 18:24:54');

insert into reports_t values (4,8,12,'2009-06-04 18:24:54');
insert into reports_t values (5,8,12,'2009-06-04 18:24:54');

insert into reports_t values (6,9,12,'2021-06-04 18:24:54');
insert into reports_t values (3,9,12,'2022-06-04 18:24:54');
insert into reports_t values (8,9,12,'2022-06-04 18:24:54');

insert into reports_t values (7,53,12,'2009-06-04 18:24:54');

insert into reports_t values (9,14,12,'2021-05-04 18:24:54');
insert into reports_t values (10,14,12,'2022-05-04 18:24:54');
insert into reports_t values (11,14,12,'2022-05-04 18:24:54');
insert into reports_t values (111,14,100,'2022-05-04 18:24:54');
insert into reports_t values (12,14,12,'2021-05-04 18:24:54');

insert into reports_t values (13,19,12,'2021-05-04 18:24:54');
insert into reports_t values (14,19,12,'2022-05-04 18:24:54');
insert into reports_t values (15,19,12,'2021-05-04 18:24:54');
insert into reports_t values (16,19,12,'2000-05-04 18:24:54');



SELECT rt.user_id, SUM(rt.reward)
FROM reports_t rt
JOIN (	SELECT * 
		FROM (SELECT min(date_part('year', r.created_at)) as min_year, r.user_id
				FROM reports_t r
				GROUP BY r.user_id) as first_report_y
		WHERE min_year = 2021) as first_report_2021
ON rt.user_id = first_report_2021.user_id
WHERE date_part('year', rt.created_at) = 2022
GROUP BY rt.user_id


-- использовав агрегатные функции, выбрать все шк и цены (reports.barcode, reports.price) 
-- с одинаковыми названиями точек продаж (pos.title)

DROP TABLE IF EXISTS pos;
CREATE TABLE pos
(
    id int PRIMARY KEY,
    title character varying
)

DROP TABLE IF EXISTS reports;
CREATE TABLE reports
(
    id int PRIMARY KEY,
    barcode character varying,
    price float,
    pos_id int
)

insert into pos values (1, 'aaa');
insert into pos values (2, 'bbb');
insert into pos values (3, 'vvv');
insert into pos values (4, 'aaa');
insert into pos values (5, 'ttt');
insert into pos values (6, 'bbb');


insert into reports values (1, 'code_1', 1.12, 1);
insert into reports values (2, 'code_2', 1.12, 2);
insert into reports values (3, 'code_3', 1.12, 1);
insert into reports values (4, 'code_1', 1.12, 1);
insert into reports values (5, 'code_5', 1.12, 3);
insert into reports values (6, 'code_6', 1.12, 1);
insert into reports values (7, 'code_7', 1.12, 1);
insert into reports values (8, 'code_8', 1.12, 4);
insert into reports values (9, 'code_8', 1.12, 4);


SELECT *
FROM 
	(SELECT COUNT(*) as cnt, t.barcode, t.price, t.title
	FROM (SELECT * 
			FROM reports r 
			JOIN pos p ON r.pos_id = p.id) as t
	GROUP BY t.barcode, t.price, t.title) as p
WHERE p.cnt > 1








