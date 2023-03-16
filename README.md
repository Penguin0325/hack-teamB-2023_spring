# hack-teamB-2023-spring

### 使い方
```
docker compose up -d
docker compose exec server /bin/bash
./mahou.sh
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### 使用しているライブラリ
- フロントエンド
    - vue.js
- バックエンド
    - python(フレームワークDjango)

### DB
ユーザーログイン
|項目	|データ型	| 説明|
|---|---|---|
|ユーザーID	|数値型(INT)|	 ログインIDとひとまとめにしてしまう場合もあります。|
|ユーザー名	|	||
|ログインID	|固定長(VARCHAR)	| ユニーク制約をかける。|
|パスワード	|VARCHAR|	 平文ではなく、暗号化関数等でハッシュ化した値を入れます。|
|作成日	|DATE|	レコード挿入日を入れる。|
|更新日	|DATE|	レコード更新日を入れる。|
|削除日	|DATE|	ここに日付が入っているレコードは論理削除されたとみなす。|

テーブル名　user
カラム id int, name varchar(20), loginID varchar(20) unique, password varchar(20), createDate date, updateDate date, deleteDate date

### アイコン

|項目	|データ型	| 説明|
|---|---|---|
|ファイルパス|||
|ID|||
|名前|||

テーブル名　icon
カラム id int, filepass text, iconName varchar(20)

