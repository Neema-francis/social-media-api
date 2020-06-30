"""
    Defines models for scial media app 
"""
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AbstractBase(models.Model):
    """
        These fields added to all tables
    """
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Tags(models.Model):
    """
        Tags for storyCards
    """
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class StoryCards(AbstractBase):
    """
        Admin create a story cards
    """
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="story_user", null=True, blank=True)
    tag = models.ManyToManyField(Tags, related_name="story_tag")
    weight = models.IntegerField(default=0)  # Weitage for tag in a StoryCard
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['weight']


class StoryCardsImage(AbstractBase):
    """
        Admin can be create story card image
    """
    story_card = models.ForeignKey(StoryCards, on_delete=models.CASCADE, related_name="story_image")
    attachment = models.ImageField(upload_to="attachement/file")
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.story_card.name


class userResponse(AbstractBase):
    """
        User response for story card
    """
    STORY_CARDS_STATUS = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )

    story_card = models.ForeignKey(StoryCards, on_delete=models.CASCADE, related_name="story_tag")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_response")
    status = models.CharField(max_length=100, choices=STORY_CARDS_STATUS)


class userTagWeitage(models.Model):
    """
        Tag weitage from user
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="story_tag_user")
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name="user_story_tag")
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering = ['weight']
  

