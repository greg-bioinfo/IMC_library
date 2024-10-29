from function import combine_marker

path=input("Saisir le chemin d'accès du dissier crée: ")
list_marker=input("Saisir les marqueurs à afficher (séparé par une virgule): ")

list_marker=list_marker.split(",")
combine_marker(list_marker,path)