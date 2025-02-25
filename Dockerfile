FROM python:3.11.7
WORKDIR /app
COPY . .
RUN pip install numpy pandas scikit-learn wandb
CMD ["python", "/app/distance_classification.py"]
