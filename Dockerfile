FROM python:3.12-slim

WORKDIR /app

ARG USER_ARG
ENV USER_NAME=${USER_ARG:-"appuser"}

USER root

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

#Adding a non-root user
RUN useradd --create-home --uid 1001 $USER_NAME

USER $USER_NAME

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
