from django.db import models


class Name(models.Model):
	name = models.CharField(max_length=100, unique=True)
	image = models.ImageField(upload_to=None)
	nickname = models.CharField(max_length=50)
	bio = models.CharField(max_length=200)

	def __str__(self):
		return '{} {} {}'.format(self.name, self.nickname, self.bio)

	def get_absolute_url(self):
		return reverse('string', args=[str(self.name)])

	@property
	def is_tutorial(self):
		return self.units == 1


class Tasks(models.Model):
	name = models.ForeignKey(Name, on_delete=models.CASCADE)
	key = models.CharField(max_length=2)
	task = models.CharField(max_length=100)