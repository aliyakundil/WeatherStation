# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Archive(models.Model):
    year = models.IntegerField(blank=True, null=True)
    january = models.IntegerField(blank=True, null=True)
    february = models.IntegerField(blank=True, null=True)
    march = models.IntegerField(blank=True, null=True)
    april = models.IntegerField(blank=True, null=True)
    may = models.IntegerField(blank=True, null=True)
    june = models.IntegerField(blank=True, null=True)
    july = models.IntegerField(blank=True, null=True)
    august = models.IntegerField(blank=True, null=True)
    september = models.IntegerField(blank=True, null=True)
    october = models.IntegerField(blank=True, null=True)
    november = models.IntegerField(blank=True, null=True)
    december = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archive'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Before7DaysLater3Months(models.Model):
    date = models.DateField(blank=True, null=True)
    from_0_before_6 = models.IntegerField(blank=True, null=True)
    from_6_before_12 = models.IntegerField(blank=True, null=True)
    from_12_before_18 = models.IntegerField(blank=True, null=True)
    from_18_before_24 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'before_7_days_later_3_months'


class Bmp(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bmp'


class Dht(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dht'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Email(models.Model):
    user_name = models.CharField(max_length=50, blank=True, null=True)
    pass_field = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'


class MobileWeatherStations(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    testimony = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobile_weather_stations'


class New7DaysDailyData(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    testimony = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_7_days_daily_data'


class Sensors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensors'


class Server(models.Model):
    id_server = models.IntegerField()
    name_system = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server'


class Settings(models.Model):
    poplib = models.CharField(max_length=30, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class Water(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    characteristic = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'water'


class WeatherappCity(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'weatherapp_city'


class WeatherappMetcast(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'weatherapp_metcast'
