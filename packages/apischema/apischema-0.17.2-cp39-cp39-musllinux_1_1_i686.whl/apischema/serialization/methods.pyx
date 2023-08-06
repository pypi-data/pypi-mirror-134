cimport cython
from dataclasses import dataclass, field
from typing import AbstractSet, Any, Callable, Dict, Optional, Tuple, Union

from apischema.conversions.utils import Converter
from apischema.fields import FIELDS_SET_ATTR
from apischema.serialization.errors import TypeCheckError
from apischema.types import AnyType, Undefined
from apischema.utils import Lazy


cdef class SerializationMethod():
    cdef int _dispatch

cdef class IdentityMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return IdentityMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 0

cdef class ListMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return ListMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 1

cdef class DictMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return DictMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 2

cdef class StrMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return StrMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 3

cdef class IntMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return IntMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 4

cdef class BoolMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return BoolMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 5

cdef class FloatMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return FloatMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 6

cdef class NoneMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return NoneMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 7

cdef class RecMethod(SerializationMethod):
    cdef readonly object lazy
    cdef readonly object method

    cpdef serialize(self, object obj, object path = None):
        return RecMethod_serialize(self, obj, path)

    def __init__(self, lazy):
        self.lazy = lazy
        self.method = None
        self._dispatch = 8

cdef class AnyMethod(SerializationMethod):
    cdef readonly object factory

    cpdef serialize(self, object obj, object path = None):
        return AnyMethod_serialize(self, obj, path)

    def __init__(self, factory):
        self.factory = factory
        self._dispatch = 9

cdef class Fallback():
    cdef int _dispatch

cdef class NoFallback(Fallback):
    cdef readonly object tp

    cpdef fall_back(self, object obj, object path):
        return NoFallback_fall_back(self, obj, path)

    def __init__(self, tp):
        self.tp = tp
        self._dispatch = 0

cdef class AnyFallback(Fallback):
    cdef readonly SerializationMethod any_method

    cpdef fall_back(self, object obj, object path):
        return AnyFallback_fall_back(self, obj, path)

    def __init__(self, any_method):
        self.any_method = any_method
        self._dispatch = 1

cdef class TypeCheckIdentityMethod(SerializationMethod):
    cdef readonly object expected
    cdef readonly Fallback fallback

    cpdef serialize(self, object obj, object path = None):
        return TypeCheckIdentityMethod_serialize(self, obj, path)

    def __init__(self, expected, fallback):
        self.expected = expected
        self.fallback = fallback
        self._dispatch = 10

cdef class TypeCheckMethod(SerializationMethod):
    cdef readonly SerializationMethod method
    cdef readonly object expected
    cdef readonly Fallback fallback

    cpdef serialize(self, object obj, object path = None):
        return TypeCheckMethod_serialize(self, obj, path)

    def __init__(self, method, expected, fallback):
        self.method = method
        self.expected = expected
        self.fallback = fallback
        self._dispatch = 11

cdef class CollectionCheckOnlyMethod(SerializationMethod):
    cdef readonly SerializationMethod value_method

    cpdef serialize(self, object obj, object path = None):
        return CollectionCheckOnlyMethod_serialize(self, obj, path)

    def __init__(self, value_method):
        self.value_method = value_method
        self._dispatch = 12

cdef class CollectionMethod(SerializationMethod):
    cdef readonly SerializationMethod value_method

    cpdef serialize(self, object obj, object path = None):
        return CollectionMethod_serialize(self, obj, path)

    def __init__(self, value_method):
        self.value_method = value_method
        self._dispatch = 13

cdef class ValueMethod(SerializationMethod):

    cpdef serialize(self, object obj, object path = None):
        return ValueMethod_serialize(self, obj, path)

    def __init__(self):
        self._dispatch = 14

cdef class EnumMethod(SerializationMethod):
    cdef readonly AnyMethod any_method

    cpdef serialize(self, object obj, object path = None):
        return EnumMethod_serialize(self, obj, path)

    def __init__(self, any_method):
        self.any_method = any_method
        self._dispatch = 15

cdef class MappingCheckOnlyMethod(SerializationMethod):
    cdef readonly SerializationMethod key_method
    cdef readonly SerializationMethod value_method

    cpdef serialize(self, object obj, object path = None):
        return MappingCheckOnlyMethod_serialize(self, obj, path)

    def __init__(self, key_method, value_method):
        self.key_method = key_method
        self.value_method = value_method
        self._dispatch = 16

