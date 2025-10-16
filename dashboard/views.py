from django.shortcuts import render
from django.views.generic import View
from django.db.models import Sum, Count, Q 
from django.db.models.functions import TruncDay
from django.utils import timezone
from datetime import timedelta
from sales.models import Sales 
from customer.models import Customer
import json 

class DashboardHomeView(View):
    template_name = 'dashboard/dashboard_home.html'

    def get_context_data(self):
        now = timezone.localtime(timezone.now())
        end_date = now.date() 
        start_date = end_date - timedelta(days=6) 

        FECHA_CAMPO = 'sale_date'

        daily_sales_qs = Sales.objects.filter(
            **{f'{FECHA_CAMPO}__date__range': [start_date, end_date]}
        ).annotate(
            day=TruncDay(FECHA_CAMPO)
        ).values('day').annotate(
            total_sum=Sum('total')
        ).order_by('day')

        sales_data = {}
        for sale in daily_sales_qs:
            day_str = sale['day'].strftime('%d %b') 
            
            try:
                total = float(sale['total_sum'])
            except (TypeError, ValueError):
                total = 0.00
                
            sales_data[day_str] = total
        chart_labels = []
        chart_data = []
        
        current_date = start_date
        while current_date <= end_date:
            day_str = current_date.strftime('%d %b')
            chart_labels.append(day_str)
            
            search_key = current_date.strftime('%d %b')
            chart_data.append(sales_data.get(search_key, 0.00))
            
            current_date += timedelta(days=1)

        # --- INICIO CÁLCULO DE KPIS ---

        # Cálculo del Total Vendido Semanal
        weekly_total = Sales.objects.filter(
            **{f'{FECHA_CAMPO}__date__range': [start_date, end_date]}
        ).aggregate(
            weekly_total_sum=Sum('total')
        )['weekly_total_sum'] or 0.00 

        # Cálculo del Total Vendido HOY 
        start_of_today = timezone.make_aware(timezone.datetime(end_date.year, end_date.month, end_date.day))
        end_of_today = start_of_today + timedelta(days=1)

        today_sales_total = Sales.objects.filter(
            sale_date__gte=start_of_today,
            sale_date__lt=end_of_today
        ).aggregate(Sum('total'))['total__sum'] or 0.00
        
        # Cálculo de Clientes Activos Semanales
        active_clients_count = Sales.objects.filter(
            **{f'{FECHA_CAMPO}__date__range': [start_date, end_date]}
        ).values('customer').distinct().count()

        context = {
            'chart_labels': json.dumps(chart_labels), 
            'chart_data': json.dumps([float(d) for d in chart_data]), 
            
            'weekly_total': weekly_total, 
            'today_sales_total': today_sales_total,
            'active_clients_count': active_clients_count,
            
            'start_date': start_date,
            'end_date': end_date,
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
