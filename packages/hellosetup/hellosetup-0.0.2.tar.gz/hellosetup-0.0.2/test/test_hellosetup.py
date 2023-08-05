# test/test_hellosetup.py

# Allow pytest to find the package root
import sys
sys.path.append("src")

from hellosetup import get_article_url, greet

def test_greet():
    assert greet() == "Hello, setuptools!"
    
def test_get_article_url():
    assert "codesolid.com" in get_article_url()