from app import *
import pytest
from config import extract_data

def test_add():
    results = add(5,5)
    assert results == 10
    
def test_even_num():
    assert is_even(4) is True
    
def test_odd_num():
    assert is_even(5) is False
    
def test_sample_data(sample_data):
    assert sample_data["env"] == "dev"
    
    
def test_extract_data():
    result = extract_data("pod.yaml")
    assert result["kind"] == "Pod"