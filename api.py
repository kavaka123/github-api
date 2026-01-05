import http.server
import urllib.request
import json

class GitHubAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        username = self.path.split('/')[-1]
        # Validate username is passed in the URL
        if not username:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Username is required') 
            return None
        
        github_url = f'https://api.github.com/users/{username}/gists'
        headers = {"User-Agent": "GitHubAPIHandler"}

        try:
            req = urllib.request.Request(github_url, headers=headers)
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())

                #Get urls of gists
                gist_urls = [gist['html_url'] for gist in data]
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"username": username, "urls": gist_urls}).encode())

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f'Error fetching gists: {e}'.encode())
            return None 

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, GitHubAPIHandler)
    print("Starting server on port 8080...")
    httpd.serve_forever()