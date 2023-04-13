echo "BUILD START"
yum update
yum clean
yum install -y libpq-dev gcc
yum -y install gcc libmariadb-dev mariadb-client
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"