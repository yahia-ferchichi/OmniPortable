# Python stubs generated by omniidl from /usr/local/share/idl/omniORB/COS/CosExternalization.idl
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

# #include "CosLifeCycle.idl"
import CosLifeCycle_idl
_0_CosLifeCycle = omniORB.openModule("CosLifeCycle")
_0_CosLifeCycle__POA = omniORB.openModule("CosLifeCycle__POA")

# #include "CosObjectIdentity.idl"
import CosObjectIdentity_idl
_0_CosObjectIdentity = omniORB.openModule("CosObjectIdentity")
_0_CosObjectIdentity__POA = omniORB.openModule("CosObjectIdentity__POA")

# #include "corbaidl.idl"
import corbaidl_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "boxes.idl"
import boxes_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "ir.idl"
import ir_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "CosRelationships.idl"
import CosRelationships_idl
_0_CosRelationships = omniORB.openModule("CosRelationships")
_0_CosRelationships__POA = omniORB.openModule("CosRelationships__POA")

# #include "CosGraphs.idl"
import CosGraphs_idl
_0_CosGraphs = omniORB.openModule("CosGraphs")
_0_CosGraphs__POA = omniORB.openModule("CosGraphs__POA")

# #include "CosStream.idl"
import CosStream_idl
_0_CosStream = omniORB.openModule("CosStream")
_0_CosStream__POA = omniORB.openModule("CosStream__POA")

#
# Start of module "CosExternalization"
#
__name__ = "CosExternalization"
_0_CosExternalization = omniORB.openModule("CosExternalization", r"/usr/local/share/idl/omniORB/COS/CosExternalization.idl")
_0_CosExternalization__POA = omniORB.openModule("CosExternalization__POA", r"/usr/local/share/idl/omniORB/COS/CosExternalization.idl")


