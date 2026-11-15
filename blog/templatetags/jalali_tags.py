import jdatetime
from django import template
from django.utils import timezone

register = template.Library()

MONTHS = ("فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد",
          "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند")

Fa_Digits = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

@register.filter
def jalali(value):
    local = timezone.localtime(value)
    j = jdatetime.datetime.fromgregorian(date=local.date())
    text = f"{j.day} {MONTHS[j.month - 1]} {j.year}"
    return text.translate(Fa_Digits)
