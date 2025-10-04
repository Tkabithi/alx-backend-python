import requests
import io
import csv
import uuid

def insert_data(connection, csv_url):
    try:
        cursor = connection.cursor()

        # Fetch file from the internet
        response = requests.get(csv_url)
        response.raise_for_status()   # raise error if download fails
        file = io.StringIO(response.text)

        # Read CSV content
        reader = csv.DictReader(file)
        for row in reader:
            user_id = str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']

            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (user_id, name, email, age))

        connection.commit()
        print("Data inserted successfully")
        cursor.close()

    except Exception as e:
        print(f"Error inserting data: {e}")
