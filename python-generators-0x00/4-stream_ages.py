#!/usr/bin/python3
seed = __import__('seed')


def stream_user_ages():
    """
    Generator that yields one user age at a time from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    # Yield one age at a time (memory-efficient)
    for row in cursor:
        yield row['age']

    connection.close()


def average_age():
    """
    Calculates the average age using the generator without loading all users into memory.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average = total_age / count
        print(f"Average age of users: {average:.2f}")


if __name__ == "__main__":
    average_age()
