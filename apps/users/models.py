# ~*~ coding: utf-8 ~*~

from __future__ import unicode_literals

import datetime
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.db import OperationalError


class Role(models.Model):
    name = models.CharField('name', max_length=80, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name='permissions',
        blank=True,
    )
    date_added = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    comment = models.CharField(max_length=80, blank=True)

    def __unicode__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        if self.user_set.all().count() > 0:
            raise OperationalError('Role %s has some member, should not be delete.' % self.name)
        else:
            return super(Role, self).delete(using=using, keep_parents=keep_parents)

    class Meta:
        db_table = 'role'

    @classmethod
    def initial(cls):
        roles = {
            'Administrator': {'permissions': Permission.objects.all(), 'comment': '管理员'},
            'User': {'permissions': [], 'comment': '用户'},
            'Auditor': {'permissions': Permission.objects.filter(content_type__app_label='audits'),
                        'comment': '审计员'},
        }

        for role_name, props in roles.items():
            if not cls.objects.filter(name=role_name):
                role = cls.objects.create(name=role_name, comment=props.get('comment', ''), created_by='System')
                if props.get('permissions'):
                    role.permissions = props.get('permissions')


class UserGroup(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='组名称')
    comment = models.TextField(blank=True, verbose_name='描述')
    date_added = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'usergroup'

    @classmethod
    def initial(cls):
        group_or_create = cls.objects.get_or_create(name='Default', comment='Default user group for all user',
                                                    created_by='System')
        return group_or_create[0]

    @classmethod
    def generate_fake(cls, count=100):
        from random import seed, randint, choice
        import forgery_py
        from django.db import IntegrityError

        seed()
        for i in range(count):
            group = cls(name=forgery_py.name.full_name(),
                        comment=forgery_py.lorem_ipsum.sentence(),
                        created_by=choice(User.objects.all()).username
                    )
            try:
                group.save()
            except IntegrityError:
                print('Error continue')
                continue


def date_expired_default():
    return timezone.now() + timezone.timedelta(days=365 * 70)


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    name = models.CharField(max_length=20, blank=True, verbose_name='姓名')
    email = models.EmailField(max_length=30, unique=True, verbose_name='邮件')
    groups = models.ManyToManyField(UserGroup, verbose_name='用户组')
    avatar = models.ImageField(upload_to="avatar", verbose_name='头像')
    wechat = models.CharField(max_length=30, blank=True, verbose_name='微信')
    phone = models.CharField(max_length=20, blank=True, verbose_name='手机号')
    enable_otp = models.BooleanField(default=False, verbose_name='启用二次验证')
    secret_key_otp = models.CharField(max_length=16, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET('None'), verbose_name='角色')
    private_key = models.CharField(max_length=5000, blank=True, verbose_name='ssh私钥')  # ssh key max length 4096 bit
    public_key = models.CharField(max_length=1000, blank=True, verbose_name='公钥')
    comment = models.TextField(max_length=200, blank=True, verbose_name='描述')
    date_expired = models.DateTimeField(default=date_expired_default, verbose_name='有效期')
    created_by = models.CharField(max_length=30, default='')

    @property
    def password_raw(self):
        raise AttributeError('Password raw is not readable attribute')

    #: Use this attr to set user object password, example
    #: user = User(username='example', password_raw='password', ...)
    #: It's equal:
    #: user = User(username='example', ...)
    #: user.set_password('password')
    @password_raw.setter
    def password_raw(self, raw_password):
        self.set_password(raw_password)

    def is_expired(self):
        if self.date_expired > timezone.now():
            return False
        else:
            return True

    def save(self, *args, **kwargs):
        # If user not set name, it's default equal username
        if not self.name:
            self.name = self.username
        super(User, self).save(*args, **kwargs)
        # Set user default group 'All'
        # Todo: It's have bug
        group = UserGroup.initial()
        if group not in self.groups.all():
            self.groups.add(group)
            # super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user'

    #: Use this method
    @classmethod
    def initial(cls):
        user = cls(username='admin',
                   email='admin@jumpserver.org',
                   name='Administrator',
                   password_raw='admin',
                   role=Role.objects.get(name='Administrator'),
                   comment='Administrator is the super user of system',
                   created_by='System')
        user.save()
        user.groups.add(UserGroup.initial())

    @classmethod
    def generate_fake(cls, count=100):
        from random import seed, choice
        import forgery_py
        from django.db import IntegrityError

        seed()
        for i in range(count):
            user = cls(username=forgery_py.internet.user_name(True),
                       email=forgery_py.internet.email_address(),
                       name=forgery_py.name.full_name(),
                       password=make_password(forgery_py.lorem_ipsum.word()),
                       role=choice(Role.objects.all()),
                       wechat=forgery_py.internet.user_name(True),
                       comment=forgery_py.lorem_ipsum.sentence(),
                       created_by=choice(cls.objects.all()).username,
                    )
            try:
                user.save()
            except IntegrityError:
                print('Duplicate Error, continue ...')
                continue
            user.groups.add(choice(UserGroup.objects.all()))
            user.save()


def init_all_models():
    for model in (Role, UserGroup, User):
        if hasattr(model, 'initial'):
            model.initial()


def generate_fake():
    for model in (Role, UserGroup, User):
        if hasattr(model, 'generate_fake'):
            model.generate_fake()
