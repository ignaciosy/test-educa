from django.db import models
from django.db.models import Max

# Create your models here.

def upload_image(obj, fname):
	ext = fname.split(".")[-1]
	image_name = "Blog_image_{}".format(obj.id_int)
	image_name = image_name + "." + ext
	return u"/".join(["blog_images", image_name])


class Blog(models.Model):
	id_int = models.IntegerField(blank=True, null=True, default=0)
	Titulo = models.CharField(max_length=255, blank=True)
	Descripcion = models.CharField(max_length=255, blank=True)
	Foto = models.FileField(upload_to=upload_image)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	
	def save(self, *args, **kwargs):
		blogs = Blog.objects.all()
		maxid = -1
		for blog in blogs:
			if blog.id_int > maxid:
				maxid = blog.id_int
		self.id_int = maxid + 1
		super(Blog, self).save(*args, **kwargs)