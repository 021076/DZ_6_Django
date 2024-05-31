import secrets
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisertForm, UserEditForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisertForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/verification/{token}/'
        send_mail('Подтверждение почты',
                  f'Перейдите по ссылке для подтверждения почты {url}',
                  EMAIL_HOST_USER,
                  [user.email]
                  )
        print(url)
        return super().form_valid(form)


def verification(request, token):
    user = get_object_or_404(User, token=token)
    user.verified = True
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class EditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:edit')

    def get_object(self, queryset=None):
        return self.request.user
