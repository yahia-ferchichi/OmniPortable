# Python stubs generated by omniidl from /usr/local/share/idl/omniORB/COS/CosLifeCycle.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


# #include "CosNaming.idl"
import CosNaming_idl
_0_CosNaming = omniORB.openModule("CosNaming")
_0_CosNaming__POA = omniORB.openModule("CosNaming__POA")

#
# Start of module "CosLifeCycle"
#
__name__ = "CosLifeCycle"
_0_CosLifeCycle = omniORB.openModule("CosLifeCycle", r"/usr/local/share/idl/omniORB/COS/CosLifeCycle.idl")
_0_CosLifeCycle__POA = omniORB.openModule("CosLifeCycle__POA", r"/usr/local/share/idl/omniORB/COS/CosLifeCycle.idl")


# typedef ... Key
class Key:
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/Key:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosLifeCycle.Key = Key
_0_CosLifeCycle._d_Key  = omniORB.typeMapping["IDL:omg.org/CosNaming/Name:1.0"]
_0_CosLifeCycle._ad_Key = (omniORB.tcInternal.tv_alias, Key._NP_RepositoryId, "Key", omniORB.typeCodeMapping["IDL:omg.org/CosNaming/Name:1.0"]._d)
_0_CosLifeCycle._tc_Key = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._ad_Key)
omniORB.registerType(Key._NP_RepositoryId, _0_CosLifeCycle._ad_Key, _0_CosLifeCycle._tc_Key)
del Key

# typedef ... Factory
class Factory:
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/Factory:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosLifeCycle.Factory = Factory
_0_CosLifeCycle._d_Factory  = omniORB.typeMapping["IDL:omg.org/CORBA/Object:1.0"]
_0_CosLifeCycle._ad_Factory = (omniORB.tcInternal.tv_alias, Factory._NP_RepositoryId, "Factory", omniORB.typeMapping["IDL:omg.org/CORBA/Object:1.0"])
_0_CosLifeCycle._tc_Factory = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._ad_Factory)
omniORB.registerType(Factory._NP_RepositoryId, _0_CosLifeCycle._ad_Factory, _0_CosLifeCycle._tc_Factory)
del Factory

# typedef ... Factories
class Factories:
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/Factories:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosLifeCycle.Factories = Factories
_0_CosLifeCycle._d_Factories  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Factory:1.0"], 0)
_0_CosLifeCycle._ad_Factories = (omniORB.tcInternal.tv_alias, Factories._NP_RepositoryId, "Factories", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Factory:1.0"], 0))
_0_CosLifeCycle._tc_Factories = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._ad_Factories)
omniORB.registerType(Factories._NP_RepositoryId, _0_CosLifeCycle._ad_Factories, _0_CosLifeCycle._tc_Factories)
del Factories

# struct NVP
_0_CosLifeCycle.NVP = omniORB.newEmptyClass()
class NVP (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/NVP:1.0"

    def __init__(self, name, value):
        self.name = name
        self.value = value

_0_CosLifeCycle.NVP = NVP
_0_CosLifeCycle._d_NVP  = (omniORB.tcInternal.tv_struct, NVP, NVP._NP_RepositoryId, "NVP", "name", omniORB.typeMapping["IDL:omg.org/CosNaming/Istring:1.0"], "value", omniORB.tcInternal.tv_any)
_0_CosLifeCycle._tc_NVP = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_NVP)
omniORB.registerType(NVP._NP_RepositoryId, _0_CosLifeCycle._d_NVP, _0_CosLifeCycle._tc_NVP)
del NVP

# typedef ... NameValuePair
class NameValuePair (_0_CosLifeCycle.NVP):
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/NameValuePair:1.0"

_0_CosLifeCycle.NameValuePair = NameValuePair
_0_CosLifeCycle._d_NameValuePair  = omniORB.typeMapping["IDL:omg.org/CosLifeCycle/NVP:1.0"]
_0_CosLifeCycle._ad_NameValuePair = (omniORB.tcInternal.tv_alias, NameValuePair._NP_RepositoryId, "NameValuePair", omniORB.typeMapping["IDL:omg.org/CosLifeCycle/NVP:1.0"])
_0_CosLifeCycle._tc_NameValuePair = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._ad_NameValuePair)
omniORB.registerType(NameValuePair._NP_RepositoryId, _0_CosLifeCycle._ad_NameValuePair, _0_CosLifeCycle._tc_NameValuePair)
del NameValuePair

