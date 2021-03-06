import numpy as np

from theline.utils import get_quadratic as gq
from drrobert.network import get_random_parameter_graph as get_rpg

# TODO: complete this
class L2RegularizedAppDetRandomParameterGraph:

    def __init__(self, N, p, fc=True, dist=True, sym=True):
        # TODO: actually use the symmetric graph option

        self.N = N
        self.p = p

        (self.ws, self.Bw, self.Dw, self.G) = get_rpg(
            self.N, 
            self.p, 
            fc=fc,
            dist=dist)
        self.d = np.sum(self.G, axis=1)
        self.L = np.diag(self.d) - self.G

        (self.e_vals, self.e_vecs) = np.linalg.eig(self.L)

class L2RegularizedParameterGraph:

    def __init__(self, G, ws, Bw=None, Dw=None):

        self.G = G
        self.ws = ws

        self.N = self.G.shape[0]

        if Bw is None:
            Bw = max(
                [np.linalg.norm(self.ws[:,i]) 
                 for i in range(self.ws.shape[1])])

        self.Bw = Bw

        if Dw is None:
            Dw = 0

            for n in range(self.N):
                Xn = self.ws[:,n]
                for m in range(n+1, self.N):
                    Xm = self.ws[:,m]
                    dist = np.linalg.norm(Xn - Xm)

                    if dist > Dw:
                        Dw = dist

        self.Dw = Dw
        self.p = self.ws.shape[0]
        self.d = np.sum(self.G, axis=1)
        self.L = np.diag(self.d) - self.G
        (self.e_vals, self.e_vecs) = np.linalg.eig(self.L)

    def get_logdet(self, loc, scale):

        eff_log_e_vals = np.log(scale * self.e_vals + loc)
        eff_logdet = np.sum(eff_log_e_vals) * self.p

        return eff_logdet

    def get_L_and_inv(self, loc, scale):

        aug_L_e_vals = scale * self.e_vals + loc
        lambda_matrix = np.diag(aug_L_e_vals)
        lambda_matrix_inv = np.diag(
            np.power(aug_L_e_vals, -1))

        aug_L = gq(self.e_vecs, lambda_matrix)
        aug_L_inv = gq(self.e_vecs, lambda_matrix_inv)

        return (aug_L, aug_L_inv)

class L2RegularizedRandomParameterGraph:

    def __init__(self, N, p, threshold=None, dist=True, sym=True):
        # TODO: actually use the symmetric graph option

        self.N = N
        self.p = p

        (self.ws, self.Bw, self.Dw, self.G) = get_rpg(
            self.N, 
            self.p, 
            threshold,
            dist=dist)
        self.d = np.sum(self.G, axis=1)
        self.L = np.diag(self.d) - self.G
        (self.e_vals, self.e_vecs) = np.linalg.eig(self.L)

    def get_logdet(self, loc, scale):

        eff_log_e_vals = np.log(scale * self.e_vals + loc)
        eff_logdet = np.sum(eff_log_e_vals) * self.p

        return eff_logdet

    def get_L_and_inv(self, loc, scale):

        aug_L_e_vals = scale * self.e_vals + loc
        lambda_matrix = np.diag(aug_L_e_vals)
        lambda_matrix_inv = np.diag(
            np.power(aug_L_e_vals, -1))

        aug_L = gq(self.e_vecs, lambda_matrix)
        aug_L_inv = gq(self.e_vecs, lambda_matrix_inv)

        return (aug_L, aug_L_inv)
