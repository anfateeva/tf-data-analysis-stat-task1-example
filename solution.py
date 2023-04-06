import pandas as pd
import numpy as np

chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    error = sts.laplace(1, 0).rvs(size = x.size)
    return ((np.mean(x) + np.mean(error))/882) # Ваш ответ
