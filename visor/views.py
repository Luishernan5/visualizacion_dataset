from django.shortcuts import render
import pandas as pd

def home(request):
    df_html = None
    error = None

    if request.method == 'POST':
        url = request.POST.get('url')

        # Convertir URL de GitHub a RAW si es necesario
        if 'github.com' in url:
            url = url.replace('github.com', 'raw.githubusercontent.com')\
                     .replace('/blob/', '/')

        try:
            # Leer CSV corregido
            df = pd.read_csv(url, on_bad_lines='skip')

            # Asegurarnos que 'duration' sea numérica
            if 'duration' in df.columns:
                df['duration'] = pd.to_numeric(df['duration'], errors='coerce').fillna(0)

            # Mostrar primeras 20 filas
            df_html = df.head(20).to_html(classes='table table-striped', index=False)
        except Exception as e:
            error = f"Error al cargar los datos: {e}"

    return render(request, 'home.html', {'df_html': df_html, 'error': error})
