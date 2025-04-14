from fastapi import FastAPI

# Create a FastAPI application instance
app = FastAPI()

# Define a GET endpoint at the route "/hello"
@app.get("/Hello")
def hello_world():
    # Return a simple string response
    return{"message":"Hello world"}