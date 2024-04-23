from django.db import models
from django.urls import reverse




class Women2(models.Model):
    slug = models.SlugField(max_length=60, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    #   photo = models.ImageField(upload_to='', verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    tag = models.ManyToManyField('Tag', blank=True, related_name='tags')
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_created', '-title']
        indexes = [
            models.Index(fields=['-time_created'])
        ]


class Category(models.Model):
    slug = models.SlugField(max_length=60, unique=True, db_index=True, verbose_name='URL')
    name = models.CharField(max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.name


class Tag(models.Model):
    slug = models.SlugField(max_length=60, unique=True, db_index=True,
                           )
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug':self.slug})




class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(default=0, null=True)

    def __str__(self):
      return self.name










class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = [
            '-time_created',
            'title',
        ]
        indexes = [
            models.Index(fields=['-time_created'])
        ]
