from django.db import models

from recipient.models import Recipient

NULLABLE = {'null': True, 'blank': True}
FREQUENCY_CHOICES = [('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц'), ]
STATUS_OF_NEWSLETTER = [("Create", 'Создана'), ("Started", 'Отправлено'), ("Done", 'Завершена'), ]


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title


class MailingSettings(models.Model):
    first_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Начало рассылки')
    end_time = models.DateTimeField(verbose_name='Конец рассылки', **NULLABLE)
    sending = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, verbose_name='Период рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщения')
    setting_status = models.CharField(max_length=50, choices=STATUS_OF_NEWSLETTER, verbose_name='Статус рассылки',
                                      default='Create')
    recipients = models.ManyToManyField(Recipient, verbose_name='Получатели')

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылки'

    def __str__(self):
        return f'{self.message} отправляется каждый {self.sending} с {self.first_datetime}'


class MailingStatus(models.Model):
    last_datetime = models.DateTimeField(auto_now_add=True, verbose_name='last_datetime')
    status = models.CharField(max_length=50, verbose_name='статус попытки')
    mailing_response = models.TextField(verbose_name='mailing_response')
    mailing_list = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка')
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, verbose_name='клиент рассылки', **NULLABLE)

    class Meta:
        verbose_name = 'Статус отправки'
        verbose_name_plural = 'Статусы отправки'

    def __str__(self):
        return f'{self.status} отправлялось {self.last_datetime}, ответ сервера: {self.mailing_response}'