cdef class MappingMethod(SerializationMethod):
    cdef readonly SerializationMethod key_method
    cdef readonly SerializationMethod value_method

    cpdef serialize(self, object obj, object path = None):
        return MappingMethod_serialize(self, obj, path)

    def __init__(self, key_method, value_method):
        self.key_method = key_method
        self.value_method = value_method
        self._dispatch = 17

cdef class BaseField():
    cdef int _dispatch

cdef class IdentityField(BaseField):
    cdef readonly str name
    cdef readonly str alias
    cdef readonly bint required

    cpdef update_result(self, object obj, dict result, bint typed_dict, bint exclude_unset):
        return IdentityField_update_result(self, obj, result, typed_dict, exclude_unset)

    def __init__(self, name, alias, required):
        self.name = name
        self.alias = alias
        self.required = required
        self._dispatch = 0

cdef class SimpleField(IdentityField):
    cdef readonly SerializationMethod method

    cpdef update_result(self, object obj, dict result, bint typed_dict, bint exclude_unset):
        return SimpleField_update_result(self, obj, result, typed_dict, exclude_unset)

    def __init__(self, name, alias, required, method):
        self.name = name
        self.alias = alias
        self.required = required
        self.method = method
        self._dispatch = 1

cdef class ComplexField(SimpleField):
    cdef readonly object skip_if
    cdef readonly bint undefined
    cdef readonly bint skip_none
    cdef readonly bint skip_default
    cdef readonly object default_value
    cdef readonly bint skippable

    cpdef update_result(self, object obj, dict result, bint typed_dict, bint exclude_unset):
        return ComplexField_update_result(self, obj, result, typed_dict, exclude_unset)

    def __init__(self, name, alias, required, method, skip_if, undefined, skip_none, skip_default, default_value):
        self.name = name
        self.alias = alias
        self.required = required
        self.method = method
        self.skip_if = skip_if
        self.undefined = undefined
        self.skip_none = skip_none
        self.skip_default = skip_default
        self.default_value = default_value
        self.skippable = (
            self.skip_if or self.undefined or self.skip_none or self.skip_default
        )
        self._dispatch = 2

cdef class SerializedField(BaseField):
    cdef readonly str alias
    cdef readonly object func
    cdef readonly bint undefined
    cdef readonly bint skip_none
    cdef readonly SerializationMethod method

    cpdef update_result(self, object obj, dict result, bint typed_dict, bint exclude_unset):
        return SerializedField_update_result(self, obj, result, typed_dict, exclude_unset)

    def __init__(self, alias, func, undefined, skip_none, method):
        self.alias = alias
        self.func = func
        self.undefined = undefined
        self.skip_none = skip_none
        self.method = method
        self._dispatch = 3

cdef class ObjectMethod(SerializationMethod):
    cdef readonly tuple fields

    def __init__(self, fields):
        self.fields = fields
        self._dispatch = 18

cdef class ClassMethod(ObjectMethod):

    cpdef serialize(self, object obj, object path = None):
        return ClassMethod_serialize(self, obj, path)

    def __init__(self, fields):
        self.fields = fields
        self._dispatch = 19

cdef class ClassWithFieldsSetMethod(ObjectMethod):

    cpdef serialize(self, object obj, object path = None):
        return ClassWithFieldsSetMethod_serialize(self, obj, path)

    def __init__(self, fields):
        self.fields = fields
        self._dispatch = 20

cdef class TypedDictMethod(ObjectMethod):

    cpdef serialize(self, object obj, object path = None):
        return TypedDictMethod_serialize(self, obj, path)

    def __init__(self, fields):
        self.fields = fields
        self._dispatch = 21

cdef class TypedDictWithAdditionalMethod(TypedDictMethod):
    cdef readonly set field_names
    cdef readonly SerializationMethod any_method

    cpdef serialize(self, object obj, object path = None):
        return TypedDictWithAdditionalMethod_serialize(self, obj, path)

    def __init__(self, fields, field_names, any_method):
        self.fields = fields
        self.field_names = field_names
        self.any_method = any_method
        self._dispatch = 22

