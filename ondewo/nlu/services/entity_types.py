# Copyright 2021 ONDEWO GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from google.longrunning.operations_pb2 import Operation
from google.protobuf.empty_pb2 import Empty

from ondewo.nlu.core.services_interface import ServicesInterface
from ondewo.nlu.entity_type_pb2 import (
    BatchDeleteEntityTypesRequest,
    BatchUpdateEntityTypesRequest,
    CreateEntityBatchRequest,
    CreateEntityTypeRequest,
    DeleteEntityBatchRequest,
    DeleteEntityTypeRequest,
    EntityType,
    GetEntityTypeRequest,
    ListEntityTypesRequest,
    ListEntityTypesResponse,
    UpdateEntityBatchRequest,
    UpdateEntityTypeRequest,
)
from ondewo.nlu.entity_type_pb2_grpc import EntityTypesStub


class EntityTypes(ServicesInterface):
    """
    Exposes the entity=type-related endpoints of ONDEWO NLU services in a user-friendly way.

    See entity_type.proto.
    """

    @property
    def stub(self) -> EntityTypesStub:
        stub: EntityTypesStub = EntityTypesStub(channel=self.grpc_channel)
        return stub

    def list_entity_types(self, request: ListEntityTypesRequest) -> ListEntityTypesResponse:
        response: ListEntityTypesResponse = self.stub.ListEntityTypes(request, metadata=self.metadata)
        return response

    def get_entity_type(self, request: GetEntityTypeRequest) -> EntityType:
        response: EntityType = self.stub.GetEntityType(request, metadata=self.metadata)
        return response

    def create_entity_type(self, request: CreateEntityTypeRequest) -> EntityType:
        response: EntityType = self.stub.CreateEntityType(request, metadata=self.metadata)
        return response

    def update_entity_type(self, request: UpdateEntityTypeRequest) -> EntityType:
        response: EntityType = self.stub.UpdateEntityType(request, metadata=self.metadata)
        return response

    def delete_entity_type(self, request: DeleteEntityTypeRequest) -> Empty:
        response: Empty = self.stub.DeleteEntityType(request, metadata=self.metadata)
        return response

    def batch_update_entity_types(self, request: BatchUpdateEntityTypesRequest) -> Operation:
        response: Operation = self.stub.BatchUpdateEntityTypes(request, metadata=self.metadata)
        return response

    def batch_delete_entity_types(self, request: BatchDeleteEntityTypesRequest) -> Operation:
        response: Operation = self.stub.BatchDeleteEntityTypes(request, metadata=self.metadata)
        return response

    def create_entity_batch(self, request: CreateEntityBatchRequest) -> Operation:
        response: Operation = self.stub.CreateEntityBatch(request, metadata=self.metadata)
        return response

    def update_entity_batch(self, request: UpdateEntityBatchRequest) -> Operation:
        response: Operation = self.stub.UpdateEntityBatch(request, metadata=self.metadata)
        return response

    def delete_entity_batch(self, request: DeleteEntityBatchRequest) -> Operation:
        response: Operation = self.stub.DeleteEntityBatch(request, metadata=self.metadata)
        return response
