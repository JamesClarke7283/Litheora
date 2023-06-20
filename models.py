from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    hashed_password = fields.CharField(max_length=255)
    attributes = fields.JSONField()

    site = fields.ForeignKeyField('models.Site', related_name='users')


class Site(Model):
    id = fields.IntField(pk=True)
    attributes = fields.JSONField()
    host = fields.CharField(max_length=255)
    db_string = fields.CharField(max_length=255)


class Image(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    path = fields.CharField(max_length=255)


class Tile(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    url = fields.CharField(max_length=255)

    icon = fields.ForeignKeyField('models.Image', related_name='tiles', null=True)


class BlockType(Model):
    id = fields.IntField(pk=True)
    template_path = fields.CharField(max_length=255)

    tile = fields.ForeignKeyField('models.Tile', related_name='block_types')


class Block(Model):
    id = fields.IntField(pk=True)
    attributes = fields.JSONField()

    type = fields.ForeignKeyField('models.BlockType', related_name='blocks')
    parent = fields.ForeignKeyField('models.Block', related_name='inner_blocks', null=True)
    page = fields.ForeignKeyField('models.Page', related_name='blocks', null=True)


class Page(Model):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=255)
    attributes = fields.JSONField()

    site = fields.ForeignKeyField('models.Site', related_name='pages')
