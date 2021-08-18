from django.db import models

class Tv(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # shows
    def __repr__(self) -> str:
        return f'{self.id}: {self.name}'
    
class Shows(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(("%d-%m-%Y"), auto_now=False, auto_now_add=False)
    network = models.ForeignKey(Tv, related_name = "shows", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=255)
    
    def __repr__(self) -> str:
        return f'[{self.id}] {self.title}, {self.release_date} from {self.network}'