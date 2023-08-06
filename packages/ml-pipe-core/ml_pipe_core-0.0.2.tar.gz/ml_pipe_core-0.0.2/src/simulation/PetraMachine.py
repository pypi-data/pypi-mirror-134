from src.ml_pipe_core.adapter.PetraMachineAdapter import PetraMachineAdapter
from ml_pipe_core.simulation.MachineService import MachineService
from src.ml_pipe_core.logger import init_logger

_logger = init_logger(__name__)


class PetraMachine(MachineService):
    def __init__(self, name):
        super().__init__(name, PetraMachineAdapter())

    def process(self, message):
        data = message.data
        # set
        # TODO: Send error message to user!
        if "hcor" in data:
            if not self._are_keys_in_dict(['names', 'values'], data["hcor"]):
                _logger.error(f"Machine Service received invalid message. Message: {data}")
                return
            self.machine_adapter.set_hcors(names=data["hcor"]["names"], strengths=data["hcor"]["values"])

        if "vcor" in data:
            if not self._are_keys_in_dict(['names', 'values'], data["vcor"]):
                _logger.error(f"Machine Service received invalid message. Message: {data}")
                return
            self.machine_adapter.set_vcors(names=data["vcor"]["names"], strengths=data["vcor"]["values"])

        if "machineparams" in data:
            if not self._are_keys_in_dict(['names', 'values'], data["machineparams"]):
                _logger.error(f"Machine Service received invalid message. Message: {data}")
                return
            self.machine_adapter.set_machine_params(names=data["machineparams"]["names"], values=data["machineparams"]["values"])


if __name__ == "__main__":
    sim = MachineService('petra_III_machine')
    sim.init_local()
