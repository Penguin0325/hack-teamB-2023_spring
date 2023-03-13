from django.db import models

class TestModel(models.Model):
    # """ user_dataテーブルへアクセスするためのモデル """
 
    # テーブル名を存在するuser_dataテーブルに変更する
    class Meta:
        db_table = 'drink'
 
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    
    
