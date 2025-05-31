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

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.