import datetime
import random

import pytest

import pycspr

_A_KNOWN_ISO_TIMESTAMP = "2021-06-28T15:55:25.335+00:00"
_A_KNOWN_DEPLOY_TIMESTAMP = datetime.datetime.fromisoformat(_A_KNOWN_ISO_TIMESTAMP).timestamp()
_A_KNOWN_DEPLOY_HUMANIZED_TTL = "1day"


@pytest.fixture(scope="session")
def a_test_chain_id() -> str:
    return "casper-net-1"


@pytest.fixture(scope="session")
def a_test_timestamp() -> int:
    return datetime.datetime.now(tz=datetime.timezone.utc).timestamp()


@pytest.fixture(scope="session")
def a_test_ttl_humanized() -> str:
    (unit, quantity) = random.choice((
        ("ms", random.randint(1, 1000 * 60 * 60 * 24)),
        ("s", random.randint(1, 60)),
        ("m", random.randint(1, 60)),
        ("h", random.randint(1, 24)),
        ("day", 1)
        ))

    return f"{quantity}{unit}"


@pytest.fixture(scope="session")
def a_test_uref() -> str:
    return "uref-827d5984270fed5aaaf076e1801733414a307ed8c5d85cad8ebe6265ba887b3a-007"


@pytest.fixture(scope="function")
def deploy_params(a_test_chain_id, a_test_ttl_humanized, cp1):
    return pycspr.factory.create_deploy_parameters(
            account=pycspr.factory.create_public_key(
                cp1.algo,
                cp1.pbk
            ),
            chain_name=a_test_chain_id,
            dependencies=[],
            gas_price=10,
            timestamp=datetime.datetime.now(tz=datetime.timezone.utc).timestamp(),
            ttl=a_test_ttl_humanized
        )


@pytest.fixture(scope="function")
def deploy_params_static(a_test_chain_id, test_account_1):
    return pycspr.factory.create_deploy_parameters(
            account=pycspr.factory.create_public_key(
                test_account_1.algo,
                test_account_1.pbk
            ),
            chain_name=a_test_chain_id,
            dependencies=[],
            gas_price=10,
            timestamp=_A_KNOWN_DEPLOY_TIMESTAMP,
            ttl=pycspr.factory.create_deploy_ttl(_A_KNOWN_DEPLOY_HUMANIZED_TTL),
        )


@pytest.fixture(scope="function")
def a_deploy(deploy_params, cp1, cp2):
    deploy = pycspr.factory.create_transfer(
        deploy_params,
        amount=2500000000,
        correlation_id=1,
        target=cp2.account_key,
        )
    deploy.set_approval(pycspr.factory.create_deploy_approval(deploy, cp1))

    return deploy
