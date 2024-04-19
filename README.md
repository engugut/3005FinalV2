Install latest version of python

Install pip

if linux (maybe windows?):
(
cd to empty directory
python -m venv .venv
. .venv/bin/activate
)

pip install psycopg2-binary

make sure environment has psycopg installed and postgresql server is running with lax permissions

python sql.py

edit psycopg2.connect to match your database postgresql
