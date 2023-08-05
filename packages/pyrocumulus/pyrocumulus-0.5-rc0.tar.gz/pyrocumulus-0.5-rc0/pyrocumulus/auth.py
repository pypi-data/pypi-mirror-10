# -*- coding: utf-8 -*-

import uuid
from tornado import gen
from mongomotor import Document
from mongomotor.fields import ReferenceField, StringField, ListField
from pyrocumulus.utils import bcrypt_string, fqualname


# Models for basic auth
class AccessToken(Document):
    name = StringField()
    token = StringField(required=True)
    domains = ListField()

    def generate_token(self):
        token = str(uuid.uuid4())
        return token

    @classmethod
    @gen.coroutine
    def get_by_token(cls, token):
        bcrypt_token = bcrypt_string(token)
        access_token = yield cls.objects.get(token=bcrypt_token)
        return access_token

    @gen.coroutine
    def save(self):
        if not self.token:
            token = self.generate_token()
            self.token = bcrypt_string(token)
        yield super(AccessToken, self).save()
        return token

    @gen.coroutine
    def get_perms(self, model):
        """ Returns the permissions for this token
        on a given model
        :param model: mongomotor.Document instance or fqualname
        """

        if not isinstance(model, str):
            model = fqualname(model)

        perms = Permission.objects.filter(access_token=self, model=model)
        perms_list = []
        for perm in (yield perms.to_list()):
            perms_list.append(perm.perms)

        perms = set(perms_list)
        return perms

    @gen.coroutine
    def has_write_perm(self, model):
        perms = yield self.get_perms(model)
        return 'w' in perms or 'rw' in perms

    @gen.coroutine
    def has_read_perm(self, model):
        perms = yield self.get_perms(model)
        return 'r' in perms or 'rw' in perms


class Permission(Document):
    access_token = ReferenceField(AccessToken, required=True)
    # model is pyrocumulus.utils.fqualname(ModelClass)
    model = StringField(required=True)
    # perms are 'r', 'w' or 'rw'
    perms = StringField(required=True)

    @classmethod
    @gen.coroutine
    def create_perms_to(cls, access_token, model, perms):
        """ Creates a Permission instance to ``token`` related to ``model``.
        :param access_token: AccessToken instance
        :param model: class or fqualname
        :param perms: perms to apply ('r', 'w', 'rw')
        """

        if not isinstance(model, str):
            model = fqualname(model)

        perms = cls(access_token=access_token, model=model, perms=perms)
        yield perms.save()
        return perms
