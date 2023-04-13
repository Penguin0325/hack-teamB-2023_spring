echo "BUILD START"
yum update
yum clean all
yum install -y libpq-dev gcc
yum -y install gcc libmariadb-dev mariadb-client
python -m pip install -U pip
pip install upgrade setuptools
pip install -r requirements.txt
pip install --upgrade pip
pip install django-allauth
pip install django-widget-tweaks
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"