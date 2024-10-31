from config.celery import app


@app.task(bind=True, ignore_result=True)
def resize_image_task(self, id):
    from core.models import Account
    from django.core.files.base import ContentFile
    from io import BytesIO

    from PIL import Image as PILImage

    instance = Account.objects.get(id=id)
    print(instance.avatar.path)
    with PILImage.open(instance.avatar) as im:
        # Resize the image only if it's not already the desired size
        if im.size != (400, 400):
            im = im.resize((400, 400), PILImage.LANCZOS)

            # Convert image to RGB mode if not already in that mode
            if im.mode != 'RGB':
                im = im.convert('RGB')
            # Save the resized image to an in-memory file
            buffer = BytesIO()
            im.save(buffer, format='JPEG')  # or use instance.avatar.file.content_type if necessary
            buffer.seek(0)

            # Save the image back to the avatar field
            instance.avatar.save(
                instance.avatar.name,
                ContentFile(buffer.read()),
                save=True
            )
    print(instance.avatar.path)
