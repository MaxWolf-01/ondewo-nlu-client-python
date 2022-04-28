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
import ondewo.nlu.project_role_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DefaultServerRole:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _DefaultServerRoleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DefaultServerRole.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SERVER_UNSPECIFIED: _DefaultServerRole.ValueType  # 0
    """unspecified server role"""

    SERVER_USER: _DefaultServerRole.ValueType  # 1
    """read-only access"""

    SERVER_MANAGER: _DefaultServerRole.ValueType  # 2
    """SERVER_USER's permissions + CRUD of projects and Users"""

    SERVER_ADMIN: _DefaultServerRole.ValueType  # 3
    """this role can do everything"""

    SERVER_INACTIVE: _DefaultServerRole.ValueType  # 4
    """this role can do nothing. Used to set a user as inactive in the server."""

class DefaultServerRole(_DefaultServerRole, metaclass=_DefaultServerRoleEnumTypeWrapper):
    pass

SERVER_UNSPECIFIED: DefaultServerRole.ValueType  # 0
"""unspecified server role"""

SERVER_USER: DefaultServerRole.ValueType  # 1
"""read-only access"""

SERVER_MANAGER: DefaultServerRole.ValueType  # 2
"""SERVER_USER's permissions + CRUD of projects and Users"""

SERVER_ADMIN: DefaultServerRole.ValueType  # 3
"""this role can do everything"""

SERVER_INACTIVE: DefaultServerRole.ValueType  # 4
"""this role can do nothing. Used to set a user as inactive in the server."""

global___DefaultServerRole = DefaultServerRole


