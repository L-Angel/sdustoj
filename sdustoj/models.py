from __future__ import unicode_literals
__author__ = 'Lonely'


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Activation(models.Model):
    user_id = models.CharField(max_length=50)
    code = models.CharField(primary_key=True, max_length=200)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activation'


class Collections(models.Model):
    col_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=30)
    title = models.CharField(max_length=300)
    description = models.TextField()
    cnt = models.IntegerField()
    div = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'collections'


class CollectionsProblem(models.Model):
    idx = models.AutoField(primary_key=True)
    col_id = models.IntegerField()
    pid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'collections_problem'


class Compileinfo(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compileinfo'


class Contest(models.Model):
    contest_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    defunct = models.CharField(max_length=1)
    points = models.TextField(blank=True, null=True)
    private = models.IntegerField()
    langmask = models.IntegerField()
    contest_mode = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'contest'

class ContestPrivilege(models.Model):
    privilege_id = models.AutoField(primary_key=True)
    privilege = models.CharField(max_length=45, blank=True, null=True)
    private_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contest_privilege'


class ContestProblem(models.Model):
    problem_id = models.IntegerField()
    contest_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contest_problem'

class ContestUsers(models.Model):
    user_id = models.CharField(max_length=20)
    contest_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contest_users'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Loginlog(models.Model):
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=40, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loginlog'


class Mail(models.Model):
    mail_id = models.AutoField(primary_key=True)
    to_user = models.CharField(max_length=20)
    from_user = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    new_mail = models.IntegerField()
    reply = models.IntegerField(blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mail'


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'news'


class Online(models.Model):
    hash = models.CharField(primary_key=True, max_length=32)
    ip = models.CharField(max_length=20)
    ua = models.CharField(max_length=255)
    refer = models.CharField(max_length=255, blank=True, null=True)
    lastmove = models.IntegerField()
    firsttime = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online'


class Privilege(models.Model):
    user_id = models.CharField(max_length=20)
    rightstr = models.CharField(max_length=30)
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'privilege'


class Problem(models.Model):
    problem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    input = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)
    sample_input = models.TextField(blank=True, null=True)
    sample_output = models.TextField(blank=True, null=True)
    spj = models.CharField(max_length=1)
    hint = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    defunct = models.CharField(max_length=1)
    accepted = models.IntegerField(blank=True, null=True)
    submit = models.IntegerField(blank=True, null=True)
    solved = models.IntegerField(blank=True, null=True)
    fileupload = models.CharField(max_length=1,default='N')
    class Meta:
        managed = False
        db_table = 'problem'


class Reply(models.Model):
    rid = models.AutoField(primary_key=True)
    author_id = models.CharField(max_length=20)
    time = models.DateTimeField()
    content = models.TextField()
    topic_id = models.IntegerField()
    status = models.IntegerField()
    ip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'reply'


class Runtimeinfo(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runtimeinfo'


class Sim(models.Model):
    s_id = models.IntegerField(primary_key=True)
    sim_s_id = models.IntegerField(blank=True, null=True)
    sim = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim'


class Solution(models.Model):
    solution_id = models.AutoField(primary_key=True)
    problem_id = models.IntegerField()
    user_id = models.CharField(max_length=20)
    time = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    result = models.SmallIntegerField(blank=True, null=True)
    language = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=15,blank=True, null=True)
    contest_id = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    code_length = models.IntegerField(blank=True, null=True)
    judgetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solution'


class SourceCode(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    source = models.TextField()

    class Meta:
        managed = False
        db_table = 'source_code'


class Topic(models.Model):
    tid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    status = models.IntegerField()
    top_level = models.IntegerField()
    cid = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField()
    author_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'topic'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=100, blank=True, null=True)
    submit = models.IntegerField(blank=True, null=True)
    solved = models.IntegerField(blank=True, null=True)
    defunct = models.CharField(max_length=1)
    ip = models.CharField(max_length=20)
    accesstime = models.DateTimeField(blank=True, null=True)
    volume = models.IntegerField()
    language = models.IntegerField()
    password = models.CharField(max_length=32, blank=True, null=True)
    reg_time = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    nick = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    activated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'

class Status(models.Model):
    result_id = models.IntegerField()
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    language = models.IntegerField(blank=True, null=True)
    language_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'



class Statusinfo(models.Model):
    solution_id = models.AutoField(primary_key=True)
    problem_id = models.IntegerField()
    user_id = models.CharField(max_length=20)
    time = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    language = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=15,blank=True, null=True)
    contest_id = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    code_length = models.IntegerField(blank=True, null=True)
    judgetime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    language_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'statusinfo'


class Contestinfo(models.Model):
    privilege = models.CharField(max_length=45, blank=True, null=True)
    contest_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    defunct = models.CharField(max_length=1)
    points = models.TextField(blank=True, null=True)
    langmask = models.IntegerField()
    contest_mode = models.IntegerField()
    language=models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        db_table = 'contestinfo'
