"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import typing

import google.protobuf.descriptor
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing_extensions

import ondewo.nlu.common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class EntityTypeView(_EntityTypeView, metaclass=_EntityTypeViewEnumTypeWrapper):
    """Represents the options for views of an entity type.
    An entity type can be a sizable object. Therefore, we provide a resource view that
    does not return all values and synonyms besides the full view that is set by default.
    """
    pass
class _EntityTypeView:
    V = typing.NewType('V', builtins.int)
class _EntityTypeViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EntityTypeView.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ENTITY_TYPE_VIEW_UNSPECIFIED = EntityTypeView.V(0)
    """Same as ENTITY_TYPE_VIEW_FULL"""

    ENTITY_TYPE_VIEW_FULL = EntityTypeView.V(1)
    """All fields are populated."""

    ENTITY_TYPE_VIEW_PARTIAL = EntityTypeView.V(2)
    """The amount of entity values and synonyms is limited"""

    ENTITY_TYPE_VIEW_SHALLOW = EntityTypeView.V(3)
    """No entity synonyms are returned, only entity values"""


ENTITY_TYPE_VIEW_UNSPECIFIED = EntityTypeView.V(0)
"""Same as ENTITY_TYPE_VIEW_FULL"""

ENTITY_TYPE_VIEW_FULL = EntityTypeView.V(1)
"""All fields are populated."""

ENTITY_TYPE_VIEW_PARTIAL = EntityTypeView.V(2)
"""The amount of entity values and synonyms is limited"""

ENTITY_TYPE_VIEW_SHALLOW = EntityTypeView.V(3)
"""No entity synonyms are returned, only entity values"""

global___EntityTypeView = EntityTypeView


class EntityTypeCategory(_EntityTypeCategory, metaclass=_EntityTypeCategoryEnumTypeWrapper):
    """Represents the category of entity types to filter by in the "List Entity Types" request"""
    pass
class _EntityTypeCategory:
    V = typing.NewType('V', builtins.int)
class _EntityTypeCategoryEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EntityTypeCategory.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ALL_ENTITY_TYPES = EntityTypeCategory.V(0)
    """represent all entity types"""

    DEFAULT_ENTITY_TYPES = EntityTypeCategory.V(1)
    """represent the default entity types"""

    USER_DEFINED_ENTITY_TYPES = EntityTypeCategory.V(2)
    """represent the user defined (custom) entity types"""


ALL_ENTITY_TYPES = EntityTypeCategory.V(0)
"""represent all entity types"""

DEFAULT_ENTITY_TYPES = EntityTypeCategory.V(1)
"""represent the default entity types"""

USER_DEFINED_ENTITY_TYPES = EntityTypeCategory.V(2)
"""represent the user defined (custom) entity types"""

global___EntityTypeCategory = EntityTypeCategory


