"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import ondewo.nlu.entity_type_pb2
import ondewo.nlu.intent_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Mode:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Mode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSPECIFIED: _Mode.ValueType  # 0
    EXCLUSIVE: _Mode.ValueType  # 1
    INCLUSIVE: _Mode.ValueType  # 2
class Mode(_Mode, metaclass=_ModeEnumTypeWrapper):
    pass

UNSPECIFIED: Mode.ValueType  # 0
EXCLUSIVE: Mode.ValueType  # 1
INCLUSIVE: Mode.ValueType  # 2
global___Mode = Mode


class _IntentAlgorithms:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _IntentAlgorithmsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IntentAlgorithms.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OndewoIntentExactContextDetector: _IntentAlgorithms.ValueType  # 0
    OndewoIntentExactMatch: _IntentAlgorithms.ValueType  # 1
    OndewoIntentNamedExactMatch: _IntentAlgorithms.ValueType  # 2
    OndewoIntentSimilarityMatch: _IntentAlgorithms.ValueType  # 3
    OndewoIntentNamedSimilarityMatch: _IntentAlgorithms.ValueType  # 4
    OndewoIntentFastTextClassifier: _IntentAlgorithms.ValueType  # 5
    OndewoIntentMachineLearningMatch: _IntentAlgorithms.ValueType  # 6
    OndewoIntentBertClassifier: _IntentAlgorithms.ValueType  # 7
    OndewoIntentMetaClassifier: _IntentAlgorithms.ValueType  # 8
    OndewoIntentSnipsClassifier: _IntentAlgorithms.ValueType  # 9
    IntentExitDetector: _IntentAlgorithms.ValueType  # 10
    OndewoIntentRankingMatch: _IntentAlgorithms.ValueType  # 11
    OndewoIntentRasaClassifier: _IntentAlgorithms.ValueType  # 12
    OndewoWeightedEnsemble: _IntentAlgorithms.ValueType  # 13
    OndewoIntentExitDetector: _IntentAlgorithms.ValueType  # 14
    OndewoIntentParameterMatch: _IntentAlgorithms.ValueType  # 15
class IntentAlgorithms(_IntentAlgorithms, metaclass=_IntentAlgorithmsEnumTypeWrapper):
    pass

OndewoIntentExactContextDetector: IntentAlgorithms.ValueType  # 0
OndewoIntentExactMatch: IntentAlgorithms.ValueType  # 1
OndewoIntentNamedExactMatch: IntentAlgorithms.ValueType  # 2
OndewoIntentSimilarityMatch: IntentAlgorithms.ValueType  # 3
OndewoIntentNamedSimilarityMatch: IntentAlgorithms.ValueType  # 4
OndewoIntentFastTextClassifier: IntentAlgorithms.ValueType  # 5
OndewoIntentMachineLearningMatch: IntentAlgorithms.ValueType  # 6
OndewoIntentBertClassifier: IntentAlgorithms.ValueType  # 7
OndewoIntentMetaClassifier: IntentAlgorithms.ValueType  # 8
OndewoIntentSnipsClassifier: IntentAlgorithms.ValueType  # 9
IntentExitDetector: IntentAlgorithms.ValueType  # 10
OndewoIntentRankingMatch: IntentAlgorithms.ValueType  # 11
OndewoIntentRasaClassifier: IntentAlgorithms.ValueType  # 12
OndewoWeightedEnsemble: IntentAlgorithms.ValueType  # 13
OndewoIntentExitDetector: IntentAlgorithms.ValueType  # 14
OndewoIntentParameterMatch: IntentAlgorithms.ValueType  # 15
global___IntentAlgorithms = IntentAlgorithms


