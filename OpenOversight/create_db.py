#!/usr/bin/python

from migrate.versioning import api
from migrate.exceptions import DatabaseAlreadyControlledError
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path

try:
    db.create_all()

    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI,
                           SQLALCHEMY_MIGRATE_REPO)
    else:  # the database already exists
        api.version_control(SQLALCHEMY_DATABASE_URI,
                           SQLALCHEMY_MIGRATE_REPO,
                           api.version(SQLALCHEMY_MIGRATE_REPO))

except DatabaseAlreadyControlledError:
  print "Database already exists, not creating"
