-- 内部結合 inner join
/**
 顧客一覧を取得したい
 都道府県idで出力されてもよくわからないので、都道府県名も表示してほしい
 */
select
    users.id,
    users.last_name,
    users.first_name,
    prefectures.name
from
    users
inner join
    prefectures
on users.prefecture_id = prefectures.id;
 /*
  inner join 構文
  select
    テーブル1.列名,
    テーブル2.列名...
  from
    テーブル名1
  inner join
    テーブル名2
  on テーブル名1.列名 = テーブル名2.列名
 */