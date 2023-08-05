# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: extracted.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='extracted.proto',
    package='',
    syntax='proto2',
    serialized_pb=_b(
        '\n\x0f\x65xtracted.proto\":\n\x1blink_extracted_extra_header\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"4\n\x15link_extracted_cookie\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"F\n\x19link_extracted_form_input\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x03 \x02(\t\"R\n\x13link_extracted_form\x12*\n\x06inputs\x18\x01 \x03(\x0b\x32\x1a.link_extracted_form_input\x12\x0f\n\x07\x65nctype\x18\x02 \x02(\t\"R\n\x14\x65xtracted_credential\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\r\n\x05login\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\"\xb3\x02\n\textracted\x12\x0f\n\x07scan_id\x18\x01 \x02(\x05\x12\x0f\n\x07link_id\x18\x02 \x01(\x05\x12\x0b\n\x03url\x18\x03 \x02(\t\x12\x0e\n\x06method\x18\x04 \x02(\t\x12\x0e\n\x04\x62ody\x18\x05 \x01(\x0cH\x00\x12$\n\x04\x66orm\x18\x06 \x01(\x0b\x32\x14.link_extracted_formH\x00\x12\x33\n\rextra_headers\x18\x07 \x03(\x0b\x32\x1c.link_extracted_extra_header\x12\'\n\x07\x63ookies\x18\x08 \x03(\x0b\x32\x16.link_extracted_cookie\x12)\n\ncredential\x18\t \x01(\x0b\x32\x15.extracted_credential\x12\x1a\n\x06parent\x18\n \x01(\x0b\x32\n.extractedB\x0c\n\nbody_oneof')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LINK_EXTRACTED_EXTRA_HEADER = _descriptor.Descriptor(
    name='link_extracted_extra_header',
    full_name='link_extracted_extra_header',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='link_extracted_extra_header.name', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value', full_name='link_extracted_extra_header.value', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=19,
    serialized_end=77,
)

_LINK_EXTRACTED_COOKIE = _descriptor.Descriptor(
    name='link_extracted_cookie',
    full_name='link_extracted_cookie',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='link_extracted_cookie.name', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value', full_name='link_extracted_cookie.value', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=79,
    serialized_end=131,
)

_LINK_EXTRACTED_FORM_INPUT = _descriptor.Descriptor(
    name='link_extracted_form_input',
    full_name='link_extracted_form_input',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='link_extracted_form_input.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value', full_name='link_extracted_form_input.value', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='type', full_name='link_extracted_form_input.type', index=2,
            number=3, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=133,
    serialized_end=203,
)

_LINK_EXTRACTED_FORM = _descriptor.Descriptor(
    name='link_extracted_form',
    full_name='link_extracted_form',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='inputs', full_name='link_extracted_form.inputs', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='enctype', full_name='link_extracted_form.enctype', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=205,
    serialized_end=287,
)

_EXTRACTED_CREDENTIAL = _descriptor.Descriptor(
    name='extracted_credential',
    full_name='extracted_credential',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='extracted_credential.type', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='login', full_name='extracted_credential.login', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='password', full_name='extracted_credential.password', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='url', full_name='extracted_credential.url', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=289,
    serialized_end=371,
)

_EXTRACTED = _descriptor.Descriptor(
    name='extracted',
    full_name='extracted',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='scan_id', full_name='extracted.scan_id', index=0,
            number=1, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='link_id', full_name='extracted.link_id', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='url', full_name='extracted.url', index=2,
            number=3, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='method', full_name='extracted.method', index=3,
            number=4, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='body', full_name='extracted.body', index=4,
            number=5, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='form', full_name='extracted.form', index=5,
            number=6, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='extra_headers', full_name='extracted.extra_headers', index=6,
            number=7, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='cookies', full_name='extracted.cookies', index=7,
            number=8, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='credential', full_name='extracted.credential', index=8,
            number=9, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='parent', full_name='extracted.parent', index=9,
            number=10, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name='body_oneof', full_name='extracted.body_oneof',
            index=0, containing_type=None, fields=[]),
    ],
    serialized_start=374,
    serialized_end=681,
)

