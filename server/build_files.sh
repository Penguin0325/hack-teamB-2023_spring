echo "BUILD START"
yum update
yum clean all
yum install -y libpq-dev gcc
yum install --upgrade pip setuptools
yum -y install gcc libmariadb-dev mariadb-client
pip install -r requirements.txt
pip install --upgrade pip
pip install django-allauth
pip install django-widget-tweaks
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"