class ExtractEntitiesRequest(google.protobuf.message.Message):
    """The request to detect parameters."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    INTENT_NAME_FIELD_NUMBER: builtins.int
    parent: typing.Text
    """the parent of the request
    Format: `projects/<Project ID>`.
    """

    text: typing.Text
    """the input text"""

    language_code: typing.Text
    """the input language"""

    intent_name: typing.Text
    """Optional. The name of the relevant intent. Used to establish preference
    hierarchy for entities that correspond to intent parameters
    Format: `projects/<Project ID>/agent/intents/<Intent ID>`
    """

    def __init__(self,
        *,
        parent: typing.Text = ...,
        text: typing.Text = ...,
        language_code: typing.Text = ...,
        intent_name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["intent_name",b"intent_name","language_code",b"language_code","parent",b"parent","text",b"text"]) -> None: ...
global___ExtractEntitiesRequest = ExtractEntitiesRequest

class ExtractEntitiesFuzzyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    POTENTIAL_ENTITIES_FIELD_NUMBER: builtins.int
    MINIMAL_SCORE_FIELD_NUMBER: builtins.int
    ALLOW_OVERLAPS_FIELD_NUMBER: builtins.int
    parent: typing.Text
    """the parent of the request
    Format: `projects/<Project ID>`.
    """

    text: typing.Text
    """The text to be analyzed"""

    @property
    def potential_entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityTypeFuzzyNerConfig]:
        """Potential entities to be extracted from the text with entity-specific configs"""
        pass
    minimal_score: builtins.float
    """Minimal similarity score to consider entity as "matched" """

    allow_overlaps: builtins.bool
    """Optional. Whether or not entities are allowed to overlap."""

    def __init__(self,
        *,
        parent: typing.Text = ...,
        text: typing.Text = ...,
        potential_entities: typing.Optional[typing.Iterable[global___EntityTypeFuzzyNerConfig]] = ...,
        minimal_score: builtins.float = ...,
        allow_overlaps: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_overlaps",b"allow_overlaps","minimal_score",b"minimal_score","parent",b"parent","potential_entities",b"potential_entities","text",b"text"]) -> None: ...
global___ExtractEntitiesFuzzyRequest = ExtractEntitiesFuzzyRequest

class EntityTypeFuzzyNerConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _FuzzyNerAlgorithm:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _FuzzyNerAlgorithmEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[EntityTypeFuzzyNerConfig._FuzzyNerAlgorithm.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PREFILTER_LEVENSHTEIN: EntityTypeFuzzyNerConfig._FuzzyNerAlgorithm.ValueType  # 0
        LOCAL_MAXIMUM: EntityTypeFuzzyNerConfig._FuzzyNerAlgorithm.ValueType  # 1
    class FuzzyNerAlgorithm(_FuzzyNerAlgorithm, metaclass=_FuzzyNerAlgorithmEnumTypeWrapper):
        """Enum of fuzzy ner algorithms"""
        pass

    PREFILTER_LEVENSHTEIN: EntityTypeFuzzyNerConfig.FuzzyNerAlgorithm.ValueType  # 0
    LOCAL_MAXIMUM: EntityTypeFuzzyNerConfig.FuzzyNerAlgorithm.ValueType  # 1

    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    MINIMAL_SCORE_FIELD_NUMBER: builtins.int
    ENTITY_VALUES_FIELD_NUMBER: builtins.int
    ALGORITHM_FIELD_NUMBER: builtins.int
    @property
    def entity_type(self) -> ondewo.nlu.entity_type_pb2.EntityType:
        """The Entity Type"""
        pass
    minimal_score: builtins.float
    """Optional. Overrides the minimal score in ExtractEntitiesFuzzyRequest."""

    @property
    def entity_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Optional. If defined, only entity value from this list are considered."""
        pass
    algorithm: global___EntityTypeFuzzyNerConfig.FuzzyNerAlgorithm.ValueType
    """Optional. Specify the Fuzzy Ner algorithm
    Should not use allow_overlaps here, since its default value is False
    bool allow_overlaps = 5;
    """

    def __init__(self,
        *,
        entity_type: typing.Optional[ondewo.nlu.entity_type_pb2.EntityType] = ...,
        minimal_score: builtins.float = ...,
        entity_values: typing.Optional[typing.Iterable[typing.Text]] = ...,
        algorithm: global___EntityTypeFuzzyNerConfig.FuzzyNerAlgorithm.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity_type",b"entity_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["algorithm",b"algorithm","entity_type",b"entity_type","entity_values",b"entity_values","minimal_score",b"minimal_score"]) -> None: ...
global___EntityTypeFuzzyNerConfig = EntityTypeFuzzyNerConfig

