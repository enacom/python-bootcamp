FROM python:3.9-slim

# Install system dependencies
# RUN apt-get update --yes && \
#     apt-get install --yes build-essential

# Configure files and directories
WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

# Install Python requirements
RUN pip install --no-cache-dir --upgrade --requirement /api/requirements.txt

COPY ./api /api

EXPOSE 9000

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "9000"]
