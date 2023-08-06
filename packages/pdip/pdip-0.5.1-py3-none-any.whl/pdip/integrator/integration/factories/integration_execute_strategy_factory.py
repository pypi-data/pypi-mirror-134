from injector import inject

from ..strategies.base import IntegrationExecuteStrategy
from ..strategies.implementation import LimitOffIntegrationExecute
from ..strategies.implementation import ParallelIntegrationExecute
from ..strategies.implementation import SingleProcessIntegrationExecute
from ....dependency import IScoped
from ....exceptions import IncompatibleAdapterException


class IntegrationExecuteStrategyFactory(IScoped):
    @inject
    def __init__(self,
                 limit_off_integration_execute: LimitOffIntegrationExecute,
                 parallel_integration_execute: ParallelIntegrationExecute,
                 single_process_integration_execute: SingleProcessIntegrationExecute,
                 ):
        self.single_process_integration_execute = single_process_integration_execute
        self.parallel_integration_execute = parallel_integration_execute
        self.limit_off_integration_execute = limit_off_integration_execute

    def get(self, limit: int, process_count: int) -> IntegrationExecuteStrategy:
        # only target query run
        if limit is None or limit == 0:
            if isinstance(self.limit_off_integration_execute, IntegrationExecuteStrategy):
                return self.limit_off_integration_execute
            else:
                raise IncompatibleAdapterException(
                    f"{self.limit_off_integration_execute} is incompatible with {IntegrationExecuteStrategy}")
        elif process_count is not None and process_count > 1:
            if isinstance(self.parallel_integration_execute, ParallelIntegrationExecute):
                return self.parallel_integration_execute
            else:
                raise IncompatibleAdapterException(
                    f"{self.execute_integration_adapter} is incompatible with {ParallelIntegrationExecute}")
        else:
            if isinstance(self.single_process_integration_execute, SingleProcessIntegrationExecute):
                return self.single_process_integration_execute
            else:
                raise IncompatibleAdapterException(
                    f"{self.single_process_integration_execute} is incompatible with {SingleProcessIntegrationExecute}")
