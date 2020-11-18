from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import resolve_url

from django.http import HttpResponse
from django.http import HttpRequest
from django.http import Http404
from django.http import HttpResponseBadRequest

from django.urls import reverse_lazy
from django.urls import reverse

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.conf import settings

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail

from .forms import UserUpdateForm
from .forms import ItemForm
from .models import Order, OrderDetail, Item, Company


def index(request):
    return render(request, "orders/index.html")


class DashboardView(LoginRequiredMixin, TemplateView):
    """ダッシュボード"""
    template_name = 'orders/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dashboard"
        return context


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetailView(OnlyYouMixin, SuccessMessageMixin, DetailView):
    model = get_user_model()
    template_name = 'orders/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザ情報"
        return context


class UserUpdateView(OnlyYouMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'orders/user_update.html'
    success_message = "ユーザー情報を更新しました"
    
    def get_success_url(self):
        return resolve_url('orders:user_detail', pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザ更新"
        return context


class CompanyListView(ListView):
    model = Company
    template_name = "orders/company/list.html"
    

class CompanyCreateView(SuccessMessageMixin, CreateView):
    model = Company
    fields = ["name"]
    template_name = "orders/company/create.html"
    success_url = reverse_lazy("orders:company_list")
    success_message = "新規作成しました"


class CompanyEditView(SuccessMessageMixin, UpdateView):
    model = Company
    fields = ["name"]
    template_name = "orders/company/edit.html"
    success_url = reverse_lazy("orders:company_list")
    success_message = "更新しました"


class CompanyDetailView(DetailView):
    model = Company
    template_name = "orders/company/detail.html"


class ItemListView(ListView):
    model = Item
    template_name = "orders/item/list.html"
    

class ItemCreateView(SuccessMessageMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = "orders/item/create.html"
    success_url = reverse_lazy("orders:item_list")
    success_message = "新規作成しました"


class ItemEditView(SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "orders/item/edit.html"
    success_url = reverse_lazy("orders:item_list")
    success_message = "更新しました"


class OrderListView(ListView):
    model = Order
    template_name = "orders/order/list.html"
    

class OrderCreateView(SuccessMessageMixin, CreateView):
    model = Order
    fields = ["title","company"]
    template_name = "orders/order/create.html"
    success_url = reverse_lazy("orders:order_list")
    success_message = "新規作成しました"


class OrderEditView(SuccessMessageMixin, UpdateView):
    model = Order
    fields = ["title","company"]
    template_name = "orders/order/edit.html"
    success_url = reverse_lazy("orders:order_list")
    success_message = "更新しました"


class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/order/detail.html"


class OrderDetailCreateView(SuccessMessageMixin, CreateView):
    model = OrderDetail
    fields = ["item","unit"]
    template_name = "orders/orderdetail/create.html"
    success_message = "新規作成しました"
    
    """
    def get_initial(self):
        initial = super().get_initial()
        order_id = self.kwargs["order_id"]
        order = Order.objects.get(pk=order_id)
        initial["order"] = order
        return initial
    """
    
    def get_success_url(self):
        return reverse_lazy('orders:order_detail', kwargs={'pk': self.object.order.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(kwargs)
        order_id = self.kwargs["order_id"]
        order = Order.objects.get(pk=order_id)
        context["order"] = order
        return context

    def form_valid(self, form):
        order_id = self.kwargs["order_id"]
        order = Order.objects.get(pk=order_id)
        
        self.object = form.save(commit=False)
        self.object.order = order
        self.object.save()
        return super().form_valid(form)


class OrderDetailEditView(SuccessMessageMixin, UpdateView):
    model = OrderDetail
    fields = ["item","unit"]
    template_name = "orders/orderdetail/edit.html"
    success_message = "更新しました"

    def get_success_url(self):
        return reverse_lazy('orders:order_detail', kwargs={'pk': self.object.order.id})


class OrderDetailDeleteView(DeleteView):
    model = OrderDetail
    
    def get(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        self.object = OrderDetail.objects.get(id=pk)
        self.object.delete()
        messages.success(self.request, "削除しました")
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk' : self.object.order.id})