class EntityType(google.protobuf.message.Message):
    """Represents an entity type.
    Entity types serve as a tool for extracting parameter values from natural
    language queries.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Kind(_Kind, metaclass=_KindEnumTypeWrapper):
        """Represents kinds of entities."""
        pass
    class _Kind:
        V = typing.NewType('V', builtins.int)
    class _KindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Kind.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        KIND_UNSPECIFIED = EntityType.Kind.V(0)
        """Not specified. This value should be never used."""

        KIND_MAP = EntityType.Kind.V(1)
        """Map entity types allow mapping of a group of synonyms to a canonical
        value.
        """

        KIND_LIST = EntityType.Kind.V(2)
        """List entity types contain a set of entries that do not map to canonical
        values. However, list entity types can contain references to other entity
        types (with or without aliases).
        """


    KIND_UNSPECIFIED = EntityType.Kind.V(0)
    """Not specified. This value should be never used."""

    KIND_MAP = EntityType.Kind.V(1)
    """Map entity types allow mapping of a group of synonyms to a canonical
    value.
    """

    KIND_LIST = EntityType.Kind.V(2)
    """List entity types contain a set of entries that do not map to canonical
    values. However, list entity types can contain references to other entity
    types (with or without aliases).
    """


    class EntityTypeStatus(_EntityTypeStatus, metaclass=_EntityTypeStatusEnumTypeWrapper):
        pass
    class _EntityTypeStatus:
        V = typing.NewType('V', builtins.int)
    class _EntityTypeStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EntityTypeStatus.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        ACTIVE = EntityType.EntityTypeStatus.V(0)
        INACTIVE = EntityType.EntityTypeStatus.V(1)

    ACTIVE = EntityType.EntityTypeStatus.V(0)
    INACTIVE = EntityType.EntityTypeStatus.V(1)

    class AutoExpansionMode(_AutoExpansionMode, metaclass=_AutoExpansionModeEnumTypeWrapper):
        """Represents different entity type expansion modes. Automated expansion
        allows an agent to recognize values that have not been explicitly listed in
        the entity (for example, new kinds of shopping list items).
        """
        pass
    class _AutoExpansionMode:
        V = typing.NewType('V', builtins.int)
    class _AutoExpansionModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AutoExpansionMode.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        AUTO_EXPANSION_MODE_UNSPECIFIED = EntityType.AutoExpansionMode.V(0)
        """Auto expansion disabled for the entity."""

        AUTO_EXPANSION_MODE_DEFAULT = EntityType.AutoExpansionMode.V(1)
        """Allows an agent to recognize values that have not been explicitly
        listed in the entity.
        """


    AUTO_EXPANSION_MODE_UNSPECIFIED = EntityType.AutoExpansionMode.V(0)
    """Auto expansion disabled for the entity."""

    AUTO_EXPANSION_MODE_DEFAULT = EntityType.AutoExpansionMode.V(1)
    """Allows an agent to recognize values that have not been explicitly
    listed in the entity.
    """


    class Entity(google.protobuf.message.Message):
        """Optional. Represents an entity."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        VALUE_FIELD_NUMBER: builtins.int
        SYNONYMS_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        DISPLAY_NAME_FIELD_NUMBER: builtins.int
        SYNONYM_COUNT_FIELD_NUMBER: builtins.int
        LANGUAGE_CODE_FIELD_NUMBER: builtins.int
        value: typing.Text = ...
        """Required.
        For `KIND_MAP` entity types:
          A canonical name to be used in place of synonyms.
        For `KIND_LIST` entity types:
          A string that can contain references to other entity types (with or
          without aliases).
        """

        @property
        def synonyms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """Required. A collection of synonyms. For `KIND_LIST` entity types this
            must contain exactly one synonym equal to `value`.
            """
            pass
        name: typing.Text = ...
        """The unique identifier of the entity. Format:
        `projects/<Project ID>/agent/entityTypes/<Entity Type ID>/entities/<Entity ID>`.
        """

        display_name: typing.Text = ...
        """The name of the entity."""

        synonym_count: builtins.int = ...
        """Optional. Total count of entity synonyms"""

        language_code: typing.Text = ...
        """Required. The language to list entity synonyms for."""

        def __init__(self,
            *,
            value : typing.Text = ...,
            synonyms : typing.Optional[typing.Iterable[typing.Text]] = ...,
            name : typing.Text = ...,
            display_name : typing.Text = ...,
            synonym_count : builtins.int = ...,
            language_code : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name","language_code",b"language_code","name",b"name","synonym_count",b"synonym_count","synonyms",b"synonyms","value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    AUTO_EXPANSION_MODE_FIELD_NUMBER: builtins.int
    ENTITIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ENTITY_COUNT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    SYNONYM_COUNT_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required for all methods except `create` (`create` populates the name
    automatically.
    The unique identifier of the entity type. Format:
    `projects/<Project ID>/agent/entityTypes/<Entity Type ID>`.
    """

    display_name: typing.Text = ...
    """Required. The name of the entity type."""

    kind: global___EntityType.Kind.V = ...
    """Required. Indicates the kind of entity type."""

    auto_expansion_mode: global___EntityType.AutoExpansionMode.V = ...
    """Optional. Indicates whether the entity type can be automatically
    expanded.
    """

    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityType.Entity]:
        """Optional. The collection of entities associated with the entity type."""
        pass
    next_page_token: typing.Text = ...
    entity_count: builtins.int = ...
    """Read-Only field. Total count of entity values of the entity type"""

    status: global___EntityType.EntityTypeStatus.V = ...
    """Indicates whether the entity type is active or not"""

    synonym_count: builtins.int = ...
    """Read-Only field. Total count of entity synonyms of the entity type"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        kind : global___EntityType.Kind.V = ...,
        auto_expansion_mode : global___EntityType.AutoExpansionMode.V = ...,
        entities : typing.Optional[typing.Iterable[global___EntityType.Entity]] = ...,
        next_page_token : typing.Text = ...,
        entity_count : builtins.int = ...,
        status : global___EntityType.EntityTypeStatus.V = ...,
        synonym_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_expansion_mode",b"auto_expansion_mode","display_name",b"display_name","entities",b"entities","entity_count",b"entity_count","kind",b"kind","name",b"name","next_page_token",b"next_page_token","status",b"status","synonym_count",b"synonym_count"]) -> None: ...
global___EntityType = EntityType

class ListEntityTypesRequest(google.protobuf.message.Message):
    """The request message for [EntityTypes.ListEntityTypes][google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_VIEW_FIELD_NUMBER: builtins.int
    FILTER_BY_CATEGORY_FIELD_NUMBER: builtins.int
    SORT_BY_FIELD_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The agent to list all entity types from.
    Format: `projects/<Project ID>/agent`.
    """

    language_code: typing.Text = ...
    """Optional. The language to list entity synonyms for. If not specified,
    the agent's default language is used.
    [More than a dozen
    languages](https://dialogflow.com/docs/reference/language) are supported.
    Note: languages must be enabled in the agent, before they can be used.
    """

    page_token: typing.Text = ...
    """Optional. The next_page_token value returned from a previous list request."""

    entity_type_view: global___EntityTypeView.V = ...
    """Optional. The resource view to apply to the returned entity type."""

    filter_by_category: global___EntityTypeCategory.V = ...
    """Optional. Applies a filter to the list. Default, no filter."""

    @property
    def sort_by_field(self) -> global___EntityTypeSorting:
        """Optional. Defines the sorting of the list. Default, no sorting."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        language_code : typing.Text = ...,
        page_token : typing.Text = ...,
        entity_type_view : global___EntityTypeView.V = ...,
        filter_by_category : global___EntityTypeCategory.V = ...,
        sort_by_field : typing.Optional[global___EntityTypeSorting] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["sort_by_field",b"sort_by_field"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_type_view",b"entity_type_view","filter_by_category",b"filter_by_category","language_code",b"language_code","page_token",b"page_token","parent",b"parent","sort_by_field",b"sort_by_field"]) -> None: ...
global___ListEntityTypesRequest = ListEntityTypesRequest

class ListEntityTypesResponse(google.protobuf.message.Message):
    """The response message for [EntityTypes.ListEntityTypes][google.cloud.dialogflow.v2.EntityTypes.ListEntityTypes]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_TYPES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def entity_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityType]:
        """The list of agent entity types. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        entity_types : typing.Optional[typing.Iterable[global___EntityType]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_types",b"entity_types","next_page_token",b"next_page_token"]) -> None: ...
global___ListEntityTypesResponse = ListEntityTypesResponse

class GetEntityTypeRequest(google.protobuf.message.Message):
    """The request message for [EntityTypes.GetEntityType][google.cloud.dialogflow.v2.EntityTypes.GetEntityType]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the entity type.
    Format: `projects/<Project ID>/agent/entityTypes/<EntityType ID>`.
    """

    language_code: typing.Text = ...
    """Optional. The language to retrieve entity synonyms for. If not specified,
    the agent's default language is used.
    [More than a dozen
    languages](https://dialogflow.com/docs/reference/language) are supported.
    Note: languages must be enabled in the agent, before they can be used.
    """

    page_token: typing.Text = ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        language_code : typing.Text = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language_code",b"language_code","name",b"name","page_token",b"page_token"]) -> None: ...
global___GetEntityTypeRequest = GetEntityTypeRequest

class CreateEntityTypeRequest(google.protobuf.message.Message):
    """The request message for [EntityTypes.CreateEntityType][google.cloud.dialogflow.v2.EntityTypes.CreateEntityType]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The agent to create a entity type for.
    Format: `projects/<Project ID>/agent`.
    """

    @property
    def entity_type(self) -> global___EntityType:
        """Required. The entity type to create."""
        pass
    language_code: typing.Text = ...
    """Optional. The language of entity synonyms defined in `entity_type`. If not
    specified, the agent's default language is used.
    [More than a dozen
    languages](https://dialogflow.com/docs/reference/language) are supported.
    Note: languages must be enabled in the agent, before they can be used.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        entity_type : typing.Optional[global___EntityType] = ...,
        language_code : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity_type",b"entity_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_type",b"entity_type","language_code",b"language_code","parent",b"parent"]) -> None: ...
global___CreateEntityTypeRequest = CreateEntityTypeRequest

class UpdateEntityTypeRequest(google.protobuf.message.Message):
    """The request message for [EntityTypes.UpdateEntityType][google.cloud.dialogflow.v2.EntityTypes.UpdateEntityType]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def entity_type(self) -> global___EntityType:
        """Required. The entity type to update.
        Format: `projects/<Project ID>/agent/entityTypes/<EntityType ID>`.
        """
        pass
    language_code: typing.Text = ...
    """Optional. The language of entity synonyms defined in `entity_type`. If not
    specified, the agent's default language is used.
    [More than a dozen
    languages](https://dialogflow.com/docs/reference/language) are supported.
    Note: languages must be enabled in the agent, before they can be used.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""
        pass
    def __init__(self,
        *,
        entity_type : typing.Optional[global___EntityType] = ...,
        language_code : typing.Text = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity_type",b"entity_type","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_type",b"entity_type","language_code",b"language_code","update_mask",b"update_mask"]) -> None: ...
global___UpdateEntityTypeRequest = UpdateEntityTypeRequest

class DeleteEntityTypeRequest(google.protobuf.message.Message):
    """The request message for [EntityTypes.DeleteEntityType][google.cloud.dialogflow.v2.EntityTypes.DeleteEntityType]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the entity type to delete.
    Format: `projects/<Project ID>/agent/entityTypes/<EntityType ID>`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteEntityTypeRequest = DeleteEntityTypeRequest

class BatchUpdateEntityTypesRequest(google.protobuf.message.Message):
    """The request message for [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_BATCH_URI_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_BATCH_INLINE_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the agent to update or create entity types in.
    Format: `projects/<Project ID>/agent`.
    """

    entity_type_batch_uri: typing.Text = ...
    """The URI to a Google Cloud Storage file containing entity types to update
    or create. The file format can either be a serialized proto (of
    EntityBatch type) or a JSON object. Note: The URI must start with
    "gs://".
    """

    @property
    def entity_type_batch_inline(self) -> global___EntityTypeBatch:
        """The collection of entity type to update or create."""
        pass
    language_code: typing.Text = ...
    """Optional. The language of entity synonyms defined in `entity_types`. If not
    specified, the agent's default language is used.
    [More than a dozen
    languages](https://dialogflow.com/docs/reference/language) are supported.
    Note: languages must be enabled in the agent, before they can be used.
    """

    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        entity_type_batch_uri : typing.Text = ...,
        entity_type_batch_inline : typing.Optional[global___EntityTypeBatch] = ...,
        language_code : typing.Text = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity_type_batch",b"entity_type_batch","entity_type_batch_inline",b"entity_type_batch_inline","entity_type_batch_uri",b"entity_type_batch_uri","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_type_batch",b"entity_type_batch","entity_type_batch_inline",b"entity_type_batch_inline","entity_type_batch_uri",b"entity_type_batch_uri","language_code",b"language_code","parent",b"parent","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["entity_type_batch",b"entity_type_batch"]) -> typing.Optional[typing_extensions.Literal["entity_type_batch_uri","entity_type_batch_inline"]]: ...
global___BatchUpdateEntityTypesRequest = BatchUpdateEntityTypesRequest

class BatchUpdateEntityTypesResponse(google.protobuf.message.Message):
    """The response message for [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchUpdateEntityTypes]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_TYPES_FIELD_NUMBER: builtins.int
    @property
    def entity_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityType]:
        """The collection of updated or created entity types."""
        pass
    def __init__(self,
        *,
        entity_types : typing.Optional[typing.Iterable[global___EntityType]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_types",b"entity_types"]) -> None: ...
global___BatchUpdateEntityTypesResponse = BatchUpdateEntityTypesResponse

class BatchDeleteEntityTypesRequest(google.protobuf.message.Message):
    """The request message for [EntityTypes.BatchDeleteEntityTypes][google.cloud.dialogflow.v2.EntityTypes.BatchDeleteEntityTypes]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_NAMES_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the agent to delete all entities types for. Format:
    `projects/<Project ID>/agent`.
    """

    @property
    def entity_type_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Required. The names entity types to delete. All names must point to the
        same agent as `parent`.
        """
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        entity_type_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_type_names",b"entity_type_names","parent",b"parent"]) -> None: ...
global___BatchDeleteEntityTypesRequest = BatchDeleteEntityTypesRequest

class EntityTypeBatch(google.protobuf.message.Message):
    """This message is a wrapper around a collection of entity types."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_TYPES_FIELD_NUMBER: builtins.int
    @property
    def entity_types(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityType]:
        """A collection of entity types."""
        pass
    def __init__(self,
        *,
        entity_types : typing.Optional[typing.Iterable[global___EntityType]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_types",b"entity_types"]) -> None: ...
global___EntityTypeBatch = EntityTypeBatch

class EntityTypeSorting(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class EntityTypeSortingField(_EntityTypeSortingField, metaclass=_EntityTypeSortingFieldEnumTypeWrapper):
        pass
    class _EntityTypeSortingField:
        V = typing.NewType('V', builtins.int)
    class _EntityTypeSortingFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EntityTypeSortingField.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        NO_ENTITY_TYPE_SORTING = EntityTypeSorting.EntityTypeSortingField.V(0)
        SORT_ENTITY_TYPE_BY_NAME = EntityTypeSorting.EntityTypeSortingField.V(1)
        SORT_ENTITY_TYPE_BY_CREATION_DATE = EntityTypeSorting.EntityTypeSortingField.V(2)
        SORT_ENTITY_TYPE_BY_LAST_UPDATED = EntityTypeSorting.EntityTypeSortingField.V(3)
        SORT_ENTITY_TYPE_BY_ENTITY_VALUE_COUNT = EntityTypeSorting.EntityTypeSortingField.V(4)
        SORT_ENTITY_TYPE_BY_SYNONYM_COUNT = EntityTypeSorting.EntityTypeSortingField.V(5)

    NO_ENTITY_TYPE_SORTING = EntityTypeSorting.EntityTypeSortingField.V(0)
    SORT_ENTITY_TYPE_BY_NAME = EntityTypeSorting.EntityTypeSortingField.V(1)
    SORT_ENTITY_TYPE_BY_CREATION_DATE = EntityTypeSorting.EntityTypeSortingField.V(2)
    SORT_ENTITY_TYPE_BY_LAST_UPDATED = EntityTypeSorting.EntityTypeSortingField.V(3)
    SORT_ENTITY_TYPE_BY_ENTITY_VALUE_COUNT = EntityTypeSorting.EntityTypeSortingField.V(4)
    SORT_ENTITY_TYPE_BY_SYNONYM_COUNT = EntityTypeSorting.EntityTypeSortingField.V(5)

    SORTING_FIELD_FIELD_NUMBER: builtins.int
    SORTING_MODE_FIELD_NUMBER: builtins.int
    sorting_field: global___EntityTypeSorting.EntityTypeSortingField.V = ...
    sorting_mode: ondewo.nlu.common_pb2.SortingMode.V = ...
    def __init__(self,
        *,
        sorting_field : global___EntityTypeSorting.EntityTypeSortingField.V = ...,
        sorting_mode : ondewo.nlu.common_pb2.SortingMode.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sorting_field",b"sorting_field","sorting_mode",b"sorting_mode"]) -> None: ...
global___EntityTypeSorting = EntityTypeSorting

class BatchEntitiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class EntityStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ENTITY_FIELD_NUMBER: builtins.int
        ERROR_MESSAGE_FIELD_NUMBER: builtins.int
        @property
        def entity(self) -> global___EntityType.Entity: ...
        error_message: typing.Text = ...
        def __init__(self,
            *,
            entity : typing.Optional[global___EntityType.Entity] = ...,
            error_message : typing.Text = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["entity",b"entity","entity_or_status",b"entity_or_status","error_message",b"error_message"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["entity",b"entity","entity_or_status",b"entity_or_status","error_message",b"error_message"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["entity_or_status",b"entity_or_status"]) -> typing.Optional[typing_extensions.Literal["entity","error_message"]]: ...

    ENTITY_STATUSES_FIELD_NUMBER: builtins.int
    HAS_ERRORS_FIELD_NUMBER: builtins.int
    @property
    def entity_statuses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BatchEntitiesResponse.EntityStatus]: ...
    has_errors: builtins.bool = ...
    """indicates if statuses of some of the training phrases have errors"""

    def __init__(self,
        *,
        entity_statuses : typing.Optional[typing.Iterable[global___BatchEntitiesResponse.EntityStatus]] = ...,
        has_errors : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_statuses",b"entity_statuses","has_errors",b"has_errors"]) -> None: ...
global___BatchEntitiesResponse = BatchEntitiesResponse

class BatchCreateEntitiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class CreateEntityRequest(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ENTITY_TYPE_NAME_FIELD_NUMBER: builtins.int
        ENTITY_FIELD_NUMBER: builtins.int
        entity_type_name: typing.Text = ...
        """Required. Name of the entity type in which to create the entity value. Format:
        `projects/<Project ID>/agent/entityTypes/<Entity Type ID>`.
        """

        @property
        def entity(self) -> global___EntityType.Entity:
            """The entity value to create"""
            pass
        def __init__(self,
            *,
            entity_type_name : typing.Text = ...,
            entity : typing.Optional[global___EntityType.Entity] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["entity",b"entity"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["entity",b"entity","entity_type_name",b"entity_type_name"]) -> None: ...

    CREATE_ENTITY_REQUESTS_FIELD_NUMBER: builtins.int
    @property
    def create_entity_requests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BatchCreateEntitiesRequest.CreateEntityRequest]: ...
    def __init__(self,
        *,
        create_entity_requests : typing.Optional[typing.Iterable[global___BatchCreateEntitiesRequest.CreateEntityRequest]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_entity_requests",b"create_entity_requests"]) -> None: ...
global___BatchCreateEntitiesRequest = BatchCreateEntitiesRequest

class BatchUpdateEntitiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITIES_FIELD_NUMBER: builtins.int
    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityType.Entity]:
        """The entities to update"""
        pass
    def __init__(self,
        *,
        entities : typing.Optional[typing.Iterable[global___EntityType.Entity]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entities",b"entities"]) -> None: ...
global___BatchUpdateEntitiesRequest = BatchUpdateEntitiesRequest

class BatchGetEntitiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMES_FIELD_NUMBER: builtins.int
    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The unique identifiers of the entities. Format:
        `projects/<Project ID>/agent/entityTypes/<Entity Type ID>/entities/<Entity ID>`.
        """
        pass
    def __init__(self,
        *,
        names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["names",b"names"]) -> None: ...
global___BatchGetEntitiesRequest = BatchGetEntitiesRequest

class BatchDeleteEntitiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMES_FIELD_NUMBER: builtins.int
    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The unique identifiers of the entities. Format:
        `projects/<Project ID>/agent/entityTypes/<Entity Type ID>/entities/<Entity ID>`.
        """
        pass
    def __init__(self,
        *,
        names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["names",b"names"]) -> None: ...
global___BatchDeleteEntitiesRequest = BatchDeleteEntitiesRequest

class BatchDeleteEntitiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class DeleteEntityStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        SUCCESSFULLY_DELETED_FIELD_NUMBER: builtins.int
        ERROR_MESSAGE_FIELD_NUMBER: builtins.int
        @property
        def successfully_deleted(self) -> google.protobuf.empty_pb2.Empty: ...
        error_message: typing.Text = ...
        def __init__(self,
            *,
            successfully_deleted : typing.Optional[google.protobuf.empty_pb2.Empty] = ...,
            error_message : typing.Text = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["delete_status",b"delete_status","error_message",b"error_message","successfully_deleted",b"successfully_deleted"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["delete_status",b"delete_status","error_message",b"error_message","successfully_deleted",b"successfully_deleted"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["delete_status",b"delete_status"]) -> typing.Optional[typing_extensions.Literal["successfully_deleted","error_message"]]: ...

    DELETE_STATUSES_FIELD_NUMBER: builtins.int
    HAS_ERRORS_FIELD_NUMBER: builtins.int
    @property
    def delete_statuses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BatchDeleteEntitiesResponse.DeleteEntityStatus]: ...
    has_errors: builtins.bool = ...
    def __init__(self,
        *,
        delete_statuses : typing.Optional[typing.Iterable[global___BatchDeleteEntitiesResponse.DeleteEntityStatus]] = ...,
        has_errors : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delete_statuses",b"delete_statuses","has_errors",b"has_errors"]) -> None: ...
global___BatchDeleteEntitiesResponse = BatchDeleteEntitiesResponse

class ListEntitiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITY_TYPE_NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_VIEW_FIELD_NUMBER: builtins.int
    entity_type_name: typing.Text = ...
    """The unique identifier of the entity type. Format:
    `projects/<Project ID>/agent/entityTypes/<Entity Type ID>
    """

    language_code: typing.Text = ...
    """Optional. The language to list training phrases, parameters and rich
    messages for. If not specified, the agent's default language is used.
    """

    page_token: typing.Text = ...
    """Optional. The next_page_token value returned from a previous list request."""

    entity_type_view: global___EntityTypeView.V = ...
    """Optional. The resource view to apply to the returned entity type."""

    def __init__(self,
        *,
        entity_type_name : typing.Text = ...,
        language_code : typing.Text = ...,
        page_token : typing.Text = ...,
        entity_type_view : global___EntityTypeView.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_type_name",b"entity_type_name","entity_type_view",b"entity_type_view","language_code",b"language_code","page_token",b"page_token"]) -> None: ...
global___ListEntitiesRequest = ListEntitiesRequest

class ListEntitiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTITIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityType.Entity]:
        """The list of entities"""
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        entities : typing.Optional[typing.Iterable[global___EntityType.Entity]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entities",b"entities","next_page_token",b"next_page_token"]) -> None: ...
global___ListEntitiesResponse = ListEntitiesResponse
