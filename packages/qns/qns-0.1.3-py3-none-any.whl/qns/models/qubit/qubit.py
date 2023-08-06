#    SimQN: a discrete-event simulator for the quantum networks
#    Copyright (C) 2021-2022 Lutong Chen, Jian Li, Kaiping Xue
#    University of Science and Technology of China, USTC.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import List, Optional
import numpy as np
import random

from qns.models.qubit.const import QUBIT_STATE_0, QUBIT_STATE_1,\
        QUBIT_STATE_P, QUBIT_STATE_N,\
        OPERATOR_HADAMARD, QUBIT_STATE_L, QUBIT_STATE_R
from qns.models.core.backend import QuantumModel


class QStateSizeNotMatchError(Exception):
    """
    This error happens when the size of state vector or matrix mismatch occurs
    """
    pass


class QStateQubitNotInStateError(Exception):
    pass


class OperatorNotMatchError(Exception):
    """
    This error happens when the size of state vector or matrix mismatch occurs
    """
    pass


class QState(object):
    """
    QState is the state of one (or multiple) qubits
    """
    def __init__(self, qubits: List["Qubit"] = [],
                 state: Optional[List[complex]] = QUBIT_STATE_0, name: Optional[str] = None):
        self.num = len(qubits)
        self.name = name

        if len(state) != 2**self.num:
            raise QStateSizeNotMatchError
        self.qubits = qubits
        self.state: np.ndarray = np.array(state)

    def measure(self, qubit: "Qubit" = None) -> int:
        """
        Measure this qubit using Z basis
        Args:
            qubit (Qubit): the measuring qubit

        Returns:
            0: QUBIT_STATE_0 state
            1: QUBIT_STATE_1 state
        """
        try:
            idx = self.qubits.index(qubit)
            shift = self.num - idx - 1
            assert(shift >= 0)
        except AssertionError:
            raise QStateQubitNotInStateError

        set_0, set_1 = [], []
        poss_0, _ = 0, 0
        for idx in range(2**self.num):
            if (idx & (1 << shift)) > 0:
                set_1.append(idx)
            else:
                set_0.append(idx)

        ns = self.state.copy()
        for i in set_0:
            poss_0 += np.abs(ns[i][0])**2

        rn = random.random()

        nns = []
        if rn <= poss_0:
            ret = 0
            ret_s = QUBIT_STATE_0
            for i in set_0:
                nns.append(ns[i])
        else:
            ret = 1
            ret_s = QUBIT_STATE_1
            for i in set_1:
                nns.append(ns[i])

        ns1 = QState([qubit], ret_s)
        qubit.state = ns1
        self.num -= 1
        self.qubits.remove(qubit)
        self.state = np.array(nns)
        self._to_1()
        return ret

    def _to_1(self):
        poss = 0
        for i in range(2**self.num):
            poss += np.abs(self.state[i][0])**2
        amp = np.sqrt(1 / poss)
        for i in range(2**self.num):
            self.state[i][0] = amp * self.state[i][0]

    def operate(self, operator: np.ndarray = None):
        """
        transform using `operator`

        Args:
            operator (np.ndarray): the operator
        Raises:
            OperatorNotMatchError
        """
        operator_size = operator.shape
        if operator_size == (2**self.num, 2**self.num):
            # joint qubit operate
            full_operator = operator
        else:
            raise OperatorNotMatchError
        self.state = np.dot(full_operator, self.state)

    def equal(self, other_state: "QState") -> bool:
        """
        compare two state vectors, return True if they are the same

        Args:
            other_state (QState): the second QState
        """
        return np.all(self.state == other_state.state)

    # def __eq__(self, __o: "QState") -> bool:
    #     return np.all(self.state == __o.state)

    def __repr__(self) -> str:
        if self.name is not None:
            return f"<qubit {self.name}: {self.state}>"
        return str(self.state)


class Qubit(QuantumModel):
    """
    Represent a qubit
    """

    def __init__(self, state=QUBIT_STATE_0, name: Optional[str] = None):
        """
        Args:
            state (list): the initial state of a qubit, default is |0> = [1, 0]^T
            name (str): the qubit's name
        """

        self.name = name
        self.state = QState([self], state)

    def measure(self):
        """
        Measure this qubit using Z basis

        Returns:
            0: QUBIT_STATE_0 state
            1: QUBIT_STATE_1 state
        """
        return self.state.measure(self)

    def measureX(self):
        """
        Measure this qubit using X basis.
        Only for not entangled qubits.

        Returns:
            0: QUBIT_STATE_P state
            1: QUBIT_STATE_N state
        """
        state = self.state.state
        state = np.dot(OPERATOR_HADAMARD, state)
        poss = np.abs(state[0][0])**2
        rn = random.random()
        if rn <= poss:
            ret = 0
            ret_s = QUBIT_STATE_P
        else:
            ret = 1
            ret_s = QUBIT_STATE_N
        self.state.state = ret_s
        return ret

    def measureY(self):
        """
        Measure this qubit using Y basis.
        Only for not entangled qubits.

        Returns:
            0: QUBIT_STATE_R state
            1: QUBIT_STATE_L state
        """
        state = self.state.state
        SH = np.array([[1, 0], [0, -1j]])
        state = np.dot(SH, state)
        state = np.dot(OPERATOR_HADAMARD, state)

        poss = np.abs(state[0][0])**2
        rn = random.random()
        if rn <= poss:
            ret = 0
            ret_s = QUBIT_STATE_R
        else:
            ret = 1
            ret_s = QUBIT_STATE_L
        self.state.state = ret_s
        return ret

    def measureZ(self):
        """
        Measure this qubit using Z basis

        Returns:
            0: QUBIT_STATE_0 state
            1: QUBIT_STATE_1 state
        """
        return self.measure()

    def __repr__(self) -> str:
        if self.name is not None:
            return f"<Qubit {self.name}>"
        return super().__repr__()

    def storage_error_model(self, t: float, **kwargs):
        """
        The default error model for storing a qubit in quantum memory.
        The default behavior is doing nothing

        Args:
            t: the time stored in a quantum memory. The unit it second.
            kwargs: other parameters
        """
        pass

    def transfer_error_model(self, length: float, **kwargs):
        """
        The default error model for transmitting this qubit
        The default behavior is doing nothing

        Args:
            length (float): the length of the channel
            kwargs: other parameters
        """
        pass
