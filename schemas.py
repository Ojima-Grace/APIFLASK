from dataclasses import fields
import imp
from importlib.resources import contents
from apiflask.schemas import Schema
from apiflask import fields

class TaskOutputSchema(Schema):
    id = fields.Integer()
    content = fields.String()
    date_added = fields.DateTime()
    is_completed = fields.Boolean()

class TaskCreatesSchema(Schema):
    content = fields.String(required=True)

class TaskUpdateSchema(Schema):
    content = fields.String(required=True)
    is_complete = fields.Boolean(required=True)