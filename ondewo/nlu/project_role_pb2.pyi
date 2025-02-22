"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DefaultProjectRole:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _DefaultProjectRoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DefaultProjectRole.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PROJECT_UNSPECIFIED: _DefaultProjectRole.ValueType  # 0
    """These roles have permissions valid only on a specific project
    unspecified, default value depends on endpoint # TODO
    """

    PROJECT_USER: _DefaultProjectRole.ValueType  # 1
    """read-only access"""

    PROJECT_EXECUTOR: _DefaultProjectRole.ValueType  # 2
    """permissions of PROJECT_USER + execution rights (detect intent, extract entities,"""

    PROJECT_DEVELOPER: _DefaultProjectRole.ValueType  # 3
    """  train, etc)

    permissions of PROJECT_EXECUTOR + CRUD rights
    """

    PROJECT_ADMIN: _DefaultProjectRole.ValueType  # 4
    """this role can do everything. The creator of a project is set"""

    PROJECT_INACTIVE: _DefaultProjectRole.ValueType  # 5
    """   automatically as PROJECT_ADMIN of it.

    This role can do nothing.
    """

class DefaultProjectRole(_DefaultProjectRole, metaclass=_DefaultProjectRoleEnumTypeWrapper):
    pass

PROJECT_UNSPECIFIED: DefaultProjectRole.ValueType  # 0
"""These roles have permissions valid only on a specific project
unspecified, default value depends on endpoint # TODO
"""

PROJECT_USER: DefaultProjectRole.ValueType  # 1
"""read-only access"""

PROJECT_EXECUTOR: DefaultProjectRole.ValueType  # 2
"""permissions of PROJECT_USER + execution rights (detect intent, extract entities,"""

PROJECT_DEVELOPER: DefaultProjectRole.ValueType  # 3
"""  train, etc)

permissions of PROJECT_EXECUTOR + CRUD rights
"""

PROJECT_ADMIN: DefaultProjectRole.ValueType  # 4
"""this role can do everything. The creator of a project is set"""

PROJECT_INACTIVE: DefaultProjectRole.ValueType  # 5
"""   automatically as PROJECT_ADMIN of it.

This role can do nothing.
"""

global___DefaultProjectRole = DefaultProjectRole


class _ProjectRoleView:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ProjectRoleViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProjectRoleView.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PROJECT_ROLE_VIEW_UNSPECIFIED: _ProjectRoleView.ValueType  # 0
    """The view depends on the endpoint:
    * CreateProjectRole: FULL
    * GetProjectRole: FULL
    * UpdateProjectRole: FULL
    * ListProjectRoles: FULL
    """

    PROJECT_ROLE_VIEW_SHALLOW: _ProjectRoleView.ValueType  # 1
    """only role ID and name fields are populated"""

    PROJECT_ROLE_VIEW_FULL: _ProjectRoleView.ValueType  # 2
    """all fields including permissions are populated"""

class ProjectRoleView(_ProjectRoleView, metaclass=_ProjectRoleViewEnumTypeWrapper):
    pass

PROJECT_ROLE_VIEW_UNSPECIFIED: ProjectRoleView.ValueType  # 0
"""The view depends on the endpoint:
* CreateProjectRole: FULL
* GetProjectRole: FULL
* UpdateProjectRole: FULL
* ListProjectRoles: FULL
"""

PROJECT_ROLE_VIEW_SHALLOW: ProjectRoleView.ValueType  # 1
"""only role ID and name fields are populated"""

PROJECT_ROLE_VIEW_FULL: ProjectRoleView.ValueType  # 2
"""all fields including permissions are populated"""

global___ProjectRoleView = ProjectRoleView


