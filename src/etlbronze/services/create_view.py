from clickhouse_connect import get_client

class NewView:
    def __init__(self, clickhouse_host: str, clickhouse_database: str, username: str = None, password: str = None):
        self.client = get_client(
            host=clickhouse_host,
            port=8123,
            database=clickhouse_database,
            username=username,
            password=password
        )

    def create_view(self, view_name: str, query: str):
        print("Creating view...")
        try:
            self.client.command(f"CREATE VIEW IF NOT EXISTS grupo3.{view_name} AS {query}")
            print(f"View {view_name} created successfully.")
        except Exception as e:
            print(f"Error creating view: {e}")
            