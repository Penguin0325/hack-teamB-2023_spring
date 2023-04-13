echo "BUILD START"
cat /etc/*-release 
yum clean 
yum install -y libpq-dev gcc
yum update
yum -y install gcc libmariadb-dev mariadb-client
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"