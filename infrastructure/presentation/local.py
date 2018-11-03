import constants

class ConsolePresenter:
    def present(self, fact):
        if fact.description == constants.DEPOSIT_NOT_ALLOWED:
            self._notify_no_more_deposits_allowed(fact.change)
        elif fact.description == constants.ACCOUNT_LIMIT_REACHED:
            self._notify_account_limit_reached(fact.change)
        elif fact.description == constants.BALANCE_INCREASED:
            pass
        elif fact.description == constants.NOT_ENOUGH_MONEY:
                self._notify_overdraw_not_allowed()
        elif fact.description == constants.BALANCE_DECREASED:
            pass
        else:
            raise Exception("Unknown deposit state!")

    def display_options(self, account):
        print("")
        print("Your current balance for #{} is ${}".format(account.account_nr, account.balance))
        print("1) Deposit money into account")
        print("2) Withdraw money from account")
    
    def _notify_no_more_deposits_allowed(self, change):
        print("Account limit of $1000 has been reached! Cannot deposit any more money!")
        print("Returned the ${}".format(change))

    def _notify_account_limit_reached(self, change):
        print("You have deposited enough to reach account limit of $1000!")
        print("Change of ${} returned".format(change))
        print("Cannot exceed account limit of $1000!")

    def _notify_overdraw_not_allowed(self):
        print("Cannot withdraw more than your current balance!")