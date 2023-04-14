echo "BUILD START"
yum update
yum clean all
easy_install -U pip
pip install --upgrade pip
pip install -upgrade pip setuptools
yum install MariaDB-server galera-4 MariaDB-client MariaDB-shared MariaDB-backup MariaDB-common git python3 python3-virtualenv make gcc gettext
pip install -r requirements.txt
pip install django-allauth
pip install django-widget-tweaks
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"