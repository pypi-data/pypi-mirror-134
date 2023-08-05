"""
/predict request body JSON example:

    {
        "inputs": [
            {
                "identifier": "foo",
                "features": {
                    "age": 20,
                    "height": 180
                }
            },
            {
                "identifier": "bar",
                "features": {
                    "age": 30,
                    "height": 200
                }
            },
            {
                "identifier": "foo",
                "features": {
                    "age": 20,
                    "height": 180
                }
            }
        ]
    }

"""
import json
import time
from enum import Enum
from functools import cached_property
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import pydantic
from opentelemetry import trace
from opentelemetry.trace import SpanKind

from energinetml.core.model import Model, TrainedModel
from energinetml.core.validation import ValidatorResponse, ValidatorStatus

tracer = trace.get_tracer(__name__)


class PredictionInput(list):
    """[summary]"""

    def __init__(self, features: List[str], *args, **kwargs):
        """[summary]

        Args:
            features (List[str]): [description]
        """
        super().__init__(*args, **kwargs)
        self.features = features

    def as_dict_of_lists(self) -> Dict[str, Any]:
        """[summary]"""
        return {
            feature: [input[feature] for input in self] for feature in self.features
        }

    def as_pandas_dataframe(self) -> pd.DataFrame:
        """[summary]

        Raises:
            RuntimeError: [description]

        Returns:
            pd.DataFram: [description]
        """

        return pd.DataFrame(self.as_dict_of_lists())


# -- Data models -------------------------------------------------------------


class PredictRequest(pydantic.BaseModel):
    """[summary]"""

    inputs: List[Any]

    def group_input_by_identifier(self):
        """[summary]

        Returns:
            [type]: TODO: I need help for this data structure.
        """
        inputs_per_identifier = {}

        for index, input in enumerate(self.inputs):
            if hasattr(input, "identifier"):
                identifier = input.identifier.value
            else:
                identifier = None

            inputs_per_identifier.setdefault(identifier, []).append(
                (index, dict(input.features))
            )

        return inputs_per_identifier.items()


class PredictResponse(pydantic.BaseModel):
    """[summary]"""

    predictions: List[Any]
    validations: Optional[List[Any]]


# -- Controller --------------------------------------------------------------


