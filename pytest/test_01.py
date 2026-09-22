import pytest



@pytest.mark.smoke
def test_firstfunc(pretest_session):
    print("I am executed first")

@pytest.mark.skip
def test_secondfunc(pretest_session):
    print("I am executed seocnd")




