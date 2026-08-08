from django.shortcuts import render, redirect
from .forms import ApplianceForm
from .models import Appliance


def add_appliance(request):

    if request.method == 'POST':
        form = ApplianceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appliance_list')

    else:
        form = ApplianceForm()

    return render(request, 'appliances/add_appliance.html', {
        'form': form
    })


def appliance_list(request):

    appliances = Appliance.objects.all()

    total_daily = sum(
        appliance.daily_consumption()
        for appliance in appliances
    )

    total_monthly = sum(
        appliance.monthly_consumption()
        for appliance in appliances
    )

    # Find the appliance using the most electricity
    highest_appliance = None

    if appliances:
        highest_appliance = max(
            appliances,
            key=lambda appliance: appliance.monthly_consumption()
        )

    # Calculate percentage for each appliance
    appliance_data = []

    for appliance in appliances:

        monthly_usage = appliance.monthly_consumption()

        if total_monthly > 0:
            percentage = (monthly_usage / total_monthly) * 100
        else:
            percentage = 0

        appliance_data.append({
            'appliance': appliance,
            'percentage': percentage,
        })

    return render(
        request,
        'appliances/appliance_list.html',
        {
            'appliances': appliances,
            'total_daily': total_daily,
            'total_monthly': total_monthly,
            'highest_appliance': highest_appliance,
            'appliance_data': appliance_data,
        }
    )

def bill_calculator(request):

    appliances = Appliance.objects.all()

    monthly_usage = sum(
        appliance.monthly_consumption()
        for appliance in appliances
    )

    bill = None
    rate = None

    if request.method == 'POST':

        rate = float(request.POST.get('rate'))

        bill = monthly_usage * rate

    return render(
        request,
        'appliances/bill_calculator.html',
        {
            'monthly_usage': monthly_usage,
            'rate': rate,
            'bill': bill,
        }
    )