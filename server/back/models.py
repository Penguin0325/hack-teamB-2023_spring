from django.db import models

class TestModel(models.Model):
    # """ user_dataテーブルへアクセスするためのモデル """
 
    # テーブル名を存在するuser_dataテーブルに変更する
    class Meta:
        db_table = 'drink'
 
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    

# id int, name varchar(20), loginID varchar(20) unique, password varchar(20), createDate date, updateDate date, deleteDate date
class UserModel(models.Model):
    class Meta:
        db_table = 'user'
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    loginID = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    deleteDate = models.DateField()

# # id int, filepath text, iconName varchar(20)
class PhotoModel(models.Model):
    class Meta:
        db_table = 'icon'
    id = models.IntegerField(primary_key=True)
    filepath = models.TextField()
    iconName = models.CharField(max_length=20)

class ImageUpload(models.Model):
    class Meta:
        db_table = 'image'
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images")#こちらの通り

    def __str__(self):
        return self.title


# class Photo(models.Model):
#     class Meta:
#         db_table = 'photo'
#     image = models.ImageField(upload_to='images/', verbose_name="画像", )

