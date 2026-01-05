### Prerequisites
- Docker installed on your machine. You can download it from [here](https://www.docker.com/get-started).
- Python 3.x installed if you want to run the service without Docker.
- `pip` installed for managing Python packages.
- GNU Make installed for using the Makefile commands.


### Running the service
1. Run tests to ensure everything is working:
   ```make test```
2. Build the Docker image:
   ```make docker/build```
3. Start the Docker container:
   ```make docker/run```
4. The service will be accessible at `http://localhost:8080/<USER>`

