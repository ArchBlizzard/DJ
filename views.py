from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order, Tag

@login_required
def order_list(request):
    orders = Order.objects.all()
    favorites = Favorite.objects.filter(user=request.user).values_list('order__id', flat=True)
    return render(request, 'orders/order_list.html', {'orders': orders, 'favorites': favorites})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['customer_name', 'order_date', 'total_price', 'tags']

class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['customer_name', 'order_date', 'total_price', 'tags']

class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')

@login_required
def favorite_toggle(request, pk):
    order = get_object_or_404(Order, pk=pk)
    favorite, created = Favorite.objects.get_or_create(order=order, user=request.user)
    if not created:
        favorite.delete()
    return redirect('order_list')
