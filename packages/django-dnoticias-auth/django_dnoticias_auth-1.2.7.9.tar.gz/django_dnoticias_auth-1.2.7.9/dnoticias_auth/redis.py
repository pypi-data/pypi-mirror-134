import redis
import logging
from datetime import datetime

from django.utils import timezone
from django.conf import settings

from redis_sessions.session import RedisServer

from dnoticias_auth.exceptions import InvalidSessionParameters

logger = logging.getLogger(__name__)


class KeycloakSessionStorage:
    REDIS_PREFIX = "dj_session"

    def __init__(self, keycloak_session_id: str, django_session_id: str):
        self.server = RedisServer(None).get()
        self.keycloak_session_id = keycloak_session_id
        self.django_session_id = django_session_id

        if not any([self.keycloak_session_id, self.django_session_id]):
            raise InvalidSessionParameters()

    def exists(self):
        return self.server.exists(self.get_real_stored_key())

    def create_or_update(self):
        if self.exists():
            self.delete()

        self.save()

    def save(self):
        logger.debug("Saving key: %s", self.keycloak_session_id)
        if redis.VERSION[0] >= 2:
            self.server.setex(
                self.get_real_stored_key(),
                self.get_expiry_age(),
                self.django_session_id
            )
        else:
            self.server.set(self.get_real_stored_key(), self.django_session_id)
            self.server.expire(self.get_real_stored_key(), self.get_expiry_age())

    def delete(self):
        logger.debug("Deleting key: %s", self.keycloak_session_id)

        try:
            self.server.delete(self.get_real_stored_key())
        except:
            pass

    def get_real_stored_key(self) -> str:
        return f"{self.REDIS_PREFIX}:{self.keycloak_session_id}"

    def get_expiry_age(self, **kwargs):
        return 3600 * 24 * 365
