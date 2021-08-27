import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import boto3
import io


def getImage(url):
    s3 = boto3.resource('s3', region_name='us-east-2')
    bucket = s3.Bucket('obsidian-product-images')
    object = bucket.Object(url)

    file_stream = io.StringIO()
    object.download_fileobj(file_stream)
    img = mpimg.imread(file_stream)

    return img