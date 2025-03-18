# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--endpoint-url", action="store",
        default="localhost.com", help="endpoint url"
    )

    parser.addoption(
        "--git-hash",
        action="store",
        default="akasfsada",
        help="hash of the deployed code",
    )