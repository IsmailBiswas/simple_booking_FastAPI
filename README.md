# Fitness Studio Booking API

A RESTful API server built with FastAPI for managing fitness class bookings at
a fictional fitness studio. This lightweight API provides endpoints for viewing
available classes, making bookings, and retrieving booking information. It's an
assignment project.

## Features

- **Class Management**: View available fitness classes with pagination support
- **Booking System**: Create and manage client bookings for fitness classes
- **Data Validation**: Robust input validation using Pydantic models
- **Database Integration**: SQLAlchemy ORM with Alembic migrations
- **Interactive Documentation**: Auto-generated Swagger UI for API exploration
- **Comprehensive Testing**: Full test suite using pytest

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/IsmailBiswas/simple_booking_FastAPI.git
   cd simple_booking_FastAPI
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Start the server**
   ```bash
   fastapi dev app/main.py
   ```
This project uses **alembic** so if you want create a new database then first
delete the provided seeded database then create a new one using bellow comand
and after that start the server.

   ```bash
   alembic upgrade head
  ````

The API server will be available at `http://localhost:8000`

## API Documentation

### Interactive Documentation

Visit `http://localhost:8000/docs` to access the Swagger UI, where you can:
- Explore all available endpoints
- Test API calls directly from the browser
- View request/response schemas
- Download the OpenAPI specification

### Alternative Documentation

Redoc documentation is available at `http://localhost:8000/redoc`

## API Endpoints

### Get Classes
Retrieve available fitness classes with optional pagination.

**Endpoint:** `GET /classes/`

**Query Parameters:**
- `offset` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

### Create Booking
Book a fitness class for a client.

**Endpoint:** `POST /book/`

**Request Body:**
```json
{
  "client_name": "John Doe",
  "client_email": "john@example.com",
  "class_id": 1
}
```

### Get Bookings
Retrieve bookings for a specific client.

**Endpoint:** `GET /booking/`

**Query Parameters:**
- `client_email` (required): Email address of the client
- `offset` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

## Testing

Run the comprehensive test suite to ensure everything works correctly:

```bash
# Make sure you're in the virtual environment
pytest -v
```

## Example API Usage

### Using cURL

**Fetch available classes:**
```bash
curl -X GET "http://localhost:8000/classes/?offset=0&limit=10" \
     -H "accept: application/json"
```

**Create a new booking:**
```bash
curl -X POST "http://localhost:8000/book/" \
     -H "accept: application/json" \
     -H "Content-Type: application/json" \
     -d '{
       "client_name": "Alice Smith",
       "client_email": "alice@example.com",
       "class_id": 1
     }'
```

**Retrieve client bookings:**
```bash
curl -X GET "http://localhost:8000/booking/?client_email=alice%40example.com&limit=10" \
     -H "accept: application/json"
```

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

```
## License

This project is open source and available under the [MIT License](LICENSE).
