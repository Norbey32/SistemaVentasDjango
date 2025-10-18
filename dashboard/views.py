from django.shortcuts import render
from django.views.generic import View
from django.db.models import Sum, Count, Q 
from django.db.models.functions import TruncDay
from django.utils import timezone
from datetime import timedelta
from sales.models import Sales 
from customer.models import Customer
import json 
from django.contrib.auth.mixins import LoginRequiredMixin 

class DashboardHomeView(LoginRequiredMixin, View):
    template_name = 'dashboard/dashboard_home.html'

    def get_context_data(self):
        now = timezone.localtime(timezone.now())
        today_date = now.date() 
        end_date = today_date 
        start_date = end_date - timedelta(days=6) 

        FECHA_CAMPO = 'sale_date'

        # --- Gráfico de Ventas Semanales ---
        
        daily_sales_qs = Sales.objects.filter(
            **{f'{FECHA_CAMPO}__date__range': [start_date, end_date]}
        ).annotate(
            day=TruncDay(FECHA_CAMPO)
        ).values('day').annotate(
            total_sum=Sum('total')
        ).order_by('day')

        sales_data = {}
        for sale in daily_sales_qs:
            # Usamos el formato %d %b (Ej: 17 Oct) para la clave
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

        # --- INICIO CÁLCULO DE KPIS CORREGIDO ---

        # 1Cálculo del Total Vendido Semanal
        weekly_total = Sales.objects.filter(
            **{f'{FECHA_CAMPO}__date__range': [start_date, end_date]}
        ).aggregate(
            weekly_total_sum=Sum('total')
        )['weekly_total_sum'] or 0.00 

        # CÁLCULO DEL TOTAL VENDIDO HOY
        
        # Obtenemos el inicio y el fin del día actual con la zona horaria correcta
        start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_today = now.replace(hour=23, minute=59, second=59, microsecond=999999)

        # Filtramos por el rango de tiempo exacto del día de hoy
        today_sales_total = Sales.objects.filter(
            sale_date__gte=start_of_today,
            sale_date__lte=end_of_today 
        ).aggregate(Sum('total'))['total__sum'] or 0.00
        
        # Cálculo de Clientes Activos Semanales
        active_clients_count = Sales.objects.filter(
            **{f'{FECHA_CAMPO}__date__range': [start_date, end_date]}
        ).values('customer').distinct().count()

        context = {
            'chart_labels': json.dumps(chart_labels), 
            'chart_data': json.dumps([float(d) for d in chart_data]), 
            
            'weekly_total': round(weekly_total, 2) if weekly_total else 0.00, 
            'today_sales_total': round(today_sales_total, 2) if today_sales_total else 0.00,
            'active_clients_count': active_clients_count,
            
            'start_date': start_date,
            'end_date': end_date,
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