# exception InvalidFileNameError
_0_CosExternalization.InvalidFileNameError = omniORB.newEmptyClass()
class InvalidFileNameError (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosExternalization/InvalidFileNameError:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_CosExternalization.InvalidFileNameError = InvalidFileNameError
_0_CosExternalization._d_InvalidFileNameError  = (omniORB.tcInternal.tv_except, InvalidFileNameError, InvalidFileNameError._NP_RepositoryId, "InvalidFileNameError")
_0_CosExternalization._tc_InvalidFileNameError = omniORB.tcInternal.createTypeCode(_0_CosExternalization._d_InvalidFileNameError)
omniORB.registerType(InvalidFileNameError._NP_RepositoryId, _0_CosExternalization._d_InvalidFileNameError, _0_CosExternalization._tc_InvalidFileNameError)
del InvalidFileNameError

# exception ContextAlreadyRegistered
_0_CosExternalization.ContextAlreadyRegistered = omniORB.newEmptyClass()
class ContextAlreadyRegistered (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/CosExternalization/ContextAlreadyRegistered:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_CosExternalization.ContextAlreadyRegistered = ContextAlreadyRegistered
_0_CosExternalization._d_ContextAlreadyRegistered  = (omniORB.tcInternal.tv_except, ContextAlreadyRegistered, ContextAlreadyRegistered._NP_RepositoryId, "ContextAlreadyRegistered")
_0_CosExternalization._tc_ContextAlreadyRegistered = omniORB.tcInternal.createTypeCode(_0_CosExternalization._d_ContextAlreadyRegistered)
omniORB.registerType(ContextAlreadyRegistered._NP_RepositoryId, _0_CosExternalization._d_ContextAlreadyRegistered, _0_CosExternalization._tc_ContextAlreadyRegistered)
del ContextAlreadyRegistered

# interface Stream
_0_CosExternalization._d_Stream = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosExternalization/Stream:1.0", "Stream")
omniORB.typeMapping["IDL:omg.org/CosExternalization/Stream:1.0"] = _0_CosExternalization._d_Stream
_0_CosExternalization.Stream = omniORB.newEmptyClass()
class Stream (_0_CosLifeCycle.LifeCycleObject):
    _NP_RepositoryId = _0_CosExternalization._d_Stream[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosExternalization.Stream = Stream
_0_CosExternalization._tc_Stream = omniORB.tcInternal.createTypeCode(_0_CosExternalization._d_Stream)
omniORB.registerType(Stream._NP_RepositoryId, _0_CosExternalization._d_Stream, _0_CosExternalization._tc_Stream)

# Stream operations and attributes
Stream._d_externalize = ((omniORB.typeMapping["IDL:omg.org/CosStream/Streamable:1.0"], ), (), None)
Stream._d_internalize = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosStream/Streamable:1.0"], ), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosStream.StreamDataFormatError._NP_RepositoryId: _0_CosStream._d_StreamDataFormatError})
Stream._d_begin_context = ((), (), {_0_CosExternalization.ContextAlreadyRegistered._NP_RepositoryId: _0_CosExternalization._d_ContextAlreadyRegistered})
Stream._d_end_context = ((), (), None)
Stream._d_flush = ((), (), None)

# Stream object reference
class _objref_Stream (_0_CosLifeCycle._objref_LifeCycleObject):
    _NP_RepositoryId = Stream._NP_RepositoryId

    def __init__(self, obj):
        _0_CosLifeCycle._objref_LifeCycleObject.__init__(self, obj)

    def externalize(self, *args):
        return self._obj.invoke("externalize", _0_CosExternalization.Stream._d_externalize, args)

    def internalize(self, *args):
        return self._obj.invoke("internalize", _0_CosExternalization.Stream._d_internalize, args)

    def begin_context(self, *args):
        return self._obj.invoke("begin_context", _0_CosExternalization.Stream._d_begin_context, args)

    def end_context(self, *args):
        return self._obj.invoke("end_context", _0_CosExternalization.Stream._d_end_context, args)

    def flush(self, *args):
        return self._obj.invoke("flush", _0_CosExternalization.Stream._d_flush, args)

omniORB.registerObjref(Stream._NP_RepositoryId, _objref_Stream)
_0_CosExternalization._objref_Stream = _objref_Stream
del Stream, _objref_Stream

# Stream skeleton
__name__ = "CosExternalization__POA"
class Stream (_0_CosLifeCycle__POA.LifeCycleObject):
    _NP_RepositoryId = _0_CosExternalization.Stream._NP_RepositoryId


    _omni_op_d = {"externalize": _0_CosExternalization.Stream._d_externalize, "internalize": _0_CosExternalization.Stream._d_internalize, "begin_context": _0_CosExternalization.Stream._d_begin_context, "end_context": _0_CosExternalization.Stream._d_end_context, "flush": _0_CosExternalization.Stream._d_flush}
    _omni_op_d.update(_0_CosLifeCycle__POA.LifeCycleObject._omni_op_d)

Stream._omni_skeleton = Stream
_0_CosExternalization__POA.Stream = Stream
omniORB.registerSkeleton(Stream._NP_RepositoryId, Stream)
del Stream
__name__ = "CosExternalization"

# interface StreamFactory
_0_CosExternalization._d_StreamFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosExternalization/StreamFactory:1.0", "StreamFactory")
omniORB.typeMapping["IDL:omg.org/CosExternalization/StreamFactory:1.0"] = _0_CosExternalization._d_StreamFactory
_0_CosExternalization.StreamFactory = omniORB.newEmptyClass()
class StreamFactory :
    _NP_RepositoryId = _0_CosExternalization._d_StreamFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosExternalization.StreamFactory = StreamFactory
_0_CosExternalization._tc_StreamFactory = omniORB.tcInternal.createTypeCode(_0_CosExternalization._d_StreamFactory)
omniORB.registerType(StreamFactory._NP_RepositoryId, _0_CosExternalization._d_StreamFactory, _0_CosExternalization._tc_StreamFactory)

# StreamFactory operations and attributes
StreamFactory._d_create = ((), (omniORB.typeMapping["IDL:omg.org/CosExternalization/Stream:1.0"], ), None)

# StreamFactory object reference
class _objref_StreamFactory (CORBA.Object):
    _NP_RepositoryId = StreamFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def create(self, *args):
        return self._obj.invoke("create", _0_CosExternalization.StreamFactory._d_create, args)

omniORB.registerObjref(StreamFactory._NP_RepositoryId, _objref_StreamFactory)
_0_CosExternalization._objref_StreamFactory = _objref_StreamFactory
del StreamFactory, _objref_StreamFactory

# StreamFactory skeleton
__name__ = "CosExternalization__POA"
class StreamFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_CosExternalization.StreamFactory._NP_RepositoryId


    _omni_op_d = {"create": _0_CosExternalization.StreamFactory._d_create}

StreamFactory._omni_skeleton = StreamFactory
_0_CosExternalization__POA.StreamFactory = StreamFactory
omniORB.registerSkeleton(StreamFactory._NP_RepositoryId, StreamFactory)
del StreamFactory
__name__ = "CosExternalization"

# interface FileStreamFactory
_0_CosExternalization._d_FileStreamFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosExternalization/FileStreamFactory:1.0", "FileStreamFactory")
omniORB.typeMapping["IDL:omg.org/CosExternalization/FileStreamFactory:1.0"] = _0_CosExternalization._d_FileStreamFactory
_0_CosExternalization.FileStreamFactory = omniORB.newEmptyClass()
class FileStreamFactory :
    _NP_RepositoryId = _0_CosExternalization._d_FileStreamFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosExternalization.FileStreamFactory = FileStreamFactory
_0_CosExternalization._tc_FileStreamFactory = omniORB.tcInternal.createTypeCode(_0_CosExternalization._d_FileStreamFactory)
omniORB.registerType(FileStreamFactory._NP_RepositoryId, _0_CosExternalization._d_FileStreamFactory, _0_CosExternalization._tc_FileStreamFactory)

# FileStreamFactory operations and attributes
FileStreamFactory._d_create = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:omg.org/CosExternalization/Stream:1.0"], ), {_0_CosExternalization.InvalidFileNameError._NP_RepositoryId: _0_CosExternalization._d_InvalidFileNameError})

# FileStreamFactory object reference
class _objref_FileStreamFactory (CORBA.Object):
    _NP_RepositoryId = FileStreamFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def create(self, *args):
        return self._obj.invoke("create", _0_CosExternalization.FileStreamFactory._d_create, args)

omniORB.registerObjref(FileStreamFactory._NP_RepositoryId, _objref_FileStreamFactory)
_0_CosExternalization._objref_FileStreamFactory = _objref_FileStreamFactory
del FileStreamFactory, _objref_FileStreamFactory

# FileStreamFactory skeleton
__name__ = "CosExternalization__POA"
class FileStreamFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_CosExternalization.FileStreamFactory._NP_RepositoryId


    _omni_op_d = {"create": _0_CosExternalization.FileStreamFactory._d_create}

FileStreamFactory._omni_skeleton = FileStreamFactory
_0_CosExternalization__POA.FileStreamFactory = FileStreamFactory
omniORB.registerSkeleton(FileStreamFactory._NP_RepositoryId, FileStreamFactory)
del FileStreamFactory
__name__ = "CosExternalization"

#
# End of module "CosExternalization"
#
__name__ = "CosExternalization_idl"

_exported_modules = ( "CosExternalization", )

# The end.
