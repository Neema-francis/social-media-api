from rest_framework import serializers

from social_media_api.utilities import DynamicFieldsSerializerMixin
from social_media_api.models import StoryCards, StoryCardsImage, Tags \
                                    , userResponse, userTagWeitage


class StoryCardsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryCardsImage
        fields = ('image',)

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'name',)


class StoryCardsSerialzer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = StoryCards
        fields = ('name', 'description', 'tag','weight', 'image',)

    def create(self, validated_data, user):
        validated_data['user'] = user
        image = validated_data.pop("image", '')
        tags = validated_data.pop("tag", [])
        story_card_obj = StoryCards.objects.create(**validated_data)
        for each_tag in tags:
            story_card_obj.tag.add(each_tag)
        if image:
            StoryCardsImage.objects.create(story_card=story_card_obj, attachment=image)  


class StoryCardsListSerialzer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    tag = serializers.SerializerMethodField("_tag_")
    images = serializers.SerializerMethodField("_image_")
    status = serializers.SerializerMethodField("_status_")

    def _tag_(self, tag_object):
        return TagsSerializer(tag_object.tag.all(), many=True).data

    def _image_(self, tag_object):
        return StoryCardsImage.objects.filter(story_card=tag_object.id).values_list("attachment", flat=True)

    def _status_(self, tag_object):
        try: return userResponse.objects.filter(story_card=tag_object.id).last().status
        except: ''

    class Meta:
        model = StoryCards
        fields = ('id','name', 'description', 'tag','weight', 'images', 'status', 'created_on', )


class StoryCardResponseSerialzer(serializers.Serializer):
    status = serializers.CharField(required=True)

    def create(self, validated_data, instance, user):
        validated_data['user'] = user
        validated_data['story_card'] = instance
        tags_list = instance.tag.all()
        story_card_weitage = instance.weight
        story_card_obj = userResponse.objects.create(**validated_data)
        status = validated_data.pop("status", 'dislike')
        for each_tag in tags_list:
            get_data, _ = userTagWeitage.objects.get_or_create(user=user, tag=each_tag)
            if status == 'like':
                get_data.weight = get_data.weight + story_card_weitage
            else:
                get_data.weight = get_data.weight - story_card_weitage
            get_data.save()
    
   