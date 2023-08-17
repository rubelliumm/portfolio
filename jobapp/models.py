import requests
from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.URLField(blank=True, null=True)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def insertLogo(self):
        image_response = requests.get(self.logo_url).content
        self.save()
        with open(f"media/org_logo/{self.name}.jpg", "ab") as file:
            file.write(image_response)
            self.logo = file.name[6:]
            self.save()
            file.close()
        self.logo_url = ""
        self.save()


class catagory(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class Circular(models.Model):
    title = models.CharField(max_length=255, unique=True)
    circular_ref_no = models.CharField(
        max_length=255, null=True, blank=True, unique=True
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    vacancy = models.IntegerField(blank=True, null=True)
    application_start_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    apply_link = models.CharField(max_length=50, default="https://", blank=True)
    description = models.TextField(max_length=1000, blank=True)
    catagory = models.ManyToManyField(catagory)
    tags = models.TextField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=50, blank=True)
    min_qualification = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=30, blank=True)
    grade_range = models.CharField(max_length=10, blank=True)
    application_fee = models.CharField(max_length=20, blank=True)
    application_published_on = models.DateField(blank=True, null=True)
    extra_info = models.TextField(max_length=300, blank=True)
    is_saved = models.BooleanField(default=False, blank=True)
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    pdf_file = models.FileField(null=True, blank=True, upload_to="circular/pdf/")

    def __str__(self):
        return self.title


class circularImage(models.Model):
    image = models.ImageField(upload_to="circular_image/", blank=True, null=True)
    circular = models.ForeignKey(Circular, on_delete=models.CASCADE)

    def __str__(self):
        return self.circular.title


class savedCircular(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    circular = models.ManyToManyField(Circular, blank=True)

    def __str__(self):
        return self.user.username + "'s saved circular"


class postName(models.Model):
    name = models.CharField(max_length=100)
    circular = models.ForeignKey(Circular, on_delete=models.DO_NOTHING)
    vacancy = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    topic_name = models.CharField(max_length=50, unique=True)
    topic_sub_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.topic_name


class Question(models.Model):
    question = models.CharField(max_length=200, unique=True)
    option_1 = models.CharField(max_length=30)
    option_2 = models.CharField(max_length=30)
    option_3 = models.CharField(max_length=30)
    option_4 = models.CharField(max_length=30)
    answer_choices = (
        ("op1", option_1),
        ("op2", option_2),
        ("op3", option_3),
        ("op4", option_4),
    )
    answer = models.CharField(max_length=30, choices=answer_choices, default=None)
    description = models.TextField(blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class examQuestion(models.Model):
    exam_name = models.CharField(
        max_length=100,
    )
    exam_taker = models.ForeignKey(Organization, on_delete=models.SET("Deleted Org."))
    exam_date = models.DateField(blank=True)

    def __str__(self):
        return self.exam_name


class questionImage(models.Model):
    question_image = models.ImageField(
        upload_to="question_image/",
        blank=True,
        null=True,
    )
    exam = models.ForeignKey(examQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return self.exam.exam_name


class News(models.Model):
    title = models.TextField(max_length=255, unique=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.DO_NOTHING, null=True
    )
    publish_data = models.DateTimeField(auto_now=True)
    details = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class Results(models.Model):
    title = models.TextField(max_length=255, unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    publish_date = models.DateTimeField(auto_now=True)
    details = models.TextField(max_length=1000, blank=True)
    pdf_file = models.FileField(null=True, blank=True, upload_to="results/")

    def __str__(self):
        return self.title
