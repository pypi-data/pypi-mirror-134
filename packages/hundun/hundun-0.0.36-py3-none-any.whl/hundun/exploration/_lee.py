from itertools import product as _product

import numpy as _np

from ._utils import (embedding_seq_1dim as _embedding_seq_1dim,
                     reshape as _reshape)


def _estimate_jacobian(e_seq, time_step, size, D, sample_size, eps=10**(-6)):
    jacobian_matrix_list = []

    for e_n in e_seq:
        # 基準点e_nとの距離計算
        distance_and_idx = [(_np.linalg.norm(e - e_n), idx)
                            for idx, e in enumerate(e_seq[:-time_step])]
        distance_and_idx.sort()

        index = _np.array(
            [data[1] for data in distance_and_idx[1:]][:sample_size])

        x = e_seq[index]


        V_j = [_np.array([a*b for a, b in _product(xk, xl)]).reshape(D, D)
               for xk, xl in zip(x,x)]
        V = sum(V_j)/sample_size

        #正則かどうか
        if _np.linalg.det(V) < eps:
            continue

        y = e_seq[index+time_step]

        C_j = [_np.array([a*b for a, b in _product(yk, xl)]).reshape(D, D)
               for yk, xl in zip(y, x)]
        C = sum(C_j)/sample_size

        jacobian = C@_np.linalg.inv(V)
        jacobian_matrix_list.append(jacobian)

        if len(jacobian_matrix_list)>=size:
            break

    return jacobian_matrix_list


def calc_les_ts_w_sano(e_seq, dt, D, T=1, m=1, M=1000, q=100):

    A_list = _estimate_jacobian(e_seq, time_step=m, size=M, D=D, sample_size=q)

    Q, R = _np.linalg.qr(A_list[0])
    R_list= [_np.diag(R)]

    for A in A_list[1:]:
        Q, R = _np.linalg.qr(A@Q)
        R_list.append(_np.diag(R))

    R_sum = _np.log(_np.abs(R_list[0]))
    R_sum = _np.zeros(D)
    les_list = _np.array(
        [(R_sum := R_sum + _np.log(_np.abs(R)))/(i*dt*m*T)
         for i, R in enumerate(R_list, 1)])

    return les_list, _np.average(les_list[-50:, :], axis=0)


if __name__ == '__main__':
    from ..utils._draw import Drawing

    u_seq = _np.load('sample/data/henon_xy.npy')[:, 0]
    u_seq = _reshape(u_seq)

    e_seq = _embedding_seq_1dim(u_seq, 1, 2)
    les_list, les_average = calc_les_ts_w_sano(e_seq, 1, 2, M=1000, m=1, q=50)
    print(les_average)

    d = Drawing()
    for i in range(2):
        d[0,0].plot(les_list[:, i], label=f'${les_average[i]:+.3f}$')
    d[0,0].legend()
    d.show()