from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from lib.common_models import BaseModel
from location.models import Location

User = get_user_model()

# Create your models here.

# Post Database
class Post(BaseModel):
    caption = models.TextField(_('caption'), blank=True)
    user = models.ForeignKey(User, related_name = 'posts', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='posts', on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return "{} ({})".format(self.user.username, self.location)


# Tag Database
class Tag(BaseModel):
    title = models.CharField(_("title"), max_length=32)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title


# PostMedia Database
class PostMedia(BaseModel):
    IMAGE = 1
    VIDEO = 2

    TYPE_CHOICES = (
        (IMAGE, _("Image")),
        (VIDEO, _("Video")),
    )
    media_type = models.PositiveSmallIntegerField(_("media type"), choices=TYPE_CHOICES, default=IMAGE)
    post = models.ForeignKey(Post, related_name='media', on_delete = models.CASCADE)
    media_file = models.FileField(
        _('media file'),
        upload_to='contenty/media/',
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'mp4', 'wmv', 'flv', 'png'))]
    )

    class Meta:
        verbose_name = _("PostMedia")
        verbose_name_plural = _("PostsMedia")

    def __str__(self):
        return "{} - {}".format(str(self.post), self.media_file)
    

# PostTag Database
class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name='hashtags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("PostTag")
        verbose_name_plural = _("PostTags")

    def __str__(self):
        return "{} - {}".format(self.post, self.tag)