from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# Create your views here.
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

#This function will render the create new account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) #Retrieve the account form
    #Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #Checks to see if the submitted form is valid and if so, saves said form
            form.save()
            return redirect('index') #returns user back to the home page
    content = {'form': form} #Saves content to the template as a dictionary
    #Adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #Retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk) #retrieve all of that account's transactions
    current_total = account.initial_deposit #Create account total variable, starting with inital deposit value
    table_contents = {}
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