cdef class TupleCheckOnlyMethod(SerializationMethod):
    cdef readonly tuple elt_methods

    cpdef serialize(self, object obj, object path = None):
        return TupleCheckOnlyMethod_serialize(self, obj, path)

    def __init__(self, elt_methods):
        self.elt_methods = elt_methods
        self._dispatch = 23

cdef class TupleMethod(SerializationMethod):
    cdef readonly tuple elt_methods

    cpdef serialize(self, object obj, object path = None):
        return TupleMethod_serialize(self, obj, path)

    def __init__(self, elt_methods):
        self.elt_methods = elt_methods
        self._dispatch = 24

cdef class CheckedTupleMethod(SerializationMethod):
    cdef readonly long nb_elts
    cdef readonly SerializationMethod method

    cpdef serialize(self, object obj, object path = None):
        return CheckedTupleMethod_serialize(self, obj, path)

    def __init__(self, nb_elts, method):
        self.nb_elts = nb_elts
        self.method = method
        self._dispatch = 25

cdef class OptionalMethod(SerializationMethod):
    cdef readonly SerializationMethod value_method

    cpdef serialize(self, object obj, object path = None):
        return OptionalMethod_serialize(self, obj, path)

    def __init__(self, value_method):
        self.value_method = value_method
        self._dispatch = 26

cdef class UnionAlternative(SerializationMethod):
    cdef readonly object cls
    cdef readonly SerializationMethod method

    cpdef serialize(self, object obj, object path = None):
        return UnionAlternative_serialize(self, obj, path)

    def __init__(self, cls, method):
        self.cls = cls
        self.method = method
        self._dispatch = 27

cdef class DiscriminatedAlternative(UnionAlternative):
    cdef readonly str alias
    cdef readonly str key

    cpdef serialize(self, object obj, object path = None):
        return DiscriminatedAlternative_serialize(self, obj, path)

    def __init__(self, cls, method, alias, key):
        self.cls = cls
        self.method = method
        self.alias = alias
        self.key = key
        self._dispatch = 28

cdef class UnionMethod(SerializationMethod):
    cdef readonly tuple alternatives
    cdef readonly Fallback fallback

    cpdef serialize(self, object obj, object path = None):
        return UnionMethod_serialize(self, obj, path)

    def __init__(self, alternatives, fallback):
        self.alternatives = alternatives
        self.fallback = fallback
        self._dispatch = 29

cdef class WrapperMethod(SerializationMethod):
    cdef readonly object wrapped

    cpdef serialize(self, object obj, object path = None):
        return WrapperMethod_serialize(self, obj, path)

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self._dispatch = 30

cdef class ConversionMethod(SerializationMethod):
    cdef readonly object converter
    cdef readonly SerializationMethod method

    cpdef serialize(self, object obj, object path = None):
        return ConversionMethod_serialize(self, obj, path)

    def __init__(self, converter, method):
        self.converter = converter
        self.method = method
        self._dispatch = 31

cdef class DiscriminateTypedDict(SerializationMethod):
    cdef readonly str field_name
    cdef readonly dict mapping
    cdef readonly Fallback fallback

    cpdef serialize(self, object obj, object path = None):
        return DiscriminateTypedDict_serialize(self, obj, path)

    def __init__(self, field_name, mapping, fallback):
        self.field_name = field_name
        self.mapping = mapping
        self.fallback = fallback
        self._dispatch = 32

cpdef inline serialize_field(IdentityField field, object obj, bint typed_dict, bint exclude_unset):
    if typed_dict:
        return field.required or field.name in obj
    else:
        return not exclude_unset or field.name in getattr(obj, FIELDS_SET_ATTR)

cpdef inline get_field_value(IdentityField field, object obj, bint typed_dict):
    return obj[field.name] if typed_dict else getattr(obj, field.name)

cdef inline IdentityMethod_serialize(IdentityMethod self, object obj, object path = None):
        return obj

cdef inline ListMethod_serialize(ListMethod self, object obj, object path = None):
        return list(obj)

cdef inline DictMethod_serialize(DictMethod self, object obj, object path = None):
        return dict(obj)

cdef inline StrMethod_serialize(StrMethod self, object obj, object path = None):
        return str(obj)

cdef inline IntMethod_serialize(IntMethod self, object obj, object path = None):
        return int(obj)

cdef inline BoolMethod_serialize(BoolMethod self, object obj, object path = None):
        return bool(obj)

