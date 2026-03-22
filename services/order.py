from django.db import transaction, models
from datetime import date

from db.models import User, Order, Ticket, MovieSession


@transaction.atomic
def create_order(
        tickets: list[dict],
        username: str,
        date: date = None
) -> None:
    user = User.objects.get(username=username)
    order = Order.objects.create(user=user)
    if date:
        order.created_at = date
        order.save()
    for ticket in tickets:
        ticket["movie_session"] = MovieSession.objects.get(
            pk=ticket["movie_session"]
        )
        Ticket.objects.create(order=order, **ticket)


def get_orders(username: str = None) -> models.QuerySet[Order]:
    if username:
        return Order.objects.filter(user__username=username)
    return Order.objects.all()
