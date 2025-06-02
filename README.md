# FastAPI Application

This project is a FastAPI application that provides endpoints for user authentication, IMC calculations, and managing IMC history.

## Project Structure

```
fastapi-app
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── models.py        # Data models for the application
│   ├── routes           # Contains route definitions
│   │   └── __init__.py  # Exports routes for the application
│   └── services         # Contains service logic for business operations
│       └── __init__.py  # Service logic for user authentication and IMC calculations
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, execute the following command:
```
uvicorn app.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- **User Registration**: `POST /register`
- **User Login**: `POST /login`
- **Calculate IMC**: `POST /calculate-imc`
- **Get IMC History**: `GET /imc-history/{user_id}`


------------------------------------------------

## How to Start the MySQL Database

You can start the MySQL database using Docker Compose. Make sure you have `docker-compose.yml` in your project root (see example above).

### Steps

1. **Open a terminal in your project directory.**

2. **Run the following command:**
   ```
   docker-compose up -d db
   ```

   This will start the MySQL database container in the background.

3. **To stop the database:**
   ```
   docker-compose down
   ```

4. **To check logs for the database:**
   ```
   docker-compose logs db
   ```

The MySQL instance will be available at `localhost:3306` (or `db:3306` from other containers in the same compose network).

**Default credentials (as set in docker-compose.yml):**
- Host: `localhost`
- Port: `3306`
- Database: `imcdb`
- User: `imcuser`
- Password: `imcpassword`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.