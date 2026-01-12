# STEP 1: Use Python 3.10 slim as base
FROM python:3.10-slim

# STEP 2: Set working directory
WORKDIR /app

# STEP 3: Copy backend and frontend
COPY backend ./backend
COPY frontend ./frontend

# STEP 4: Install dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# STEP 5: Expose backend port
EXPOSE 5000

# Use Flask environment variables
ENV FLASK_APP=backend/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

CMD ["flask", "run"]




