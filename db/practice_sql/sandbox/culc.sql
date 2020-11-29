-- 絶対値を求める
select abs(-10);

-- 四捨五入 round
/*
    まるめ
    小数第一位 round(10.555,0) -> 11
    小数第二位 round(10.555,1) -> 10.6
 */
 -- 商品一覧を税込み価格も含めて取得ただし、小数第一位で四捨五入
 select id, name, round(price * 1.08, 1) from products;


-- 文字列の連結 concat
-- ユーザ一覧を苗字 + スペース + 名前 + さん　のフォーマットで出力する
select concat(last_name,'',first_name,'さん') from users;



-- 今日の日付、時刻の取得
select current_date();
select current_time();
select current_timestamp();

-- n日後の日付
select current_date() + interval 3 day;
-- n日前の日付
select current_date() - interval 3 day;
--　x時間後の時刻
select current_time () + interval 6 hour;
