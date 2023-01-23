from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Product, Receipt


def index(request):
    return HttpResponse('Главная страница')

class ReceiptListView(ListView):
    model = Receipt
    context_object_name = 'receipts'
    paginate_by = 3
    template_name = 'receipts/list.html'

# def receipts_list(request):
#     object_list = Receipt.objects.all()
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         receipts = paginator.page(page)
#     except PageNotAnInteger:
#         receipts = paginator.page(1)
#     except EmptyPage:
#         receipts = paginator.page(paginator.num_pages)
#     return render(
#         request,
#         'receipts/list.html',
#         {'page': page, 'receipts': receipts}
#     )

def receipt_detail(request, pk):
    receipt = Receipt.objects.get(id=pk)
    print(receipt.id)
    products = Product.objects.filter(receipt=receipt.id)
    print(products)

    return render(request,
            'receipts/detail.html',
            {'receipt': receipt, 'products': products}
        )


def groups_list(request):
    pass

def group(request, slug):
    return HttpResponse(f'Страница группы {slug}')
