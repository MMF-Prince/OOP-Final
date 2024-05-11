

class Bank:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.total_balance=0
        self.total_loan_balance=0
        self.loan_feature_activation=True
        self.admin_panel=[]
        self.user_archive=[]
        