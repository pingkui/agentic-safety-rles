from client.session import Session


def fetch_inventory(url):
    """Return the inventory document served at ``url``."""
    return Session().get_json(url)
