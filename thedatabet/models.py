from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class BettingTips(models.Model):
    date = models.DateField()
    games = models.JSONField()
    host_sc_mse = models.FloatField()
    host_sc_r2 = models.FloatField()
    guest_sc_mse = models.FloatField()
    guest_sc_r2 = models.FloatField()
    result_mse = models.FloatField()
    result_r2 = models.FloatField()

    panels = [
        FieldPanel("date"),
        FieldPanel("games")

    ]

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")


@register_snippet
class BetwayOdds(models.Model):
    date = models.DateField()
    odds = models.JSONField()

    panels = [
        FieldPanel("date"),
        FieldPanel("odds"),
    ]

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

@register_snippet
class BettingStats(models.Model):
    date = models.DateField()
    average = models.JSONField()
    describe = models.JSONField()
    variance = models.JSONField()
    standard_deviation = models.JSONField()
    home_win_len = models.IntegerField()
    home_win_percentage = models.FloatField()
    away_win_len = models.IntegerField()
    away_win_percentage = models.FloatField()
    over_25_len = models.IntegerField()
    over_25_percentage = models.FloatField()
    under_25_len = models.IntegerField()
    under_25_percentage = models.FloatField()
    btts_len = models.IntegerField()
    btts_percentage = models.FloatField()
    home_over_15_len = models.IntegerField()
    home_over_15_percentage = models.FloatField()
    away_over_15_len = models.IntegerField()
    away_over_15_percentage = models.FloatField()
    home_draw_len = models.IntegerField()
    home_draw_percentage = models.FloatField()
    away_draw_len = models.IntegerField()
    away_draw_percentage = models.FloatField()

    panels = [
        FieldPanel("date")
    ]
    def __str__(self):
        return self.date.strftime("%Y-%m-%d")


class TheDataBet(Page):
    betting_tips = models.ForeignKey(
        'thedatabet.BettingTips',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('betting_tips'),  # This creates the dropdown
    ]