class ProjectRole(google.protobuf.message.Message):
    """Project Role messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROLE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    role_id: builtins.int
    """unique identifier of the role"""

    name: typing.Text
    """unique name of the role"""

    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """defines the permissions for the given role (the strings can be gotten from the ListProjectPermissions)"""
        pass
    def __init__(self,
        *,
        role_id: builtins.int = ...,
        name: typing.Text = ...,
        permissions: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","permissions",b"permissions","role_id",b"role_id"]) -> None: ...
global___ProjectRole = ProjectRole

class CreateProjectRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    PROJECT_ROLE_VIEW_FIELD_NUMBER: builtins.int
    parent: typing.Text
    @property
    def role(self) -> global___ProjectRole:
        """If the role_id is not provided, an incremental value will be assigned
        The "name" and "role_type" are mandatory values
        The permissions all default to False if not provided specifically
        """
        pass
    project_role_view: global___ProjectRoleView.ValueType
    """Optional. specify the view of the created project role, PROJECT_ROLE_VIEW_FULL by default"""

    def __init__(self,
        *,
        parent: typing.Text = ...,
        role: typing.Optional[global___ProjectRole] = ...,
        project_role_view: global___ProjectRoleView.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["role",b"role"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","project_role_view",b"project_role_view","role",b"role"]) -> None: ...
global___CreateProjectRoleRequest = CreateProjectRoleRequest

class UpdateProjectRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    PROJECT_ROLE_VIEW_FIELD_NUMBER: builtins.int
    parent: typing.Text
    @property
    def role(self) -> global___ProjectRole:
        """role_id in the Role message should be given, if empty will throw an error in the backend
        other fields in the Role are optional. Only the fields to be updated should be provided
        """
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""
        pass
    project_role_view: global___ProjectRoleView.ValueType
    """Optional. specify the view of the updated project role, PROJECT_ROLE_VIEW_FULL by default"""

    def __init__(self,
        *,
        parent: typing.Text = ...,
        role: typing.Optional[global___ProjectRole] = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        project_role_view: global___ProjectRoleView.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["role",b"role","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","project_role_view",b"project_role_view","role",b"role","update_mask",b"update_mask"]) -> None: ...
global___UpdateProjectRoleRequest = UpdateProjectRoleRequest

class GetProjectRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    ROLE_ID_FIELD_NUMBER: builtins.int
    ROLE_NAME_FIELD_NUMBER: builtins.int
    PROJECT_ROLE_VIEW_FIELD_NUMBER: builtins.int
    parent: typing.Text
    role_id: builtins.int
    """role is identified by role id"""

    role_name: typing.Text
    """role can also be uniquely identified by its name"""

    project_role_view: global___ProjectRoleView.ValueType
    """Optional. specify the view of the project role, PROJECT_ROLE_VIEW_FULL by default"""

    def __init__(self,
        *,
        parent: typing.Text = ...,
        role_id: builtins.int = ...,
        role_name: typing.Text = ...,
        project_role_view: global___ProjectRoleView.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["project_role_identifier",b"project_role_identifier","role_id",b"role_id","role_name",b"role_name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","project_role_identifier",b"project_role_identifier","project_role_view",b"project_role_view","role_id",b"role_id","role_name",b"role_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["project_role_identifier",b"project_role_identifier"]) -> typing.Optional[typing_extensions.Literal["role_id","role_name"]]: ...
global___GetProjectRoleRequest = GetProjectRoleRequest

class DeleteProjectRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    ROLE_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text
    role_id: builtins.int
    """role is identified by role id, if empty will throw an error in the backend"""

    def __init__(self,
        *,
        parent: typing.Text = ...,
        role_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","role_id",b"role_id"]) -> None: ...
global___DeleteProjectRoleRequest = DeleteProjectRoleRequest

class ListProjectRolesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PROJECT_ROLE_VIEW_FIELD_NUMBER: builtins.int
    parent: typing.Text
    page_token: typing.Text
    """Optional. The next_page_token value returned from a previous list request."""

    project_role_view: global___ProjectRoleView.ValueType
    """Optional. specify the view of the project roles, PROJECT_ROLE_VIEW_FULL by default"""

    def __init__(self,
        *,
        parent: typing.Text = ...,
        page_token: typing.Text = ...,
        project_role_view: global___ProjectRoleView.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_token",b"page_token","parent",b"parent","project_role_view",b"project_role_view"]) -> None: ...
global___ListProjectRolesRequest = ListProjectRolesRequest

class ListProjectRolesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROJECT_ROLES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def project_roles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProjectRole]:
        """The list of project roles. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
        pass
    next_page_token: typing.Text
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        project_roles: typing.Optional[typing.Iterable[global___ProjectRole]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","project_roles",b"project_roles"]) -> None: ...
global___ListProjectRolesResponse = ListProjectRolesResponse
