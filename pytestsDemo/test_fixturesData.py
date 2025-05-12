import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self, dataLoad):
        for d in dataLoad:
            print(d)
