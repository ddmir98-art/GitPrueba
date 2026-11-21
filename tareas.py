tareas = []

def agregar_tarea(titulo):
	if not titulo.strip():
		raise ValueError("Titulo vacio")
	tareas.append(titulo.strip())

def eliminar_tarea(indice):
	return tareas.pop(indice)

def listar_tareas():
	return tareas

def tareas_prioritarias(prefijo="!"):
	return [t for t in tareas if t.startswith(prefijo)]