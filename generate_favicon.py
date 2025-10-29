"""
Script para generar favicons en diferentes tamaños desde SVG
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Crear directorio si no existe
os.makedirs('static/images', exist_ok=True)

# Tamaños comunes de favicon
sizes = [16, 32, 48, 64, 128, 256]

def create_favicon(size):
    """Crea un favicon con gradiente y las iniciales RJ"""
    # Crear imagen con transparencia
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Dibujar círculo con gradiente simulado
    margin = int(size * 0.05)
    
    # Crear efecto de gradiente con múltiples círculos
    max_offset = (size - 2 * margin) // 2
    for i in range(20):
        alpha = int(255 * (1 - i/20) * 0.95)
        color_r = int(168 + (236 - 168) * i / 20)  # a855f7 a ec4899
        color_g = int(85 + (72 - 85) * i / 20)
        color_b = int(247 + (153 - 247) * i / 20)
        
        offset = min(int(i * size / 40), max_offset - 1)
        x0 = margin + offset
        y0 = margin + offset
        x1 = size - margin - offset
        y1 = size - margin - offset
        
        if x1 > x0 and y1 > y0:  # Verificar que el círculo sea válido
            draw.ellipse([x0, y0, x1, y1], fill=(color_r, color_g, color_b, alpha))
    
    # Dibujar brackets y texto
    bracket_width = max(2, int(size * 0.06))
    bracket_margin = int(size * 0.2)
    bracket_height = int(size * 0.4)
    
    # Bracket izquierdo <
    draw.line(
        [(bracket_margin, size//2 - bracket_height//2),
         (bracket_margin - bracket_width*2, size//2),
         (bracket_margin, size//2 + bracket_height//2)],
        fill=(255, 255, 255, 255),
        width=bracket_width
    )
    
    # Bracket derecho >
    draw.line(
        [(size - bracket_margin, size//2 - bracket_height//2),
         (size - bracket_margin + bracket_width*2, size//2),
         (size - bracket_margin, size//2 + bracket_height//2)],
        fill=(255, 255, 255, 255),
        width=bracket_width
    )
    
    # Dibujar texto RJ en el centro
    font_size = int(size * 0.35)
    try:
        # Intentar usar una fuente monospace
        font = ImageFont.truetype("consola.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("cour.ttf", font_size)
        except:
            # Fallback a fuente por defecto
            font = ImageFont.load_default()
    
    text = "RJ"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - int(size * 0.02)
    
    draw.text((text_x, text_y), text, fill=(255, 255, 255, 255), font=font)
    
    # Dibujar slash /
    slash_y = int(size * 0.75)
    slash_width = max(2, int(size * 0.06))
    draw.line(
        [(size//2 - int(size*0.08), slash_y + int(size*0.02)),
         (size//2 + int(size*0.08), slash_y - int(size*0.02))],
        fill=(255, 255, 255, 255),
        width=slash_width
    )
    
    return img

# Generar favicons en diferentes tamaños
for size in sizes:
    img = create_favicon(size)
    filename = f'static/images/favicon-{size}x{size}.png'
    img.save(filename, 'PNG')
    print(f"✓ Generado: {filename}")

# Crear el favicon.ico con múltiples tamaños
favicon_sizes = [16, 32, 48]
favicon_images = [create_favicon(size) for size in favicon_sizes]
favicon_images[0].save(
    'static/images/favicon.ico',
    format='ICO',
    sizes=[(size, size) for size in favicon_sizes]
)
print(f"✓ Generado: static/images/favicon.ico")

# Crear apple-touch-icon
apple_icon = create_favicon(180)
apple_icon.save('static/images/apple-touch-icon.png', 'PNG')
print(f"✓ Generado: static/images/apple-touch-icon.png")

print("\n✅ Todos los favicons han sido generados exitosamente!")
