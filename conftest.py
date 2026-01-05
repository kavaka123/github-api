import pytest
import threading
import time
import http.server
from api import GitHubAPIHandler

@pytest.fixture(scope="session")
def api_server():
    # Setup: Start the server on a test port
    server_address = ('localhost', 8080)
    httpd = http.server.HTTPServer(server_address, GitHubAPIHandler)
    
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
    
    # Give it a tiny bit of time to bind to the port
    time.sleep(0.1)
    
    yield "http://localhost:8080"  # This is provided to the tests
    
    # Teardown: Stop the server after tests are done
    httpd.shutdown()
    httpd.server_close()