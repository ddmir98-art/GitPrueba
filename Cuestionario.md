CUESTIONARIO:

	Evaluación: Opción Múltiple.

¿Qué comando mueve cambios al staging area?​
	Respuesta correcta: git add.

¿Qué tipo de VCS es Git?​
	Respuesta correcta: Distribuido.

¿Quién creó Git y en qué año?​
	Respuesta correcta: Linus Torvalds, 2005.

¿Qué hace git fetch?​
	Respuesta correcta: Descarga sin fusionar​.

Quieres deshacer un commit que ya subiste. ¿Qué usas?​
	Respuesta correcta: git revert​.

¿Qué es origin?​
	Respuesta correcta: El nombre por defecto del remot.

¿Qué es un fork?​
	Respuesta correcta: Una copia del repo en tu cuenta de GitHub​.

Los marcadores <<<<<<<, =======, >>>>>>> indican…​
	Respuesta correcta: Un conflicto de fusión​.

-----------------------------------------------------------------------------------------------------------------------------------------------
	Evaluación: Preguntas Abiertas​
Explica con una analogía propia las tres áreas de Git.​
Eres un estudiante y te estas preparando para la escuela.
Directorio de trabajo: Es el escritorio donde están todos tus cuadernos o materiales para la escuela.
Staging Area: Es donde tienes lo que vas a llevar.
Repositorio: Tu mochila ya cerrada, guardada con todo lo que metiste.

¿Cuándo usarías git stash?​
Cuando me doy cuenta de que aun no termino de editar los archivos, así que para evitar usar un commit con datos incompletos.

Encontraste un bug en una librería open source que usa tu sistema. Describe el flujo completo para enviar la corrección.​
Clono, creo ramas, corrijo y pruebo yo mismo, guardo todo, y lo subo en pull.

Un compañero subió el .env con la contraseña de producción. ¿Por qué es grave y qué pasos sigues?
Es grave porque no queremos que esos datos se muestren en publico, y lo que seguiría después de esto seria incluirlo al git ignore.

Un deploy de ayer rompió producción y el commit ya está en main. ¿Usas reset o revert? ¿Por qué?​
Usaría un revert para poder deshacer, y no resetear todo, siendo que es mas accesible por la creación del commit cuando se ejecuta.

-----------------------------------------------------------------------------------------------------------------------------------------------
	Ejercicio De Diagnóstico​

Ordena correctamente esta secuencia para publicar un cambio nuevo:​

git pull​->
git switch -c feat/x​->
editar archivos​->
git add . ->
git commit -m "..."​->
git push
