import time
import pyflann

class EvaluarArbol:   
    def __init__(self, dataset):
        self.dataset = dataset
        self.flann = pyflann.FLANN()
        
    def linear_scan(self):
        print("linear scan {} de Q={} x R={}".format(
            self.dataset.nombre, self.dataset.q.shape, self.dataset.r.shape))
        self.flann.build_index(self.dataset.r, algorithm="linear")
        t0 = time.time()
        self.gt_nns, self.gt_dists = self.flann.nn_index(self.dataset.q, num_neighbors=1, cores=4)
        self.gt_segundos = time.time() - t0
        print("linear scan = {:.1f} segundos".format(self.gt_segundos))
    
    def evaluar_busqueda(self, nns, dists, tiempo):
        correctas = 0
        incorrectas = 0
        for i in range(len(self.gt_nns)):
            if nns[i] == self.gt_nns[i] or dists[i] == self.gt_dists[i]: 
                correctas += 1
            else:
                incorrectas += 1 
        precision = 100 * correctas / (correctas + incorrectas)
        eficiencia = 100 * tiempo / self.gt_segundos
        return precision, eficiencia

    def evaluar_arbol(self, algorithm, trees=0, branching=0):
        t0 = time.time()
        self.flann.build_index(self.dataset.r, algorithm=algorithm, trees=trees, branching=branching)
        name = "{}-{}".format(algorithm, max(trees, branching))
        print("{} construcción {} = {:.2f} segundos".format(self.dataset.nombre, name, time.time() - t0))
        curva = Curva()
        for checks in (1, 10, 40, 70, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 5000):
            t0 = time.time()
            nn, dist = self.flann.nn_index(self.dataset.q, num_neighbors=1, cores=4, checks=checks)
            precision, eficiencia = self.evaluar_busqueda(nn, dist, time.time() - t0)
            print("  {}\tprecision={:.1f}%\ttiempo={:.1f}% checks={}".format(name, precision, eficiencia, checks))
            curva.precisiones.append(precision)
            curva.eficiencias.append(eficiencia)
        return curva