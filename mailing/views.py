from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailing.models import Message, MailingSettings


class MailingMessageCreateView(CreateView):
    model = Message
    fields = ['title', 'content']
    success_url = reverse_lazy('mailing:list')


class MailingMessageUpdateView(UpdateView):
    model = Message
    fields = ['title', 'content']
    success_url = reverse_lazy('mailing:list')


class MailingMessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:list')


class MailingMessageListView(ListView):
    model = Message


class MailingMessageDetailView(DetailView):
    model = Message


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:settings_list')