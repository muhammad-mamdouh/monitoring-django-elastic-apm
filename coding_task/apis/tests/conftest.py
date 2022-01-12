import random

import pytest


@pytest.fixture
def n_random_input_number():
    return random.randint(0, 10_000)
