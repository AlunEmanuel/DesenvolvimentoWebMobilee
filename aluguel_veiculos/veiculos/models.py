from django.db import models
from django.core.exceptions import ValidationError
from .consts import OPCOES_MARCAS, OPCOES_CORES, OPCOES_COMBUSTIVEIS

def validate_ano(value):
    if not (1950 < value < 2026):
        raise ValidationError('O ano deve ter 4 dígitos e estar entre 1951 e 2025.')

MARCAS_MODELOS = {
    1: ['A1', 'A3', 'A4', 'Q3', 'Q5'], # AUDI
    2: ['320i', 'X1', 'X3', 'X5', 'M3'], # BMW
    3: ['Onix', 'Cruze', 'S10', 'Tracker', 'Spin'], # CHEVROLET - GM
    4: ['488', 'Roma', 'Portofino', 'SF90', 'F8'], # FERRARI
    5: ['500', 'Panda', 'Tipo', 'Punto', 'Doblo'], # FIAT
    6: ['Fiesta', 'Focus', 'Mustang', 'EcoSport', 'Ka'], # FORD
    7: ['Civic', 'Fit', 'City', 'HR-V', 'WR-V'], # HONDA
    8: ['HB20', 'Creta', 'Tucson', 'Santa Fe', 'Azera'], # HYUNDAI
    9: ['Gol', 'Polo', 'Virtus', 'T-Cross', 'Jetta'], # VOLKSWAGEN
}

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField(validators=[validate_ano])
    cor = models.SmallIntegerField(choices=OPCOES_CORES, null=True, blank=True)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS, null=True, blank=True)
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='veiculos_fotos/', null=True, blank=True)

    def clean(self):
        super().clean()
        if self.modelo not in MARCAS_MODELOS.get(self.marca, []):
            raise ValidationError({'modelo': f'O modelo {self.modelo} não é válido para a marca {self.marca}.'})

    def __str__(self):
        return f"{self.get_marca_display()} {self.modelo} ({self.ano})"
    
    class Meta:
        db_table = 'veiculos_veiculo'
