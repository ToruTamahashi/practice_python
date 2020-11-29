/**
集約関数

記述順序（必ずこの順序で書くこと）
1. select
2. from
3. where
4. group by
5. having
6. order by
7. limit

 実行順序
 1. from
 2. where
 3. group by
 4. having
 5. select
 6. order by
 7. limit
 */

-- 復習
-- 1月の売上を取得
select * from orders where order_time >= '2017-01-01 00:00:00' and order_time < '2017-02-01 00:00:00';

 -- 合計値 sum
 -- ordersテーブルから1月の売り上げの合計値を求める
select sum(amount) from orders where order_time >= '2017-01-01 00:00:00' and order_time < '2017-02-01 00:00:00';

-- 平均値 avg
-- products テーブルから商品の平均価格を求める
select avg(price) from products;

-- 最小値 min
-- products テーブルから商品価格の最小値を求める
select min(price) from products;

-- 最大値 max
-- products テーブルから商品価格の最大値を求める
select max(price) from products;


-- 行数を数える count
-- users テーブルからユーザ数を求める
select count(*) from users;
-- 女性ユーザ数を求める
select count(*) from users where gender = 2;
-- access_logテーブルから1月1日にアクセスしたユーザ数を求める（同ユーザの複数回アクセスはカウントしない）
-- count(distinct)で重複を排除して計算する
select count(distinct user_id) from access_logs where request_month = '2017-01-01';


-- グループ化 group_by
-- usersテーブルから都道府県idごとのユーザ数を求める
/*
 処理イメージ
 1. group by でprefecture_idごとにグループを作る
 2. グループごとにselect文を実行し、行数をカウント
 */
select prefecture_id, count(*) from users group by prefecture_id;


-- 集約結果をさらに絞り込む having
-- access_logsテーブルから,2017年の月間利用ユーザ数が630人以上の月を取得する
/**
 処理イメージ　
 whereで2017年のアクセスログのみ取得
 group by で月ごとにグループ化
 having で行数が630以上のグループのみ絞り込み
 select で結果を取得
 */
select request_month, count(distinct user_id) from access_logs where request_month >= '2017-01-01' and request_month < '2018-01-01' group by request_month having count(distinct user_id) >= 630;


-- 並べ替え order by
-- productsテーブルから商品の価格が高い順に一覧表示
/*
    並び順の指定
    asc : 昇順（デフォルト）
    desc : 降順
 */
select * from products order by price desc;

-- 複数条件で並び替え
-- 商品一覧を価格が高い順に並べ替え、価格が同じときは、登録順（products.idが小さい順）に並び替える
select * from products order by price desc, id asc;