cdef inline FloatMethod_serialize(FloatMethod self, object obj, object path = None):
        return float(obj)

cdef inline NoneMethod_serialize(NoneMethod self, object obj, object path = None):
        return None

cdef inline RecMethod_serialize(RecMethod self, object obj, object path = None):
        if self.method is None:
            self.method = self.lazy()
        return SerializationMethod_serialize(self.method, obj)

cdef inline AnyMethod_serialize(AnyMethod self, object obj, object path = None):
        method = self.factory(obj.__class__)  # tmp  variable for substitution
        return SerializationMethod_serialize(method, obj, path)

cdef inline TypeCheckIdentityMethod_serialize(TypeCheckIdentityMethod self, object obj, object path = None):
        return (
            obj
            if isinstance(obj, self.expected)
            else Fallback_fall_back(self.fallback, obj, path)
        )

cdef inline TypeCheckMethod_serialize(TypeCheckMethod self, object obj, object path = None):
        if isinstance(obj, self.expected):
            try:
                return SerializationMethod_serialize(self.method, obj)
            except TypeCheckError as err:
                if path is None:
                    raise
                raise TypeCheckError(err.msg, [path, *err.loc])
        else:
            return Fallback_fall_back(self.fallback, obj, path)

cdef inline CollectionCheckOnlyMethod_serialize(CollectionCheckOnlyMethod self, object obj, object path = None):
        for i, elt in enumerate(obj):
            SerializationMethod_serialize(self.value_method, elt, i)
        return obj

cdef inline CollectionMethod_serialize(CollectionMethod self, object obj, object path = None):
        return [SerializationMethod_serialize(self.value_method, elt, i) for i, elt in enumerate(obj)]

cdef inline ValueMethod_serialize(ValueMethod self, object obj, object path = None):
        return obj.value

cdef inline EnumMethod_serialize(EnumMethod self, object obj, object path = None):
        return SerializationMethod_serialize(self.any_method, obj.value)

cdef inline MappingCheckOnlyMethod_serialize(MappingCheckOnlyMethod self, object obj, object path = None):
        for key, value in obj.items():
            SerializationMethod_serialize(self.key_method, key, key)
            SerializationMethod_serialize(self.value_method, value, key)
        return obj

cdef inline MappingMethod_serialize(MappingMethod self, object obj, object path = None):
        return {
            SerializationMethod_serialize(self.key_method, key, key): SerializationMethod_serialize(self.value_method, value, key)
            for key, value in obj.items()
        }

cdef inline ClassMethod_serialize(ClassMethod self, object obj, object path = None):
        result: dict = {}
        for i in range(len(self.fields)):
            field: BaseField = self.fields[i]
            BaseField_update_result(field, obj, result, False, False)
        return result

cdef inline ClassWithFieldsSetMethod_serialize(ClassWithFieldsSetMethod self, object obj, object path = None):
        result: dict = {}
        for i in range(len(self.fields)):
            field: BaseField = self.fields[i]
            BaseField_update_result(field, obj, result, False, True)
        return result

cdef inline TypedDictMethod_serialize(TypedDictMethod self, object obj, object path = None):
        result: dict = {}
        for i in range(len(self.fields)):
            field: BaseField = self.fields[i]
            BaseField_update_result(field, obj, result, True, False)
        return result

cdef inline TypedDictWithAdditionalMethod_serialize(TypedDictWithAdditionalMethod self, object obj, object path = None):
        result: dict = TypedDictMethod_serialize(<TypedDictMethod>self, obj)
        for key, value in obj.items():
            if key not in self.field_names and isinstance(key, str):
                result[str(key)] = SerializationMethod_serialize(self.any_method, value, key)
        return result

cdef inline TupleCheckOnlyMethod_serialize(TupleCheckOnlyMethod self, tuple obj, object path = None):
        for i in range(len(self.elt_methods)):
            method: SerializationMethod = self.elt_methods[i]
            SerializationMethod_serialize(method, obj[i], i)
        return obj

cdef inline TupleMethod_serialize(TupleMethod self, tuple obj, object path = None):
        elts: list = [None] * len(self.elt_methods)
        for i in range(len(self.elt_methods)):
            method: SerializationMethod = self.elt_methods[i]
            elts[i] = SerializationMethod_serialize(method, obj[i], i)
        return elts

