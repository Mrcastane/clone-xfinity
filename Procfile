web: gunicorn a_xfinityclone.wsgi
release: sh -c "python manage.py collectstatic --noinput && python manage.py migrate --noinput"