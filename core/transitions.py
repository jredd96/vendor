from core.states import IdleState, VendState
class StateTransition:

    def __init__(self):
        self.idle_state = IdleState()
        self.vend_state = VendState()

    def to_processing_purchase(self, vending_machine, item, quantity):
        if self.vend_state.purchase_processing(vending_machine, item, quantity):
            return self.vend_state
        else:
            return self.idle_state

    def to_idle(self):
        return self.idle_state
