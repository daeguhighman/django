from django.db import models
from django.contrib.auth.models import User # 추가

### 🔻 이 부분 추가 ####
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=32, blank=True)
    major = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f"id={self.id}, user_id={self.user.id}, college={self.college}, major={self.major}"
### 🔺 이 부분 추가 ####