class EntityDetected(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITY_FIELD_NUMBER: builtins.int
    EXTRACTION_METHOD_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    @property
    def entity(self) -> ondewo.nlu.intent_pb2.Intent.TrainingPhrase.Entity: ...
    extraction_method: typing.Text
    score: builtins.float
    def __init__(self,
        *,
        entity: typing.Optional[ondewo.nlu.intent_pb2.Intent.TrainingPhrase.Entity] = ...,
        extraction_method: typing.Text = ...,
        score: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity",b"entity"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity",b"entity","extraction_method",b"extraction_method","score",b"score"]) -> None: ...
global___EntityDetected = EntityDetected

class ExtractEntitiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITIES_DETECTED_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    @property
    def entities_detected(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EntityDetected]: ...
    text: typing.Text
    def __init__(self,
        *,
        entities_detected: typing.Optional[typing.Iterable[global___EntityDetected]] = ...,
        text: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entities_detected",b"entities_detected","text",b"text"]) -> None: ...
global___ExtractEntitiesResponse = ExtractEntitiesResponse

class GetAlternativeSentencesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONFIG_FIELD_NUMBER: builtins.int
    SENTENCE_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    PROTECTED_WORDS_FIELD_NUMBER: builtins.int
    WORDS_TO_CHANGE_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> global___DataEnrichmentConfig: ...
    sentence: typing.Text
    language_code: typing.Text
    parent: typing.Text
    @property
    def protected_words(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def words_to_change(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        config: typing.Optional[global___DataEnrichmentConfig] = ...,
        sentence: typing.Text = ...,
        language_code: typing.Text = ...,
        parent: typing.Text = ...,
        protected_words: typing.Optional[typing.Iterable[typing.Text]] = ...,
        words_to_change: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","language_code",b"language_code","parent",b"parent","protected_words",b"protected_words","sentence",b"sentence","words_to_change",b"words_to_change"]) -> None: ...
global___GetAlternativeSentencesRequest = GetAlternativeSentencesRequest

class GenerateUserSaysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    N_REPEAT_SYNONYM_FIELD_NUMBER: builtins.int
    BRANCH_FIELD_NUMBER: builtins.int
    language_code: typing.Text
    parent: typing.Text
    n_repeat_synonym: builtins.int
    branch: typing.Text
    def __init__(self,
        *,
        language_code: typing.Text = ...,
        parent: typing.Text = ...,
        n_repeat_synonym: builtins.int = ...,
        branch: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["branch",b"branch","language_code",b"language_code","n_repeat_synonym",b"n_repeat_synonym","parent",b"parent"]) -> None: ...
global___GenerateUserSaysRequest = GenerateUserSaysRequest

class GenerateResponsesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    N_REPEAT_SYNONYM_FIELD_NUMBER: builtins.int
    BRANCH_FIELD_NUMBER: builtins.int
    DROP_UNKNOWN_PARAMETERS_FIELD_NUMBER: builtins.int
    language_code: typing.Text
    parent: typing.Text
    n_repeat_synonym: builtins.int
    branch: typing.Text
    drop_unknown_parameters: builtins.bool
    def __init__(self,
        *,
        language_code: typing.Text = ...,
        parent: typing.Text = ...,
        n_repeat_synonym: builtins.int = ...,
        branch: typing.Text = ...,
        drop_unknown_parameters: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["branch",b"branch","drop_unknown_parameters",b"drop_unknown_parameters","language_code",b"language_code","n_repeat_synonym",b"n_repeat_synonym","parent",b"parent"]) -> None: ...
global___GenerateResponsesRequest = GenerateResponsesRequest

class GetAlternativeTrainingPhrasesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONFIG_FIELD_NUMBER: builtins.int
    TRAINING_PHRASE_FIELD_NUMBER: builtins.int
    INTENT_NAME_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    DETECT_ENTITIES_FIELD_NUMBER: builtins.int
    SIMILARITY_THRESHOLD_FIELD_NUMBER: builtins.int
    PROTECTED_WORDS_FIELD_NUMBER: builtins.int
    WORDS_TO_CHANGE_FIELD_NUMBER: builtins.int
    BRANCH_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> global___DataEnrichmentConfig: ...
    @property
    def training_phrase(self) -> ondewo.nlu.intent_pb2.Intent.TrainingPhrase: ...
    intent_name: typing.Text
    language_code: typing.Text
    parent: typing.Text
    detect_entities: builtins.bool
    similarity_threshold: builtins.float
    """similarity threshold defines how similar sentences should be to drop generated training phrase
    as duplicate. Meaningful values of similarity_threshold are between 0.95 and 1.0
    """

    @property
    def protected_words(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def words_to_change(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    branch: typing.Text
    def __init__(self,
        *,
        config: typing.Optional[global___DataEnrichmentConfig] = ...,
        training_phrase: typing.Optional[ondewo.nlu.intent_pb2.Intent.TrainingPhrase] = ...,
        intent_name: typing.Text = ...,
        language_code: typing.Text = ...,
        parent: typing.Text = ...,
        detect_entities: builtins.bool = ...,
        similarity_threshold: builtins.float = ...,
        protected_words: typing.Optional[typing.Iterable[typing.Text]] = ...,
        words_to_change: typing.Optional[typing.Iterable[typing.Text]] = ...,
        branch: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config","training_phrase",b"training_phrase"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["branch",b"branch","config",b"config","detect_entities",b"detect_entities","intent_name",b"intent_name","language_code",b"language_code","parent",b"parent","protected_words",b"protected_words","similarity_threshold",b"similarity_threshold","training_phrase",b"training_phrase","words_to_change",b"words_to_change"]) -> None: ...
global___GetAlternativeTrainingPhrasesRequest = GetAlternativeTrainingPhrasesRequest

class GetSynonymsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONFIG_FIELD_NUMBER: builtins.int
    WORD_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    @property
    def config(self) -> global___DataEnrichmentConfig: ...
    word: typing.Text
    language_code: typing.Text
    parent: typing.Text
    def __init__(self,
        *,
        config: typing.Optional[global___DataEnrichmentConfig] = ...,
        word: typing.Text = ...,
        language_code: typing.Text = ...,
        parent: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","language_code",b"language_code","parent",b"parent","word",b"word"]) -> None: ...
global___GetSynonymsRequest = GetSynonymsRequest

class GetSynonymsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SYNONYMS_FIELD_NUMBER: builtins.int
    @property
    def synonyms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Synonym]: ...
    def __init__(self,
        *,
        synonyms: typing.Optional[typing.Iterable[global___Synonym]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["synonyms",b"synonyms"]) -> None: ...
global___GetSynonymsResponse = GetSynonymsResponse

class Synonym(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SYNONYM_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    synonym: typing.Text
    score: builtins.int
    def __init__(self,
        *,
        synonym: typing.Text = ...,
        score: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["score",b"score","synonym",b"synonym"]) -> None: ...
global___Synonym = Synonym

class GetAlternativeSentencesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ALTERNATIVE_SENTENCES_FIELD_NUMBER: builtins.int
    @property
    def alternative_sentences(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AltSentence]: ...
    def __init__(self,
        *,
        alternative_sentences: typing.Optional[typing.Iterable[global___AltSentence]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alternative_sentences",b"alternative_sentences"]) -> None: ...
global___GetAlternativeSentencesResponse = GetAlternativeSentencesResponse

class GenerateResponsesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESPONSES_FIELD_NUMBER: builtins.int
    @property
    def responses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        responses: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["responses",b"responses"]) -> None: ...
global___GenerateResponsesResponse = GenerateResponsesResponse

class GenerateUserSaysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USER_SAYS_FIELD_NUMBER: builtins.int
    @property
    def user_says(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        user_says: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_says",b"user_says"]) -> None: ...
global___GenerateUserSaysResponse = GenerateUserSaysResponse

class GetAlternativeTrainingPhrasesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ALTERNATIVE_TRAINING_PHRASES_FIELD_NUMBER: builtins.int
    @property
    def alternative_training_phrases(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AltTrainingPhrase]: ...
    def __init__(self,
        *,
        alternative_training_phrases: typing.Optional[typing.Iterable[global___AltTrainingPhrase]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alternative_training_phrases",b"alternative_training_phrases"]) -> None: ...
global___GetAlternativeTrainingPhrasesResponse = GetAlternativeTrainingPhrasesResponse

class AltSentence(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SENTENCE_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    sentence: typing.Text
    score: builtins.float
    def __init__(self,
        *,
        sentence: typing.Text = ...,
        score: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["score",b"score","sentence",b"sentence"]) -> None: ...
global___AltSentence = AltSentence

class AltTrainingPhrase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TRAINING_PHRASE_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    @property
    def training_phrase(self) -> ondewo.nlu.intent_pb2.Intent.TrainingPhrase: ...
    score: builtins.float
    def __init__(self,
        *,
        training_phrase: typing.Optional[ondewo.nlu.intent_pb2.Intent.TrainingPhrase] = ...,
        score: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["training_phrase",b"training_phrase"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["score",b"score","training_phrase",b"training_phrase"]) -> None: ...
global___AltTrainingPhrase = AltTrainingPhrase

class DataEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTITY_ENRICHMENT_FIELD_NUMBER: builtins.int
    THESAURUS_ENRICHMENT_FIELD_NUMBER: builtins.int
    WORD2VEC_ENRICHMENT_FIELD_NUMBER: builtins.int
    WORD_NET_ENRICHMENT_FIELD_NUMBER: builtins.int
    GPT2_ENRICHMENT_FIELD_NUMBER: builtins.int
    GLOVE_ENRICHMENT_FIELD_NUMBER: builtins.int
    FASTTEXT_ENRICHMENT_FIELD_NUMBER: builtins.int
    BERT_ENRICHMENT_FIELD_NUMBER: builtins.int
    XLNET_ENRICHMENT_FIELD_NUMBER: builtins.int
    @property
    def entity_enrichment(self) -> global___EntityEnrichmentConfig: ...
    @property
    def thesaurus_enrichment(self) -> global___ThesaurusEnrichmentConfig: ...
    @property
    def word2vec_enrichment(self) -> global___Word2VecEnrichmentConfig: ...
    @property
    def word_net_enrichment(self) -> global___WordNetAugEnrichmentConfig: ...
    @property
    def gpt2_enrichment(self) -> global___GPT2EnrichmentConfig: ...
    @property
    def glove_enrichment(self) -> global___GloVeEnrichmentConfig: ...
    @property
    def fasttext_enrichment(self) -> global___FastTextEnrichmentConfig: ...
    @property
    def bert_enrichment(self) -> global___BertAugEnrichmentConfig: ...
    @property
    def xlnet_enrichment(self) -> global___XLNetAugEnrichmentConfig: ...
    def __init__(self,
        *,
        entity_enrichment: typing.Optional[global___EntityEnrichmentConfig] = ...,
        thesaurus_enrichment: typing.Optional[global___ThesaurusEnrichmentConfig] = ...,
        word2vec_enrichment: typing.Optional[global___Word2VecEnrichmentConfig] = ...,
        word_net_enrichment: typing.Optional[global___WordNetAugEnrichmentConfig] = ...,
        gpt2_enrichment: typing.Optional[global___GPT2EnrichmentConfig] = ...,
        glove_enrichment: typing.Optional[global___GloVeEnrichmentConfig] = ...,
        fasttext_enrichment: typing.Optional[global___FastTextEnrichmentConfig] = ...,
        bert_enrichment: typing.Optional[global___BertAugEnrichmentConfig] = ...,
        xlnet_enrichment: typing.Optional[global___XLNetAugEnrichmentConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bert_enrichment",b"bert_enrichment","entity_enrichment",b"entity_enrichment","fasttext_enrichment",b"fasttext_enrichment","glove_enrichment",b"glove_enrichment","gpt2_enrichment",b"gpt2_enrichment","thesaurus_enrichment",b"thesaurus_enrichment","word2vec_enrichment",b"word2vec_enrichment","word_net_enrichment",b"word_net_enrichment","xlnet_enrichment",b"xlnet_enrichment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bert_enrichment",b"bert_enrichment","entity_enrichment",b"entity_enrichment","fasttext_enrichment",b"fasttext_enrichment","glove_enrichment",b"glove_enrichment","gpt2_enrichment",b"gpt2_enrichment","thesaurus_enrichment",b"thesaurus_enrichment","word2vec_enrichment",b"word2vec_enrichment","word_net_enrichment",b"word_net_enrichment","xlnet_enrichment",b"xlnet_enrichment"]) -> None: ...
global___DataEnrichmentConfig = DataEnrichmentConfig

class EntityEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___EntityEnrichmentConfig = EntityEnrichmentConfig

class ThesaurusEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___ThesaurusEnrichmentConfig = ThesaurusEnrichmentConfig

class FastTextEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___FastTextEnrichmentConfig = FastTextEnrichmentConfig

class BertAugEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___BertAugEnrichmentConfig = BertAugEnrichmentConfig

class GloVeEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___GloVeEnrichmentConfig = GloVeEnrichmentConfig

class GPT2EnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___GPT2EnrichmentConfig = GPT2EnrichmentConfig

class Word2VecEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___Word2VecEnrichmentConfig = Word2VecEnrichmentConfig

class WordNetAugEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___WordNetAugEnrichmentConfig = WordNetAugEnrichmentConfig

class XLNetAugEnrichmentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    ENRICHMENT_FACTOR_FIELD_NUMBER: builtins.int
    EXECUTION_ORDER_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    enrichment_factor: builtins.int
    execution_order: builtins.int
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        enrichment_factor: builtins.int = ...,
        execution_order: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrichment_factor",b"enrichment_factor","execution_order",b"execution_order","is_active",b"is_active"]) -> None: ...
global___XLNetAugEnrichmentConfig = XLNetAugEnrichmentConfig

class ClassifyIntentsRequest(google.protobuf.message.Message):
    """The request for intent classification."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    ACTIVE_CONTEXTS_FIELD_NUMBER: builtins.int
    CONTEXT_NAMES_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    ALGORITHMS_FIELD_NUMBER: builtins.int
    parent: typing.Text
    """the parent of the request
    Format: `projects/<Project ID>`.
    """

    text: typing.Text
    """the input text"""

    language_code: typing.Text
    """the input language"""

    active_contexts: builtins.bool
    """Optional: if restrict classification result with input contexts listed in the field `context_names`"""

    @property
    def context_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Optional: names of the input contexts to restrict the classification result with.
        Intents can only be classified if the intent's input context set is the subset of the given context set.
        """
        pass
    mode: global___Mode.ValueType
    """Optional: Which mode to use:
    EXCLUSIVE - skip algorithms listed in `algorithms` field,
    INCLUSIVE - run ONLY algorithms listed in `algorithms` field,
    UNSPECIFIED - default mode, described in agent config
    """

    @property
    def algorithms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___IntentAlgorithms.ValueType]:
        """Optional: Algorithm list"""
        pass
    def __init__(self,
        *,
        parent: typing.Text = ...,
        text: typing.Text = ...,
        language_code: typing.Text = ...,
        active_contexts: builtins.bool = ...,
        context_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        mode: global___Mode.ValueType = ...,
        algorithms: typing.Optional[typing.Iterable[global___IntentAlgorithms.ValueType]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_contexts",b"active_contexts","algorithms",b"algorithms","context_names",b"context_names","language_code",b"language_code","mode",b"mode","parent",b"parent","text",b"text"]) -> None: ...
global___ClassifyIntentsRequest = ClassifyIntentsRequest

class IntentClassified(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INTENT_NAME_FIELD_NUMBER: builtins.int
    INTENT_DISPLAY_NAME_FIELD_NUMBER: builtins.int
    CLASSIFIER_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    intent_name: typing.Text
    """The unique identifier of this intent.
    Format: `projects/<Project ID>/agent/intents/<Intent ID>`.
    """

    intent_display_name: typing.Text
    """The name of the intent."""

    classifier: typing.Text
    score: builtins.float
    def __init__(self,
        *,
        intent_name: typing.Text = ...,
        intent_display_name: typing.Text = ...,
        classifier: typing.Text = ...,
        score: builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["classifier",b"classifier","intent_display_name",b"intent_display_name","intent_name",b"intent_name","score",b"score"]) -> None: ...
global___IntentClassified = IntentClassified

class ClassifyIntentsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INTENTS_CLASSIFIED_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    ACTIVE_CONTEXTS_FIELD_NUMBER: builtins.int
    CONTEXT_NAMES_FIELD_NUMBER: builtins.int
    @property
    def intents_classified(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___IntentClassified]: ...
    text: typing.Text
    active_contexts: builtins.bool
    @property
    def context_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        intents_classified: typing.Optional[typing.Iterable[global___IntentClassified]] = ...,
        text: typing.Text = ...,
        active_contexts: builtins.bool = ...,
        context_names: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["active_contexts",b"active_contexts","context_names",b"context_names","intents_classified",b"intents_classified","text",b"text"]) -> None: ...
global___ClassifyIntentsResponse = ClassifyIntentsResponse
