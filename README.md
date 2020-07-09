# atos_solver_exercice

Le fichier solver.py contient la classe Solver <br/>
La méthode E est la réécriture de la fonction f(x) = x^T . Q . x <br/>
Les 2 méthodes principales sont annealing_max(self, Q, x0, nb_iter, t_init, cool) et annealing_min(self, Q, x0, nb_iter, t_init, cool) qui respectivement recherche le maximum et le minimum de la fonction E à l'aide de l'algorithme du recuit simulé. <br/> <br/>

Le fichier solver_brut.py contient la classe SolverBrut  <br/>
La méthode brut_force permet de tester l'ensemble des x possibles afin de trouver le x minimisant f(x) et le x maximisant f(x) <br/>
Elle renvoie (la valeur de xmin tel que f(xmin) soit le minimum de f, la valeur de f(xmin), la valeur de xmax tel que f(xmax) soit le maximum de f, la valeur de f(xmax))

Le fichier test permet de comparer les résultats du Solver utilisant l'algorithme du recuit simulé et du Solver brut force. <br/>
Le test 1 génère une matrice symétrique puis affiche les résultats des deux solvers <br/>
Le test 2 affiche les résultats des deux solvers pour une matrice définie <br/>
Le test 3 fait n_iter tests des 2 solvers et compte le nombre de bons maximums trouvés et le nombre de bons minimums trouvés. <br/>
Le test dit "générique", permet de tester le Solver simplement en changeant les variables <br/>


Le dossier not_used peut être ignoré (différente recherche de voisins dans l'algorithme du recuit simulé)
