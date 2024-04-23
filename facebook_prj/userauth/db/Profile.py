from django.db import models
from PIL import Image
from shortuuid.django_fields import ShortUUIDField
from .User import User

RELATIONSHIP = (("single", "Single"), ("Married", "Married"))

GENDER = (("female", "Female"), ("male", "Male"))


def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.user.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)


class Profile(models.Model):
    pid = ShortUUIDField(
        max_length=25, length=7, alphabet="abcdefghijklmnopqrstuvwxyz0123456789"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_img = models.ImageField(upload_to=user_directory_path, default="cover.jpg")
    image = models.ImageField(upload_to=user_directory_path, default="default.jpg")
    fullname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER, default="male")
    relationship = models.CharField(
        max_length=100, choices=RELATIONSHIP, default="Single"
    )
    bio = models.CharField(max_length=200, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)

    country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    working_at = models.CharField(max_length=200, null=True, blank=True)

    instagram = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=200, null=True, blank=True)
    veriifed = models.BooleanField(default=False)

    folllowers = models.ManyToManyField(User, blank=True, related_name="followers")
    following = models.ManyToManyField(User, blank=True, related_name="following")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    blocked = models.ManyToManyField(User, blank=True, related_name="blocked")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
