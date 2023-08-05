# Test-tools


## Usage

Test files in project

    /tests
        __init__.py
        /pkg1
            /fixtures
                foo1.json
                foo2.json
            __init__.py
            test1.py
        /pkg2
            /fixtures
                bar1.json
                bar2.json
            __init__.py
            test2.py


Content of "**tests/pkg1/fixtures/foo1.json**":

```javascript

    {
        "blah1": [
            ["foo"],
            ["bar"],
            [1],
            [2],
            [true],
            [null]
        ],
        "blah2": [
            [-1234, 0],
            [3456, -2.345],
            [1, 1],
            [99999, false],
            [11, 789],
            [null, null]
        ]
    }
```

Content of "**tests/pkg1/test1**":

```python 

    from unittest import TestCase
    
    from test_tools import data_provider, FixtureManager
    
    fx_man1 = FixtureManager()
    fx_man1.load(fixture_file='foo1')
    
    fx_man2 = FixtureManager()
    fx_man2.load(fixture_file='foo2')
    
    
    class MyTestCase(TestCase):
        @data_provider(fx_man1['blah1'])
        def test_my_cool_feature(self, param1):
            # some code
            pass
            
        @data_provider(fx_man1['blah2'])
        def test_my_cool_feature(self, param1, param2):
            # some code
            pass
            
        @data_provider(fx_man2['blah3'])
        def test_my_cool_feature(self, param):
            # some code
            pass
```     
