import helloworld


class TestHelloWorld(object):
    def test_returns_hello_world(self):
        assert helloworld.helloworld() == 'Hello world'
