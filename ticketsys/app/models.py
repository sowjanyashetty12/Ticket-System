from django.db import models

# Create your models here.
class Tickets(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    Name=models.CharField(max_length=50)
    Cisco_id=models.CharField(max_length=50)
    Ticket_description=models.CharField(max_length=200)
    OS_type=models.CharField(max_length=10)
    Tool=models.CharField(max_length=10)
    Ticket_State=models.CharField(max_length=50)


    def __str__(self):
        return self.Name+ "  "+self.Cisco_id