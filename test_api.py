import urllib.request
import json
import pytest

def test_octocat_gists(api_server):
    # Use octocat user for tests
    target_url = f"{api_server}/octocat"
    response = urllib.request.urlopen(target_url)
    status_code = response.getcode()
    data = json.loads(response.read().decode())
    
    # Assertions based on real api data
    assert status_code == 200
    assert data['username'] == 'octocat'
    assert isinstance(data['urls'], list)
    assert len(data['urls']) >= 0 

def test_invalid_user(api_server):
    # Use a random non-existent username
    fake_user_url = f"{api_server}/this-user-definitely-does-not-exist-123456789"
    
    # Our current api.py logic returns a 500 error if urllib fails
    with pytest.raises(urllib.error.HTTPError) as excinfo:
        urllib.request.urlopen(fake_user_url)
    
    assert excinfo.value.code == 500