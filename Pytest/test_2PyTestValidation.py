"""
Fixture in PyTest?

Pytest fixtures are a powerful feature that allows you to set up and tear down resources needed for your tests.
They help in creating reusable and maintainable test code by providing a way to define and manage the setup and
teardown logic.
"""

"""
Pytest provides four levels of fixture scopes:

- Function (Set up and tear down once for each test function)
- Class (Set up and tear down once for each test class)
- Module (Set up and tear down once for each test module/file)
- Session (Set up and tear down once for each test session i.e comprising one or more test files)
"""

import pytest

# @pytest.mark.smoke                        # Marked TC as smoke
def testthirdcheck(PreSetupWork):
    print("This is third test")