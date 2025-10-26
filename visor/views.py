from django.shortcuts import render
import pandas as pd

def home(request):
    df_html = None
    error = None

    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            df = pd.read_csv(url)
            df_html = df.head(20).to_html(classes='table table-striped', index=False)
        except Exception as e:
            error = f"Error al cargar los datos: {e}"

    return render(request, 'home.html', {'df_html': df_html, 'error': error})