_LINK_EXTRACTED_FORM.fields_by_name['inputs'].message_type = _LINK_EXTRACTED_FORM_INPUT
_EXTRACTED.fields_by_name['form'].message_type = _LINK_EXTRACTED_FORM
_EXTRACTED.fields_by_name['extra_headers'].message_type = _LINK_EXTRACTED_EXTRA_HEADER
_EXTRACTED.fields_by_name['cookies'].message_type = _LINK_EXTRACTED_COOKIE
_EXTRACTED.fields_by_name['credential'].message_type = _EXTRACTED_CREDENTIAL
_EXTRACTED.fields_by_name['parent'].message_type = _EXTRACTED
_EXTRACTED.oneofs_by_name['body_oneof'].fields.append(
    _EXTRACTED.fields_by_name['body'])
_EXTRACTED.fields_by_name['body'].containing_oneof = _EXTRACTED.oneofs_by_name['body_oneof']
_EXTRACTED.oneofs_by_name['body_oneof'].fields.append(
    _EXTRACTED.fields_by_name['form'])
_EXTRACTED.fields_by_name['form'].containing_oneof = _EXTRACTED.oneofs_by_name['body_oneof']
DESCRIPTOR.message_types_by_name['link_extracted_extra_header'] = _LINK_EXTRACTED_EXTRA_HEADER
DESCRIPTOR.message_types_by_name['link_extracted_cookie'] = _LINK_EXTRACTED_COOKIE
DESCRIPTOR.message_types_by_name['link_extracted_form_input'] = _LINK_EXTRACTED_FORM_INPUT
DESCRIPTOR.message_types_by_name['link_extracted_form'] = _LINK_EXTRACTED_FORM
DESCRIPTOR.message_types_by_name['extracted_credential'] = _EXTRACTED_CREDENTIAL
DESCRIPTOR.message_types_by_name['extracted'] = _EXTRACTED

link_extracted_extra_header = _reflection.GeneratedProtocolMessageType('link_extracted_extra_header',
                                                                       (_message.Message,), dict(
        DESCRIPTOR=_LINK_EXTRACTED_EXTRA_HEADER,
        __module__='extracted_pb2'
        # @@protoc_insertion_point(class_scope:link_extracted_extra_header)
    ))
_sym_db.RegisterMessage(link_extracted_extra_header)

link_extracted_cookie = _reflection.GeneratedProtocolMessageType('link_extracted_cookie', (_message.Message,), dict(
    DESCRIPTOR=_LINK_EXTRACTED_COOKIE,
    __module__='extracted_pb2'
    # @@protoc_insertion_point(class_scope:link_extracted_cookie)
))
_sym_db.RegisterMessage(link_extracted_cookie)

link_extracted_form_input = _reflection.GeneratedProtocolMessageType('link_extracted_form_input', (_message.Message,),
                                                                     dict(
                                                                         DESCRIPTOR=_LINK_EXTRACTED_FORM_INPUT,
                                                                         __module__='extracted_pb2'
                                                                         # @@protoc_insertion_point(class_scope:link_extracted_form_input)
                                                                     ))
_sym_db.RegisterMessage(link_extracted_form_input)

link_extracted_form = _reflection.GeneratedProtocolMessageType('link_extracted_form', (_message.Message,), dict(
    DESCRIPTOR=_LINK_EXTRACTED_FORM,
    __module__='extracted_pb2'
    # @@protoc_insertion_point(class_scope:link_extracted_form)
))
_sym_db.RegisterMessage(link_extracted_form)

extracted_credential = _reflection.GeneratedProtocolMessageType('extracted_credential', (_message.Message,), dict(
    DESCRIPTOR=_EXTRACTED_CREDENTIAL,
    __module__='extracted_pb2'
    # @@protoc_insertion_point(class_scope:extracted_credential)
))
_sym_db.RegisterMessage(extracted_credential)

extracted = _reflection.GeneratedProtocolMessageType('extracted', (_message.Message,), dict(
    DESCRIPTOR=_EXTRACTED,
    __module__='extracted_pb2'
    # @@protoc_insertion_point(class_scope:extracted)
))
_sym_db.RegisterMessage(extracted)

# @@protoc_insertion_point(module_scope)
