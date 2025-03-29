import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')
django.setup()

from backend.tasks.models import Task

fake = Faker()

def create_dummy_tasks(n):
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.paragraph(nb_sentences=3)
        Task.objects.create(title=title, description=description)

if __name__ == '__main__':
    create_dummy_tasks(100)
    print("Dummy tasks created successfully.")