cdef inline CheckedTupleMethod_serialize(CheckedTupleMethod self, tuple obj, object path = None):
        if not len(obj) == self.nb_elts:
            raise TypeError(f"Expected {self.nb_elts}-tuple, found {len(obj)}-tuple")
        return SerializationMethod_serialize(self.method, obj)

cdef inline OptionalMethod_serialize(OptionalMethod self, object obj, object path = None):
        return SerializationMethod_serialize(self.value_method, obj, path) if obj is not None else None

cdef inline UnionAlternative_serialize(UnionAlternative self, object obj, object path = None):
        return SerializationMethod_serialize(self.method, obj, path)

cdef inline DiscriminatedAlternative_serialize(DiscriminatedAlternative self, object obj, object path = None):
        res = UnionAlternative_serialize(<UnionAlternative>self, obj, path)
        if isinstance(res, dict) and self.alias not in res:
            res[self.alias] = self.key
        return res

cdef inline UnionMethod_serialize(UnionMethod self, object obj, object path = None):
        for i in range(len(self.alternatives)):
            alternative: UnionAlternative = self.alternatives[i]
            if isinstance(obj, alternative.cls):
                try:
                    return SerializationMethod_serialize(alternative, obj, path)
                except Exception:
                    pass
        return Fallback_fall_back(self.fallback, obj, path)

cdef inline WrapperMethod_serialize(WrapperMethod self, object obj, object path = None):
        return self.wrapped(obj)

cdef inline ConversionMethod_serialize(ConversionMethod self, object obj, object path = None):
        return SerializationMethod_serialize(self.method, self.converter(obj))

cdef inline DiscriminateTypedDict_serialize(DiscriminateTypedDict self, object obj, object path = None):
        try:
            method: SerializationMethod = self.mapping[obj[self.field_name]]
        except Exception:
            return Fallback_fall_back(self.fallback, obj, path)
        return SerializationMethod_serialize(method, obj, path)

cdef inline NoFallback_fall_back(NoFallback self, object obj, object path):
        raise TypeCheckError(
            f"Expected {self.tp}, found {obj.__class__}",
            [path] if path is not None else [],
        )

cdef inline AnyFallback_fall_back(AnyFallback self, object obj, object key):
        return SerializationMethod_serialize(self.any_method, obj, key)

cdef inline IdentityField_update_result(IdentityField self, object obj, dict result, bint typed_dict, bint exclude_unset):
        if serialize_field(self, obj, typed_dict, exclude_unset):
            result[self.alias] = get_field_value(self, obj, typed_dict)

cdef inline SimpleField_update_result(SimpleField self, object obj, dict result, bint typed_dict, bint exclude_unset):
        if serialize_field(self, obj, typed_dict, exclude_unset):
            result[self.alias] = SerializationMethod_serialize(self.method, 
                get_field_value(self, obj, typed_dict), self.alias
            )

cdef inline ComplexField_update_result(ComplexField self, object obj, dict result, bint typed_dict, bint exclude_unset):
        if serialize_field(self, obj, typed_dict, exclude_unset):
            value: object = get_field_value(self, obj, typed_dict)
            if not self.skippable or not (
                (self.skip_if is not None and self.skip_if(value))
                or (self.undefined and value is Undefined)
                or (self.skip_none and value is None)
                or (self.skip_default and value == self.default_value)
            ):
                if self.alias is not None:
                    result[self.alias] = SerializationMethod_serialize(self.method, value, self.alias)
                else:
                    result.update(SerializationMethod_serialize(self.method, value, self.alias))

cdef inline SerializedField_update_result(SerializedField self, object obj, dict result, bint typed_dict, bint exclude_unset):
        value = self.func(obj)
        if not (self.undefined and value is Undefined) and not (
            self.skip_none and value is None
        ):
            result[self.alias] = SerializationMethod_serialize(self.method, value, self.alias)

