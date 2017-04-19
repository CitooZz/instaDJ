from uuid import uuid4


def image_upload_handler(instance, filename):
    return 'posts/{}/{}.{}'.format(instance.creator.username, uuid4().get_hex(), filename.split('.')[-1])
