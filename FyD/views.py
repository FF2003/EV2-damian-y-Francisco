from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'templatesProductos/home.html')


def guitarra(request):
    data={
        "titulo":"guitarra",
        'Informacion':"la guitarra es un instrumento musical de la familia de los cordófonos, es decir los instrumentos que producen su sonido al hacer vibrar las cuerdas.",
        'clasificación ':"cuerda",
        'origen ': "se cree que la guitarra se originó en España en el siglo XVI y durante los siglos de la conquista árabe en España y la península Ibérica",
        'imagen':'imagenes/guitarra.jpg'
       }
    return render(request,'templatesProductos/home.html',data)

def saxofon(request):
    data={
        "titulo":"saxofón",
        'Información':"Instrumento musical de viento, de metal, con boquilla de madera, caña y varias llaves, que es de invención moderna y muy usado, principalmente en las bandas militares y orquestas de jazz.",
        'clasificación ':"bronce, viento",
        'origen ': "Hace 180 años que Adolphe Sax, en 1841, un fabricante de instrumentos belga, tocó en público en Bruselas por primera vez su nuevo invento al que llamó saxofón",
        'imagen':'imagenes/saxo.jpg'
       }
    return render(request,'templatesProductos/home.html',data)

def bateria(request):
    data={
        "titulo":"Batería",
        'Informacion':"La batería es un conjunto de instrumentos musicales de percusión usado por muchas agrupaciones musicales. En algunos países, el término «batería» también se refiere al músico que toca estos instrumentos, al igual que el término «baterista», ambos equivalentes",
        'clasificación ':"Percusión ",
        'origen ': "El origen de la batería se localiza en los Estados Unidos a finales del siglo XIX y radica en la unión, en 1890",
        'imagen':'imagenes/bateria.jpg'
       }
    return render(request,'templatesProductos/home.html',data)