cdef inline SerializationMethod_serialize(SerializationMethod self, object obj, object path = None):
    cdef int _dispatch = self._dispatch
    if _dispatch == 0:
        return IdentityMethod_serialize(<IdentityMethod>self, obj, path)
    elif _dispatch == 1:
        return ListMethod_serialize(<ListMethod>self, obj, path)
    elif _dispatch == 2:
        return DictMethod_serialize(<DictMethod>self, obj, path)
    elif _dispatch == 3:
        return StrMethod_serialize(<StrMethod>self, obj, path)
    elif _dispatch == 4:
        return IntMethod_serialize(<IntMethod>self, obj, path)
    elif _dispatch == 5:
        return BoolMethod_serialize(<BoolMethod>self, obj, path)
    elif _dispatch == 6:
        return FloatMethod_serialize(<FloatMethod>self, obj, path)
    elif _dispatch == 7:
        return NoneMethod_serialize(<NoneMethod>self, obj, path)
    elif _dispatch == 8:
        return RecMethod_serialize(<RecMethod>self, obj, path)
    elif _dispatch == 9:
        return AnyMethod_serialize(<AnyMethod>self, obj, path)
    elif _dispatch == 10:
        return TypeCheckIdentityMethod_serialize(<TypeCheckIdentityMethod>self, obj, path)
    elif _dispatch == 11:
        return TypeCheckMethod_serialize(<TypeCheckMethod>self, obj, path)
    elif _dispatch == 12:
        return CollectionCheckOnlyMethod_serialize(<CollectionCheckOnlyMethod>self, obj, path)
    elif _dispatch == 13:
        return CollectionMethod_serialize(<CollectionMethod>self, obj, path)
    elif _dispatch == 14:
        return ValueMethod_serialize(<ValueMethod>self, obj, path)
    elif _dispatch == 15:
        return EnumMethod_serialize(<EnumMethod>self, obj, path)
    elif _dispatch == 16:
        return MappingCheckOnlyMethod_serialize(<MappingCheckOnlyMethod>self, obj, path)
    elif _dispatch == 17:
        return MappingMethod_serialize(<MappingMethod>self, obj, path)
    elif _dispatch == 19:
        return ClassMethod_serialize(<ClassMethod>self, obj, path)
    elif _dispatch == 20:
        return ClassWithFieldsSetMethod_serialize(<ClassWithFieldsSetMethod>self, obj, path)
    elif _dispatch == 21:
        return TypedDictMethod_serialize(<TypedDictMethod>self, obj, path)
    elif _dispatch == 22:
        return TypedDictWithAdditionalMethod_serialize(<TypedDictWithAdditionalMethod>self, obj, path)
    elif _dispatch == 23:
        return TupleCheckOnlyMethod_serialize(<TupleCheckOnlyMethod>self, obj, path)
    elif _dispatch == 24:
        return TupleMethod_serialize(<TupleMethod>self, obj, path)
    elif _dispatch == 25:
        return CheckedTupleMethod_serialize(<CheckedTupleMethod>self, obj, path)
    elif _dispatch == 26:
        return OptionalMethod_serialize(<OptionalMethod>self, obj, path)
    elif _dispatch == 27:
        return UnionAlternative_serialize(<UnionAlternative>self, obj, path)
    elif _dispatch == 28:
        return DiscriminatedAlternative_serialize(<DiscriminatedAlternative>self, obj, path)
    elif _dispatch == 29:
        return UnionMethod_serialize(<UnionMethod>self, obj, path)
    elif _dispatch == 30:
        return WrapperMethod_serialize(<WrapperMethod>self, obj, path)
    elif _dispatch == 31:
        return ConversionMethod_serialize(<ConversionMethod>self, obj, path)
    elif _dispatch == 32:
        return DiscriminateTypedDict_serialize(<DiscriminateTypedDict>self, obj, path)

cdef inline Fallback_fall_back(Fallback self, object obj, object path):
    cdef int _dispatch = self._dispatch
    if _dispatch == 0:
        return NoFallback_fall_back(<NoFallback>self, obj, path)
    elif _dispatch == 1:
        return AnyFallback_fall_back(<AnyFallback>self, obj, path)

cdef inline BaseField_update_result(BaseField self, object obj, dict result, bint typed_dict, bint exclude_unset):
    cdef int _dispatch = self._dispatch
    if _dispatch == 0:
        return IdentityField_update_result(<IdentityField>self, obj, result, typed_dict, exclude_unset)
    elif _dispatch == 1:
        return SimpleField_update_result(<SimpleField>self, obj, result, typed_dict, exclude_unset)
    elif _dispatch == 2:
        return ComplexField_update_result(<ComplexField>self, obj, result, typed_dict, exclude_unset)
    elif _dispatch == 3:
        return SerializedField_update_result(<SerializedField>self, obj, result, typed_dict, exclude_unset)

