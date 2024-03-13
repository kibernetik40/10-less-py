import pandas as pd

# Исходный DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# Получаем уникальные значения столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создаем DataFrame с нулями, где строки - индексы исходного DataFrame,
# а столбцы - уникальные значения 'whoAmI'
one_hot_df = pd.DataFrame(0, index=data.index, columns=unique_values)

# Заполняем one-hot DataFrame значениями 1 в соответствии с исходным DataFrame
for index, value in data['whoAmI'].iteritems():
    one_hot_df.loc[index, value] = 1

print(one_hot_df)
