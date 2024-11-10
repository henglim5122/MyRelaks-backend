from database import Base, engine
from models import Users

if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")
