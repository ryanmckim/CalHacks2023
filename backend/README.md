# Running the backend Flask app

## Using venv
```

cd backend
source venv/bin/activate

```
cd backend

// Mac/Linux
source venv/bin/activate
// Windows
py -m venv venv
.\venv\Scripts\activate

// Installing dependencies
pip install -r requirements.txt

// Run the server
python server.py

```

## Using Docker
From the home directory, run `docker build -f Dockerfile.api -t tuneai-app-api .` to build the Docker image. Then, run `docker run --rm -p 5000:5000 tuneai-app-api .` to start the server.
