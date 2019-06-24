import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgres://kbpddadfwwurgk:e6741f6ba904e7068a8255e3211a1bd072b72896e8675507decf7b3796e37cd2@ec2-75-101-147-226.compute-1.amazonaws.com:5432/dc4i1k15scgoru"
    SQLALCHEMY_TRACT_MODIFICATIONS = False
    S3_BUCKET = "gallery-website"
    S3_SECRET = "ZwdspoMrplh3ihwxKhSJy0mblFMsg0Bcc59LGJu0S"
    S3_KEY = "AKIAUE2VKDPVYXUUL3G2"
    S3_LOCATION = "http://s3.us-west-1.amazonaws.com/gallery-website"
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    SECRET_KEY = "secret-key-secret"
