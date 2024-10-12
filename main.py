import pandas as pd   # type: ignore

# 1. DataFrame yaratish  test xabar bu
data = {  
    'Ism': ['Ali', 'Vali', 'Sardor', 'Hasan', 'Javohir'],  
    'Yosh': [20, 25, 30, 35, 40],  
    'Shahar': ['Toshkent', 'Samarqand', 'Buxoro', 'Qashqadaryo', 'Navoi']  
}  
df = pd.DataFrame(data)  

# 2. Ma'lumotlarni ko'rish  
print(df)  

# 3. Filtrlash  
young_people = df[df['Yoshi'] < 30]  
print("30 yoshdan kichiklar:\n", young_people)  

# 4. O'zgartirish  
df['Yoshi'] += 1  # Har bir shaxsning yoshini 1 ga oshirish  
print("Yangilangan DataFrame:\n", df)  

# 5. CSV formatda saqlash  
df.to_csv('data.csv', index=False)