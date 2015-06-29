from time import time

def RateLimiter(delay):
    cache = {}

    def recent(key):
        now = time()

        if key in cache and (now - cache[key]) < delay:
            return True

        cache[key] = now
        return False

    return recent

