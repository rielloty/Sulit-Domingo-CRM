from django.db import models



class Team_A_Member(models.Model):
		created_at = models.DateTimeField(auto_now_add=True)
		first_name = models.CharField(max_length=50)
		code_name = models.CharField(max_length=50)
		food_to_bring = models.CharField(max_length=200)
		nabunot = models.CharField(max_length=100)

		def __str__(self):
				return(f"{self.code_name}")