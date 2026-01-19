import pytest

def add(a, b):
    return a+b


def is_even(a):
    return a % 2 == 0

@pytest.fixture
def sample_data():
    return {"env": "dev", "region": "us-east-1"}

# test = sample_data()
# print(test.get("env", ""))


# def test_dict(var):
#     return var


# konda = test_dict({"env": "dev", "region": "us-east-1"})    
# print(konda)