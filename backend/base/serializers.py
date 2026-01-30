# from rest_framework import serializers

# from .models import Projects, Tasks



# # 1. Task serializer(Read)
# # 2. Project    (read + nested)
# # 3. project create , task create



# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Tasks
#         fields=["id","title","compeleted","created_at"]

# class ProjectSerializer(serializers.ModelSerializer):
#     tasks= TaskSerializer(many=True,read_only=True)
#     class Meta:
#         model=Projects
#         fields=["id","name","description","created_at","tasks"]


# class ProjectCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Projects
#         fields=["name","description"]

# class TaskCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Tasks
#         fields=["title"]
        