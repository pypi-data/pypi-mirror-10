Python Service Container
========================

This is a pretty trivial service container with the ability to register Services in it. On
retrieval of an registered service the class got instantiated and behaves as a singleton.

```
    from servicecontainer import Service, Container, ServiceInterface

    # This is a sample service
    class ExampleService(object):
        val = None
        def __init__(self, param1):
            self.val = param1

    class ExampleService2(ServiceInterface):
        val = None
        def __init__(self, param1):
            self.val = param1

        @classmethod
        def asService(cls, parameters):
            return Service("testservice2", cls, parameters)

    # Create the container
    c = Container()

    # build an service
    s = Service("testservice", ExampleService, {"param1": "param1_value"})

    # add the service to the container
    c.add(s)
    c.add(ExampleService2.asService({"param1": "param1_value"}))

    # retrive the service from the container (gots instantiated at this point)
    instance = c.get('testservice')
    self.assertEqual('param1_value', instance.val)

    # list all services
    list = c.list()
    self.assertEqual(2, len(list))
    self.assertEqual(list[0], 'testservice')

    # be sure its the same instance
    instance2 = c.get('testservice')
    assert instance is instance2
```
