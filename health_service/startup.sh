python manage.py makemigrations ;
python manage.py migrate ;
python manage.py migrate api zero --fake ;
python manage.py migrate api ;

python manage.py grpcrunserver 127.0.0.1:$GRPC_PORT_HOSPITAL &
gunicorn health_service.wsgi --bind=0.0.0.0:8082
