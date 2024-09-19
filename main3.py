import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import matplotlib.pyplot as plt

def parse_prices(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Не удалось получить доступ к сайту")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    prices = []
    price_elements = soup.find_all('span', class_='ui-LD-ZU')  # Нужно адаптировать к реальной структуре

    for element in price_elements:
        price_text = element.get_text(strip=True).replace('руб.', '').replace(' ', '')
        try:
            price = int(price_text)
            prices.append(price)
        except ValueError:
            continue

    return prices

def save_to_csv(prices, filename='sofa_prices.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Цена"])
        for price in prices:
            writer.writerow([price])


def calculate_average(prices):
    return np.mean(prices)


def plot_histogram(prices):
    plt.figure(figsize=(8, 6))
    plt.hist(prices, bins=20, color='blue', alpha=0.7)
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (рубли)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()

def main():
    url = 'https://www.divan.ru/category/modulnye-divany'
    prices = parse_prices(url)
    if prices:
        save_to_csv(prices)

        avg_price = calculate_average(prices)
        print(f"Средняя цена диванов: {avg_price:.2f} рублей")
        plot_histogram(prices)
    else:
        print("Не удалось извлечь цены.")

if __name__ == '__main__':
    main()
