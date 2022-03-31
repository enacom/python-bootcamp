FROM python:3.9-slim

# Install system dependencies
RUN apt-get update --yes && \
    apt-get install --yes build-essential

# Configure files and directories
WORKDIR /bootcamp

COPY ./requirements.txt /bootcamp/requirements.txt

# Install Python requirements
RUN pip install --no-cache-dir --upgrade --requirement /bootcamp/requirements.txt

COPY . /bootcamp

EXPOSE 9000

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "9000"]
