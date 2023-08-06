from circle.resources.abstract import CreateableAPIResource, ListableAPIResource


class BusinessAccountDepositAddress(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "businessAccount.wallets.addresses.deposit"
