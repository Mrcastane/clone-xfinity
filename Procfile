web: gunicorn a_xfinityclone.wsgi
release: |
  python manage.py collectstatic --noinput
  python manage.py migrate --noinput
