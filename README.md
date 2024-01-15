# frontend-backend-containerd-requests

This is a simple Dockerized application consisting of two backend services (backend1 and backend2) and a frontend service. The frontend randomly selects one of the backends and makes a request to it. The selected backend responds with a message, and the frontend displays both the chosen backend and the response.

## Access the frontend:

Open your web browser and navigate to http://localhost:5000/. The frontend will randomly choose a backend, make a request, and display the chosen backend along with the response.

## Technologies Used
### Flask:

All services (frontend, backend1 and backend2) are built using the Flask framework.

The frontend (frontend) uses the `requests library` to make HTTP requests to the chosen backend, and it displays the received response.

## Notes
This is a development setup, and the containers are running in a bridge network named mynetwork. Ensure that the required ports (5000, 5001, 5002) are available 