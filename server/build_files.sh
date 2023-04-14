echo "BUILD START"
yum update
yum clean all
yum install mysql-community-client -y
pip install -r requirements.txt
pip install --upgrade pip
pip install django-allauth
pip install django-widget-tweaks
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"