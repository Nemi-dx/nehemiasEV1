from django.shortcuts import render


def index(request):
	perfil = {
            'nombre': 'Nehemias Venegas',
            'especialidad': 'Analista Programador',
            'edad': 20,
            'ciudad': 'Longavi',
            'foto': 'img/x.jpg',
        }
    
	return render(request, 'categoriaApp/index.html', {'perfil': perfil})


def videojuegos(request):
	lista = [
		{
			'id': 1,
			'titulo': 'Hollow Knight',
			'estudio': 'Team Cherry',
			'genero': 'Metroidvania',
			'plataforma': 'PC / Switch',
			'imagen': 'img/Hollow_Knight.jpg',
			'link': 'https://store.steampowered.com/app/367520/Hollow_Knight/',
		},
		{
			'id': 2,
			'titulo': 'Celeste',
			'estudio': 'Maddy Makes Games',
			'genero': 'Plataformas',
			'plataforma': 'PC / Consolas',
			'imagen': 'img/celeste.jpg',
			'link': 'https://store.steampowered.com/app/504230/Celeste/',
			
		},
		{
			'id': 3,
			'titulo': 'Hades',
			'estudio': 'Supergiant Games',
			'genero': 'Roguelike',
			'plataforma': 'PC / Consolas',
			'imagen': 'img/hades.jpg',
			'link': 'https://store.steampowered.com/app/1145360/Hades/',
		},
	]
	return render(request, 'categoriaApp/videojuegos.html', {'lista': lista})

