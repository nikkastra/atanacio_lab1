from django.db import models


class Name(models.Model):
	name = models.CharField(max_length=100, unique=True, default="test")
	nickname = models.CharField(max_length=50, default='Your nickname')
	bio = models.CharField(max_length=200, default='A short bio about yourself')
	image = models.ImageField(upload_to='profilepictures', default='static/img/default.jpg')

	def __str__(self):
		return '{} {} {}'.format(self.name, self.nickname, self.bio)

	def get_absolute_url(self):
		return reverse('name_detail', args=[str(self.pk)])

	@property
	def is_tutorial(self):
		return self.units == 1


class Key(models.Model):
	key = models.CharField(max_length=50)
	description = models.CharField(max_length=100)

	def __str__(self):
		return '{} - {}'.format(self.key, self.description)


class Tasks(models.Model):
	name = models.ForeignKey(Name, on_delete=models.CASCADE)
	key = models.ForeignKey(Key, on_delete=models.CASCADE)
	task = models.CharField(max_length=100)

	def __str__(self):
		return '{}: {}'.format(self.key, self.task)