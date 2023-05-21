import uuid
from django.db import models
# from django.contrib.auth.models import User

from django.utils import timezone 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# from django.contrib.auth.models import User
# from django_mysql.models import ListCharField
# class TestModel(models.Model):
#     # """ user_dataテーブルへアクセスするためのモデル """

#     # テーブル名を存在するuser_dataテーブルに変更する
#     class Meta:
#         db_table = 'drink'

#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=40)


class UserManager(BaseUserManager):
    def create_user(self, loginID, password=None):
        if not loginID:
            raise ValueError('Users must have an loginID address')

        user = self.model(
            loginID=self.normalize_email(loginID),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, loginID, password):
        user = self.create_user(
            loginID,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, loginID, password):
        user = self.create_user(
            loginID,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# id int, name varchar(20), loginID varchar(20) unique, password varchar(20), createDate date, updateDate date, deleteDate date


class User(AbstractBaseUser):
    class Meta:
        db_table = 'userScertification'

    name = models.CharField(max_length=500)
    loginID = models.CharField(max_length=20, unique=True)
    createDate = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    # towns = ListCharField(
    #     models.CharField(max_length=10),size=6, max_length=(6 * 11))

    USERNAME_FIELD = 'loginID'
    objects = UserManager()

    def __str__(self):
        return self.loginID

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

class ImageUpload(models.Model):
    class Meta:
        db_table = 'images'
    title = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to="images")  # こちらの通り

    def __str__(self):
        return self.title
    
class ImageConnectModels(models.Model):
    user = models.IntegerField()
    icon = models.IntegerField()
    is_published = models.IntegerField()

    class Meta:
        db_table = 'imagesconnnect'
        constraints = [
            models.UniqueConstraint(fields=['user', 'icon', 'is_published'], name='unique_constraint')
        ]

class Post(models.Model):
    images_id = models.ForeignKey("User", on_delete=models.CASCADE)


# class ImagesModel(models.Model):
#     class Meta:
#         db_table = 'images'
#     title = models.CharField(max_length=100)
#     img = models.ImageField(upload_to="images")


class UserPostList(models.Model):
    posts = models.ForeignKey("Post", on_delete=models.CASCADE)
    images = models.ForeignKey("ImageUpload", on_delete=models.CASCADE)

class RoomModels(models.Model):
    class Meta:
        db_table = 'rooms'
    id = models.AutoField(primary_key=True)
    # id = models.AutoField(primary_key=True,default=uuid.uuid4,editable=False)
    roomname = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_datetime = models.DateTimeField(auto_now=True)

class MessageModels(models.Model):
    class Meta:
        db_table = 'messages'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(
        RoomModels, null=True, on_delete=models.CASCADE
    )
    contest = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)


# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.IntegerField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     stores = models.ManyToManyField("Store")

# class UserModel(models.Model):
#     class Meta:
#         db_table = 'user'

#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     loginID = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     createDate = models.DateField(auto_now_add=True)
#     updateDate = models.DateField(auto_now=True)
#     deleteDate = models.DateField()
# class ImgStatus(models.Model):
#     class Meta:
#         db_table = 'image_status'
#     id = models.IntegerField()


# class Photo(models.Model):
#     class Meta:
#         db_table = 'photo'
#     image = models.ImageField(upload_to='images/', verbose_name="画像", )
