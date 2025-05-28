import pandas as pd
import numpy as np

products = ['P1', 'P2', 'P3']
location_types = ['small', 'medium', 'large', 'oversized']
days = 100

data = []

for product in products:
    for loc_type in location_types:
        on_hand = np.maximum(0, np.cumsum(np.random.randint(-5, 6, size=days)) + 50)
        incoming = np.random.poisson(3, size=days)
        outgoing = np.random.poisson(3, size=days)
        loc_full = (on_hand // 10).clip(0, 20)
        loc_empty = 20 - loc_full
        for day in range(days):
            data.append({
                'product_id': product,
                'location_type': loc_type,
                'day': day,
                'on_hand_qty': on_hand[day],
                'incoming_qty': incoming[day],
                'outgoing_qty': outgoing[day],
                'location_full': loc_full[day]
            })

df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)
