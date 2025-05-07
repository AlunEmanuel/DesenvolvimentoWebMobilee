from django.db import models
from django.core.exceptions import ValidationError

def validate_ano(value):
    if not (1950 < value < 2026):
        raise ValidationError('O ano deve ter 4 dígitos e estar entre 1951 e 2025.')

MARCAS_MODELOS = {
    'Ford': ['Fiesta', 'Focus', 'Mustang', 'Explorer', 'F-150'],
    'Chevrolet': ['Camaro', 'Silverado', 'Malibu', 'Equinox', 'Tahoe'],
    'Toyota': ['Corolla', 'Camry', 'RAV4', 'Highlander', 'Tacoma'],
    'Honda': ['Civic', 'Accord', 'CR-V', 'Pilot', 'Fit'],
    'Nissan': ['Altima', 'Sentra', 'Rogue', 'Pathfinder', 'Frontier'],
    'Volkswagen': ['Jetta', 'Passat', 'Tiguan', 'Golf', 'Atlas'],
    'Hyundai': ['Elantra', 'Sonata', 'Tucson', 'Santa Fe', 'Kona'],
    'Jeep': ['Wrangler', 'Cherokee', 'Grand Cherokee', 'Compass', 'Renegade'],
    'Tesla': ['Model S', 'Model 3', 'Model X', 'Model Y', 'Cybertruck'],
    'BMW': ['3 Series', '5 Series', 'X3', 'X5', 'Z4'],
    'Mercedes-Benz': ['C-Class', 'E-Class', 'GLC', 'GLE', 'S-Class'],
    'Porsche': ['911', 'Cayenne', 'Macan', 'Panamera', 'Taycan'],
    'Cadillac': ['Escalade', 'XT5', 'CT5', 'XT4', 'CT4'],
    'Fiat': ['500', 'Panda', 'Tipo', 'Punto', 'Doblo'],
    'Mitsubishi': ['Outlander', 'Eclipse Cross', 'Mirage', 'Lancer', 'Pajero'],
    'Ferrari': ['488', 'Roma', 'Portofino', 'SF90', 'F8'],
    'Lamborghini': ['Huracan', 'Aventador', 'Urus', 'Gallardo', 'Murcielago'],
    'McLaren': ['720S', '570S', '650S', 'P1', 'Artura'],
    'Bugatti': ['Chiron', 'Veyron', 'Divo', 'Centodieci', 'Bolide'],
    'Peugeot': ['208', '308', '508', '2008', '3008'],
    'Renault': ['Clio', 'Megane', 'Captur', 'Kadjar', 'Talisman'],
    'Suzuki': ['Swift', 'Vitara', 'Jimny', 'Baleno', 'Celerio']
}

class Veiculo(models.Model):
    marca = models.CharField(max_length=50, choices=[(marca, marca) for marca in MARCAS_MODELOS.keys()])
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField(validators=[validate_ano])
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if self.modelo not in MARCAS_MODELOS.get(self.marca, []):
            raise ValidationError({'modelo': f'O modelo {self.modelo} não é válido para a marca {self.marca}.'})

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