class User(google.protobuf.message.Message):
    """User messages

    this message contains all the fields that required for user db
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_ID_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    SERVER_ROLE_ID_FIELD_NUMBER: builtins.int
    USER_EMAIL_FIELD_NUMBER: builtins.int
    user_id: typing.Text
    """when creating user user_id is empty, then it will be generated on creation time on backend"""

    display_name: typing.Text
    """Optional field display_name is the name that will be used on the frontend to interact with the user
    it shouldn't be unique. If not provided user_name will also be used as display name
    """

    server_role_id: builtins.int
    """server role type of the given user. If nothing is provided, the user is set to USER (minimum access)"""

    user_email: typing.Text
    """user e-mail should be a valid e-mail and unique"""

    def __init__(self,
        *,
        user_id: typing.Text = ...,
        display_name: typing.Text = ...,
        server_role_id: builtins.int = ...,
        user_email: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["display_name",b"display_name","server_role_id",b"server_role_id","user_email",b"user_email","user_id",b"user_id"]) -> None: ...
global___User = User

class UserInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ProjectRolesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> ondewo.nlu.project_role_pb2.ProjectRole: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[ondewo.nlu.project_role_pb2.ProjectRole] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    USER_FIELD_NUMBER: builtins.int
    PROJECT_ROLES_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User: ...
    @property
    def project_roles(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, ondewo.nlu.project_role_pb2.ProjectRole]:
        """If in GetUser, ListUser requests UserView is FULL, then the mapping is additionally provided
        of parent of the project and corresponding ProjectRole of the user
        """
        pass
    def __init__(self,
        *,
        user: typing.Optional[global___User] = ...,
        project_roles: typing.Optional[typing.Mapping[typing.Text, ondewo.nlu.project_role_pb2.ProjectRole]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["project_roles",b"project_roles","user",b"user"]) -> None: ...
global___UserInfo = UserInfo

class CreateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User: ...
    password: typing.Text
    def __init__(self,
        *,
        user: typing.Optional[global___User] = ...,
        password: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["password",b"password","user",b"user"]) -> None: ...
global___CreateUserRequest = CreateUserRequest

class UpdateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """user_id in the User message should be given, if empty will throw an error in the backend
        password and other fields in the User are optional. Only the fields to be updated should be provided
        """
        pass
    password: typing.Text
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""
        pass
    def __init__(self,
        *,
        user: typing.Optional[global___User] = ...,
        password: typing.Text = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask","user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["password",b"password","update_mask",b"update_mask","user",b"user"]) -> None: ...
global___UpdateUserRequest = UpdateUserRequest

class GetUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_ID_FIELD_NUMBER: builtins.int
    USER_EMAIL_FIELD_NUMBER: builtins.int
    user_id: typing.Text
    """the user is identified by user id"""

    user_email: typing.Text
    """the user can identified by their email"""

    def __init__(self,
        *,
        user_id: typing.Text = ...,
        user_email: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user_email",b"user_email","user_id",b"user_id","user_identifier",b"user_identifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_email",b"user_email","user_id",b"user_id","user_identifier",b"user_identifier"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["user_identifier",b"user_identifier"]) -> typing.Optional[typing_extensions.Literal["user_id","user_email"]]: ...
global___GetUserRequest = GetUserRequest

class DeleteUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_ID_FIELD_NUMBER: builtins.int
    user_id: typing.Text
    """user is identified by user id, if empty will throw an error in the backend"""

    def __init__(self,
        *,
        user_id: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_id",b"user_id"]) -> None: ...
global___DeleteUserRequest = DeleteUserRequest

class ListUsersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_token: typing.Text
    """Optional. The next_page_token value returned from a previous list request."""

    def __init__(self,
        *,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_token",b"page_token"]) -> None: ...
global___ListUsersRequest = ListUsersRequest

class ListUsersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___User]:
        """The list of users. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
        pass
    next_page_token: typing.Text
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        users: typing.Optional[typing.Iterable[global___User]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","users",b"users"]) -> None: ...
global___ListUsersResponse = ListUsersResponse

class ListUserInfosResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserInfo]:
        """The list of server roles. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
        pass
    next_page_token: typing.Text
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        users: typing.Optional[typing.Iterable[global___UserInfo]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","users",b"users"]) -> None: ...
global___ListUserInfosResponse = ListUserInfosResponse

class ServerRole(google.protobuf.message.Message):
    """Server Role messages"""
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
        """defines the permissions for the given role (the strings can be gotten from the ListServerPermissions)"""
        pass
    def __init__(self,
        *,
        role_id: builtins.int = ...,
        name: typing.Text = ...,
        permissions: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","permissions",b"permissions","role_id",b"role_id"]) -> None: ...
global___ServerRole = ServerRole

class CreateServerRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROLE_FIELD_NUMBER: builtins.int
    @property
    def role(self) -> global___ServerRole:
        """If the role_id is not provided, an incremental value will be assigned
        The "name" and "role_type" are mandatory values
        The permissions all default to False if not provided specifically
        """
        pass
    def __init__(self,
        *,
        role: typing.Optional[global___ServerRole] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["role",b"role"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["role",b"role"]) -> None: ...
global___CreateServerRoleRequest = CreateServerRoleRequest

class UpdateServerRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROLE_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def role(self) -> global___ServerRole:
        """role_id in the Role message should be given, if empty will throw an error in the backend
        other fields in the Role are optional. Only the fields to be updated should be provided
        """
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which fields get updated."""
        pass
    def __init__(self,
        *,
        role: typing.Optional[global___ServerRole] = ...,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["role",b"role","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["role",b"role","update_mask",b"update_mask"]) -> None: ...
global___UpdateServerRoleRequest = UpdateServerRoleRequest

class DeleteServerRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROLE_ID_FIELD_NUMBER: builtins.int
    role_id: builtins.int
    """role is identified by role id, if empty will throw an error in the backend"""

    def __init__(self,
        *,
        role_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["role_id",b"role_id"]) -> None: ...
global___DeleteServerRoleRequest = DeleteServerRoleRequest

class GetServerRoleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROLE_ID_FIELD_NUMBER: builtins.int
    ROLE_NAME_FIELD_NUMBER: builtins.int
    role_id: builtins.int
    """role is identified by role id"""

    role_name: typing.Text
    """role can also be uniquely identified by its name"""

    def __init__(self,
        *,
        role_id: builtins.int = ...,
        role_name: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["role_id",b"role_id","role_name",b"role_name","server_role_identifier",b"server_role_identifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["role_id",b"role_id","role_name",b"role_name","server_role_identifier",b"server_role_identifier"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["server_role_identifier",b"server_role_identifier"]) -> typing.Optional[typing_extensions.Literal["role_id","role_name"]]: ...
global___GetServerRoleRequest = GetServerRoleRequest

class ListServerRolesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_token: typing.Text
    """Optional. The next_page_token value returned from a previous list request."""

    def __init__(self,
        *,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_token",b"page_token"]) -> None: ...
global___ListServerRolesRequest = ListServerRolesRequest

class ListServerRolesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVER_ROLES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def server_roles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServerRole]:
        """The list of server roles. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
        pass
    next_page_token: typing.Text
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        server_roles: typing.Optional[typing.Iterable[global___ServerRole]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","server_roles",b"server_roles"]) -> None: ...
global___ListServerRolesResponse = ListServerRolesResponse

class ListServerPermissionsRequest(google.protobuf.message.Message):
    """Server permissions"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_token: typing.Text
    """Optional. The next_page_token value returned from a previous list request."""

    def __init__(self,
        *,
        page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_token",b"page_token"]) -> None: ...
global___ListServerPermissionsRequest = ListServerPermissionsRequest

class ListServerPermissionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PERMISSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def permissions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The list of server permissions. There will be a maximum number of items
        returned based on the page_token field in the request.
        """
        pass
    next_page_token: typing.Text
    """Token to retrieve the next page of results, or empty if there are no
    more results in the list.
    """

    def __init__(self,
        *,
        permissions: typing.Optional[typing.Iterable[typing.Text]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","permissions",b"permissions"]) -> None: ...
global___ListServerPermissionsResponse = ListServerPermissionsResponse

class LoginRequest(google.protobuf.message.Message):
    """Authentication messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_EMAIL_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    user_email: typing.Text
    password: typing.Text
    def __init__(self,
        *,
        user_email: typing.Text = ...,
        password: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password",b"password","user_email",b"user_email"]) -> None: ...
global___LoginRequest = LoginRequest

class LoginResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_FIELD_NUMBER: builtins.int
    AUTH_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User: ...
    auth_token: typing.Text
    def __init__(self,
        *,
        user: typing.Optional[global___User] = ...,
        auth_token: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auth_token",b"auth_token","user",b"user"]) -> None: ...
global___LoginResponse = LoginResponse
