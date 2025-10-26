from django.shortcuts import render
import pandas as pd

def home(request):
    df_html = None
    error = None

    if request.method == 'POST':
        url = request.POST.get('url')

        # Reemplazar con la URL RAW si el usuario puso la normal
        if 'github.com' in url:
            url = url.replace('github.com', 'raw.githubusercontent.com')\
                     .replace('/blob/', '/')

        try:
            # Leer CSV ignorando líneas problemáticas
            df = pd.read_csv(url, on_bad_lines='skip')  # pandas >= 1.4

            # Mostrar solo las primeras 20 filas
            df_html = df.head(20).to_html(classes='table table-striped', index=False)
        except Exception as e:
            error = f"Error al cargar los datos: {e}"

    return render(request, 'home.html', {'df_html': df_html, 'error': error})
