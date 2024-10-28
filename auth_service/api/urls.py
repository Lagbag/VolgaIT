from django.urls import path, include

# and also CASCADE on delete, there're linked models in timetable_microservice!

app_name = 'api'

urlpatterns = [
    path("Authentication", include('api.authentication.urls')),
    path("Accounts", include('api.accounts.urls')),
    path("Doctors", include('api.doctors.urls')),
]
