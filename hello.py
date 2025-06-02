def say_hello():
    return "Hello, CI/CD!"

def test_say_hello():
    assert say_hello() == "Hello, CI/CD!"  #hello test
