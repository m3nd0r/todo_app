import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dsgjKJDS&GSDGHDSgsd88gdshg38DU'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
