# WeatherPulseAPI

WeatherPulseAPI is a Django-based REST API that periodically aggregates real-time weather data from Poland's IMGW meteorological service using Celery and Redis. The system automatically stores these weather metrics in a PostgreSQL database and exposes clean API endpoints for weather stations, measurements, and statistics.

## Setup and Running

1. **Clone and navigate**:
   ```bash
   git clone https://github.com/PiotrFrasik/WeatherPulseAPI.git
   cd WeatherPulseAPI/imgw_aggregator
   ```

2. **Environment Variables**:
   Create a `.env` file in `imgw_aggregator/` with:
   ```env
   DEBUG=True
   SECRET_KEY=django-insecure-your-secret-key-here
   DB_NAME=weather_db
   DB_USER=weather_user
   DB_PASSWORD=weather_pass123
   DB_HOST=127.0.0.1
   DB_PORT=5433
   ```

3. **Start services**:
   ```bash
   docker compose up -d
   ```

4. **Virtual Environment**:
   ```bash
   python -m venv venv
   pip install -r requirements.txt
   ```

5. **Migrations and Initial Data**:
   ```bash
   python manage.py migrate
   python manage.py fetch_weather
   ```

6. **Start Django & Celery**:
   - Run server: `python manage.py runserver`
   - Run Celery (Windows): `celery -A core worker -l info -P solo`

## API Endpoints

- `/api/` (GET) - API Root
- `/api/weather` (GET) - Weather measurements list
- `/api/weather/stations/` (GET) - Weather stations list
- `/api/weather/stats/` (GET) - Aggregated weather statistics
- `/api/schema/` (GET) - OpenAPI 3.0 schema
- `/api/docs/` (GET) - Swagger UI documentation

## Running Tests

```bash
python manage.py test weather
```