from rest_framework import generics, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.author == self.request.user:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Вы не можете изменять пост")

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_id'])
        if Like.objects.filter(post=post, user=self.request.user).exists():
            raise serializers.ValidationError("Вы уже поставили лайк на пост")
        serializer.save(user=self.request.user, post=post)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer