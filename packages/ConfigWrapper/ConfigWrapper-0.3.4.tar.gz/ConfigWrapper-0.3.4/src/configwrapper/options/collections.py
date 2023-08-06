from configwrapper import ValidationError
from configwrapper.options import ConfigOption

__author__ = 'Lai Tash (lai.tash@yandex.ru)'


class ListOption(ConfigOption):
    def __init__(self, option, *args, **kwargs):
        self.option = option
        if isinstance(option, type):
            self.option = option()
        super(ListOption, self).__init__(*args, **kwargs)

    def deserialize(self, string_, instance):
        result = []
        items = map(str.strip, string_.split(','))
        for item in items:
            self.option.validate(instance, item)
            value = self.option.deserialize(item, instance)
            self.option._validate_value(value)
            result.append(value)
        return result

    def serialize(self, value, instance):
        value = [self.option.serialize(v, instance) for v in value]
        for item in value:
            self.option.validate(instance, item)
        return ', '.join(value)

    def _validate_value(self, value):
        if not isinstance(value, list):
            raise ValidationError('list expected')

    def _validate_serialized(self, string_):
        pass