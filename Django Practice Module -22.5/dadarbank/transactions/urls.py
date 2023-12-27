from django.urls import path
from .views import  money_transfer_view, DepositMoneyView, WithdrawMoneyView, TransactionReportView,LoanRequestView,LoanListView,PayLoanView


# app_name = 'transactions'
urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionReportView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("loan_request/", LoanRequestView.as_view(), name="loan_request"),
    # path("money_transfer/", MoneyTransferView.as_view(), name="money_transfer"),
    # path('money_transfer/', money_transfer, name='money_transfer'),
    path('money-transfer/', money_transfer_view, name='money_transfer'),
    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loans/<int:loan_id>/", PayLoanView.as_view(), name="pay"),
]

# 100003