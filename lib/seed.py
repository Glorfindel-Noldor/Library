from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model_1 import Base, ExampleModel  # Adjust the import path as needed

engine = create_engine('sqlite:///lib/company.db')  # Adjust the path if needed
Session = sessionmaker(bind=engine)
session = Session()

# Ensure tables are created (if not already)
Base.metadata.create_all(engine)

# Create some example data
example_data = [
    ExampleModel(name="Example 1"),
    ExampleModel(name="Example 2"),
    ExampleModel(name="Example 3")
]

# Add the data to the session and commit it to the database
session.add_all(example_data)
session.commit()

print("Database seeded!")