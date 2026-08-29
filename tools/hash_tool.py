import hashlib


def generate_hash(text, algorithm):

    try:
        hasher = hashlib.new(algorithm)

    except ValueError:
        return None

    hasher.update(text.encode("utf-8"))

    return hasher.hexdigest()
