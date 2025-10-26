from django.shortcuts import render
import pandas as pd

# Definir columnas en caso de que el CSV no las tenga
COLUMNAS = [
    'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment',
    'urgent','hot','num_failed_logins','logged_in','num_compromised','root_shell','su_attempted',
    'num_root','num_file_creations','num_shells','num_access_files','num_outbound_cmds',
    'is_host_login','is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
    'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate',
    'dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate',
    'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','label','id'
]

def home(request):
    df_html = None
    error = None

    if request.method == 'POST':
        url = request.POST.get('url')

        # Convertir GitHub normal a RAW
        if 'github.com' in url:
            url = url.replace('github.com', 'raw.githubusercontent.com')\
                     .replace('/blob/', '/')

        try:
            # Leer CSV, ignorando líneas malas y agregando encabezados si faltan
            df = pd.read_csv(url, on_bad_lines='skip', names=COLUMNAS)

            # Limitar filas mostradas
            df_html = df.head(20).to_html(classes='table table-striped', index=False)
        except Exception as e:
            error = f"Error al cargar los datos: {e}"

    return render(request, 'home.html', {'df_html': df_html, 'error': error})
