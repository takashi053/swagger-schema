from .lib.serializer import SerializableObject
from jsonschema.validators import Draft4Validator


class JsonSchemaObject(dict, SerializableObject):

    def __init__(self, *args, **kwargs):
        super(self).__init__(*args, **kwargs)
        Draft4Validator.validate(self)

    def dump(self):
        return dict(self)

    @classmethod
    def load(cls, value):
        return cls(**value)
