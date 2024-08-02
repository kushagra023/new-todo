# Use a specific Python version for consistency
FROM python:3.12-slim

# Set the working directory
WORKDIR /data

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run database migrations
RUN python manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

# Use a non-root user for better security
RUN useradd -ms /bin/sh -u 1001 appuser
USER appuser

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
