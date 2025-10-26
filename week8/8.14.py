def make_car(manufacturer, model, **options):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in options.items():
        car[key] = value
    return car

car_profile = make_car ('subaru', 'outback', color='blue', tow_package=True)
print(car_profile)