# typedef ... Criteria
class Criteria:
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/Criteria:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosLifeCycle.Criteria = Criteria
_0_CosLifeCycle._d_Criteria  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/NameValuePair:1.0"], 0)
_0_CosLifeCycle._ad_Criteria = (omniORB.tcInternal.tv_alias, Criteria._NP_RepositoryId, "Criteria", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosLifeCycle/NameValuePair:1.0"], 0))
_0_CosLifeCycle._tc_Criteria = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._ad_Criteria)
omniORB.registerType(Criteria._NP_RepositoryId, _0_CosLifeCycle._ad_Criteria, _0_CosLifeCycle._tc_Criteria)
del Criteria

# exception NoFactory
_0_CosLifeCycle.NoFactory = omniORB.newEmptyClass()
class NoFactory (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/NoFactory:1.0"

    def __init__(self, search_key):
        CORBA.UserException.__init__(self, search_key)
        self.search_key = search_key

_0_CosLifeCycle.NoFactory = NoFactory
_0_CosLifeCycle._d_NoFactory  = (omniORB.tcInternal.tv_except, NoFactory, NoFactory._NP_RepositoryId, "NoFactory", "search_key", omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Key:1.0"])
_0_CosLifeCycle._tc_NoFactory = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_NoFactory)
omniORB.registerType(NoFactory._NP_RepositoryId, _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle._tc_NoFactory)
del NoFactory

# exception NotCopyable
_0_CosLifeCycle.NotCopyable = omniORB.newEmptyClass()
class NotCopyable (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/NotCopyable:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_CosLifeCycle.NotCopyable = NotCopyable
_0_CosLifeCycle._d_NotCopyable  = (omniORB.tcInternal.tv_except, NotCopyable, NotCopyable._NP_RepositoryId, "NotCopyable", "reason", (omniORB.tcInternal.tv_string,0))
_0_CosLifeCycle._tc_NotCopyable = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_NotCopyable)
omniORB.registerType(NotCopyable._NP_RepositoryId, _0_CosLifeCycle._d_NotCopyable, _0_CosLifeCycle._tc_NotCopyable)
del NotCopyable

# exception NotMovable
_0_CosLifeCycle.NotMovable = omniORB.newEmptyClass()
class NotMovable (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/NotMovable:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_CosLifeCycle.NotMovable = NotMovable
_0_CosLifeCycle._d_NotMovable  = (omniORB.tcInternal.tv_except, NotMovable, NotMovable._NP_RepositoryId, "NotMovable", "reason", (omniORB.tcInternal.tv_string,0))
_0_CosLifeCycle._tc_NotMovable = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_NotMovable)
omniORB.registerType(NotMovable._NP_RepositoryId, _0_CosLifeCycle._d_NotMovable, _0_CosLifeCycle._tc_NotMovable)
del NotMovable

# exception NotRemovable
_0_CosLifeCycle.NotRemovable = omniORB.newEmptyClass()
class NotRemovable (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/NotRemovable:1.0"

    def __init__(self, reason):
        CORBA.UserException.__init__(self, reason)
        self.reason = reason

_0_CosLifeCycle.NotRemovable = NotRemovable
_0_CosLifeCycle._d_NotRemovable  = (omniORB.tcInternal.tv_except, NotRemovable, NotRemovable._NP_RepositoryId, "NotRemovable", "reason", (omniORB.tcInternal.tv_string,0))
_0_CosLifeCycle._tc_NotRemovable = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_NotRemovable)
omniORB.registerType(NotRemovable._NP_RepositoryId, _0_CosLifeCycle._d_NotRemovable, _0_CosLifeCycle._tc_NotRemovable)
del NotRemovable

# exception InvalidCriteria
_0_CosLifeCycle.InvalidCriteria = omniORB.newEmptyClass()
class InvalidCriteria (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/InvalidCriteria:1.0"

    def __init__(self, invalid_criteria):
        CORBA.UserException.__init__(self, invalid_criteria)
        self.invalid_criteria = invalid_criteria

_0_CosLifeCycle.InvalidCriteria = InvalidCriteria
_0_CosLifeCycle._d_InvalidCriteria  = (omniORB.tcInternal.tv_except, InvalidCriteria, InvalidCriteria._NP_RepositoryId, "InvalidCriteria", "invalid_criteria", omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"])
_0_CosLifeCycle._tc_InvalidCriteria = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_InvalidCriteria)
omniORB.registerType(InvalidCriteria._NP_RepositoryId, _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle._tc_InvalidCriteria)
del InvalidCriteria

# exception CannotMeetCriteria
_0_CosLifeCycle.CannotMeetCriteria = omniORB.newEmptyClass()
class CannotMeetCriteria (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosLifeCycle/CannotMeetCriteria:1.0"

    def __init__(self, unmet_criteria):
        CORBA.UserException.__init__(self, unmet_criteria)
        self.unmet_criteria = unmet_criteria

_0_CosLifeCycle.CannotMeetCriteria = CannotMeetCriteria
_0_CosLifeCycle._d_CannotMeetCriteria  = (omniORB.tcInternal.tv_except, CannotMeetCriteria, CannotMeetCriteria._NP_RepositoryId, "CannotMeetCriteria", "unmet_criteria", omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"])
_0_CosLifeCycle._tc_CannotMeetCriteria = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_CannotMeetCriteria)
omniORB.registerType(CannotMeetCriteria._NP_RepositoryId, _0_CosLifeCycle._d_CannotMeetCriteria, _0_CosLifeCycle._tc_CannotMeetCriteria)
del CannotMeetCriteria

# interface FactoryFinder
_0_CosLifeCycle._d_FactoryFinder = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosLifeCycle/FactoryFinder:1.0", "FactoryFinder")
omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"] = _0_CosLifeCycle._d_FactoryFinder
_0_CosLifeCycle.FactoryFinder = omniORB.newEmptyClass()
class FactoryFinder :
    _NP_RepositoryId = _0_CosLifeCycle._d_FactoryFinder[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosLifeCycle.FactoryFinder = FactoryFinder
_0_CosLifeCycle._tc_FactoryFinder = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_FactoryFinder)
omniORB.registerType(FactoryFinder._NP_RepositoryId, _0_CosLifeCycle._d_FactoryFinder, _0_CosLifeCycle._tc_FactoryFinder)

# FactoryFinder operations and attributes
FactoryFinder._d_find_factories = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Key:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Factories:1.0"], ), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory})

# FactoryFinder object reference
class _objref_FactoryFinder (CORBA.Object):
    _NP_RepositoryId = FactoryFinder._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def find_factories(self, *args):
        return self._obj.invoke("find_factories", _0_CosLifeCycle.FactoryFinder._d_find_factories, args)

omniORB.registerObjref(FactoryFinder._NP_RepositoryId, _objref_FactoryFinder)
_0_CosLifeCycle._objref_FactoryFinder = _objref_FactoryFinder
del FactoryFinder, _objref_FactoryFinder

# FactoryFinder skeleton
__name__ = "CosLifeCycle__POA"
class FactoryFinder (PortableServer.Servant):
    _NP_RepositoryId = _0_CosLifeCycle.FactoryFinder._NP_RepositoryId


    _omni_op_d = {"find_factories": _0_CosLifeCycle.FactoryFinder._d_find_factories}

FactoryFinder._omni_skeleton = FactoryFinder
_0_CosLifeCycle__POA.FactoryFinder = FactoryFinder
omniORB.registerSkeleton(FactoryFinder._NP_RepositoryId, FactoryFinder)
del FactoryFinder
__name__ = "CosLifeCycle"

# interface LifeCycleObject
_0_CosLifeCycle._d_LifeCycleObject = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosLifeCycle/LifeCycleObject:1.0", "LifeCycleObject")
omniORB.typeMapping["IDL:omg.org/CosLifeCycle/LifeCycleObject:1.0"] = _0_CosLifeCycle._d_LifeCycleObject
_0_CosLifeCycle.LifeCycleObject = omniORB.newEmptyClass()
class LifeCycleObject :
    _NP_RepositoryId = _0_CosLifeCycle._d_LifeCycleObject[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosLifeCycle.LifeCycleObject = LifeCycleObject
_0_CosLifeCycle._tc_LifeCycleObject = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_LifeCycleObject)
omniORB.registerType(LifeCycleObject._NP_RepositoryId, _0_CosLifeCycle._d_LifeCycleObject, _0_CosLifeCycle._tc_LifeCycleObject)

# LifeCycleObject operations and attributes
LifeCycleObject._d_copy = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosLifeCycle/LifeCycleObject:1.0"], ), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotCopyable._NP_RepositoryId: _0_CosLifeCycle._d_NotCopyable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
LifeCycleObject._d_move = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotMovable._NP_RepositoryId: _0_CosLifeCycle._d_NotMovable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
LifeCycleObject._d_remove = ((), (), {_0_CosLifeCycle.NotRemovable._NP_RepositoryId: _0_CosLifeCycle._d_NotRemovable})

# LifeCycleObject object reference
class _objref_LifeCycleObject (CORBA.Object):
    _NP_RepositoryId = LifeCycleObject._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def copy(self, *args):
        return self._obj.invoke("copy", _0_CosLifeCycle.LifeCycleObject._d_copy, args)

    def move(self, *args):
        return self._obj.invoke("move", _0_CosLifeCycle.LifeCycleObject._d_move, args)

    def remove(self, *args):
        return self._obj.invoke("remove", _0_CosLifeCycle.LifeCycleObject._d_remove, args)

omniORB.registerObjref(LifeCycleObject._NP_RepositoryId, _objref_LifeCycleObject)
_0_CosLifeCycle._objref_LifeCycleObject = _objref_LifeCycleObject
del LifeCycleObject, _objref_LifeCycleObject

# LifeCycleObject skeleton
__name__ = "CosLifeCycle__POA"
class LifeCycleObject (PortableServer.Servant):
    _NP_RepositoryId = _0_CosLifeCycle.LifeCycleObject._NP_RepositoryId


    _omni_op_d = {"copy": _0_CosLifeCycle.LifeCycleObject._d_copy, "move": _0_CosLifeCycle.LifeCycleObject._d_move, "remove": _0_CosLifeCycle.LifeCycleObject._d_remove}

LifeCycleObject._omni_skeleton = LifeCycleObject
_0_CosLifeCycle__POA.LifeCycleObject = LifeCycleObject
omniORB.registerSkeleton(LifeCycleObject._NP_RepositoryId, LifeCycleObject)
del LifeCycleObject
__name__ = "CosLifeCycle"

# interface GenericFactory
_0_CosLifeCycle._d_GenericFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosLifeCycle/GenericFactory:1.0", "GenericFactory")
omniORB.typeMapping["IDL:omg.org/CosLifeCycle/GenericFactory:1.0"] = _0_CosLifeCycle._d_GenericFactory
_0_CosLifeCycle.GenericFactory = omniORB.newEmptyClass()
class GenericFactory :
    _NP_RepositoryId = _0_CosLifeCycle._d_GenericFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosLifeCycle.GenericFactory = GenericFactory
_0_CosLifeCycle._tc_GenericFactory = omniORB.tcInternal.createTypeCode(_0_CosLifeCycle._d_GenericFactory)
omniORB.registerType(GenericFactory._NP_RepositoryId, _0_CosLifeCycle._d_GenericFactory, _0_CosLifeCycle._tc_GenericFactory)

# GenericFactory operations and attributes
GenericFactory._d_supports = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Key:1.0"], ), (omniORB.tcInternal.tv_boolean, ), None)
GenericFactory._d_create_object = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Key:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (omniORB.typeMapping["IDL:omg.org/CORBA/Object:1.0"], ), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})

# GenericFactory object reference
class _objref_GenericFactory (CORBA.Object):
    _NP_RepositoryId = GenericFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def supports(self, *args):
        return self._obj.invoke("supports", _0_CosLifeCycle.GenericFactory._d_supports, args)

    def create_object(self, *args):
        return self._obj.invoke("create_object", _0_CosLifeCycle.GenericFactory._d_create_object, args)

omniORB.registerObjref(GenericFactory._NP_RepositoryId, _objref_GenericFactory)
_0_CosLifeCycle._objref_GenericFactory = _objref_GenericFactory
del GenericFactory, _objref_GenericFactory

# GenericFactory skeleton
__name__ = "CosLifeCycle__POA"
class GenericFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_CosLifeCycle.GenericFactory._NP_RepositoryId


    _omni_op_d = {"supports": _0_CosLifeCycle.GenericFactory._d_supports, "create_object": _0_CosLifeCycle.GenericFactory._d_create_object}

GenericFactory._omni_skeleton = GenericFactory
_0_CosLifeCycle__POA.GenericFactory = GenericFactory
omniORB.registerSkeleton(GenericFactory._NP_RepositoryId, GenericFactory)
del GenericFactory
__name__ = "CosLifeCycle"

#
# End of module "CosLifeCycle"
#
__name__ = "CosLifeCycle_idl"

_exported_modules = ( "CosLifeCycle", )

# The end.
