# Singleton Pattern - decorator-based approached


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances(cls)

    return get_instance


@singleton
class DatabaseConnection:
    def __init__(self, host, username, password):
        # In a real app, this would establish a database connection
        self.host = host
        self.username = username
        self.password = password
        print(f"Connecting to database on {host}")


# Creates only one connection regardless of how many times it's instantiated
conn1 = DatabaseConnection("localhost", "admin", "password123")
conn2 = DatabaseConnection("127.0.0.1", "root", "different_password")
print(conn1.host)  # Output: localhost (not 127.0.0.1)
print(conn1 is conn2)  # Output: True