class PredictionController:
    """[summary]"""

    def __init__(
        self,
        model: Model,
        trained_model: TrainedModel,
        model_version: str = None,
    ):
        """[summary]

        Args:
            model (Model): [description]
            trained_model (TrainedModel): [description]
            model_version (str, optional): [description]. Defaults to None.
        """
        self.model = model
        self.trained_model = trained_model
        self.model_version = model_version

        self.predict_features = self.generate_validator_model(
            model_name="PredictFeatures", use_validation=False
        )
        self.predict_features_validator = self.generate_validator_model(
            model_name="PredictFeaturesValidator", use_validation=True
        )

    def generate_validator_model(
        self, model_name: str, use_validation: bool = True
    ) -> pydantic.BaseModel:
        """A method for creating the validator object during initialization of the
        endpoint. The method depends on self.trained_model.validator and returns a
        pydantic.BaseModel if validator has been provided during training.

        Args:
            model_name (str): Name of the pydantic.BaseModel.
            use_validation (bool, optional): A boolean which enables the
            pydantic.BaseModel to use a validtor. Defaults to True.

        Returns:
            pydantic.BaseModel: A pydantic.BaseModel with or without a valdator.
        """
        return (
            self.trained_model.validator.get_pydantic_model(
                model_name=model_name, use_validation=use_validation
            )
            if self.trained_model.validator
            else None
        )

    @property
    def identifiers(self) -> List[str]:
        """[summary]

        Returns:
            List[str]: [description]
        """
        return self.trained_model.identifiers

    @property
    def features(self) -> List[str]:
        """[summary]

        Returns:
            List[str]: [description]
        """
        return self.trained_model.features

    @property
    def requires_identity(self) -> bool:
        """[summary]

        Returns:
            bool: [description]
        """
        return not self.trained_model.has_default_model()

    @cached_property
    def request_model(self):
        """
        Build a request model class (inherited from pydantic.BaseModel)
        based on a specific TrainedModel instance. The resulting model
        can be used for JSON input validation, Swagger docs etc.
        """

        predict_features = (
            self.predict_features
            if self.predict_features
            else pydantic.create_model(
                "PredictFeatures", **{feature: (Any, ...) for feature in self.features}
            )
        )

        predict_input_attributes = {"features": (predict_features, ...)}

        if self.requires_identity:
            identifier_enum = Enum("IdentifierEnum", {i: i for i in self.identifiers})
            predict_input_attributes["identifier"] = (identifier_enum, ...)

        PredictInput = pydantic.create_model("PredictInput", **predict_input_attributes)

        return pydantic.create_model(
            "PredictRequest",
            __base__=PredictRequest,
            inputs=(List[PredictInput], ...),
        )

    @property
    def response_model(self):
        """[summary]"""
        return PredictResponse

    def predict(
        self, request: PredictRequest, correlation_id: str = None
    ) -> PredictResponse:
        """[summary]

        Args:
            request (PredictRequest): [description]
            correlation_id (str, optional): [description]. Defaults to None.

        Returns:
            PredictResponse: [description]
        """
        start_span = tracer.start_span(name="prediction", kind=SpanKind.SERVER)

        with start_span as span:
            start = time.perf_counter()
            identifiers, features, predictions, validations = self.invoke_model(request)
            end = time.perf_counter()

            if correlation_id:
                span.set_attribute("correlation_id", correlation_id)
            span.set_attribute("duration_model", str(end - start))
            span.set_attribute("model_name", self.model.name)
            if self.model_version is not None:
                span.set_attribute("model_version", self.model_version)
            span.set_attribute("identifiers", json.dumps(identifiers))
            span.set_attribute("features", json.dumps(features))
            span.set_attribute("predictions", json.dumps(predictions))
            span.set_attribute("validations", json.dumps(validations))

        return self.response_model(predictions=predictions, validations=validations)

    def invoke_model(
        self, request: PredictRequest
    ) -> Tuple[List[str], List[str], List[Any], List[ValidatorResponse]]:
        """[summary]

        Args:
            request (PredictRequest): [description]

        Raises:
            RuntimeError: [description]

        Returns:
            PredictResponse: [description]
        """
        groups = list(request.group_input_by_identifier())
        identifiers_ordered = [... for _ in range(len(request.inputs))]
        features_ordered = [i for i in request.inputs]
        predictions_ordered = [... for _ in range(len(request.inputs))]
        validated_features_ordered: List[ValidatorResponse] = [
            ... for _ in range(len(request.inputs))
        ]

        # Invoke predict() for each unique identifier
        for identifier, inputs in groups:
            indexes = [i[0] for i in inputs]
            feature_sets = [i[1] for i in inputs]
            input_data = PredictionInput(self.features, feature_sets)

            validated_features: List[ValidatorResponse] = []
            if self.predict_features_validator:
                for features in input_data:

                    try:

                        self.predict_features_validator(**features)
                    except pydantic.ValidationError as pve:

                        error_dict = json.loads(pve.json())

                        validated_features.append(
                            ValidatorResponse(
                                state=ValidatorStatus.NOT_VALID
                                if [
                                    ValidatorStatus(item.get("ctx", {}).get("state"))
                                    for item in error_dict
                                ]
                                else ValidatorStatus.WARNING,
                                message=json.dumps(error_dict),
                            )
                        )
                    else:
                        validated_features.append(
                            ValidatorResponse(state=ValidatorStatus.VALID)
                        )

            else:
                validated_features = [
                    ValidatorResponse(state=ValidatorStatus.VALID)
                    for _ in range(len(input_data))
                ]

            predict_result = self.model.predict(
                trained_model=self.trained_model,
                identifier=identifier,
                input_data=input_data,
            )

            for index, features, prediction, validated_feature in zip(
                indexes, feature_sets, predict_result, validated_features
            ):

                identifiers_ordered[index] = identifier
                features_ordered[index] = features
                predictions_ordered[index] = prediction
                if self.predict_features_validator:
                    validated_features_ordered[index] = validated_feature.dict()

        if ... in predictions_ordered:
            raise RuntimeError()

        return (
            identifiers_ordered,
            features_ordered,
            predictions_ordered,
            validated_features_ordered if self.predict_features_validator else None,
        )
