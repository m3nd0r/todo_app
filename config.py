import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dsgjKJDS&GSDGHDSgsd88gdshg38DU'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'todo.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
