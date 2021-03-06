# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/pokemon/lobby_pokemon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/pokemon/lobby_pokemon.proto',
  package='pogoprotos.map.pokemon',
  syntax='proto3',
  serialized_pb=_b('\n*pogoprotos/map/pokemon/lobby_pokemon.proto\x12\x16pogoprotos.map.pokemon\x1a!pogoprotos/enums/pokemon_id.proto\"o\n\x0cLobbyPokemon\x12\n\n\x02id\x18\x01 \x01(\x03\x12/\n\npokedex_id\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\n\n\x02\x63p\x18\x03 \x01(\x05\x12\x16\n\x0epercent_health\x18\x04 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOBBYPOKEMON = _descriptor.Descriptor(
  name='LobbyPokemon',
  full_name='pogoprotos.map.pokemon.LobbyPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.map.pokemon.LobbyPokemon.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_id', full_name='pogoprotos.map.pokemon.LobbyPokemon.pokedex_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp', full_name='pogoprotos.map.pokemon.LobbyPokemon.cp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='percent_health', full_name='pogoprotos.map.pokemon.LobbyPokemon.percent_health', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=216,
)

_LOBBYPOKEMON.fields_by_name['pokedex_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
DESCRIPTOR.message_types_by_name['LobbyPokemon'] = _LOBBYPOKEMON

LobbyPokemon = _reflection.GeneratedProtocolMessageType('LobbyPokemon', (_message.Message,), dict(
  DESCRIPTOR = _LOBBYPOKEMON,
  __module__ = 'pogoprotos.map.pokemon.lobby_pokemon_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.pokemon.LobbyPokemon)
  ))
_sym_db.RegisterMessage(LobbyPokemon)


# @@protoc_insertion_point(module_scope)
