echo "BUILD START"
cat /etc/*-release
apt update
apt-get update 
apt-get clean 
apt-get install -y libpq-dev gcc
apt-get update
apt-get -y install gcc libmariadb-dev mariadb-client
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"