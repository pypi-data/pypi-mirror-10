__author__ = 'plasmashadow'

try:
    from pymongo.dbref import DBRef
    from pymongo.objectid import ObjectId
except ImportError:
    from bson.dbref import DBRef
    from bson.objectid import ObjectId

from datetime import datetime
import json


class EmptyProperty(Exception):
    pass

class Property(object):
    """
      This is used to store the data on to mongodb as mongo friendly values
      and recive it as like application friendly values.
    """
    _value_type = None

    def __init__(self, value_type=None, **kwargs):
        """
         Constructor used to invoke Field Objects
        :param value_type:
        :param kwargs:
        :return:
        """
        self._value_type = value_type or self._value_type
        self._required = kwargs.get("required", False) or False
        if "default" in kwargs:
            self.default = kwargs["default"]
        _set_callback = getattr(self, "_set_callback", None)
        _get_callback = getattr(self, "_get_callback", None)
        _force_callback = getattr(self, "_force_callback", None)

        self._set_callback = kwargs.get("_set_callback", _set_callback)
        self._get_callback = kwargs.get("_get_callback", _get_callback)
        self._force_callback = kwargs.get("_force_callback", _force_callback)
        #used to index the field
        self._id = id(self)
        self._field_name = kwargs.get("field_name", None)

    def __get__(self, instance, owner):
        """
          Getter for the Field Class
        :param instance:
        :param owner:
        :return:
        """
        if instance is None:
            return self
        value = self._get_value(instance)
        return value

    def _get_field_name(self, model_object):
        if self._field_name:
            return self._field_name
        fields = getattr(model_object, "_fields")
        return fields[self._id]

    def _get_value(self, instance):
        """
         Used to get the value from the instance
        :param instance: Model instance of type dict
        :return:
        """
        field_name = self._get_field_name(instance)
        # print "field name is ",field_name
        value = None
        if not field_name in instance:
            if self._required:
                raise EmptyProperty(self.__class__.__name__ +"Should not be empty")
            self._set_default(instance, field_name)
        value = instance.get(field_name)
        if self._get_callback(instance, value):
            value = self._get_callback(instance, value)
        return value

    def _set_default(self, model, field):
        if field in model:
            return
        default_value = None
        if hasattr(self, "default"):
            if not callable(self.default):
                default_value = self.default
            else:
                default_value = self.default()
        setattr(model, field, default_value)

    def _check_value_types(self, value, field_name):
        """
        Used to check whether the given value matches the given field type
        :param value:
        :param field_name:
        :return:
        """
        if not value and not self._value_type:
            flag = isinstance(value, self._value_type)
            if not flag:
                value_type = type(value)
                raise TypeError("Invalid type for %s for %s field" %(self._value_type, field_name))

    def __set__(self, instance, value):
        """
        Set the value to the model
        :param instance:
        :param value:
        :return:
        """
        field_name = self._get_field_name(instance)
        # print "field name is ", field_name
        try:
            self._check_value_types(value, field_name)
        except TypeError as e:
            if not self._force_callback:
                raise
            value = self._force_callback(value)
            self._check_value_types(value, field_name)

        if self._set_callback:
            value = self._set_callback(instance, value)

        instance[field_name] = value


class ReferenceProperty(Property):
    """
    This Property is used to Hold other property
    """
    def __init__(self, model, **kwargs):
        super(ReferenceProperty, self).__init__(model, **kwargs)
        self.model = model

    def _get_callback(self, instance, value):
        if value:
            return self.model.find_one({"_id": value._id})
        return value

    def _set_callback(self, instance, value):
        if value:
            value = DBRef(self.model._get_name(), value._id)
        return value



class StringProperty(Property):

    def __init__(self, *args, **kwargs):
        super(StringProperty, self).__init__(str, *args, **kwargs)

    def _get_callback(self, instance, value):
        return str(value)

    def _set_callback(self, instance, value):
        return str(value)

class IntegerProperty(Property):

    def __init__(self, *args, **kwargs):
        super(IntegerProperty, self).__init__(int, *args, **kwargs)

    def _get_callback(self, instance, value):
        return int(value)

    def _set_callback(self, instance, value):
        if not value:
            return str(value)
        return int(value)

class DateTimeProperty(Property):

    def __init__(self, *args, **kwargs):
        super(DateTimeProperty, self).__init__(datetime, *args, **kwargs)
        self.auto_add = kwargs.get("auto_add", False)
        self.utc = kwargs.get("utc", True)

    def _get_callback(self, instance, value):
        if not isinstance(value, datetime):
            raise TypeError("Should be a python datetime object")
        return value

    def _set_callback(self, instance, value):
        if not value and not self.auto_add:
            raise TypeError("Invalid datetime object")
        if self.auto_add:
            value = datetime.utcnow() if self.utc else datetime.now()
        return value

class ListProperty(Property):

    def __init__(self, *args, **kwargs):
        super(ListProperty, self).__init__(list, *args, **kwargs)

    def _get_callback(self, instance, value):
        return value

    def _set_callback(self, instance, value):
        if not value:
            return list()

        def _all(itr):
            return True if isinstance(itr, int) or isinstance(itr, str) or isinstance(itr, datetime) else False

        if not all(map(_all, value)):
            raise TypeError("Value should in int, 'str', datetime")
        return value

class ObjectIDProperty(Property):

    def __init__(self, *args, **kwargs):
        super(ObjectIDProperty, self).__init__(list, *args, **kwargs)

    def _get_callback(self, instance, value):
        return value

    def _set_callback(self, instance, value):

        return ObjectId(unicode(value))

class DictProperty(Property):

    def __init__(self, *args, **kwargs):
        super(DictProperty, self).__init__(dict, *args, **kwargs)

    def _get_callback(self, instance, value):
        return value

    def _set_callback(self, instance, value):
        if not value:
            return dict()
        return dict(value)

class JsonProperty(Property):

    def __init__(self, *args, **kwargs):
        super(JsonProperty, self).__init__(str, *args, **kwargs)

    def _get_callback(self, instance, value):
        return json.loads(value)

    def _set_callback(self, instance, value):
        if not value:
            return json.dumps(dict())
        if not isinstance(value, str):
            raise TypeError("not a json string")
        return value



