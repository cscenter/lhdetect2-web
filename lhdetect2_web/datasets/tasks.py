from django.conf import settings
from celery import shared_task
from subprocess import Popen, PIPE

import os

from datasets.models import Image


@shared_task
def process_image(img_id):
    img = Image.objects.get(id=img_id)
    img_path = img.file.path

    program = os.path.join(settings.STATIC_URL, 'lhdetect2')
    proc = Popen([program, '-c', 'detect', '-i', img_path, '-o', 'tmp.png'],
                 stdout=PIPE, stderr=PIPE, cwd=settings.BASE_DIR)
    check_image_process.apply_async([proc, img_id], countdown=0.5)


@shared_task
def check_image_process(proc, img_id):
    retcode = proc.poll()
    if retcode is not None:
        if retcode != 0:
            # TODO add error handling
            pass

        img = Image.objects.get(id=img_id)
        img.lhdetect_desc = proc.stdout
        img.save()
    else:
        check_image_process.apply_async([proc, img_id], countdown=0.5)
