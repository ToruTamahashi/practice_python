/*
docker-compose exec db sh
mysql -u root -p
use test_db;
*/

-- 全カラム取得
select * from task;

-- idカラムのみ取得
select id from task;

-- idとname を取得
select id, name from task;

-- 表示する際のカラム名を変更 as
select id as aa, name as bb from task;

-- カラムに対し演算を行って表示
select id , val , val * 1.10 as tax from task;

-- 条件を指定して取得 where
select id, name, val from task where val >= 80;

/*
演算子の種類　「=」「>」「<」「!=」「in」「not in」「is null」「in not null」「like」「between and」
 */
-- id が 1か3の行を取得 in
select id, name, val from task where id in(1,3);

-- valがnull以外の行を取得
select id, name, val from task where val is not null;

-- valが10~82の行を取得
select id, name, val from task where val between 10 and 82;
select id, name, val from task where val >= 10 and val <= 82;

-- valが90か100の行を取得
select id, name, val from task where val = 90 or val = 100;

/*
あいまい検索 like
ワイルドカード
% : 0文字以上の任意の文字列
_ : 任意の一文字

例）
1, '中%' -> '中'で始まる文字列
2, '%中%' -> '中'を含む文字列
3, '%子' -> '子'で終わる文字列
4, '__子' -> 何かしらの2文字から始まり'子'で終わる文字列
*/
-- commentがaから始まる行を取得 like
select * from task where comment like 'a%';


-- 取得件数を制限する limit
-- 頭から最大三件取得
select * from task limit 3;
select * from task limit 0, 3;

-- 3行目から3行取得（0から数えるので3行目は2）
select * from task limit 2, 3;