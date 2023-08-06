from src.ml_pipe_core.adapter.PetraSimulationAdapter import PetraSimulationAdapter
from optics_sim import OpticsSimulation
from ml_pipe_core.simulation.MachineService import MachineService

from src.ml_pipe_core.adapter.PetraAdapter import PetraAdapter
from src.ml_pipe_core.logger import init_logger

_logger = init_logger(__name__)


class PetraOrbitSimulation(MachineService):
    def __init__(self, name, optic: str):
        super().__init__(name, PetraSimulationAdapter())
        self.optic_sim = OpticsSimulation(self.machine_adapter, optic)

    def process(self, message):
        data = message.data
        # set
        # TODO: Send error message to user!
        machine_state_changed = False
        if "hcor" in data:
            if not self._are_keys_in_dict(['names', 'values'], data["hcor"]):
                _logger.error(f"Machine Service received invalid message. Message: {data}")
                return
            self.machine_adapter.set_hcors(names=data["hcor"]["names"], strengths=data["hcor"]["values"])
            machine_state_changed = True

        if "vcor" in data:
            if not self._are_keys_in_dict(['names', 'values'], data["vcor"]):
                _logger.error(f"Machine Service received invalid message. Message: {data}")
                return
            self.machine_adapter.set_vcors(names=data["vcor"]["names"], strengths=data["vcor"]["values"])
            machine_state_changed = True

        if "machineparams" in data:
            if not self._are_keys_in_dict(['names', 'values'], data["machineparams"]):
                _logger.error(f"Machine Service received invalid message. Message: {data}")
                return
            self.machine_adapter.set_machine_params(names=data["machineparams"]["names"], values=data["machineparams"]["values"])
            machine_state_changed = True

        if "twiss" in data:
            if not self._are_keys_in_dict(['names', 'mat'], data["twiss"]):
                _logger.error(f"Machine Service received invalid message. Message: {data}")
                return
            self.machine_adapter.set_twiss(names=data["twiss"]["names"], mat=data["twiss"]["mat"])
            machine_state_changed = True

        # simulate
        if machine_state_changed:
            self.optic_sim.simulate()
        return list(data.keys())


if __name__ == "__main__":
    sim = PetraOrbitSimulation('petra_III_sim', 'v24')
    sim.init_local()
