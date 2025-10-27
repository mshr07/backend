from django.core.management.base import BaseCommand
from expenses.models import ExpenseCategory


class Command(BaseCommand):
    help = 'Create default expense categories'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Food & Dining', 'description': 'Restaurants, groceries, coffee shops'},
            {'name': 'Transportation', 'description': 'Gas, public transit, uber, parking'},
            {'name': 'Shopping', 'description': 'Clothing, electronics, general purchases'},
            {'name': 'Entertainment', 'description': 'Movies, concerts, games, streaming'},
            {'name': 'Bills & Utilities', 'description': 'Rent, electricity, internet, phone'},
            {'name': 'Healthcare', 'description': 'Doctor visits, pharmacy, insurance'},
            {'name': 'Education', 'description': 'Books, courses, training, tuition'},
            {'name': 'Travel', 'description': 'Hotels, flights, vacation expenses'},
            {'name': 'Personal Care', 'description': 'Haircuts, cosmetics, gym membership'},
            {'name': 'Other', 'description': 'Miscellaneous expenses'},
        ]

        for category_data in categories:
            category, created = ExpenseCategory.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                self.stdout.write(f'Category already exists: {category.name}')