import pandas as pd


# From the avocado dataset find:
# which region had the lowest average price for conventionally grown avocados each year, and know the same information
# for organic avocados.

# which region had the highest average price for both types of avocado for each given year.

# lowest all time price for both conventionally grown and organic avocados, and also the highest price as well.

def get_average_by_year(df):
    averages = {}
    years = df.year.unique()

    for year in years:
        averages_for_year = filter_by_year(df, year).groupby("region").mean()
        averages.update({year: averages_for_year})

    return averages


def filter_by_year(df, year):
    return df.query("year == @year").drop(columns="year")


def display_data(avg):
    for year, data in avg.items():
        highest_value = data.price.max()
        location = data.query("price == @highest_value").index[0]
        print(f"Highest price for conventional avocados in {year} was ${highest_value:.2f} in {location}.")

    print()

    for year, data in avg.items():
        lowest_value = data.price.min()
        location = data.query("price == @lowest_value").index[0]
        print(f"Lowest price for conventional avocados in {year} was ${lowest_value:.2f} in {location}.")

    print()


with open("avocado.csv", "r") as avocado_prices:
    df = pd.read_csv(avocado_prices).rename(columns={"AveragePrice": "price"})

df = df[["year", "region", "price", "type"]]

conventional = df.query("type == 'conventional'").copy()
conventional.drop(columns="type", inplace=True)

organic = df.query("type == 'organic'").copy()
organic.drop(columns="type", inplace=True)

conventional_averages = get_average_by_year(conventional)
organic_averages = get_average_by_year(organic)

highest_conventional = conventional.price.max()
print(f"The highest price for conventional avocados was ${highest_conventional:.2f}")

lowest_conventional = conventional.price.min()
print(f"The lowest price for conventional avocados was ${lowest_conventional:.2f}")

highest_organic = organic.price.max()
print(f"The highest price for organic avocados was ${highest_organic:.2f}")

lowest_organic = organic.price.min()
print(f"The lowest price for organic avocados was ${lowest_organic:.2f}")
