from django.db import models
from django.utils.text import slugify

class Module(models.Model):
    CODE_LENGTH = 7

    code = models.SlugField(max_length=CODE_LENGTH, editable=False, unique=True)
    departement = models.CharField(max_length=3)
    intitule = models.CharField(max_length=200)
    coef = models.IntegerField()
    nombre_credit = models.IntegerField()
    volume_horaires_cm = models.IntegerField()
    volume_horaires_td = models.IntegerField()
    volume_horaires_tp = models.IntegerField()
    unite_enseignement = models.CharField(max_length=100)
    semestre = models.IntegerField()
    enseignant_responsable = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.pk:  # Nouvel enregistrement (création)
            modules_count = Module.objects.filter(departement=self.departement, semestre=self.semestre).count()
            self.code = self.generate_code(self.departement, self.semestre, modules_count + 1)

        super().save(*args, **kwargs)

    def generate_code(self, departement_code, semestre, module_number):
        return f"{departement_code}{semestre:02d}{module_number:02d}"

    def __str__(self):
        return f"{self.code} - {self.intitule}"
    
    
    
    
    
    
    
