from ondewo.nlu.aiservices_pb2 import ExtractEntitiesRequest, GetAlternativeSentencesRequest, \
    GenerateUserSaysRequest, GenerateUserSaysResponse, \
    GenerateResponsesRequest, GenerateResponsesResponse, \
    GetAlternativeTrainingPhrasesRequest, GetAlternativeTrainingPhrasesResponse, \
    GetAlternativeSentencesResponse, ExtractEntitiesResponse, GetSynonymsResponse, GetSynonymsRequest
from ondewo.nlu.aiservices_pb2_grpc import AiServicesStub
from ondewo.nlu.core.services_interface import ServicesInterface


class AIServices(ServicesInterface):
    """
    Exposes the ai-services-related endpoints of ONDEWO NLU services in a user-friendly way.

    See aiservices.proto.
    """

    @property
    def stub(self) -> AiServicesStub:
        stub: AiServicesStub = AiServicesStub(channel=self.grpc_channel)
        return stub

    def extract_entities(self, request: ExtractEntitiesRequest) -> ExtractEntitiesResponse:
        response: ExtractEntitiesResponse = self.stub.ExtractEntities(request, metadata=self.metadata)
        return response

    def get_alternative_sentences(self,
                                  request: GetAlternativeSentencesRequest) -> GetAlternativeSentencesResponse:
        response: GetAlternativeSentencesResponse = \
            self.stub.GetAlternativeSentences(request, metadata=self.metadata)
        return response

    def generate_user_says(self,
                           request: GenerateUserSaysRequest) -> GenerateUserSaysResponse:
        response: GenerateUserSaysResponse = \
            self.stub.GenerateUserSays(request, metadata=self.metadata)
        return response

    def generate_responses(self,
                           request: GenerateResponsesRequest) -> GenerateResponsesResponse:
        response: GenerateResponsesResponse = \
            self.stub.GenerateResponses(request, metadata=self.metadata)
        return response

    def get_alternative_training_phrases(
            self,
            request: GetAlternativeTrainingPhrasesRequest
    ) -> GetAlternativeTrainingPhrasesResponse:
        response: GetAlternativeTrainingPhrasesResponse = \
            self.stub.GetAlternativeTrainingPhrases(request, metadata=self.metadata)
        return response

    def get_synonyms(self, request: GetSynonymsRequest) -> GetSynonymsResponse:
        response: GetSynonymsResponse = self.stub.GetSynonyms(request, metadata=self.metadata)
        return response
