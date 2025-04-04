from dataclasses import dataclass
from typing import List, Dict
from collections import defaultdict
import random
from datetime import datetime, timedelta

@dataclass
class Venta:
    """Clase para representar una venta"""
    id_venta: int
    producto: str
    cantidad: int
    precio_unitario: float
    fecha: datetime

class AnalizadorVentas:
    """Clase para analizar ventas y generar reportes"""
    def __init__(self):
        self.ventas: List[Venta] = []
        self.categorias = {"Electrónica": ["TV", "Laptop", "Celular"],
                         "Ropa": ["Camisa", "Pantalón", "Zapatos"],
                         "Hogar": ["Silla", "Mesa", "Lámpara"]}

    def generar_datos_ejemplo(self, num_ventas: int) -> None:
        """Genera datos de ventas aleatorios para demostración"""
        productos = [p for cat in self.categorias.values() for p in cat]
        for i in range(num_ventas):
            venta = Venta(
                id_venta=i + 1,
                producto=random.choice(productos),
                cantidad=random.randint(1, 10),
                precio_unitario=round(random.uniform(10.0, 500.0), 2),
                fecha=datetime.now() - timedelta(days=random.randint(0, 30))
            )
            self.ventas.append(venta)

    def calcular_ventas_por_categoria(self) -> Dict[str, float]:
        """Calcula el total de ventas por categoría"""
        totales = defaultdict(float)
        for venta in self.ventas:
            for categoria, productos in self.categorias.items():
                if venta.producto in productos:
                    totales[categoria] += venta.cantidad * venta.precio_unitario
        return dict(totales)

    def producto_mas_vendido(self) -> tuple[str, int]:
        """Encuentra el producto con mayor cantidad vendida"""
        cantidades = defaultdict(int)
        for venta in self.ventas:
            cantidades[venta.producto] += venta.cantidad
        return max(cantidades.items(), key=lambda x: x[1])

    def reporte_diario(self) -> Dict[datetime, float]:
        """Genera un reporte de ventas por día"""
        reporte = defaultdict(float)
        for venta in self.ventas:
            fecha = venta.fecha.date()
            reporte[fecha] += venta.cantidad * venta.precio_unitario
        return dict(reporte)

def main():
    # Crear instancia y generar datos
    analizador = AnalizadorVentas()
    analizador.generar_datos_ejemplo(100)
    
    # Mostrar resultados
    print("=== Reporte de Ventas ===")
    print("\n      Ventas")
    for cat, total in analizador.calcular_ventas_por_categoria().items():
        print(f"{cat}: ${total:,.2f}")
    
    producto, cantidad = analizador.producto_mas_vendido()
    print(f"\nProducto más vendido: {producto} \n{cantidad} unidades de {producto}")
    
    print("\nVentas de los ultimos 5 dias:")
    reporte = analizador.reporte_diario()
    for fecha, total in sorted(reporte.items())[-5:]:
        print(f"{fecha}: ${total:,.2f}")

if __name__ == "__main__":
    main()