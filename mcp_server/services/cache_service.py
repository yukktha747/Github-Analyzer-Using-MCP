import json
import os
import time

from config import Config


class CacheService:
    """
    Simple file-based cache.
    """

    CACHE_FOLDER = "cache"

    @staticmethod
    def _cache_file(key: str):

        os.makedirs(
            CacheService.CACHE_FOLDER,
            exist_ok=True
        )

        filename = key.replace("/", "_") + ".json"

        return os.path.join(
            CacheService.CACHE_FOLDER,
            filename
        )

    @staticmethod
    def get(key: str):

        path = CacheService._cache_file(key)

        if not os.path.exists(path):
            return None

        with open(path, "r", encoding="utf-8") as file:
            cached = json.load(file)

        timestamp = cached["timestamp"]

        if (
            time.time() - timestamp
            > Config.CACHE_DURATION
        ):
            return None

        return cached["data"]

    @staticmethod
    def save(key: str, data):

        path = CacheService._cache_file(key)

        payload = {
            "timestamp": time.time(),
            "data": data,
        }

        with open(path, "w", encoding="utf-8") as file:
            json.dump(
                payload,
                file,
                indent=4
            )
