from django.db import models

# Create your models here.

#model enseignant
class Enseignant(models.Model):
    id_ensg = models.AutoField(primary_key=True)
    nom_eng = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telph = models.IntegerField()
    Diplome = models.CharField(max_length=50)
    Statut = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/')

    #class Meta:
        #db_table = "Enseignant"

    #def __str__(self):
         #return str(self.nom_eng)

 

    
    
    
    
    
    
    
    
    
    
    
    
    
