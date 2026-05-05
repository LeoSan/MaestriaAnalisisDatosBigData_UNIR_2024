import datetime
import calendar
from typing import List, Tuple
from dateutil.relativedelta import relativedelta

def generate_monthly_intervals(lookback_months: int = 24) -> List[Tuple[int, int]]:
    """
    Genera una lista de tuplas (from_date, to_date) en formato Unix Timestamp
    para cada uno de los últimos `lookback_months` meses completos.
    El mes actual en curso no se incluye para no sesgar datos incompletos.
    
    Returns:
        List[Tuple[int, int]]: [(unix_start_1, unix_end_1), (unix_start_2, unix_end_2), ...]
        El orden será desde el mes más antiguo hasta el mes anterior al actual.
    """
    intervals = []
    
    # Tomamos el primer día del mes actual a las 00:00:00 como ancla superior
    today = datetime.datetime.now()
    first_day_current_month = datetime.datetime(today.year, today.month, 1)
    
    # Retrocedemos mes a mes
    for i in range(lookback_months, 0, -1):
        target_month = first_day_current_month - relativedelta(months=i)
        
        # Último día de ese mes objetivo
        _, last_day = calendar.monthrange(target_month.year, target_month.month)
        
        start_date = datetime.datetime(target_month.year, target_month.month, 1)
        end_date = datetime.datetime(target_month.year, target_month.month, last_day, 23, 59, 59)
        
        # Convertir a timestamp unix (entero)
        intervals.append((int(start_date.timestamp()), int(end_date.timestamp())))
        
    return intervals
