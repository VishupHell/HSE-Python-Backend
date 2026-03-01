docker build -t my_first_django_project .
docker run -d -p 9000:5432 --name my_first_django_project my_first_django_project