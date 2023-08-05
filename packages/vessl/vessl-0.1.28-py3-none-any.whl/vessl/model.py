from typing import List

from openapi_client.models import (
    ModelCreateAPIPayload,
    ModelUpdateAPIPayload,
    ResponseModelDetail,
)
from vessl import vessl_api
from vessl.organization import _get_organization_name


def read_model(
    repository_name: str, model_number: int, **kwargs
) -> ResponseModelDetail:
    """Read model

    Keyword args:
        organization_name (str): override default organization
    """
    return vessl_api.model_read_api(
        organization_name=_get_organization_name(**kwargs),
        repository_name=repository_name,
        number=model_number,
    )


def list_models(repository_name: str, **kwargs) -> List[ResponseModelDetail]:
    """List models

    Keyword args:
        organization_name (str): override default organization
    """
    return vessl_api.model_list_api(
        organization_name=_get_organization_name(**kwargs),
        repository_name=repository_name,
    ).results


def create_model(
    repository_name: str,
    repository_description: str = None,
    experiment_id: int = None,
    model_name: str = None,
    paths: List[str] = None,
    **kwargs,
) -> ResponseModelDetail:
    """Create model

    Keyword args:
        organization_name (str): override default organization
    """
    return vessl_api.model_create_api(
        organization_name=_get_organization_name(**kwargs),
        repository_name=repository_name,
        model_create_api_payload=ModelCreateAPIPayload(
            repository_description=repository_description,
            experiment_id=experiment_id,
            model_name=model_name,
            paths=paths,
        ),
    )


def update_model(
    repository_name: str, number: int, name: str, **kwargs
) -> ResponseModelDetail:
    """Update model

    Keyword args:
        organization_name (str): override default organization
    """
    return vessl_api.model_update_api(
        organization_name=_get_organization_name(**kwargs),
        repository_name=repository_name,
        number=number,
        model_update_api_payload=ModelUpdateAPIPayload(name=name),
    )


def delete_model(repository_name: str, number: int, **kwargs) -> object:
    """Delete model

    Keyword args:
        organization_name (str): override default organization
    """
    return vessl_api.model_delete_api(
        organization_name=_get_organization_name(**kwargs),
        repository_name=repository_name,
        version=number,
    )
