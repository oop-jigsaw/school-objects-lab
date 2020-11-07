def test_email_exception():
    """test that exception is raised for invalid emails"""
    with pytest.raises(Exception):
        assert check_email_format("bademail.com")